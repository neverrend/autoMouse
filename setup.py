from setuptools import setup, find_packages

setup(
    name="automouse",
    version='0.0.1',
    url='https://github.com/neverrend/autoMouse',
    license='Apache License, Version 2.0',
    description='Tool for refreshing pages during tests because I am incredibly lazy',
    author='neverrend',
    packages=find_packages(),
    zip_safe=False
)
