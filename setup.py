from setuptools import find_packages,setup
from typing import List


newvar = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This list contains the packages which presents in requiremnts.txt
    '''
    requiremnts = []
    with open(file_path) as file_obj:
        requiremnts = file_obj.readlines()
        requiremnts = [req.replace('\n','') for req in requiremnts]

        if newvar in requiremnts:
            requiremnts.remove(newvar)

    return requiremnts
setup(
   name='MLproject',
   version='0.0.1',
   author='Mohammed',
   author_email='bakrolmohammed2002@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt') #external packages as dependencies
)