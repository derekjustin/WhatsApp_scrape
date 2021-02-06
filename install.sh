echo "####################################\n"
echo "    INSTALLING WHATSAPP SCRAPPER\n"
echo "####################################\n"

# Create a venv using the name of the directory we're in, and created a symlink
#to the activate script.
python3 -m venv "$(basename `pwd`)-venv" && ln -s "$(basename `pwd`)-venv"/bin/activate activate

# Activate the virtualenv (this just adds the Python environment to your $PATH variable).
source activate

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


echo "\n\n######################################################################\n"
echo "    TO RUN A FEATURE OF THE SCRAPER RUN ONE OF THE COMMANDS BELOW\n"
echo "######################################################################\n"

echo "   foo\n"
echo "      description: print hello world\n"
echo "   scrape\n"
echo "      description: Scrape the web and join WhatsApp groups\n"

