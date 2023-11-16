#Auther:trimpta
#program:file-folderizer-3000
#17:17 16/11/2023

import os

def getList(File:bool = True):
    if File:
        return [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    else:
        return [f for f in os.listdir(os.getcwd()) if not os.path.isfile(f)]

def createFolder(folder:str):
    path=os.path.join(os.getcwd(),folder)
    os.mkdir(folder)
    print(f"Created new folder:{folder}")

def movefile(file:str,folder:str):
    file = f"{os.getcwd()}\\{file}"
    nameNew = file.lstrip(file[0:file.find("]")+1])
    destination = f"{os.getcwd()}\\{folder}\\{nameNew}"
    os.rename(file,destination)
    #moves {file} from working dir to dir/folder

print(f"Currently executing program in {os.getcwd}")
while True:
    for i in getList():
        if i.startswith("["):
            print(f"File:{i}")
            folderlist = getList(False)
            print(f"FolderList:{folderlist}")
            try:

                folder=i[1:i.find("]")]
                print(f"Folder:{folder}")
                if folder not in folderlist:
                    createFolder(folder)
                
                movefile(i,folder)
            
            except Exception as Error:
                print(f"An error occurred: {Error}")
