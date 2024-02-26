#---------------------------------------------------------------------------#
#
#
#Purpose: Rename files
#
#
#
#Author:     Patches56
#
#
#Created:    2/11/2024
#----------------------------------------------------------------------------#
import os

def main():
    # Create the empty arrays
    imgFiles = []        # Image files
    vidFiles = []        # Video files
    musFiles = []        # Music files

    lowFiles = []        # allFiles in lower case
    allFiles = []        # Image, Video, and Music files
    lowPrefix = []       # Prefix all lower case of all files
    
    #Display welcome to the media rename program
    print("Welcome to the Media Re-name Program\n")
    print("This program will expect a folder named 'Media' to contain all the media files that will be renamed. It will rename in order image, video, and music files.\n")
      


   # Build the path from the current folder
    path = os.path.dirname(os.path.realpath(__file__))
    path = f"{path}//Media"

    print(path)

 #Verify the media folder exist
    if os.path.exists(path) != True:
        print("---------\n)| Error |\n---------")
        print("Media sub folder does not exist . please create the folder")
        print("and place your media files within the folder.\n")
        exit(-1)


    # Assign prefix variable to user input
    # Assign startNum variable to user input
    prefix = input("Enter the prefix to use for the remaining:")
    startNum = float(input("Enter the starting number for the renumbering:"))

    createLists(imgFiles,vidFiles,musFiles,lowFiles,lowPrefix,path)
    rename_musicfiles(path,musFiles,lowFiles,prefix,startNum)
    printfiles(path)

def createLists(imgFiles,vidFiles,musFiles,lowFiles,lowPrefix,path):
    music_ext=('wav','m4a','flac','mp3','wma','aac')
    for files in os.listdir(path):
        lowFiles.append(files.lower())
        if files.endswith(music_ext):
            musFiles.append(files.lower())
    print(musFiles)    

def rename_musicfiles(path,musFiles,lowFiles,prefix,startNum):
    txt_ext=('txt','docx')
    count_music_files=0
    newname =''
    for file in musFiles:
        if not file.endswith(txt_ext):
            sufix = file.split('.')[1]
            num=str(startNum)
            newname=prefix+'_'+num+'.'+sufix
            startNum = startNum+1

            if newname not in lowFiles:
                #print(path+file)
                os.rename(f"{path}//{file}",f"{path}//renamed_Files//{newname}")
                count_music_files +=1

def printfiles(path):
    music_ext=('wav','m4a','flac','mp3','wma','aac')
    for files in os.listdir(path):
        
        if files.endswith(music_ext):
            print(files)
    

if __name__=='__main__':
    main()


