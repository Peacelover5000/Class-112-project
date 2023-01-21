import os
import shutil

from_dir = "/Users/apple/Downloads"
to_dir = "/Users/apple/Desktop/Downloaded_files_waste"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in ['.ppt', '.xls', '.csv', '.pdf', '.txt','.zip','.doc','.docx','py']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_files"
        path3 = to_dir + '/' +  "Document_files" + '/' + file_name

        if os.path.exists(path2):
             print("Moving " + file_name + ".....")
             shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)
