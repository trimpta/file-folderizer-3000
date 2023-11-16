#Auther:trimpta
#program:file-folderizer-3000
#17:17 16/11/2023

import os

def get_file_list():
    return [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]

def createFolder(folder:str):
    path=os.path.join(os.getcwd(),folder)
    os.mkdir(folder)
    print(f"Created new folder:{folder}")

def movefile(file:str,folder:str):
    file = os.path.join(os.getcwd(),file)
    name_new = file.lstrip(file[0:file.find("]")+1])
    destination = os.path.join(os.getcwd(),folder,name_new)
    os.rename(file,destination)
    print(f"Moved {file} to {folder}.")
    #moves {file} from working dir to dir/folder after removing the [folder] prefix

print(f"Currently executing program in {os.getcwd()}")
while True:
    for i in get_file_list():
    
        if i.startswith("["):
            print(f"File:{i}")
            try:

                folder=i[1:i.find("]")]
                print(f"Folder:{folder}")
                if os.path.exists(folder):
                    if not os.path.isdir(folder):
                        raise ValueError("sorry bro ur dum dum")
                else:
                    createFolder(folder)
                
                movefile(i,folder)
            
            except Exception as Error:
                print(f"An error occurred: {Error}")
