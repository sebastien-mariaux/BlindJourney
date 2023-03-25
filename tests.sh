echo 'RUN TESTS...'
# coverage run --source='.' manage.py test
pytest

echo 'GENERATE COVERAGE...'
coverage report
coverage html


echo 'RUN AUTOPEP8...'
autopep8 $(git ls-files '**.py') --in-place --aggressive

echo 'RUN PYCODESTYLE...'
pycodestyle reverse_midjourney


echo 'RUN MYPY...'
mypy --config-file tox.ini reverse_midjourney


echo 'RUN PYLINT...'
pylint -j0 reverse_midjourney

