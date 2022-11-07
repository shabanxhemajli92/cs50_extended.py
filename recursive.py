import os
parent_dir="/home/dci-admin/Documents/cs50_extended.py/test"

os_path=(os.listdir(parent_dir))
#print(os_path)


list_comp_file=[file for file in os_path if os.path.isfile(parent_dir+"/"+file)]#file directory

list_comp_dir=[element  for element in os_path if not os.path.isfile(parent_dir+"/"+element)]#parent directory

def traverse(folders):
    if len(folders) == 0:
        pass
    else:
        for index,folder in enumerate(folders):
            slicing=folders[index + 1:]
            print(slicing)
            print(folder)
            
traverse(list_comp_dir)         