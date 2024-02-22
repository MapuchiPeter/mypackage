from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Sample Python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    author='Mapuchi Peter Asmah',
    author_email='mapuchi.peter@gmail.com',
    download_url='https://github.com/mapuchipeter'
)