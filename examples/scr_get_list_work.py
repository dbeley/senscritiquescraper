"""scr_get_list_work

This script will export in a csv file an user list_work.
Launch the script with the -h flag to see available options.
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
        url = args.main_argument
    elif args.url:
        url = args.url
    else:
        logger.error("ERREUR")
        exit()

    list_work = Senscritique.get_list_work(url)
    df_list_work = pd.DataFrame(list_work)

    df_list_work.to_csv(
        Senscritique.create_list_work_filename(url), sep="\t", index=False
    )
    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    custom_format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(
        description="Senscritique scraper for a list_work."
    )
    parser.add_argument(
        "--debug",
        help="Display debugging information",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument(
        "main_argument", nargs="?", type=str, help="URL to parse."
    )
    parser.add_argument(
        "-u", "--url", help="URL to parse (same as without argument)", type=str
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
