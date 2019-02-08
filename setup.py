from setuptools import setup, find_packages

setup(
    name='sphinx_example',
    version='0.0.1',
    description='This is an example project',
    packages=find_packages(),    
    install_requires=['sphinx >= 2.0.0'],
)
