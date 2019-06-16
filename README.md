# senscritique-scraper

[![Build Status](https://travis-ci.com/dbeley/senscritique-scraper.svg?branch=master)](https://travis-ci.com/dbeley/senscritique-scraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ee8dea2d8d24e368147fa3337b9acb5)](https://app.codacy.com/app/dbeley/senscritique-scraper?utm_source=github.com&utm_medium=referral&utm_content=dbeley/senscritique-scraper&utm_campaign=Badge_Grade_Dashboard)

Utility to scrap senscritique.com.

- scr_get_top : Scraper for a top list/chart (take an URL as parameter)
- scr_get_collection : Scraper for an user collection (take a username as parameter)
- scr_get_infos_item : Scraper for an item (not implemented yet)
- scr_get_infos_artist : Scraper for an artist (not implemented yet)

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

```
scr_get_collection -h
```

```
usage: scr_get_collection [-h] [--debug] [-u USER] [main_argument]

Senscritique scraper for an user collection

positional arguments:
  main_argument         Name of the user

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -u USER, --user USER  Name of the user (same as without argument)
```
