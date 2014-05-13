<?php

/************ URL ZUGRIFF *************/

$dip = $_GET["dip"];
$state = $_GET["state"];
$time = $_GET["time"];
$group = $_GET["group"];


echo $dip;
echo $state;
echo $time;

if ($dip=="")
{
	 $dip=09990;
}

if ($time=="")
{
	 $time=0;
}

if ($state=="")
{
	$state=toggle;
}

if ($group=="")
{
	$group=no_group;
}

$temp = exec("sudo /var/www/send.py $dip $state");

echo "success";

/************* GUI ********************/
?> 
