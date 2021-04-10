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
- morceau: individual tracks from an album

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

### Work/oeuvre

Extract the URL of the first result for the query "Star Wars" with a filter on movies, then extract infos about it:

```python
>>> # Possible genres are Films, Livres, Séries, BD, Jeux, Morceaux, Albums (setting the genre is optional).
>>> sw_url = Senscritique.get_url("Star Wars", rank=1, genre="Films")
>>> sw_infos = Senscritique.get_work_details(sw_url)
>>> import json
>>> json.dumps(sw_infos, indent=4, ensure_ascii=False)
```

```
{
    "Title": "La Guerre des Étoiles",
    "URL": "https://www.senscritique.com/film/La_Guerre_des_Etoiles/365132",
    "Rating": "7.8",
    "Rating Details": {
        "1": 187,
        "2": 143,
        "3": 294,
        "4": 629,
        "5": 1940,
        "6": 5722,
        "7": 17573,
        "8": 23914,
        "9": 12138,
        "10": 6868
    },
    "Year": "1977",
    "Cover URL": "https://media.senscritique.com/media/000012797534/160/La_Guerre_des_Etoiles.png",
    "Review Count": "299",
    "Vote Count": "69408",
    "Favorite Count": "3800",
    "Wishlist Count": "2500",
    "In Progress Count": null,
    "Description": "Dans une galaxie lointaine, l'univers est dominé par l'Empire galactique avec à sa tête le sombre et impitoyable Dark Vador. Mais la révolte gronde, l'Alliance rebelle menée par la princesse Leia, s'empare des plans de l'Etoile Noire, la base secrète de l'Empire. Avant d'être capturée par les...",
    "Producer": "George Lucas",
    "Genre": "Aventure, science-fiction et action",
    "Length": "2 h 01 min",
    "Release Date": "19 octobre 1977 (France)",
    "Category": "Movie"
}
```

### User Collection

Extract the user collection of the user 34nUBqnQvCSkt:

```python
>>> user_collection = Senscritique.get_user_collection("34nUBqnQvCSkt")
>>> df_user_collection = pd.DataFrame(user_collection)
>>> df_user_collection[["Title", "Year", "Category", "User Rating", "Number of Ratings", "Average Rating"]]
```

```
                                      Title  Year    Category User Rating Number of Ratings Average Rating
0                                   Walk On  1974       Track          10                54            7.5
1                           Symphonie no. 9  1984       Music          10              1068            9.1
2                          Berserk, tome 13  1997      Comics          10               922            9.1
3  The Legend of Zelda : Breath of the Wild  2017  Video Game          10             11728            8.8
4                                Sur écoute  2002      Series          10             21979            9.1
5                       12 hommes en colère  1957       Movie          10             45414            8.7
6                                      1984  1949        Book          10             81697            8.4
```

### Top Chart

Extract infos about the Top 111 Musique topchart:

```python
>>> topchart = Senscritique.get_topchart("https://www.senscritique.com/musique/tops/top111")
>>> df_topchart = pd.DataFrame(topchart)
>>> df_topchart[['Title', 'Year', 'Average Rating', 'Number of Ratings']]
```
```
                                         Title  Year Average Rating Number of Ratings
0    Dvořák: Symphonie No. 9 / Smetana: Moldau  1985            9.1               428
1                                      Requiem  1971            9.1              1548
2                              Symphonie no. 9  1984            9.1              1068
3                                      Requiem  2011            8.9              2353
4                                    Nocturnes  1992            8.9              1293
..                                         ...   ...            ...               ...
106                                Long Season  1996            8.2              1430
107                                   Murmuüre  2010            8.2               800
108                         Saxophone Colossus  1956            8.2               555
109                                 Solo Piano  1989            8.2               452
110                        The Main Ingredient  1994            8.2               320
```

### Work List

Extract infos about all the RPG video games listed on Senscritique:

```python
>>> list_work = Senscritique.get_list_work("https://www.senscritique.com/jeuxvideo/oeuvres/RPG--3094")
>>> df_list_work = pd.DataFrame(list_work)
>>> df_list_work[["Title", "Year", "Genre", "Average Rating"]]
```
```
                                     Title  Year                                              Genre Average Rating
0                        Madô Monogatari I  None                                                                 -
1                           Arc The Lad II  2012                                                RPG            7.1
2                        Kingdom Hearts II  2006                                      RPG et action            8.1
3     Might and Magic III : Isles of Terra  1991                                                RPG            7.8
4                          Siege Of Avalon  2000                                                RPG              -
...                                    ...   ...                                                ...            ...
6675                          Silver Ghost  1988                                                                 -
6676                          Memetown USA  2018                            Aventure et jeu de rôle              -
6677                        Lords of Chaos  1990  Stratégie tour par tour, tactique, wargame et ...              -
6678                       Marginalia Hero  2019                                        Jeu de rôle              -
6679                    The Eternal Dagger  1987                                                                 -
```

### Survey

Extract infos about the best movies of 2021 survey:

```python
>>> survey = Senscritique.get_survey("https://www.senscritique.com/top/resultats/Les_meilleurs_films_de_2021/2917616")
>>> df_survey = pd.DataFrame(survey)
>>> df_survey[["Title", "Year", "Producer"]]
```
```
                          Title  Year                                     Producer
0               Malcolm & Marie  2021                                 Sam Levinson
1  Zack Snyder's Justice League  2021                                  Zack Snyder
2             Pieces of a Woman  2021                             Kornél Mundruczó
3                  I Care a Lot  2021                                   J Blakeson
4                       The Dig  2021                                  Simon Stone
5                    La Mission  2020                              Paul Greengrass
6         Promising Young Woman  2020                              Emerald Fennell
7     Raya et le dernier dragon  2021  Don Hall, Carlos López Estrada, Paul Briggs
8                     Nomadland  2020                                   Chloé Zhao
9                        Minari  2021                              Lee Isaac Chung
```

### Example Scripts

Some scripts using the API are provided in the examples folder.

For each scripts, you can see the help and the available options with the `-h` argument.

```
python scr_get_topchart.py -h
```

#### scr_get_topchart

```
usage: scr_get_topchart.py [-h] [--debug] [-u URL] [main_argument]

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
usage: scr_get_collection.py [-h] [--debug] [-u USER] [main_argument]

Senscritique scraper for an user collection.

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

This script will export in a csv file one or several works from senscritique contained in a csv file (it will use the 'URL' field).

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
usage: scr_get_work_urls.py [-h] [--debug] [-f FILE] [-g GENRE] [main_argument]

This script will export in a file the URLs for the first Senscritique search result of each search terms contained in another file.

positional arguments:
  main_argument         File to parse.

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  File to parse.
  -g GENRE, --genre GENRE
                        Genre to filter (available choices : Morceaux, Albums, Films, Livres, Séries, BD, Jeux).
```
