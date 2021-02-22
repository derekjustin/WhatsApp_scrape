# Upgrade pip using pip (this is just hygenic, good practice).
pip install --upgrade pip

# Install all of your project's dependencies.
pip install -r requirements.txt

# Install *this* project itself, in development mode.
python setup.py develop

echo "####################################\n"
echo "        RUNNING STYLE GUIDE\n"
echo "####################################\n"

pep8 --show-source --show-pep8 --ignore=E501 scrape/

echo "####################################\n"
echo "        RUNNING PYTHON TESTS\n"
echo "####################################\n"
# Run tests!
py.test

python -c 'from scrape.print_endpoints import *; print_endpoints()'
