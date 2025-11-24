from setuptools import setup, find_packages

setup(
    name='GabrielsPythonToolBox',          
    version='1.9.2',                       # "fundemental change"."finished feature"."bug fix"
    packages=find_packages(),              
    install_requires=[                     
        "matplotlib>=3.10.6,<3.11",
        "PyYAML>=6.0.2,<7.0",
        "pytest>=8.4.2,<8.5",
        "pytest-cov",
        "pytest",
        "setuptools"


    ],
    author="Gabriel Røer",
    author_email="NorgeSkiFollo@gmail.com",
    description="A collection of my useful Python tools",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/NorgeSkiFollo/GabrielsPythonToolBox.git",  
    classifiers=[                          
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
)
