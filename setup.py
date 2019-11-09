import os
from setuptools import setup, find_packages

INSTALL_REQUIRED=[]
with open('requirements.txt') as f:
    INSTALL_REQUIRED = f.read().splitlines()

setup(name='azure_api',
      version='0.1',
      description='azure_api',
      url='https://github.com/kathuriaas/azure_api',
      author='Ashish Kathuria',
      author_email='',
      license='',
      packages=find_packages(),
      zip_safe=False,
      install_requires=INSTALL_REQUIRED)