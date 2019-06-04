import os
import setuptools
from pprint import pprint
from setuptools.command.develop import develop
from setuptools.command.install import install

#with open("README.md", "r") as fh:
#    long_description = fh.read()

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(self)

font_dir = 'cvttf/fonts'
font_files = {}

for dirName, subDirs, files in os.walk(font_dir):
    for file in files:
        if os.path.isfile(dirName+'/'+file):
            dirName = dirName.replace('\\', '/')
            if dirName in font_files:
                font_files[dirName].append(dirName+'/'+file)
            else:
                font_files[dirName] = [dirName+'/'+file]


setuptools.setup(
    name="cvttf",
    version="0.0.1",
    author="Issac Lin",
    author_email="issaclin32@gmail.com",
    description="Draw text on OpenCV images using TTF/OTF fonts",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/issaclin32/CVTTF",
    packages=['cvttf'],
    install_requires=['numpy', 'Pillow', 'fontTools'],
    # not using data_dir parameter due to Anaconda compatibility issues
    data_files=font_files.items(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)