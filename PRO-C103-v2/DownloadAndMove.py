import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/aarsh/Downloads"
to_dir = "C:/Users/aarsh/Desktop/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        
            # Remember the path of the downloaded file is
            # returned from the event object of the on_created()
            # method?
            # We can get the path of the directory where the file is
            # created using event.src_path.

        for key, value in dir_tree.items():
            time.sleep(1)
             # Loop through all the items in the dictionary. For this,
            # we can use the <dic_name>.item() method that
            # returns the key and value of the dictionary.

            if extension in value:
                file_name = os.path.basename(event.src_path)
                # we need the actual name of the downloaded file
                # (excluding the directory path)
                # to form the correct path value strings for the source
                # and destination path to be used in shutil.move() method.
                # For this, we will use os.path.basename() on the
                # downloaded file. This method in Python is used to
                # get the basename in the specified path.
                
                # This method internally uses os.path.split() method
                # to split the specified path into a pair (head, tail).
                # os.path.basename() method returns the tail part
                # after splitting the specified path into (head, tail) pair.

                print("Downloaded " + file_name)

                # Create path variables:
                
                path1 = from_dir + '/' + file_name #name of the source path. 
                # Example: path1: Downloads/ImageName1.jpg
                
                
                path2 = to_dir + '/' + key
                # we want to create a new folder with that extension name 
                # and move the files to that folder.
                
                # Example: path2: D:/My Files/Image_Files
                
                path3 = to_dir + '/' + key + '/' + file_name # key is taken from dir_tree dictionary
                # to assign the destination path with the same file name as the source.
                
                # Example: path3: D:/MyFiles/Image_Files/ImageName1.jpg
                

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    # If the path is not created.
                    # Use os.makedirs() to create path2.

                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)
 
# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
    