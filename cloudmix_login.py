#!/usr/bin/env python
import cgi
import cgitb
import os,commands
cgitb.enable()
import mysql.connector as sql

print 'content-type:text/html'
print ''

webdata=cgi.FieldStorage()


uname=webdata.getvalue('username')
passwd=webdata.getvalue('password')

#these variables are just to define whether it is login or signup 
signupbtn=webdata.getvalue('acc_create')
loginbtn=webdata.getvalue('acc_login')

#creating database connection
conn=sql.connect(user='root',password='ok',database='cloudmix',host='localhost')

cur=conn.cursor()

cur.execute('select username,password from userinfo where username=%s and password=%s',(uname,passwd))

out=cur.fetchall()
conn.close()

#condition for checking whether username and password matches or not by checking if there is any matching output

if len(out)>0:
	execfile('welcome.py')
	#print '<meta http-equiv="refresh" content="0;url=http://127.0.0.1/welcome_page.html" />'
else:
	print '<script>'
	print 'alert ("Wrong Credentials!")'
	print '</script>'
	print '<meta http-equiv="refresh" content="0;url=http://192.168.122.69/cloudmix_login.html" />'
	
