import os,sys
import shutil
import csv
currentdir=os.getcwd()
folders_settings =currentdir + r'\FolderSettings.csv'
os.chdir('C:')
os.chdir(os.path.join(os.environ['HOMEPATH'], 'Desktop'))
desktop_directories=os.listdir('.')
clear=False

folders=[]
with open(folders_settings) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        folders.append(row)

def getFolders():
    return folders

def path(file,folder_type):
    if not os.path.exists(folder_type):
        os.makedirs(folder_type)
    shutil.move(file,folder_type)
    return

def create_folder(folder_name,extn):
    #folder_name=input("Enter the Name of the folder you would like to create \n")
    #folder_extensions=input("Enter the extensions seperated by commas (i.e .jpg, .pdf, .docx, etc) /n ").split(",")
    folder_extensions=str(extn).split(',')
    folder_extensions.insert(0,folder_name)
    folders.append(folder_extensions)
    return

def remove_folder(folder_name):
    for folder in folders:
        if folder[0] == folder_name:
            folders.remove(folder)
    return


def CleanDesktop():
   # print("Getting all Files........")
   # print("Moving the Following Files")
    for file in desktop_directories:
        if os.path.isfile(file):
            #print(file)
            file_name, file_extension = os.path.splitext(file)
            #print (file_extension)
            for folder in folders:
                name=folder[0]
                if file_extension in folder[1:]:
                    path(file,name)
                    clear=True
            if not clear:
                path(file,"Other")
        clear=False
    return


def saveFolders():
    with open(folders_settings, mode='w',newline='') as csvfile:
                writer=csv.writer(csvfile,delimiter=',')
                for folder in folders:
                    writer.writerow(folder)
    return


