import setuptools
import os
from os.path import splitext

long_description = """
This package is required for cvttf (https://pypi.org/project/cvttf)\n
This part is separated from the main package because CJK fonts have large file sizes and cannot fit within the limit of 60 MB.
"""

data_files = []

for folder in os.listdir('.'):
    if folder[:6] == 'cvttf_':
        package_name = folder
        for file in os.listdir('./'+folder):
            if splitext(file)[1].lower() in ['.ttf', '.ttc', '.otf']:
                data_files.append(folder+'/'+file)
                break
        else:
            raise FileNotFoundError('Font file not found.')
        break  # This line will only be executed if previous for-loop was "brake"d.
else:
    raise FileNotFoundError('Font file not found.')

setuptools.setup(
    name=package_name,
    version="1.0",
    author="Issac Lin",
    author_email="issaclin32@gmail.com",
    description="Font file for CVTTF",
    long_description=long_description,
    long_description_content_type="text",
    url="https://github.com/issaclin32/CVTTF",
    packages=[package_name],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    data_files=data_files,
)