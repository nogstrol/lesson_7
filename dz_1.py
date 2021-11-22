import os

path = r'C:\Users\NGS\PycharmProjects\lesson_7'
projectname = 'my_project' 
folders = \
    ['settigs', 
     'mainapp',
     'adminapp',
     'authapp']


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)


fullPath = os.path.join(path, projectname)
createFolder(fullPath)

for f in folders:
    folder = os.path.join(fullPath, f)
    createFolder(folder)
