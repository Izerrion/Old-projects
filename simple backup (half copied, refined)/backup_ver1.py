import os
import time

source = ['/root/Documents/Notes']


target_dir = '/root/HDD/backup'


target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'



zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Succesful backup to', target)
else:
    print('Backup FAILED')
