from setuptools import setup, find_packages

setup(
	name='permission_exchanger',
    version='1.0.1',
    author="Serhii Poprovka",
    packages=find_packages(include=["src", "src.*"]),
    package_dir={'': 'src'},
)