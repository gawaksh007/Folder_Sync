# Folder_Sync

#This method is rudimentary now as dropbox has changed their rules in regard of using their API's, a better scenario would be to use google drive API, most things would remain same about the process, if any doubt arises, mail me at gawaksh007@gmail.com

Setting Up and Usage:

1. Create a API on dropbox and set the authorization token in the config.py file.

2. Set the local directory on your pc that you want to sync with folders of other devices.

3. We will set up a cron job for the file fileDownload.py on our system. A cron job can be set up on Ubuntu by the following commands. crontab -e
Append the below line to the file with the appropriate path to the file.
*/2 * * * * /usr/bin/python /home/gawaksh/mystuff/FolderSync/fileDownload.py

This enables us to run the script fileDownload.py every 2 mins where the script iterates through the files on dropbox client and downloads the necessary files onto our system.

4. Run the file fileUpload.py in the background as a daemon. This script watches the folder that we specified in the config.py file as LOCAL_DIRECTORY_WATCH and fires an event whenever the specified folder undergoes any modification. The modified file is pushed to dropbox.

Installation and Dependencies

sudo pip install dropbox
sudo pip install watchdog

Additional Considerations

We might get the following warning on running the scripts
/usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#snimissingwarning. SNIMissingWarning
Also Refer to the below stackoverflow link and install the dependencies to solve the warning.
http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent

