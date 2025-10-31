from setuptools import setup, find_packages
from typing import List


# A custom function to get all the packages as a list from requirements.txt
def get_requirements(file_path:str) -> List:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace('\n', '') for requirement in requirements]

        # removing -e . from requirements as it is not a package and only triggers setup.py
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements


# The setup for my project
setup(
    name="House Price Prediction",
    version="0.0.1",
    author="Muhammed Ibrahim",
    author_email="muhammedibrahimshabandri@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)