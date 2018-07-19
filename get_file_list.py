from os import listdir,stat
from os.path import isfile, join



def get_files(mypath):
    for f in listdir(mypath):
        if isfile(join(mypath, f)) and stat(join(mypath, f)).st_size > 0:
            yield f

file_name=get_files("c:\\users\\glenn\\")
out_file="c:\\users\\glenn\\filelist.csv"
with open(out_file, mode='w+') as f:
    f.write(next(file_name) + ',')