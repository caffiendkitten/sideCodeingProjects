# A smiple program to list months out for a year

year = "1994"
month = "08"

for i in range(2,9):
    day = "0"+str(i)
    print("{}/{}/{}".format(year,month,day))