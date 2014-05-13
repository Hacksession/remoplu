#!/usr/bin/env python
import sys, sqlite3, os

#'''
name = sys.argv[1] # can be string or dip code
state = sys.argv[2]

'''
name = 'New'
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
            print result
            group(result[0][0])
        elif result[0][2] == 'plug':
            print 'category is plug'
            print result
            plug(result[0][0])
    else:
        print 'nothing to do'


def group(value):
    values = ('%' + value + '%', state)
    sql = "SELECT * FROM device WHERE groupname LIKE (?) AND state != (?)"  # Achtung wert ist case sensitiv! Sollte noch geaendert weden
    cur.execute(sql, values)
    result = cur.fetchall()
    print result
    for plug in result:
        print plug
        sql = "UPDATE device SET state = (?) WHERE name = (?)"
        values = (state, str(plug[0]))
        cur2 = con.cursor()
        cur2.execute(sql, values)
        con.commit()

        command = "send %s %s" % (plug[1], state)
        os.system("sudo /home/pi/raspberry-remote/%s" %command)  # call c++ script


def plug(name):
    sql = "UPDATE device SET state = (?) WHERE name = (?)"
    values = (state, name)
    cur2 = con.cursor()
    cur2.execute(sql, values)
    con.commit()
    command = "send %s %s" % (name, state)
    os.system("sudo /home/pi/raspberry-remote/%s" %command)  # call c++ script

get_info_about(name)






