# Instagram Bio Auto-Updater

> By Langston Howley

Using the [Selenium Web Driver](https://selenium-python.readthedocs.io/) and [Requests](https://requests.readthedocs.io/en/master/) modules this program updates a user's Instagram Bio to a planet's current position information every 10 minutes. A planet's name is selected at random and its position replaces the previous text in the user's bio.

The planet position information comes from a table on [The Sky Live's website](https://theskylive.com/) and is formatted to appear like this example:

```
Mars RA|DEC|CO: 01h 05m 31s | +04° 45’ 04” | Pisces
When: 2020-10-27 @ 13:35:35
```

### Key

- RA  : Right Ascension (hours : minutes : seconds)
- DEC : Declination (° : minutes : seconds)
- CO  : Constellation (name)

## Installation and Running

If you'd like, first set up a [virtual enviroment](https://realpython.com/python-virtual-environments-a-primer/#using-virtual-environments) for storing the dependencies locally rather than on your machine.

```bash
# clone the repository into your current directory
git clone https://github.com/langstonhowley/Instagram-Bio-Auto-Updater.git
# go into the project directory
cd Instagram-Bio-Auto-Updater
# install all of the required packages
pip3 install -r requirements.txt
# create a .env folder and insert your credentials
touch .env
echo "INSTAGRAM_USERNAME = {YOUR_INSTA_USERNAME}" >> .env
echo "INSTAGRAM_PASSWORD = {YOUR_INSTA_PASSWORD}" >> .env
# run the updater 😁
python3 main.py
```
