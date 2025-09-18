from setuptools import setup, find_packages

setup(
    name='GabrielsPythonToolBox',          # Name of your package
    version='1.6.0',                       # fundemental change.finished feature.bug fix
    packages=find_packages(),              # Automatically finds all packages
    install_requires=[                     # List your dependencies here
        "matplotlib>=3.9.2,<3.10"


    ],
    author="Gabriel Røer",
    author_email="NorgeSkiFollo@gmail.com",
    description="A collection of my useful Python tools",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/NorgeSkiFollo/GabrielsPythonToolBox.git",  # Replace with your repo URL
    classifiers=[                          # Classifiers for your library
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
)
