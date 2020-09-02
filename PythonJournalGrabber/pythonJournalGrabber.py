# !/user/bin/python3

import urllib.request
import string
import requests
import sys
import json
import os
import xml.etree.ElementTree as ET
import time
from datetime import datetime



# Makes list of all journal entried and saves them to file
def create(file):
    print("\nFile does not exist and will be created and filled... ")
    authas = input("Enter name of account from URL path with '_' as spaces and '-': ")
    cookie = input("Enter the cookie from logged in account: ")

    if '-' in authas:
        authas =  authas.replace('-', '_')
    if ' ' in authas:
        authas =  authas.replace(' ', '_')
  
    try:
        # Define the main URL that is needed for the user. You should just need to replace 
        URL = "https://www.livejournal.com/export_do.bml?authas={}".format(authas)
        print("Trying to connect to: ",URL)

        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Accept-Language": "en-US,en;q=0.5", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Content-Length": "199", 
        "Origin": "https://www.livejournal.com", 
        "DNT": "1", 
        "Connection": "keep-alive", 
        "Referer": "https://www.livejournal.com/export.bml", 
        "Cookie": '', 
        "Upgrade-Insecure-Requests": "1", 
        "Host": "www.livejournal.com"}
        
        header["Cookie"] = cookie

        yearRangeStart = int(input("Enter Range for years in format: "))
        yearRangeStop = int(input("Enter Range for years in format: ")) + 1

        for year in range(yearRangeStart, yearRangeStop): 
            for month in range(1, 13):
                payload = "what:journal,year:{},month:{},format:xml,header:on,encid:2,field_itemid:on,field_eventtime:on,field_logtime:on,field_subject:on,field_event:on,field_security:on,field_allowmask:on,field_currents:on".format(year, month)

                # Converts payload to dictionary
                formattedPayload = dict(x.split(":") for x in payload.split(","))

                #Performs a POST on the specified url to get the service ticket
                response = requests.post(URL,data=formattedPayload, headers=header)
                responseContent = response.content
                decodedResponseContent = responseContent.decode('utf-8', errors="ignore")

                if len(decodedResponseContent) > 68:
                    file.write("\n")
                    decodedResponseContentString = str(responseContent).replace("b'", "")
                    decodedResponseContentString = decodedResponseContentString.replace("'", '')
                    file.write(decodedResponseContentString)
                    print("Wrote {}, {}".format(year, month))
                else:
                    print("{}, {} is empty".format(year, month))
        print("Done")
    except Exception as err:
        print("error is ", err)
    file.close() 
    print("Done creating file\n")



# Seperate out entries for better formatting of the XML
def separate(file):
    data = file.read()
    data = str(data)
    
    # This will clear the existing file to a blank slate
    temp = "       "
    for x in data:
        x = " "
        temp = temp + x
    file.seek(0)
    file.write(temp)

    # Set first xml encoding to proper format
    returnValue = data.replace('\\', '"', 2)

    # replace rest of xml encoding with proper quotes
    stringA = r'<?xml version="1.0" encoding=\utf-8\?>\n<livejournal>\n'
    if stringA in returnValue:
        returnValue = returnValue.replace(r'<?xml version="1.0" encoding=\utf-8\?>\n<livejournal>\n', r'')

    # delete any other xml and live journal strings
    stringB = r'\n<livejournal>\n'
    if stringB in returnValue:
        returnValue = returnValue.replace(stringB, r'<livejournal>')
    stringB = r'\n<livejournal>'
    if stringB in returnValue:
        returnValue = returnValue.replace(stringB, r'<livejournal>')


    # fix the formatting of the last string2
    string2 = r'\n</livejournal>\n'
    if string2 in returnValue:
        returnValue = returnValue.replace(string2, '</livejournal>')
    
    # delete all but the last one of the string2
    string5 = r'</livejournal>'
    count = returnValue.count(string5)
    if string5 in returnValue:
        returnValue = returnValue.replace(string5, '',count-1)

    # turn all newlines after a tag into a new line
    string3 = r'>\n<'
    if string3 in returnValue:
        returnValue = returnValue.replace(string3, r'><')

    # set all connected tags on a new line
    string4 = r'><'
    if string4 in returnValue:
        returnValue = returnValue.replace(string4, r'''>
<''')

    # The next two lines will replace the existing text in the file with the new processed text
    file.seek(0)
    file.write(returnValue)

def readIt(file):
    try:
        data = file.read()
        root = ET.fromstring(data)
        
        count = 0
        for entry in root.findall("entry"):
            count += 1
        print("\nThere are {} entries currently".format(count))#, rank)
    
        entryLocation = int(input("which entry would you like to read?: ")) - 1

        print("\nitemid: ",root[entryLocation][0].text)
        print("eventtime: ",root[entryLocation][1].text)
        print("logtime: ",root[entryLocation][2].text)
        print("subject: ",root[entryLocation][3].text)
        print("event: ",root[entryLocation][4].text)
    except ET.ParseError as err:
        print("error:", err)

def addto(data, file_name):
    dateTimeObj = datetime.now()
    eventTime = dateTimeObj.strftime("%F %H:%M:%S")

    try:
        root = ET.fromstring(data)

        count = 0
        for entry in root:
                count += 1                
        print("\nYou currently have {} entries.".format(count))

        entry = ET.Element("entry")

        itemid = ET.SubElement(entry, "itemid")
        itemid.text = str(count + 1)

        eventtime = ET.SubElement(entry, "eventtime")
        eventtime.text = str(eventTime)

        dateTimeObj2 = datetime.now()
        logTime = dateTimeObj2.strftime("%F %H:%M:%S")
        logtime = ET.SubElement(entry, "logtime")
        logtime.text = str(logTime)

        subject = ET.SubElement(entry, "subject")
        subject.text = input("Enter the subject of the entry: ")

        entryData = ET.SubElement(entry, "event")
        entryData.text = input("What would you like to say? : ")

        security = ET.SubElement(entry, "security")
        security.text = "usemask"

        allowmask = ET.SubElement(entry, "allowmask")
        allowmask.text = str(1)

        currentMusic = ET.SubElement(entry, "current_music")
        currentMusic.text = input("What are you listening to? : ")

        currentMood = ET.SubElement(entry, "current_mood")
        currentMood.text = input("What is your current mood? : ")


        print(ET.dump(entry))

        root.append(entry)
        tree = ET.ElementTree(root)
        tree.write(file_name, encoding="utf-8")

        return 

    except ET.ParseError as err:
        print("errors:", err)




menuList = '''
~~~~~~~~~~~~~~~~~~~~~~~~
Enter your value:
1 = Create journal file
2 = Seperate data in file
3 = Read Journal File
4 = Add Entry
0 = Quit
~~~~~~~~~~~~~~~~~~~~~~~~\n'''

val = int(input(menuList))

while val > 0:
    if val == 1:
        print("#1: Create file\r\n")
        file_name = input("Enter a file name to check existance:\r\n" )
        if os.path.exists(file_name):
            print(file_name + " already exists\r\n")
        else:
            file = open(file_name, "a")
            create(file)
            file.close()
        val = int(input(menuList))
        print(val,"chosen \n") 
    
    elif val == 2:
        # sets file up to be added to
        print("\r\n#2: Format file")
        file_name = input("Enter a file name to process:\r\n" )
        if os.path.exists(file_name):
            file = open(file_name, "r+", encoding="utf-8")
            separate(file)
            file.close()
        else:
            print(file_name + "does not exist")
        val = int(input(menuList))
        print(val, "chosen \n")
    
    elif val == 3:
        # sets file up to be processed
        print("\r\n#3: Read File")
        file_name = input("Enter a file name to reading:\r\n" )
        if os.path.exists(file_name):
            file = open(file_name, "r", encoding="utf-8")
            readIt(file)
            file.close()
        else:
            print("not found")
        val = int(input(menuList))
        print(val, "chosen \n")

    elif val == 4:
        # sets file up to be processed
        print("\r\n#4: Add Entry")
        file_name = input("Enter a file name to add entry to:\r\n" )
        if os.path.exists(file_name):
            with open(file_name) as file_in:
                lines = ""
                for line in file_in:
                    lines = lines + line
                file_in.close()
            file = open(file_name, "a+")
            addto(lines, file_name)
        else:
            print("not found")
        val = int(input(menuList))
        print(val, "chosen \n")
else:
    print("bye")
