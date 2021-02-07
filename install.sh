echo "####################################\n"
echo "    INSTALLING WHATSAPP SCRAPPER\n"
echo "####################################\n"

rm activate
rm -fr scrape.egg-info
rm -fr WhatsApp_scrape-venv

# Create a venv using the name of the directory we're in, and created a symlink
#to the activate script.
python3 -m venv "$(basename `pwd`)-venv" && ln -s "$(basename `pwd`)-venv"/bin/activate activate

# Tell the user to Activate the virtualenv 
echo "####################################\n"
echo "    Installation Successful!\n"
echo "Copy/Paste the command below and hit ENTER to start scraping\n\n"
echo "source activate;sh run.sh\n\n"


