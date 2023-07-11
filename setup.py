from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = "simple google image scrapper for your computer vision tasks"

setup(
        name="pixel_collect", 
        version=VERSION,
        author="charles TCHANAKE",
        author_email="datadevfernolf@gmail.com",
        url="https://github.com/charleslf2/pixel_collect",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=open("README.md","r",encoding="utf-8").read(),
        packages=find_packages(),
        install_requires=["requests","beautifulsoup4"],  
        keywords=["Computer-vision","Images","Dataset","scrapping"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
