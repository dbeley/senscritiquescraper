# senscritiquescraper

[![Build Status](https://travis-ci.com/dbeley/senscritiquescraper.svg?branch=master)](https://travis-ci.com/dbeley/senscritiquescraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e95f1fcf5d2e47b480a3ef9c98ce1b1d)](https://www.codacy.com/app/dbeley/senscritiquescraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dbeley/senscritiquescraper&amp;utm_campaign=Badge_Grade)

API to extract data from senscritique.com.

Some examples of its usage are included in the examples folder.

Examples of what's extractable :
- topchart : <https://www.senscritique.com/films/tops/top111>
- collection : <https://www.senscritique.com/34nUBqnQvCSkt/collection/all/all/all/all/all/all/all/all/all/page-1>
- survey : <https://www.senscritique.com/top/resultats/Les_meilleurs_films_de_2019/2301802>
- list_work : <https://www.senscritique.com/films/oeuvres>

The "list_work" urls are difficult to find, here are the one for each genre where you can access all the subgenres :
- <https://www.senscritique.com/films/oeuvres>
- <https://www.senscritique.com/series/oeuvres>
- <https://www.senscritique.com/jeuxvideo/oeuvres>
- <https://www.senscritique.com/livres/oeuvres>
- <https://www.senscritique.com/bd/oeuvres>
- <https://www.senscritique.com/musique/oeuvres>


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
python scr_get_topchart.py -h
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
python scr_get_collection.py -h
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

```
python scr_get_survey.py -h
```

```
usage: scr_get_survey.py [-h] [--debug] [-u URL] [main_argument]

Senscritique scraper for a survey.

positional arguments:
  main_argument      URL to parse

optional arguments:
  -h, --help         show this help message and exit
  --debug            Display debugging information
  -u URL, --url URL  URL to parse (same as without argument)
```

```
python scr_get_list_work.py -h
```

```
usage: scr_get_list_work.py [-h] [--debug] [-u URL] [main_argument]

Senscritique scraper for a list_work.

positional arguments:
  main_argument      URL to parse.

optional arguments:
  -h, --help         show this help message and exit
  --debug            Display debugging information
  -u URL, --url URL  URL to parse (same as without argument)
```
