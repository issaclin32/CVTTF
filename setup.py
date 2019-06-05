import os
import setuptools
from pkg_resources import DistributionNotFound, get_distribution

#with open("README.md", "r") as fh:
#    long_description = fh.read()


def get_dist(package_name):
    try:
        return get_distribution(package_name)
    except DistributionNotFound:
        return None

install_requires=['numpy', 'Pillow', 'fontTools']
if get_dist('opencv_python') is None and get_dist('opencv_contrib_python') is None:
    install_requires.append('opencv_contrib_python')

# font packages
install_requires.extend(['cvttf-NotoSansCJK-Black', 'cvttf-NotoSansCJK-Bold', 'cvttf-NotoSansCJK-DemiLight',
                         'cvttf-NotoSansCJK-Light', 'cvttf-NotoSansCJK-Medium', 'cvttf-NotoSansCJK-Regular',
                         'cvttf-NotoSansCJK-Thin'])

# include files under cvttf/fonts into the package
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
    version="0.0.2",
    author="Issac Lin",
    author_email="issaclin32@gmail.com",
    description="Draw text on OpenCV images using TTF/OTF fonts",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/issaclin32/CVTTF",
    packages=['cvttf'],
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=False,
    data_files=font_files.items()
)
