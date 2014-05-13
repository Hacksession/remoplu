<?php

/* Check which button was pressed */
if (isset($_POST['buttonA0'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 1 0'); }
if (isset($_POST['buttonA1'])) { shell_exec('sudo /home/pi/raspberry-remote/send 10010 1 1'); }
 
if (isset($_POST['buttonB0'])) { exec("sudo /var/www/send.py B off 0 no_group"); }
if (isset($_POST['buttonB1'])) { exec("sudo /var/www/send.py B on 0 no_group"); }
 
if (isset($_POST['buttonC0'])) { exec("sudo /var/www/send.py C off 0 no_group"); }
if (isset($_POST['buttonC1'])) { exec("sudo /var/www/send.py C on 0 no_group"); }


$var1 = $_POST['name'];
if ($var1 == ''){ $var1 = 'o';}
$var2 = $_POST['code'];
if ($var2 == ''){ $var2 = 'o';}
$var3 = $_POST['group'];
if ($var3 == ''){ $var3 = 'o';}



if ($_POST['formaction']=='create') 
{	
 $var4 = "create";
 exec("sudo /var/www/database.py $var1 $var2 $var3 $var4");
 $new_button = TRUE;

 }	
if ($_POST['delete']=='delete') {	
 $var4 = "delete";
 exec("sudo /var/www/database.py $var1 $var2 $var3 $var4");
 $delete_button = TRUE;

 }	

if (isset($_POST['show_SQL'])) { 
// print SQL DATA
//connect to DB
$db = new SQLite3('/home/pi/Steckdosen.db');
    $tablesquery = $db->query("SELECT * FROM plugs;");

    while ($table = $tablesquery->fetchArray(SQLITE3_ASSOC)) {
        echo $table['name'] . ' | ';
	echo $table['address'] . ' | ';
	echo $table['state'] . ' | ';
	echo $table['category'] . '<br />';
    }
$db->close();
}
?>
 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
       "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>

<h1>neue Steckdose anlegen</h1>

<form action="plugPHP.php" method="post">
  <p>name:<br><input name="name" type="text" size="30" maxlength="30"></p>
  <p>code:<br><input name="code" type="text" size="30" maxlength="40"></p>
  <p>group:<br><input name="group" type="text" size="30" maxlength="40"></p>
  <input type="submit" name="formaction" value="create">
  <input type="submit" name="delete" value="delete">
  <input type="submit" name="show_SQL" value="show_SQL">
</form>
 <p>create requires input in every field. Delete only requires one field <br></p>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>RPi</title>
 
<style type="text/css">
body {
	background-color:#1b191a;
	background-image:url(bg.jpg);
	color: white;
	}
 
.wrapButtons {
	text-align:center;
	font-size:25px;
	font-family:verdana, sans-serif;
	}
.onButton, .offButton {
	width:200px;
	height:100px;
	margin:-10px 10px 0px 10px; /* o-r-u-l */
	color:white;
	background-color:#53bc41;
	border-radius:8px;
	font-size:50px;
	}
 
.offButton {
	background-color:#e40e12;
	}
</style>
 
<script type="text/javascript"></script>
</head>
<body>
 
<form action="" method="post">

	<div class="wrapButtons">
	<p>Steckdose A</p>
    	<button class="offButton" type="submit" name="buttonA0">Aus</button>
    	<button class="onButton" type="submit" name="buttonA1">Ein</button>
    </div>
 
    <div class="wrapButtons">
	<p>Steckdose B</p>
    	<button class="offButton" type="submit" name="buttonB0">Aus</button>
    	<button class="onButton" type="submit" name="buttonB1">Ein</button>
    </div>
 
    <div class="wrapButtons">
	<p>Steckdose C</p>
    	<button class="offButton" type="submit" name="buttonC0">Aus</button>
    	<button class="onButton" type="submit" name="buttonC1">Ein</button>
    </div>
<?php
if ($new_button = TRUE)
{
?>
<form action="" method="post">

	<div class="wrapButtons">
	<p><?php echo $var1 ?></p>
    	<button class="offButton" type="submit" name="buttonD0">Aus</button>
    	<button class="onButton" type="submit" name="buttonD1">Ein</button>
    </div>

<?php
$new_button = FALSE;
}
?>
</form>
 
<hr style="margin-top:35px;">
<p style="text-align:center;">System: <?php echo $sysinfo; ?> - Systemzeit: <?php echo $systime; ?></p>
 
</body>
</html>