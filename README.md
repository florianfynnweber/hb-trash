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
python3 hb-trash.py -h
usage: hb-trash.py [-h] (-i | -c) [-s STREET] [-n NR]

Tool for getting the garbage collection dates in Bremen, Germany

optional arguments:
  -h, --help            show this help message and exit
  -i, --ical            ical format
  -c, --csv             csv
  -s STREET, --street STREET
                        Name of street
  -n NR, --nr NR        Street number

```