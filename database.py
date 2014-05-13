#!/usr/bin/env python
import sys
import urllib2
import time
import os
from time import sleep
import sqlite3 as lite

#sys.argv[0] # this is the file name
#sys.argv[1] # this is the plug name
#sys.argv[2] # this is the plug code
#sys.argv[3] # this is the plug state
#sys.argv[4] # create or delete SQL entry

php_name=sys.argv[1]
php_code=sys.argv[2]
php_group=sys.argv[3]
php_sql=sys.argv[4]


txtfiletest = open("/var/www/test.txt", "a")
txtfiletest.write("PARAMERTER: name %s code %s\n" % (php_name, php_code))
txtfiletest.close()
	
################ Refresh State in SQL ########################
con = lite.connect('/home/pi/Steckdosen.db')			#Connect to SQL Database				
with con:
	cur = con.cursor()
#	#cur.execute("DROP TABLE IF EXISTS plugs")
	cur.execute("CREATE TABLE IF NOT EXISTS plugs(name TEXT, address TEXT, state TEXT, category TEXT)")
#	cur.execute("UPDATE plugs SET state=? WHERE address=?", (state, php_dip))
#	#cur.execute("INSERT INTO plugs VALUES(?, ?, ?)", (NAME,ADDRESS,STATE))	
	if php_sql == "create":
        	cur.execute("INSERT INTO plugs VALUES(?,?,?,?)",(php_name,php_code,'1',php_group));
	elif php_sql == "delete":
		cur.execute("DELETE FROM plugs WHERE name=?", (php_name,)); 	#delete by name
		cur.execute("DELETE FROM plugs WHERE address=?", (php_code,));	#delete by code
		cur.execute("DELETE FROM plugs WHERE category=?", (php_group,)); #delete by group
	con.close
#