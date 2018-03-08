
# This file will be run as a cron job every x minutes so that the local folder 
# gets synchronized by downloading the necessary files from the dropbox. 

try:
	import os
	import sys
	import dropbox
	from dropbox.client import DropboxClient
	from config import ACCESS_TOKEN,DROPBOX_SYNC_LOCATION
	import time
	import unicodedata
except Exception as e:
	print e

client = dropbox.Dropbox(ACCESS_TOKEN)

#Recursively checks the folder for dropbox files

results=client.files_list_folder(DROPBOX_SYNC_LOCATION,recursive=True)

results=results.entries

#Parse through the files present in dropbox and obtain the respective path
for object in results:
	if isinstance(object,dropbox.files.FileMetadata):
		file_path=object.path_display
		
		#convert unicode string into ascii
		file_path=unicodedata.normalize('NFKD', file_path).encode('ascii','ignore')
		
		#downloading the neccesary files from the dropbox
		md, res = client.files_download(file_path)
		data = res.content
		
		#set the local file path where we want the files to be synced and stored.
		file_path=file_path.replace(DROPBOX_SYNC_LOCATION,"/home")
		homedir = os.environ['HOME']+DROPBOX_SYNC_LOCATION
		file_path=homedir+file_path
		#if file doesn't exist then create the respective directories before writing it to disk.
		if not os.path.exists(os.path.dirname(file_path)):
			try:
				os.makedirs(os.path.dirname(file_path))
			except OSError as exc: # This condition guards against the race condition
				if exc.errno != errno.EEXIST:
					raise
		with open(file_path, "w+") as f:
			f.write(data)


#RaceCondition : A race condition occurs when two or more threads can
#access shared data and they try to change it at the same time. 
#Because the thread scheduling algorithm can swap between threads at any time, 
#you don't know the order in which the threads will attempt 
#to access the shared data. Therefore, the result of the change 
#in data is dependent on the thread scheduling algorithm, i.e. 
#both threads are "racing" to access change the data.
