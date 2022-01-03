# ascii-fetch
> Python script which downloads and displays ASCII images in your terminal.

## Features
1. Downloading and displaying ASCII arts from https://www.asciiart.eu directly in your terminal

## How to run?
1. Clone this repo  
   `git clone https://github.com/danrog303/console-calc`  
   `cd console-calc`
2. Install required dependencies (preferably in virtual environment)  
   `pip3 install -r requirements.txt`
3. Run script  
   `python3 asciifetch.py`
   
## Usage
Print available categories  
`asciifetch.py`  

Print available subcategories in Animals category  
`asciifetch.py "https://www.asciiart.eu/animals"`  

Print all ascii-arts in Cats subcategory  
`asciifetch.py "https://www.asciiart.eu/animals/cats"`

Print 10th ascii-art in Cats subcategory  
`asciifetch.py "https://www.asciiart.eu/animals/cats" 10` 


## Technologies used
This script has been written in Python 3.10.