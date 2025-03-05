from setuptools import setup, find_packages

setup(
	name='permission_exchanger',
    version='1.0.2',
    author="Serhii Poprovka",
    packages=find_packages(include=["permission_exchanger", "permission_exchanger.*"]),
)
