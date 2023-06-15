from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    ##############################################
    # Function will return a list of packages
    ##############################################
    
    requirements = []
    with open('requirements.txt') as temp_obj:
        requirements = temp_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        
    return requirements
    

setup(
    name='ML Projects',
    author='akshaybhat',
    author_email='akshaybhat422@gmail.com',
    version='0.0.1',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)