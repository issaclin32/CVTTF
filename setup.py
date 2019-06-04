import os
import time
import setuptools
from setuptools.command.install import install
from pkg_resources import DistributionNotFound, get_distribution
from distutils.sysconfig import get_python_lib
import urllib.request as req  # urlretrieve
import zipfile

#with open("README.md", "r") as fh:
#    long_description = fh.read()

def report_hook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    if duration > 0:
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)
        print('%d%% (%d MB) completed, %d KB/s   ' % (percent, progress_size / (1024 * 1024), speed), flush=True, end='\r')


# Using post-installation commands to download font files since PyPI does not support packages larger than 60MB.
class RedefinedInstallCommand(install):
    def run(self):
        install.run(self)  # run installation

        # --- post-installation commands ---

        # not using cvttf.__file__ since there is a "cvttf" folder under current path
        CVTTF_ROOT_PATH = get_python_lib()+'\\cvttf'  # under site-packages
        if not os.path.isdir(CVTTF_ROOT_PATH):
            raise FileNotFoundError(f'Error: path "{CVTTF_ROOT_PATH}" cannot be found. Package "CVTTF" is probably not correctly installed.')

        print('Downloading font files from Github...')
        req.urlretrieve('https://github.com/issaclin32/CVTTF/raw/master/cvttf_fonts.zip', CVTTF_ROOT_PATH+'\\cvttf_fonts.zip', report_hook)

        print('Extracting...')
        with zipfile.ZipFile(CVTTF_ROOT_PATH+'\\cvttf_fonts.zip') as f:
            f.extractall(CVTTF_ROOT_PATH)

        os.remove(CVTTF_ROOT_PATH+'\\cvttf_fonts.zip')
        print('Font files are successfully installed.')
        return

def get_dist(package_name):
    try:
        return get_distribution(package_name)
    except DistributionNotFound:
        return None


install_requires=['numpy', 'Pillow', 'fontTools']
if get_dist('opencv_python') is None and get_dist('opencv_contrib_python') is None:
    install_requires.append('opencv_contrib_python')


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
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'cvttf': []},
    include_package_data=False,
    data_files=[],
    cmdclass={
        'install': RedefinedInstallCommand,
    },
    scripts=['aha.py']
)