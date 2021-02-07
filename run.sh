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


echo "\n\n######################################################################"
echo "    TO RUN A FEATURE OF THE WEB SCRAPER PLEASE ENSURE"
echo "        1) You are currently logged in to your Google Account through Chrome"
echo "        2) You are using Chrome Version XXXXX"
echo "        3) You are logged into WhatsApp Web (https://web.whatsapp.com)"
echo "        4) The Google Chrome Browser is currently closed\n"
echo "    Once the steps above are verified execute one of the commands" 
echo "        below to start scraping!" 
echo "######################################################################\n"

echo "   foo"
echo "      description: print hello world\n"
echo "   scrape"
echo "      description: Scrape the web and join WhatsApp groups\n"

