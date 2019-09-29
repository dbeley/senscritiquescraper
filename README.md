# senscritiquescraper

[![Build Status](https://travis-ci.com/dbeley/senscritiquescraper.svg?branch=master)](https://travis-ci.com/dbeley/senscritiquescraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e95f1fcf5d2e47b480a3ef9c98ce1b1d)](https://www.codacy.com/app/dbeley/senscritiquescraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dbeley/senscritiquescraper&amp;utm_campaign=Badge_Grade)

API to extract data from senscritique.com.

Some examples of its usage are included in the examples folder.

## Requirements

- requests
- beautifulsoup4
- lxml
- pandas

## Installation in a virtualenv (recommended)

```
pipenv install '-e .'
```

## Examples Usage

Show the help and the available options.

```
scr_get_topchart -h
```

```
usage: scr_get_topchart [-h] [--debug] [-u URL] [main_argument]

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
