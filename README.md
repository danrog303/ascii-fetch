# ascii-fetch
> Python script which downloads and displays ASCII images in your terminal.

## Features
1. Downloading and displaying ASCII arts from https://www.asciiart.eu directly in your terminal
2. Printing image in color by using `--color` argument.

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

Print 10th ascii-art in Cats subcategory and make it blue  
`asciifetch.py "https://www.asciiart.eu/animals/cats" 10 --color blue`  
(supported colors are: black, blue, cyan, green, magenta, red, white, yellow)

Print 10th ascii-art in Cats subcategory and make it bold  
`asciifetch.py "https://www.asciiart.eu/animals/cats" 10 --bold`  

## Screenshots
<img alt="Screenshot: category listing" src="https://user-images.githubusercontent.com/32397526/148364767-cf02cd5b-3adf-4430-880f-381dc828fda3.png" width="600">
<img alt="Screenshot: deer asci-art" src="https://user-images.githubusercontent.com/32397526/148364764-cc184174-9af7-41aa-84e9-c13dba75c84a.png" width="600">

## Technologies used
This script has been written in Python 3.10.