import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="via",
    version="0.0.1",
    author="Keming Yang",
    author_email="kemingy94@gmail.com",
    description="initialize your repos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kemingy/via",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
