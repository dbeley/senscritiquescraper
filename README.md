# senscritiquescraper

![Build Status](https://github.com/dbeley/senscritiquescraper/workflows/CI/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e95f1fcf5d2e47b480a3ef9c98ce1b1d)](https://www.codacy.com/app/dbeley/senscritiquescraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dbeley/senscritiquescraper&amp;utm_campaign=Badge_Grade)

API to extract data from senscritique.com.

Example of what can be extracted:
- topchart: <https://www.senscritique.com/films/tops/top111>
- collection: <https://www.senscritique.com/34nUBqnQvCSkt/collection/all/all/all/all/all/all/all/all/all/page-1>
- survey: <https://www.senscritique.com/top/resultats/Les_meilleurs_films_de_2019/2301802>
- list_work: <https://www.senscritique.com/films/oeuvres>
- work: <https://www.senscritique.com/film/J_ai_perdu_mon_corps/39006031>

Type of work:
- film: <https://www.senscritique.com/films>
- serie: <https://www.senscritique.com/series>
- jeu: <https://www.senscritique.com/jeuxvideo>
- livre: <https://www.senscritique.com/livres>
- bd: <https://www.senscritique.com/bd>
- album: <https://www.senscritique.com/musique>
- morceau: As of now, individual tracks are not supported.

The "list_work" urls are difficult to find, here are the one for each genre where the subgenres can be accessed:
- <https://www.senscritique.com/films/oeuvres>
- <https://www.senscritique.com/series/oeuvres>
- <https://www.senscritique.com/jeuxvideo/oeuvres>
- <https://www.senscritique.com/livres/oeuvres>
- <https://www.senscritique.com/bd/oeuvres>
- <https://www.senscritique.com/musique/oeuvres>

Some examples of the API usage are included in the examples folder:
- `scr_get_collection.py`: Extract the collection of an user.
- `scr_get_get_list_work.py`: Extract a list of work.
- `scr_get_get_survey.py`: Extract the results of a survey.
- `scr_get_get_topchart.py`: Extract the results of a topchart.
- `scr_get_get_work_details.py`: Extract infos about a list of Senscritique urls.
- `scr_get_get_work_urls.py`: From a list of search terms in a text file, extract the urls of the first result on Senscritique for each term.

## Requirements

- requests
- beautifulsoup4
- lxml
- pandas

## Installation

### First method (installing the senscritiquescraper package)

```
git clone https://github.com/dbeley/senscritiquescraper
cd senscritiquescraper
python setup.py install
python examples/scr_get_work_urls.py -h
```

### Second method (installing with pipenv)

```
git clone https://github.com/dbeley/senscritiquescraper
cd senscritiquescraper
pipenv install '-e .'
pipenv run python examples/scr_get_work_urls.py -h
```

## Example

```python
>>> import pandas as pd
>>> from senscritiquescraper import Senscritique
```

### work/oeuvre
```python
>>> sw_url = Senscritique.get_url("Star Wars", rank=1, genre="Films")
>>> sw_infos = Senscritique.get_work_details(sw_url)
>>> sw_infos
{'Title': 'La Guerre des Étoiles', 'URL': 'https://www.senscritique.com/film/La_Guerre_des_Etoiles/365132', 'Rating': '7.8', 'Rating Details': ['187', '143', '294', '629', '1940', '5721', '17569', '23911', '12138', '6868'], 'Year': '1977', 'Cover URL': 'https://media.senscritique.com/media/000012797534/160/La_Guerre_des_Etoiles.png', 'Review Count': '300', 'Vote Count': '69400', 'Favorite Count': '3800', 'Wishlist Count': '2500', 'In Progress Count': None, 'Producer': 'Film de   George Lucas', 'Genre': 'Aventure, science-fiction et action', 'Length': '2 h 01 min', 'Release Date': '19 octobre 1977 (France)', 'Category': 'Movie'}
```

### user collection
```python
>>> user_collection = Senscritique.get_user_collection("34nUBqnQvCSkt")
>>> df_user_collection = pd.DataFrame(user_collection)
>>> df_user_collection[["Title", "Year", "Category", "User Rating", "Number of Ratings", "Average Rating"]]
                                      Title  Year    Category User Rating Number of Ratings Average Rating
0                           Symphonie no. 9  1984       Music          10              1068            9.1
1                          Berserk, tome 13  1997      Comics          10               922            9.1
2  The Legend of Zelda : Breath of the Wild  2017  Video Game          10             11722            8.8
3                                Sur écoute  2002      Series          10             21978            9.1
4                       12 hommes en colère  1957       Movie          10             45409            8.7
5                                      1984  1949        Book          10             81687            8.4
```

### survey
```python
>>> survey = Senscritique.get_survey("https://www.senscritique.com/top/resultats/Les_meilleurs_films_de_2021/2917616")
>>> df_survey = pd.DataFrame(survey)
>>> df_survey[["Title", "Year", "Producer"]]
                          Title  Year                                     Producer
0               Malcolm & Marie  2021                                 Sam Levinson
1  Zack Snyder's Justice League  2021                                  Zack Snyder
2             Pieces of a Woman  2021                             Kornél Mundruczó
3                       The Dig  2021                                  Simon Stone
4                  I Care a Lot  2021                                   J Blakeson
5                    La Mission  2020                              Paul Greengrass
6         Promising Young Woman  2020                              Emerald Fennell
7     Raya et le dernier dragon  2021  Don Hall, Carlos López Estrada, Paul Briggs
8                     Nomadland  2020                                   Chloé Zhao
9                        Minari  2021                              Lee Isaac Chung
```

### topchart
```python
>>> topchart = Senscritique.get_topchart("https://www.senscritique.com/musique/tops/top111")
>>> df_topchart = pd.DataFrame(topchart)
>>> df_topchart[['Title', 'Year', 'Average Rating', 'Number of Ratings']]
                                          Title  Year Average Rating Number of Ratings
0    Dvořák: Symphonie No. 9 / Smetana: Moldau  1985            9.1               428
1                                      Requiem  1971            9.1              1548
2                              Symphonie no. 9  1984            9.1              1068
3                                      Requiem  2011            8.9              2353
4                                    Nocturnes  1992            8.9              1293
..                                         ...   ...            ...               ...
106                                Long Season  1996            8.2              1430
107                                   Murmuüre  2010            8.2               797
108                         Saxophone Colossus  1956            8.2               555
109                                 Solo Piano  1989            8.2               452
110                        The Main Ingredient  1994            8.2               320
```

### list_work
```python
>>> list_work = Senscritique.get_list_work("https://www.senscritique.com/jeuxvideo/oeuvres/RPG--3094")
>>> df_list_work = pd.DataFrame(list_work)
>>> df_list_work[["Title", "Year", "Genre", "Average Rating"]]
                                         Title  Year                           Genre Average Rating
0                            Madô Monogatari I  None                                              -
1           Final Fantasy XII : Revenant Wings  2008                             RPG            6.1
2                               Arc The Lad II  2012                             RPG            7.1
3                            Kingdom Hearts II  2006                   RPG et action            8.1
4         Might and Magic III : Isles of Terra  1991                             RPG            7.8
...                                        ...   ...                             ...            ...
6678                               RESEQUENCED  2018  Action-Aventure et jeu de rôle              -
6679                   Legend of the Time Star  None                                              -
6680  The Elder Scrolls Online : Thieves Guild  2016              MMO et jeu de rôle            7.4
6681     Mobile Suit Gundam: Classic Operation  1990                                              -
6682     Mobile Suit Gundam : Desert Operation  1990                                              -
```

### Example Scripts

Show the help and the available options.

```
python scr_get_topchart.py -h
```

Some scripts using the API are provided in the examples folder.

#### scr_get_topchart

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

#### scr_get_collection

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

#### scr_get_survey

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

#### scr_get_list_work

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

#### scr_get_work_details

```
python scr_get_work_details.py -h
```

```
usage: scr_get_work_details.py [-h] [--debug] [-f FILE] [main_argument]

This script will export in a csv file one or several works from senscritique.
The -f option will use the 'URL' field of a csv file.

positional arguments:
  main_argument         File to parse.

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  File to parse.
```

#### scr_get_work_urls

Running `scr_get_work_url -f FILE` will extract the first search result on Senscritique for each line of a text file and export it in a new file.

It's useful to be used with the `scr_get_work_details.py` script.

```
usage: scr_get_work_urls.py [-h] [--debug] [-f FILE] [main_argument]

This script will export in a file the URLs for the first Senscritique search
result of each search terms contained in another file.

positional arguments:
  main_argument         File to parse.

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  File to parse.
```
