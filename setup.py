from setuptools import find_packages,setup  # find_packages automatically find out all the packages that are available in the directory that we created 
from typing import List

HYPHEN_E_DOT='-e .'
# This function will return the list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
        
    
# Can be considered as the metadata information of the complete project
setup(
    name='StudentPerformanceIndicator',
    version='0.0.1', # Next version can be updated here and the entire package will be built
    author='Akash',
    author_email='akash.shantha@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   # Will automatically install these libraries

)