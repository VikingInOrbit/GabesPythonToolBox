# Gabriel's Toolbox 
## What is this?
Gabe's Python Toolbox is a collection code snippets. It's not a specialized library for one thing. it's a general-purpose grab-n-go for code snippets i find usful.

## Setup Guide
in terminal for project 

'''
py -m pip install git+https://github.com/VikingInOrbit/GabesPythonToolBox.git
'''


## How to install

Quick install for development and testing:

```bash
python -m venv .venv
python -m pip install pip-tools
pip-compile requirements.in
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Development Setup

How to commit code destined for dev:

```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type pre-push
pre-commit install --hook-type commit-msg
pre-commit run --all-files
```


If pre-commit fails:

```bash
pytest -q --maxfail=1  
tox 
isort .  
black .
```


### comands
#### unit test
'''
pytest UnitTest -v
'''
#### get filestucture
'''
tree /F /A > folder_tree.txt
'''

## Current Features

### ControllSoftwere
- StateManager

### Utility Functions
Documentation Here(in progress)
- Time Managment
- configManager
- Collor
- UnitConverter
- Debug.log


### Data Processing
Documentation Here(in progress)
- signal Filtering
- input to data managment
- csv reding, handeling and consol printing

## Working on
- Unit tests
- State Machine
- Pyside6
- Programin Patterns

## What's Next?
- future code i need and want to shere
- QuaternionTools
- SensorFusion
- arduinio lib
- InverseKinematics
- csv telemetry frame reader ,w multipex suport
- config manager gui
- debug logfile
- Sorting of file structure (No new peojects before done)


##  Why Should You Use This?
It's modular, use waht you need, grab the function you need and move on.
