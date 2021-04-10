"""scr_get_work_url

Given a file senscritique.txt containing
the following content:
    OK Computer
    English Settlement
    Mëkanïk Dëstruktïẁ Kömmandöh

Running scr_get_work_url -f senscritique.txt
will extract the first search result on Senscritique
for each line of the text file
and export it in a new file senscritique_URLs.csv.

It's useful to be used with the scr_get_work_details.py script.
Run the script with the -h flag to see available options.
"""

import logging
import time
import argparse
import pandas as pd
from senscritiquescraper import Senscritique

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()

    if args.main_argument:
        file = args.main_argument
    elif args.file:
        file = args.file
    else:
        logger.error("No file entered. Exiting.")
        exit()

    df = pd.read_csv(file, sep="\t", header=None)

    list_urls = []
    for index, row in df.iterrows():
        if url_search := Senscritique.get_url(row[0], rank=1, genre=args.genre):
            list_urls.append({"URL": url_search})

    df_urls = pd.DataFrame(list_urls)
    export_filename = f"{file.split('.')[0]}_URLs.csv"
    logger.info(f"Results exported to {export_filename}.")
    df_urls.to_csv(export_filename, sep="\t", index=False)

    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    custom_format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(
        description="This script will export in a file the URLs for the first Senscritique search result of each search terms contained in another file."
    )
    parser.add_argument(
        "--debug",
        help="Display debugging information",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument("main_argument", nargs="?", type=str, help="File to parse.")
    parser.add_argument("-f", "--file", type=str, help="File to parse.")
    parser.add_argument(
        "-g",
        "--genre",
        type=str,
        help="Genre to filter (available choices : Morceaux, Albums, Films, Livres, Séries, BD, Jeux).",
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
