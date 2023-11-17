#Auther:trimpta
#program:file-folderizer-3000
#17:17 16/11/2023

import os
import time

def time_printable():
    time_string = f"{time.localtime()[3]} {time.localtime()[4]}-{time.localtime()[5]} {time.localtime()[2]}-{time.localtime()[1]}"
    return time_string
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

log_file=f"folderizer-log-{time_printable()}.txt"

with open(log_file,"a") as f:
    f.write(f"Currently executing program in {os.getcwd()}\n")
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

                    time.sleep(1)       #for mitigating windows error
                    movefile(i,folder)
                    f.write(f'{time_printable()}:   Moved   {i.lstrip(i[0:i.find("]")+1])}  to  {folder}.\n')

                
                except Exception as Error:
                    print(f"An error occurred: {Error}")
                    f.write(f"An error occurred: {Error}\n")



