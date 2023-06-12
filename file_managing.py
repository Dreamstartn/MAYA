import os
import shutil
import time

# Define the source and destination folders
src_folder = "C:\\Users\\nites\\Downloads"
dst1_folder = "D:\\pictures"
dst2_folder = "D:\\study doucuments"
dst3_folder = "E:\\all softwares"
dst4_folder = "D:\\Videos"
dst5_folder = "D:\\audio"
# Create a function to move files
def move_media(src_folder, dst_folder):
    for filename in os.listdir(src_folder):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.jpg', '.png', '.gif','.jpeg']:
            # Move the file to the destination folder
            shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))
        if ext in ['.pdf', '.docx', '.xlsx' , '.pptx','.csv']:
            # Move the file to the destination folder
             shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))  

def move_documents(src_folder, dst_folder):
    for filename in os.listdir(src_folder):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.pdf', '.docx', '.xlsx' , '.pptx']:
            # Move the file to the destination folder
             shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))  
            
def move_video(src_folder, dst_folder):
    for filename in os.listdir(src_folder):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.mp4', '.mov', '.mkv' , '.webm','.mpej-4']:
            # Move the file to the destination folder
             shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename)) 

def move_audio(src_folder, dst_folder):
    for filename in os.listdir(src_folder):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.mp3', '.aac', '.wav']:
            # Move the file to the destination folder
             shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))  


def move_software(src_folder, dst_folder):
    for filename in os.listdir(src_folder):
        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.rar', '.iso', '.zip']:
            # Move the file to the destination folder
             shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))  

# Create a loop to continuously check for new files
while True:
    # Check for new files every 10 seconds
    time.sleep(10)
    # Call the move files function when a new file is detected
    move_media(src_folder, dst1_folder)
    move_documents(src_folder, dst2_folder)
    move_software(src_folder,dst3_folder)
    move_video(src_folder,dst4_folder)
    move_audio(src_folder,dst5_folder)