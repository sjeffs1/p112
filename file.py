import os
import shutil

from_dir = "C:/Users/Shlok/Downloads"
to_dir = "C:/Users/Shlok/Downloads/monkey"

list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extensions = os.path.splitext(file_name)
    if extensions == "":
        continue

    if extensions in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "document_files"
        path3 = to_dir + "/" + "document_files" + "/" + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "...")

            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "...")
            shutil.move(path1, path3)
