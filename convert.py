import os

files = os.listdir('designs')
for file in files:
    file_name = file.split(".")[0]
    os.system("pyuic5 -x 'designs/{0}.ui' -o 'forms/{0}_form.py'".format(file_name))
