#Create a code coverage report

coverage erase
coverage run --source=scrape -m py.test
coverage report -m
coverage html

echo "\n\n Coverage report located in \n/WhatsApp_scrape/htmlcov/index.html\n"
