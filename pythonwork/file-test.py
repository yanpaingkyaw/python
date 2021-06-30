import glob
import os
from shutil import copyfile
from datetime import datetime

path = "C:\\Users\\Lenovo\\Downloads\\"
path_findAll = path + "*" 
paste_Path  = "C:\\Users\\Lenovo\\Documents\\Python_Copy_Paste_Folder\\"

#grab the latest file
list_of_files = glob.glob(path_findAll) # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

print("Before Rename:")
print(latest_file)

#set filename with current date and time
now = datetime.now()
filename = now.strftime("%d_%m_%Y %H_%M_%S") + ".xls"


#Rename file
print("After Rename:")
rename_file = path + filename
os.rename(latest_file, rename_file)
print(rename_file)

#file copy and paste operation
pasteDestination = paste_Path + filename
copyfile(rename_file, pasteDestination)
print("Copy to below destination:")
print(pasteDestination)