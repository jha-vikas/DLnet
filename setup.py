
from setuptools import find_packages, setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name='DLnet',
      version='0.0.1',
      description='Neural Net from Scratch',
      long_description=long_description,
      license='MIT',
      author='Vikas Jha',
      author_email='vikasjhanitk@gmail.com',
      packages=['DLnet'],
      install_requires=['numpy']

     )