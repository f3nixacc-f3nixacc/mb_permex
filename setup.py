from setuptools import setup, find_packages

setup(
	name='permission_exchanger',
    version='1.0.1',
    author="Serhii Poprovka",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)