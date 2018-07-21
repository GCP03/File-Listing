#TODO: Add filtering on filetype

import os
#mypath="f:\\music\\"
mypath=input("Enter directory to scan (e.g. c:) : ")
outfile="c:\\users\\glenn\\filelist.csv"
outfile=input("Enter name for output (e.g. c:\\users\\glenn\\filelist.txt)")

def scan_dir(dir, f):
    try:
        for name in os.listdir(dir):
            #use this if you want the path along with filename
            path = os.path.join(dir, name)
            
            #check if the item is a file with size > 0
            if os.path.isfile(path) and os.path.getsize(path)>0:
                print (path + ' size of: ' + str(os.path.getsize(path)))
                #write the filename to the file
                f.write(path + '\n')
            else:
                #we hist a subdirectory, so recurse and rescan
                scan_dir(path, f)
    except FileNotFoundError:
        print(f"Error! Can't open directory {dir}, please check directory name and try again.")

try:
    f=open(outfile, mode='w+') 
except:
    print("Error opening file for write.")
    
scan_dir(mypath,f)
f.close()
print(f"\nOutput written to {outfile}")
