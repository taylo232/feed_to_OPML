#!/usr/bin/env python3

# TODO; Comment lines 
# TODO: tidy up list/tuple mash in opml string build

import sqlite3
import time
#### SQL to extract rss data from db
# TODO: Check file exists
db = sqlite3.connect('./Database.db')
# TODO: err trap for no connection 
cursor = db.cursor()

#Read all records
cursor.execute('''SELECT * FROM feed;''')
all_rows = cursor.fetchall()

# Create opml body
opml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><opml version=\"1.1\"><head>"
opml += "<title><![CDATA[Feed)]]></title><dateCreated>"
opml += time.strftime("%a, %d %b %Y %H:%M:%S +0000")
opml += "</dateCreated></head><body>"

for i in all_rows:
	feedtext=i[6]
	if "&" in feedtext:
		feedtext=feedtext.replace(" & "," and ")
		print(feedtext)
	feedXML=str(i[9])
	if "=" in feedXML:
		feedXML = feedXML[:-(len(feedXML) - feedXML.find("?"))]
		print(feedXML)
	feedHTML=i[4]
	feedtype=str(i[3])
	foo="<outline "
	foo += "text=\"" + feedtext + "\" "
	foo += "title=\"" + feedtext + "\" "
	foo += "xmlUrl=\"" + feedXML + "\" "
	foo += "htmlUrl=\"" + feedHTML + "\" "
	foo += "type=\"" + feedtype + "\"></outline>"
	opml += foo
opml += "</body></opml>"
db.close()	

opmfile=time.strftime("feed-%Y-%m-%d-%H%M.opml")
# Write into feed.opml
f = open(opmfile, 'w')
f.write(opml)
f.close()

