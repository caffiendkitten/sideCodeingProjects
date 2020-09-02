** LiveJournal downloading Project **
------

Because of the way that LiveJournal.com only lets you download your journal history one month at a time I built this project to itterate over a range of years and months to download the entries.

Currently there is very basic error catching so it might crash.

### User stories:
This program will also allow a user to:
- Downloand their journal entries
- Clean up the downloaded entries to create one xml file of journal entries
- Read all entries
- Add new entries


### To Run
Be sure that you are logged in on a browser as you will need an active cookie for the program to pull entries and you know how your username is presented in the browser. 
For example: If your username is "I-Like Cheese" it will need to be "I_like_cheese" when prompted for it.

To run enter `py pythonJournalGrabber.py` in the terminal within the files location.

This program uses Python3 and the Python3 Requests model to send HTTP requests and receives a Response Object with all the response data (content, encoding, status, etc). 

The Python Requests model lives on layer 7 of the OSI model to make requests.

Note: you might need to import some of the pip imports if you don't have them already.
