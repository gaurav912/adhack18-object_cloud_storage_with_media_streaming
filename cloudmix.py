#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import os,commands
import mysql.connector as sql

print 'content-type:text/html'
print ''

webdata=cgi.FieldStorage()


uname=webdata.getvalue('username')
passwd=webdata.getvalue('password')
st_name=webdata.getvalue('storage_name')
st_size=webdata.getvalue('storage_size')
#these variables are just to define whether it is login or signup 
loginbtn=webdata.getvalue('acc_login')
signupbtn=webdata.getvalue('acc_create')

#creating database connection
conn=sql.connect(user='root',password='ok',database='cloudmix',host='localhost')

cur=conn.cursor()

cur.execute('select username,password from userinfo where username=%s or storage_name=%s',(uname,st_name))

out=cur.fetchall()

if len(out)>0:
	print '<script>'
	print 'alert ("Username/Storage already exists!")'
	print '</script>'
	#print 'The username or storage name has already been used by other'
	print '<meta http-equiv="refresh" content="0;url=http://192.168.122.69/cloudmix.html" />'
else:
	#ins_query='insert into userinfo(username,password,storage_name,storage_size) values("{}","{}","{}","{}");'.format(uname,passwd,st_name,st_size)

	cur.execute('insert into userinfo(username,password,storage_name,storage_size) values("{}","{}","{}","{}");'.format(uname,passwd,st_name,st_size))

	conn.commit()

	#creating  disk for user
	disk_storage='sudo lvcreate --name '+st_name+' -V'+st_size+'gb  --thin cloud_storage/media'
	commands.getoutput(disk_storage)

	#formatting the harddisk provided to user
	commands.getoutput('sudo mkfs.xfs  /dev/cloud_storage/'+st_name)

	#making the directory inside html of apache server to mount the storage
	commands.getoutput('sudo mkdir /var/www/html/storages/'+st_name)     
	#mounting the storage in apache server inside html
	commands.getoutput('sudo mount  /dev/cloud_storage/'+st_name+'  /var/www/html/storages/'+st_name)
	#providing permission to all users
	commands.getoutput('sudo chmod 777  /var/www/html/storages/'+st_name)

conn.close()

#print '<meta http-equiv="refresh" content="0;url=http://127.0.0.1/welcome_page.html" />'

execfile('welcome.py')





