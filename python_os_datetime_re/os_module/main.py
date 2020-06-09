import os

# file_path= os.path.abspath(__file__)
# print(file_path)
# file_dir = os.path.dirname(file_path)
# print(file_dir)
# project_dir = os.path.dirname(file_dir)
# print(project_dir)

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /home/idris/Docker_group/python_os_datetime_re
# files_dir = project_dir + '/files/'

files_dir = os.path.join(project_dir, 'files')
print(os.getcwd())

os.chdir(files_dir)

print(os.getcwd())

with open('file1.txt', 'w') as f:
    f.write('salam')

mk_folder_dir = os.path.join(project_dir, 'code')

os.chdir('..')
print(os.getcwd())

if not os.path.isdir(mk_folder_dir):
    os.mkdir(mk_folder_dir)

main_file_path = os.path.join(mk_folder_dir, 'main.py')
print(main_file_path)

with open(main_file_path, 'w') as f:
    f.write('''print('salam')
print(1+5)
''')
os.system(f'python {main_file_path}')