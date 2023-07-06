import os
import shutil
from_dir="C:/Users/ACER/Downloads"
to_dir="C:/Users/ACER/Downloads/output"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(extension)
    if extension =="":
        continue
    if extension in [".doc",".pdf",".dot",".docm",".docx"]:
        path1=from_dir+'/'+i
        path2=to_dir+"/"+"document"
        path3=to_dir+"/"+"document"+"/"+i
        if os.path.exists(path2):
            print("moving "+i+"......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+i+"......")
            shutil.move(path1,path3)
    
        