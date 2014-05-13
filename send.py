#!/usr/bin/env python
import sys, sqlite3, os


name = sys.argv[1] # can be string or dip code
state = sys.argv[2]

'''
name = '1111000110'
state = '00'
'''

con = sqlite3.connect("Steckdosen.db")
cur = con.cursor()


def get_info_about(value):
    """
    Funktion stellt fest welcher Kategorie das Device zugehoerig ist

    group = Gruppierung einzelner Steckdosen
    plug = einzelne Steckdose

    """

    values = (value, value)
    sql = "SELECT * FROM device WHERE dip = (?)  OR name = (?)"  # Achtung wert ist case sensitiv! Sollte noch geaendert weden
    cur.execute(sql, values)
    result = cur.fetchall()
    if len(result) != 0:
        if result[0][2] == 'group':
            print 'category is group'
            group(result[0][0])
        elif result[0][2] == 'plug':
            print 'category is plug'
            plug(result[0][1])
    else:
        print 'nothing to do'


def group(value):
    values = ('%' + value + '%', state)
    sql = "SELECT * FROM device WHERE groupname LIKE (?) AND state != (?)"  # Achtung wert ist case sensitiv! Sollte noch geaendert weden
    cur.execute(sql, values)
    for row in cur:
        sql = "UPDATE device SET state = (?) WHERE dip = (?)"
        values = (state, str(row[1]))
        cur2 = con.cursor()
        cur2.execute(sql, values)
        con.commit()
        command = "send %s %s" % (row[1], state)
        os.system("sudo /home/pi/raspberry-remote/%s" %command)  # call c++ script


def plug(dip):
    sql = "UPDATE device SET state = (?) WHERE dip = (?)"
    values = (state, dip)
    cur2 = con.cursor()
    cur2.execute(sql, values)
    con.commit()
    command = "send %s %s" % (dip, state)
    os.system("sudo /home/pi/raspberry-remote/%s" %command)  # call c++ script

get_info_about(name)






