from setuptools import setup, find_packages

setup(
	name='permission_exchanger',
    version='1.0.1',
    author="Serhii Poprovka",
    packages=find_packages('src', include=["src.permission_exchanger", "src.permission_exchanger.*"]),
    package_dir={'': 'src'},
)