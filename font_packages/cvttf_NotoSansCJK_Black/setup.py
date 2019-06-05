import setuptools

long_description = """
This package is required for <a href="https://pypi.org/project/cvttf">cvttf</a>.
This part is separated from the main package because CJK fonts have large file sizes and cannot fit within the limit of 60 MB.
"""

setuptools.setup(
    name="cvttf_NotoSansCJK_Black",
    version="1.0",
    author="Issac Lin",
    author_email="issaclin32@gmail.com",
    description="Font file for CVTTF",
    long_description=long_description,
    long_description_content_type="text",
    url="https://github.com/issaclin32/CVTTF",
    packages=['cvttf_NotoSansCJK_Black'],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    data_files=['cvttf_NotoSansCJK_Black/NotoSansCJKtc-Black.otf'],
)