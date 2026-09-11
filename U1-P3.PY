import os   #Creating folders,file

project_root = 'ai_project'
dirs_to_create = [  
    os.path.join(project_root, 'data'),
    os.path.join(project_root,'logs'),
    os.path.join(project_root,'config'),
    os.path.join(project_root,'requriements.txt'),
    os.path.join(project_root, 'src'),
    os.path.join(project_root,'.env')
]

for d in dirs_to_create:
    os.makedirs(d, exist_ok=True)
    print(f'Created directory: {d}')


files = [
    os.path.join(project_root, 'src', 'main.py'),
    os.path.join(project_root, 'src', 'utils.py'),
    os.path.join(project_root, 'README.md'),
    os.path.join(project_root, '.env.example'),
    os.path.join(project_root, 'requirements.txt'),
]

for f in files:
    with open(f, 'w') as file:
        if 'README' in f:
            file.write('# My AI Project\nThis is a standard template project.')
    print(f'Created file: {f}')


project_root = 'ai_project'
dirs = [
    os.path.join(project_root,'logs'),
        os.path.join(project_root,'config'),
        os.path.join(project_root,'requriements.txt'),
        os.path.join(project_root, 'src'),
        os.path.join(project_root,'.env')
   
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f'Created directory: {d}')

# Create empty source files and README.md
files = [
    os.path.join(project_root, 'src', 'main.py'),
    os.path.join(project_root, 'src', 'utils.py'),
    os.path.join(project_root, 'README.md'),
    os.path.join(project_root, '.env.example'),
    os.path.join(project_root, 'requirements.txt'),
]



