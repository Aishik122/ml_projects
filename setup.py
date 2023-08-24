from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this function returns a list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[x.replace("\n", "") for x in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
setup(
    name='ml_project',
    version='0.0.1',
    author='Aishik',
    author_email='aishikchatterjee12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)