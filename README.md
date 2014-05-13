Remote-Plug-Control-Server
==========================

This project is about developing a continuously running service on a raspberry pi to access and control every remote plug within its range. The plugs will be controllable with every internet-capable device.

You will need to install a webserver first to run this project on your Raspberry Pi.
Therefore just follow this tutorial: 
http://www.raspberrypi-spy.co.uk/2013/06/how-to-setup-a-web-server-on-your-raspberry-pi/

After lighttpd is installed you need to:
-put the files in the directory /var/www/
-make the scripts executable "sudo visudo" 

possible commands:
http://192.168.1.111/mfi.php?dip="address"&state=on&time=t -address can be the name or the dip code; time in seconds
http://192.168.1.111/mfi.php?dip="all on" 		   -switch all on
http://192.168.1.111/mfi.php?dip="all off"		   -switch all off
http://192.168.1.111/mfi.php?state=on&group="group_name"   		  -switch plugs in group "on"
http://192.168.1.111/mfi.php?state=off&group="group_name"&time=10	  -switch plugs in group "off" in 10 seconds
http://192.168.1.111/mfi.php?dip="address"&time=10			  -invert state of plug in 10 seconds			

database.py interacts with sqlite3 database
send.py grabs values from php.skript and sends command to send c++ file to interact with the switches
