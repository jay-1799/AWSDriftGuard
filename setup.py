from setuptools import setup, find_packages

setup(
    name='awsdriftguard',
    version='0.1',
    packages=find_packages(include=['awsdriftguard']),
    install_requires=[
        'boto3',
        'requests',
    ],
    entry_points={
        'console_scripts': [
             'awsdriftguard = awsdriftguard.cli:main', 
        ],
    },
)
