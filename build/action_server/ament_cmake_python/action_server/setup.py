from setuptools import find_packages
from setuptools import setup

setup(
    name='action_server',
    version='0.0.0',
    packages=find_packages(
        include=('action_server', 'action_server.*')),
)
