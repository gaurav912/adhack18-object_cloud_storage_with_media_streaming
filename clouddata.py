#!/usr/bin/env python
import cgi
import cgitb
import os,commands
cgitb.enable()

print 'content-type:text/html'
print ''

#defining fieldarea to accept values
webdata=cgi.FieldStorage()

play_input=webdata.getvalue('file_play')
folder_name=webdata.getvalue('folder_name')
file_name=webdata.getvalue('file_name')

name,ext=os.path.splitext(file_name)

video_ext=['.mp4','.mpg','.mpeg','.avi','.wmv','.mov','.flv','.ogg','.webm']
audio_ext=['.mp3','.aac','.wav']

if ext in video_ext:

	print '''<video width="720" height="440" controls autoplay>
			<source src="http://192.168.122.69/storages/'''+folder_name+'''/'''+file_name+'''" type="video/mp4">
			Upgrade your browser
			</video>
			'''
elif ext in audio_ext:
	print '''<audio controls autoplay>
			<source src="http://192.168.122.69/storages/'''+folder_name+'''/'''+file_name+'''" type="audio/mpeg">
			Upgrade your browser
			</audio>
			'''
