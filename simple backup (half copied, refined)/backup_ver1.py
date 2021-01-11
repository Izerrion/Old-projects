import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# example on our OS:
source = ['/root/Documents/Notes']

# 2. The backup must be stored in a
# main backup directory
# example on our OS:
target_dir = '/root/HDD/backup'

# 3. The files are backed up into a zip file
# 4. Name of the zip file archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#Create the target directory if it is not present
#if not os.path.exists(target_dir):
#    os.mkdir(target_dir)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

#Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Succesful backup to', target)
else:
    print('Backup FAILED')