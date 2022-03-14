# On Terminal

ls         # Directory listing
clear      # clear screen
man ls     # get more information on an command
pwd         #present working directory
cd Desktop   # change directory to Desktop
mkdir folder_name     #make directory
touch file_name.txt       # create a text file named file_name
history             # shows all types commands
cp old_file new_file          # for copying files
mv                             # cut or move files
rm file_name                # remove / delete file

# sudo command : To execute command with super user previllege


# example

pwd
cd Desktop/
mkdir test
cd test/
touch myfile.txt
cp myfile.txt new_file.txt
ls -l                         # for listing
mkdir testdir
cd testdir/
touch newfile.txt
cd..                        # go to 1 directory behind
cp -r testdir/newdir
clear
mv newfile.txt oldfile.txt
rm myfile.txt
ls -l
rm -r newdir/                    # for deleting folder also
cat test.txt                     # file read
cat -n test.txt                   # read line numbers also
head test.txt                     # first 10 lines will show
head -n 5 test.txt                 # show 5 lines from top
tail test.txt                      # show 10 lines from bottom
