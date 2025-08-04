"""
Package setup.
"""


from setuptools import find_packages, setup


with open('README.md', encoding='utf-8') as file:
    long_description = file.read()


setup(
    name = 'nephila-logging', # Installation name (pip install <name>)
    version = '0.0.0',
    description = 'Nephila loggers',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Nephila Ecosystem',
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
    include_package_data = True,
)