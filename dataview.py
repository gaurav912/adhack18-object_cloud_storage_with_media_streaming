#!/usr/bin/env python
import  cgi,commands,os
import cgitb
cgitb.enable()

print "Content-type:text/html"
print ""

webdata=cgi.FieldStorage()

st_name=webdata.getvalue('stor_name')



def print_directory_contents(sPath):                                      
	content = []
	contPath = []
	global content,contPath
	for sChild in os.listdir(sPath):                
            	content.append(sChild)
		sChildPath = os.path.join(sPath,sChild)
		contPath.append(sChildPath)
	print "<h1 align=center>Your Data</h1>"	
	if len(content)==0:
		print "<h2 align=center >Is Empty Now</h2>"
		

print_directory_contents("/var/www/html/storages/"+st_name+"/")
print """
	<!DOCTYPE html>
<html>
<head>
	<title>Cloud Data</title>
	 
	   <STYLE>
		#TOPBTN {   box-shadow: 0px 8px 30px 10px gray; }    
		#topdiv {  box-shadow: 0px 8px 30px 10px gray; margin:30px;  margin-left:100px; margin-right:100px;}                              		
	   </STYLE>
	<style>
		
		input[type=button]{
		    
		    color: black;
		    padding: 14px 20px;
		    width:40%;
		    border-style: none;
		    border-radius: 10px;
		    margin:2px;
		}
		 input[type=submit]{
		    width:10%
		    color: black;
		    padding: 14px 20px;
		    border-style: none;
		    border-radius: 10px;
		    cursor:pointer;
		    margin:2px;
		    background-color: rgb(100,200,300);
		}
		input[type=submit]:HOVER    
			{
				background-color: blue;
			}
		form{
			display:inline;
		}
	</style>
</head>
<body>	
		
	
	<div id="topdiv">
"""
for i in content:
	print '''<input type="button" class = "button" name="Launch" value="'''+i+'''">'''
	#print '''<a href="file:///home/udeshay/Desktop/pp/'''+i+'''">hh</a> &nbsp;&nbsp;'''
	
	print '''<a href="http://192.168.122.69/storages/'''+st_name+'''/'''+i+''' " download="">Download</a> &nbsp;&nbsp;'''
	
#----------------------------------------------------------------------------------------------------
#									Streaming audio/Video
	#execfile('clouddata.py')
	#print '<meta http-equiv="refresh" content="0;url=http://192.168.122.28/cgi-bin/clouddata.py"/>'
	print '''
			<form action="http://192.168.122.69/cgi-bin/clouddata.py" method="post">

			<input type="submit" name="file_play" value="Open">
			<input type="radio" name="folder_name" value="'''+st_name+'''" checked style="display:none">
			<input type="radio" name="file_name" value="'''+i+'''" checked style="display:none">

			</form>

		   '''
		

	print "<br/>"
print """</div>	
</body></html>
"""


#print html
#print_directory_contents("/home/udeshay/Desktop/pp/")
