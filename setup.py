import re

from setuptools import setup, find_packages


VERSION_FILE = 'src/_version.py'
verstrline = open(VERSION_FILE, 'rt').read()

print(verstrline)

VERSION_REGEX = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VERSION_REGEX, verstrline, re.M)
if mo:
    version_string = mo.group(1)
else:
    raise RuntimeError(f'Unable to find version string in {VERSION_FILE}')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='refresh_repositories',
    version=version_string,
    description='Refresh local GitHub repositories',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)
