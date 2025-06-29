from setuptools import setup, find_packages
from pathlib import Path

def get_requirements(file_path):
    """
    Reads the requirements from a file and returns them as a list.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements=[req.replace('\n','') for req in requirements ]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(
    name='Role Based Access Chatbot',
    version='0.1',
    author='Ayaz ul haq ',
    author_email='syedthescientist@gmail.com',
    description='A chatbot that provides role-based access to users',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)