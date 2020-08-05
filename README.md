# hb-trash
Tool for getting the garbage collection dates in Bremen, Germany as ics or csv
## Install
```bash
git clone https://github.com/florianfynnweber/hb-trash.git
virtualenv -p /usr/bin/python3 .
source bin/activate
pip install -r requirements.txt
```
## Usage
```bash
usage: hb-trash.py [-h] -s STREET -n NR [-p PATH]

Tool for getting the garbage collection dates in Bremen, Germany as ics or csv

optional arguments:
  -h, --help            show this help message and exit
  -s STREET, --street STREET
                        Name of street
  -n NR, --nr NR        Street number
  -p PATH, --path PATH  Absolut path to nextpickup.json
```
