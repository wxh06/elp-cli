import setuptools


setuptools.setup(
    name="elp",
    author="汪心禾",
    author_email="wangxinhe06@gmail.com",
    description="elpsh.com's command-line interface",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wxh06/elp-cli",
    packages=['elp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
