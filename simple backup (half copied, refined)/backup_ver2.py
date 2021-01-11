import os
import time

# source dir
source = ['/root/Documents/Notes']

# target dir
target_dir = '/root/HDD/backup'

# target dir check
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# backed up in zip with the current day as the name of the subdir in main dir
today = target_dir + os.sep + time.strftime('%Y%m%d')
# current time is the name of zip
now = time.strftime('%H%M%S')

# name of zip
target = today + os.sep + now + '.zip'

# subdir check
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# zip command
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successfully backed up to', target)
else:
    print('Backup FAILED')