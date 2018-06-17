#!/usr/bin/env python
import cgi
import cgitb
import os,commands
cgitb.enable()
import mysql.connector as sql


#defining fieldarea to accept values
webdata=cgi.FieldStorage()

print '''
		<html>
			<head>
				<style>
					body
					{
						margin:0px;
					}
					.header
					{
						width:100%;
						text-align:left;
						background-color:black;
						color:white;
						position: fixed;
						top: 0px;
						height: 55px;
						font-size:42px;
						padding-top: 5px;
						
					}
					.header a
					{
						float:right;
						font-size:23px;
						text-decoration:none;
						color: grey;
						text-align: center;
						font-size: 23px;
						padding: 12px 15px;
					}
					.header a:hover{background-color: grey; color: white;}
					.footer
					{
						background-color: black;
						bottom: 0px;
						position: fixed;
						width: 100%;
						text-align: center;
						color: grey;
						height: 50px;
						
					}
					input[type=file]
					{
						font-size:30px;
					}
					#upload_submit input[type=submit]
					{
						width:150px;
						margin-left:-359px;
						text-align: center;
						border-radius:10%;
						font-size:30px;
						border-width:1px;
						background-color:#2CE5F2;

					}
					input[type=submit]:hover
					{
						background-color:blue;
						box-shadow: 5px 5px 10px 1px black;
						color:white;
					}
					.view_file input[type=submit]
					{
						width:150px;
						text-align: center;
						border-radius:10%;
						font-size:25px;
						border-width:1px;
						background-color:#2CE5F2;
					}

				</style>
			</head>
	'''


print '<div class="header">'
print 'Cloud'
print '<a href="http://192.168.122.69/cloudmix_login.html">Log Out</a>'
print '</div>'
print '\n\n\n'
#creating database connection
conn=sql.connect(user='root',password='ok',database='cloudmix',host='localhost')
#creating cursor object
cur=conn.cursor()

#displaying username
print '<div style="font-size:20px; text-align: left; padding-top: 65px;">'
print 'Welcome '+uname
commands.getoutput('espeak -g15 "welcome '+uname+' to the cloudmix"')

print '<hr></div>'

if signupbtn:
	
	print '''
			<p align="center">Upload your data in cloud storage<p>
			<div class="upload_file" align="center">
			<div id="upload_submit">
			<form action="http://192.168.122.69/cgi-bin/upload.py" enctype="multipart/form-data" method="post">
			<input type="file" name="filename"><br><br>
			<input type="submit" name="upload" value="Upload">
			<input type="radio" name="stor_name" value="'''+st_name+'''" checked style="display:none">
			</form>
			</div>
			</div>
			<p align="center">View ur cloud data<p>
			<div class="view_file" align="center">
			<form action="http://192.168.122.69/cgi-bin/dataview.py" method="post">
			<input type="submit" name="viewdata" value="View Data">
			<input type="radio" name="stor_name" value="'''+st_name+'''" checked style="display:none">'

			</form>
			</div>

			<div class="footer">
			<br/>Copyright Developed By Avid learners
			</div>
		'''



elif loginbtn:
	cur.execute('select storage_name from userinfo where username="{}";'.format(uname))
	out=cur.fetchall()
	#Changing to string format and splitting for getting organised data output
	org_out=str(out).split("'")
	st_name=org_out[1]
	
	print '''
			<p align="center">Upload your data in cloud storage<p>
			<div class="upload_file" align="center">
			<div id="upload_submit" >
			<form action="http://192.168.122.69/cgi-bin/upload.py" enctype="multipart/form-data" method="post">
			<input type="file" name="filename" ><br><br>
			<input type="submit" name="upload" value="Upload">
			<input type="radio" name="stor_name" value="'''+st_name+'''" checked style="display:none">
			</form>
			</div>
			</div><br><br>

			<p align="center">View ur cloud data<p>
			<div class="view_file" align="center">
			<form action="http://192.168.122.69/cgi-bin/dataview.py" method="post">

			<input type="submit" name="viewdata" value="View Data">
			<input type="radio" name="stor_name" value="'''+st_name+'''" checked style="display:none">'

			</form>
			</div>

			<div class="footer">
			<br/>Copyright Developed By Avid learners
			</div>
		  '''

conn.close()
print '</html>'



