from setuptools import find_packages, setup
from typing import List

HYFON_E_DOT="-e ."



def get_requirements(filepath:str)->List[str]:
    '''
    this function will return the list of requrements 
    '''
    requirements=[]
    with open(filepath) as file_object:
        requirements=file_object.readline()
        requirements=[req.replace ("\n","") for req in requirements]
        if HYFON_E_DOT  in requirements:
            requirements.remove(HYFON_E_DOT)

setup(
name="mlproject",
version="0.0.1",
author="Siddharth Rai",
author_email="siddharth23153065@akgec.ac.in",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)