import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()


# Package requirements
requirements = [
    'numpy==1.17.1',
    'pandas==0.25.1',
    'pkg-resources==0.0.0',
    'prettytable==0.7.2',
    'python-dateutil==2.8.0',
    'pytz==2019.2',
    'six==1.12.0',
]


setuptools.setup(

    name='python data profiler',

    version='0.1',

    author="Thaneshwor Joshi",

    author_email="thaneshwor10@gmail.com",

    description="A tool to profile csv, tsv, fwf, etc files",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/Thaneshwor/python-data-profiler",

    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    install_requires=requirements,

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

)
