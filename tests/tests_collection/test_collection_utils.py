from senscritiquescraper.utils import collection_utils


def test_get_dict_available_pages(collection_soup):
    available_pages = collection_utils.get_dict_available_pages(collection_soup)
    if available_pages:
        raise AssertionError()


def test_get_next_collection_link(collection_soup):
    next_collection_link = collection_utils.get_next_collection_link(collection_soup)
    if next_collection_link:
        raise AssertionError()


def test_get_rows_from_collection(collection_soup):
    rows = collection_utils.get_rows_from_collection(collection_soup)
    if len(rows) != 6:
        raise AssertionError()


def test_get_collection_infos(collection_soup):
    infos = collection_utils.get_collection_infos(collection_soup)
    if len(infos) != 6:
        raise AssertionError()

    assert len(infos) == 6

    test_infos = [
        {
            "Title": "Symphonie no. 9",
            "URL": "https://www.senscritique.com/album/Symphonie_no_9/1315369",
            "Year": "1984",
            "Release Date": "Sortie : 1984",
            "Genre": "Romantique et classique",
            "Number of Songs": "5  morceaux",
            "Picture URL": "https://media.senscritique.com/media/000005442496/90/Symphonie_no_9.jpg",
            "Artist": "Ludwig van Beethoven, Berliner Philharmoniker, Herbert von Karajan",
            "Average Rating": "9.1",
            "Number of Ratings": "1027",
            "User Action": "Rated",
            "Recommended": False,
            "User Rating": "10",
            "Category": "Music",
        },
        {
            "Title": "Berserk, tome 13",
            "URL": "https://www.senscritique.com/bd/Berserk_tome_13/17431552",
            "Original Title": "Beruseruku",
            "Year": "2006",
            "Release Date": "Sortie : 3 mai 2006",
            "Picture URL": "https://media.senscritique.com/media/000011614353/90/Berserk_tome_13.jpg",
            "Author": "Kentaro Miura",
            "Average Rating": "9.1",
            "Number of Ratings": "877",
            "User Action": "Rated",
            "Recommended": False,
            "User Rating": "10",
            "Category": "Comics",
        },
        {
            "Title": "The Legend of Zelda : Breath of the Wild",
            "URL": "https://www.senscritique.com/jeuvideo/The_Legend_of_Zelda_Breath_of_the_Wild/10416244",
            "Original Title": "Zeruda no densetsu: Buresu obu za wairudo",
            "Year": "2017",
            "Release Date": "Sortie : 3 mars 2017",
            "Picture URL": "https://media.senscritique.com/media/000016771881/90/The_Legend_of_Zelda_Breath_of_the_Wild.jpg",
            "Genre": "Action-Aventure",
            "Developer": "Nintendo EPD, Monolith Software, Nintendo",
            "Platforms": "Jeu vidéo\n\t\t\t\t\n\t\t\t\t\tde Nintendo EPD, Monolith Software et Nintendo",
            "Average Rating": "8.8",
            "Number of Ratings": "11108",
            "User Action": "Rated",
            "Recommended": False,
            "User Rating": "10",
            "Category": "Video Game",
        },
        {
            "Title": "Sur écoute",
            "URL": "https://www.senscritique.com/serie/Sur_ecoute/155448",
            "Original Title": "The Wire",
            "Year": "2002",
            "Release Date": "Première diffusion : 2 juin 2002",
            "Number of Seasons": "5 saisons",
            "Picture URL": "https://media.senscritique.com/media/000006471542/90/Sur_ecoute.jpg",
            "Genre": "Policier et drame",
            "Producer": "David Simon",
            "Average Rating": "9.1",
            "Number of Ratings": "21525",
            "User Action": "Rated",
            "Recommended": False,
            "User Rating": "10",
            "Category": "Series",
        },
        {
            "Title": "12 hommes en colère",
            "URL": "https://www.senscritique.com/film/12_hommes_en_colere/370894",
            "Original Title": "12 Angry Men",
            "Year": "1957",
            "Release Date": "Sortie : 10 avril 1957",
            "Length": "1 h 36 min",
            "Picture URL": "https://media.senscritique.com/media/000017381024/90/12_hommes_en_colere.jpg",
            "Genre": "Policier et drame",
            "Producer": "Sidney Lumet",
            "Average Rating": "8.7",
            "Number of Ratings": "44455",
            "User Action": "Rated",
            "Recommended": False,
            "User Rating": "10",
            "Category": "Movie",
        },
        {
            "Title": "1984",
            "URL": "https://www.senscritique.com/livre/1984/245854",
            "Original Title": "Nineteen Eighty-Four",
            "Year": "1949",
            "Release Date": "Sortie : 8 juin 1949",
            "Picture URL": "https://media.senscritique.com/media/000004731893/90/1984.jpg",
            "Genre": "Science-fiction et roman",
            "Author": "George Orwell",
            "Average Rating": "8.4",
            "Number of Ratings": "79782",
            "User Action": "Rated",
            "Recommended": False,
            "User Rating": "10",
            "Category": "Book",
        },
    ]

    assert infos[0] == test_infos[0]
    assert infos[1] == test_infos[1]
    assert infos[2] == test_infos[2]
    assert infos[3] == test_infos[3]
    assert infos[4] == test_infos[4]
    assert infos[5] == test_infos[5]
