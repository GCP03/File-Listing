import os
#mypath="f:\\music\\"
mypath=input("Enter directory to scan (e.g. c:) : ")
outfile="c:\\users\\glenn\\filelist.csv"
outfile=input("Enter name for output (e.g. c:\filelist.txt)")

scan_dir(mypath)

def scan_dir(dir):
    try:
        with open(outfile, mode='w+') as f:
            try:
                for name in os.listdir(dir):
                    #use this if you want the path along with filename
                    path = os.path.join(dir, name)
                    if os.path.isfile(path):
                        print (path)
                        f.write(path + '\n')
                    else:
                        scan_dir(path)
            except FileNotFoundError:
                print(f"Error! Can't open directory {dir}, please check directory name and try again.")
            except:
                print("Error!  Try again")
    except:
        print("Error opening file for write.")
    else:
        print(f"\nOutput written to {outfile}")
