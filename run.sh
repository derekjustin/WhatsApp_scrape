# Upgrade pip using pip (this is just hygenic, good practice).
pip install --upgrade pip

# Install all of your project's dependencies.
pip install -r requirements.txt

# Install *this* project itself, in development mode.
python setup.py develop

echo "####################################\n"
echo "        RUNNING PYTHON TESTS\n"
echo "####################################\n"
# Run tests!
py.test

python scrape/print_tools.py