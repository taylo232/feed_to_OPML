#!/usr/bin/python3

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
opml += "<title><![CDATA[Feed+)]]></title><dateCreated>"
opml += time.strftime("%a, %d %b %Y %H:%M:%S +0000")
opml += "</dateCreated></head><body>"

for i in all_rows:
	feedtext=i[6]
	feedtitle=i[6]
	feedXML=i[9]
	feedHTML=i[4]
	feedtype=i[3]
	foo="<outline "
	foo += "text=\"" + str(feedtext) + "\" "
	foo += "title=\"" + str(feedtitle) + "\" "
	foo += "xmlUrl=\"" + str(feedXML) + "\" "
	foo += "htmlUrl=\"" + str(feedHTML) + "\" "
	foo += "type=\"" + str(feedtype) + "\"></outline>"
	opml += foo
opml += "</body></opml>"
db.close()	


opmfile=time.strftime("feed-%Y-%m-%d-%H%M.opml")
# Write into feed.opml
f = open(opmfile, 'w')
f.write(opml)
f.close()


