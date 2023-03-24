# REVERSE MIDJOURNEY

Find the Midjourney prompt that generated those images!

*Work in progress*

## Installation

- Clone repository
- Install requirements `pip install -r requirements.txt`
- `./manage.py runserver`


## Code quality

- Run test & pipeline: `./tests.sh`
- Run pipeline: `./pipeline.sh`

Tests use Django testing module and generate a coverage report (which is not good ATM ;))

Pipeline includes :
- autopep8
- Mypy
- Pycodestyle
- Pylint