import setuptools

setuptools.setup(
    name="cvttf_NotoSansCJK_Black",
    version="0.0.1",
    author="Issac Lin",
    author_email="issaclin32@gmail.com",
    description="Font file for CVTTF",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
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