# used to build applications as a package that can be used for distribution or even deploy packages on 
# Pypi  

from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_name: str) -> List[str]:
    requirements = []

    with open(file_name) as file_obj:
        ''' 
        this function will return requirements as a list of strings
        '''
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]

        if '-e .' in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements

setup(
    name="mlProject",
    version="0.0.1",
    author="Hamzah",
    author_email="hamzahshaikh529@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
