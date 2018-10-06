import os
import shutil
import zipfile
# csgoDemoFileMover.py - Moves .dem files from csgofolder to another folder for backup

print("""Moves all .dem files from a choosen path to a entered destination.

You can enter any path and it will move all .dem files to the designated folder
(if the path has many folders/files it will take longer)
copy & paste csgo folder from explorer""")
print(r'example path: C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive')
print('')

targetpath = ''
csgopath = ''
zipfile_wanted = False

# csgo path enter
while True:
    csgopath = input(r'csgo folder path: ')

    if os.path.isdir(csgopath):
        break
    else:
        print('Error: Enter a valid directory Path')

# target path enter
while True:
    targetpath = input(r'target path/folder: ')
    print(targetpath)
    if os.path.isdir(targetpath):
        break
    else:
        print('Error: Enter a valid directory Path')


# zip file "yes or no" enter
yes = {'yes', 'y', 'ye'}
no = {'no', 'n'}
while True:
    zip_yn = input(r'Pack demos in Zip (compressed)? (Y/n): ')
    if zip_yn.lower() in yes:
        zipfile_wanted = True
        break
    elif zip_yn.lower() in no:
        zipfile_wanted = False
        break

print('csgopath: ' + csgopath)
print('targetpath: ' + targetpath)

for folderName, subfolders, filenames in os.walk(csgopath):
    # print('The current folder is ' + folderName)
    # print(os.path.isdir(folderName))
    for filename in filenames:
        if filename.endswith('.dem'):
            if os.path.isfile(os.path.join(folderName, filename)):
                shutil.move(os.path.join(folderName, filename),
                            os.path.join(targetpath, filename))
                print(os.path.join(folderName, filename) +
                      ' moved to ' + os.path.join(targetpath, filename))

    for subfolder in subfolders:
         # print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:

            if filename.endswith('.dem'):
                if os.path.isfile(os.path.join(folderName, filename)):

                    shutil.move(os.path.join(folderName, filename),
                                os.path.join(targetpath, filename))
                    print(os.path.join(folderName, filename) +
                          ' moved to ' + os.path.join(targetpath, filename))


if zipfile_wanted:
    os.chdir(targetpath)
    number = 1

    while True:
        zipFilename = 'DemoBackup' + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print(zipFilename)

    for files in os.listdir(targetpath):
        os.path.join(targetpath, files)
        with zipfile.ZipFile(zipFilename, 'a', compression=zipfile.ZIP_DEFLATED) as demzip:
            if not files.endswith('.zip'):
                demzip.write(files)
                os.remove(files)
                print(files + ' packed to ' + zipFilename)
