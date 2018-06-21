#!/usr/bin/env python
#importing modules
import cgi
import cgitb
cgitb.enable()
import os,commands
import mysql.connector as sql

print 'content-type:text/html'
print ''

webdata=cgi.FieldStorage()

#extracting data from frontend
uname=webdata.getvalue('username')
passwd=webdata.getvalue('password')
st_name=webdata.getvalue('storage_name')
st_size=webdata.getvalue('storage_size')
#these variables are just to make use to define whether it is login or signup 
loginbtn=webdata.getvalue('acc_login')
signupbtn=webdata.getvalue('acc_create')

#creating database connection
conn=sql.connect(user='root',password='ok',database='cloudmix',host='localhost')
#creating cursor object
cur=conn.cursor()
#Executing the select query to find username and password from database
cur.execute('select username,password from userinfo where username=%s or storage_name=%s',(uname,st_name))
#saving the output of select query to variable
output=cur.fetchall()

'''checking condition for login: 
		--if length of output is greater than 0 ,the data user is entering is already in database
		--else there is no entries in database hence user can  be registered
'''
if len(output)>0:
	#Javascript code to popup the message
	print '<script>'
	print 'alert ("Username/Storage already exists!")'
	print '</script>'
	#Redirecting to the login page after login failure
	print '<meta http-equiv="refresh" content="0;url=http://192.168.122.69/cloudmix.html" />'

#codes for successful login part
else:
	#executing the insert query to register the user information in database
	cur.execute('insert into userinfo(username,password,storage_name,storage_size) values("{}","{}","{}","{}");'.format(uname,passwd,st_name,st_size))
	#commiting the query
	conn.commit()

#-------------------------------------Assigning Storage to user--------------------------------------
	#creating  disk partition for user
	disk_storage='sudo lvcreate --name '+st_name+' -V'+st_size+'gb  --thin cloud_storage/media'
	commands.getoutput(disk_storage)

	#formatting the partitioned disk provided to user
	commands.getoutput('sudo mkfs.xfs  /dev/cloud_storage/'+st_name)

	#making the directory inside html of apache server to mount the storage
	commands.getoutput('sudo mkdir /var/www/html/storages/'+st_name)     
	#mounting the storage in apache server inside html
	commands.getoutput('sudo mount  /dev/cloud_storage/'+st_name+'  /var/www/html/storages/'+st_name)
	#providing permission on mounted disk for all users
	commands.getoutput('sudo chmod 777  /var/www/html/storages/'+st_name)
#closing the connection
conn.close()

#calling another python cgi file 'welcome.py' for user access to their portal
#calling through execfile so that the variables in this script can be used there too
execfile('welcome.py')





