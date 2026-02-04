from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements():

    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open('requirements.txt') as file_obj:
        return [
            line.strip()
            for line in file_obj
            if line.strip() and not line.startswith("-")
        ]


setup(

name='ML_Project',
version='0.0.1',
author='Praneetha',
author_email='praneetharamagiri2006@gmail.com',
packages=find_packages(),
install_requires=get_requirements()

)