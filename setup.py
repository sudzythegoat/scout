import subprocess
import sys

def install_libraries(requirements_file):
    with open(requirements_file, 'r') as file:
        libraries = file.readlines()
    
    for library in libraries:
        library = library.strip()
        if library:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])

if __name__ == '__main__':
    requirements_file = 'requirements.txt'
    install_libraries(requirements_file)
