from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="via",
    version="0.0.2",
    author="Keming Yang",
    author_email="kemingy94@gmail.com",
    description="initialize your repos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kemingy/via",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'via=via:main',
        ],
    },
)
