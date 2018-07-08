# UK Citizenship Trip Adder

Automate the tedious task of adding each applicant's trip details from over your many years in the UK!

## Setup

1. Get the [latest Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and put it in your *PATH* somewhere
1. `python3.6 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`

## Usage

1. Get your data in the proper format - see `trips.csv`. Dates are `dd/mm/yy` format
1. Enter an `application_id` and `password` for the application
1. If you're doing multiple applicants, edit the `applicant_index` to indicate which one you're adding trips to (0 = first in your list, etc)
1. `source .venv/bin/activate`
1. `python main.py`
1. Check over each entry after being filled in, then hit "Save and continue"
1. If you're starting/stopping, delete rows that are done or mark an `x` in the `Done` column of the CSV
