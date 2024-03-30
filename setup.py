from setuptools import find_packages,setup
from typing import List

e_value='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements
    '''
    requiremensts=[]
    with open(file_path) as file_obj:
        requiremensts=file_obj.readlines()
        requiremensts=[req.replace("\n","") for req in requiremensts]

        if e_value in requiremensts:
            requiremensts.remove(e_value)
    return requiremensts

setup(
name='Ml_project',
version='0.0.1',
author='nitin',
author_email='nitnpawar4315@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)