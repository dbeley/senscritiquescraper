# senscritique-scraper

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ee8dea2d8d24e368147fa3337b9acb5)](https://app.codacy.com/app/dbeley/senscritique-scraper?utm_source=github.com&utm_medium=referral&utm_content=dbeley/senscritique-scraper&utm_campaign=Badge_Grade_Dashboard)

Utility to scrap senscritique.com.

- scr_get_top : Scraper for a top list/chart (i.e. Top 111 Films)
- scr_get_collection : Scraper for an user collection (not implemented yet)
- scr_get_infos_item : Scraper for an item (not implemented yet)

## Requirements

- requests
- bs4
- lxml
- pandas

## Installation in a virtualenv (recommended)

```
pipenv install '-e .'
```

## Usage

Show the help and the available options.

```
scr_get_top -h
```

```
usage: scr_get_top [-h] [--debug] [-u URL] [main_argument]

Senscritique scraper for a top list/chart.

positional arguments:
  main_argument      URL to parse

optional arguments:
  -h, --help         show this help message and exit
  --debug            Display debugging information
  -u URL, --url URL  URL to parse (same as without argument)
```
