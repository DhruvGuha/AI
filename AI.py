import os
import shutil
import sys
import time
import random


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt' , '.zip' , '.pptx' , '.docx' , '.fdf'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "Programming_files" : ['.c','.cgi','.pl','.class','.cpp','.cs','.h','.java','.php','.py','.sh','.swift','.vb','.htm','.html']
}

from_dir = "C:/Users/Dhruv/Downloads"
to_dir = "C:/Users/Dhruv/Downloads/Downloaded_Files"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    name , extension = os.path.splitext(file_name)
    
    if extension == "":
        continue

    for key , value in dir_tree.items():
        if extension in value or extension in [x.upper() for x in value]:

            path1 = from_dir + '/' + file_name                       # Example path1 : c102assets/dog.jpg        
            path2 = to_dir + '/' + key                     # Example path2 : c102assets/Image_Files      
            path3 = to_dir + '/' + key + '/' + file_name   # Example path3 : c102assets/Image_Files/dog.jpg

            if os.path.exists(path2):
                print("Moving " + file_name + ".....")
                # Move from path1 ---> path3
                shutil.move(path1, path3)

            else:
                os.makedirs(path2)
                print("Moving " + file_name + ".....")
                shutil.move(path1, path3)

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name , ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key , value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                file_name=os.path.basename(event.src_path)
                print("Downloaded",file_name)
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name
                if os.path.exists(path2) :
                    print("Directory exists")
                    print("Moving" + file_name + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else :
                    print("Making directory")
                    os.makedirs(path2)
                    print("Moving" + file_name + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name, "has been created!")

    def on_modified(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name , "has been modified!")

    def on_moved(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name , "has been moved!")

    def on_deleted(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name , "has been deleted!")

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try :
    while True:
        time.sleep(2)
        print("running...")

    
except KeyboardInterrupt :
    print("Stopped")
    observer.stop()
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

