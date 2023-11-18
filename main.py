#Auther:trimpta
#program:file-folderizer-3000
#17:17 16/11/2023

import os
import time

def date_printable():
    return f"{time.localtime()[2]}-{time.localtime()[1]}-{time.localtime()[0]}" #"date-month-year"

def time_printable():
    return f"{time.localtime()[3]}:{time.localtime()[4]}:{time.localtime()[5]}" #hour:minute:second

def get_file_list():
    return [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]

def create_folder(folder:str):
    path=os.path.join(os.getcwd(),folder)
    os.mkdir(folder)
    print(f"Created new folder:{folder}")

def movefile(file:str,folder:str):
    file = os.path.join(os.getcwd(),file)
    name_new = file[file.find("]")+1::]
    destination = os.path.join(os.getcwd(),folder,name_new)
    if os.path.exists(destination):
        prefix=file[file.rfind('.')::] if file.rfind('.')!=-1  else file[-1]
        name_copy = name_new[0:file.rfind('.')]
        destination = os.path.join(os.getcwd(),folder,name_copy+"(Copy)"+prefix)
        print("File already exists. Appending (copy) to file name.")
    os.rename(file,destination)

    print(f"Moved   {file} to {destination}.")
    #moves {file} from working dir to dir/folder after removing the [folder] prefix
    


log_file=f"folderizer-log-{date_printable() }.txt"

with open(log_file,"a") as f:
    f.write(f"Currently executing program in {os.getcwd()}\nTime:{time.ctime()}")
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
                                raise ValueError("User attempted to create folder which already exists as a file.")
                            
                        else:
                            create_folder(folder)

                        time.sleep(0.35)       #for mitigating windows error#and also it looks kinda cool with 0.4 or something
                        movefile(i,folder)
                        f.write(f'{date_printable()} {time_printable()}:       Moved       {i.lstrip(i[0:i.find("]")+1])} to {folder}.\n')

                    except Exception as Error:
                        print(f"{date_printable()}  An error occurred: {Error}")
                        f.write(f"{date_printable()} {time_printable()}    An error occurred: {Error}\n")
                        
        time.sleep(60)