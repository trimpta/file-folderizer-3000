#Auther:trimpta
#program:file-folderizer-3000
#17:17 16/11/2023

import os

def getList(File:bool = True):
    if File:
        return [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    else:
        return [f for f in os.listdir(os.getcwd()) if os.path.isdir(f)]

def createFolder(folder:str):
    path=os.path.join(os.getcwd(),folder)
    os.mkdir(folder)
    print(f"Created new folder:{folder}")

def movefile(file:str,folder:str):
    file = f"{os.getcwd()}/{file}"
    destination = f"{os.getcwd()}/{folder}/{file}"
    os.rename(file,destination)
    #moves {file} from working dir to dir/folder

while True:
    for i in getList():

        folderlist = getList(False)

        try:

            folder=i[1:i.find("]")]
            if folder not in folderlist:
                createFolder(folder)
            
            movefile(i,folder)
        
        except Exception as Error:
            print(f"An error occurred: {Error}")
