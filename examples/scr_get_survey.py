"""scr_get_survey

This script will export in a csv file a survey.
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
        logger.error("No url set.")
        exit()

    survey = Senscritique.get_survey(url)
    df_survey = pd.DataFrame(survey)

    df_survey.to_csv(
        f"{int(time.time())}_{Senscritique.create_survey_filename(url)}",
        sep="\t",
        index=False,
    )
    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    custom_format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(description="Senscritique scraper for a survey.")
    parser.add_argument(
        "--debug",
        help="Display debugging information",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument("main_argument", nargs="?", type=str, help="URL to parse")
    parser.add_argument(
        "-u", "--url", help="URL to parse (same as without argument)", type=str
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
