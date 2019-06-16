import logging
import time
import argparse
import pandas as pd
from .utils import scr_utils

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

    logger.info("URL : %s", url)
    soup = scr_utils.get_soup(url)

    chart_infos = scr_utils.get_collection_infos(soup)

    df = pd.DataFrame(chart_infos)
    df = df[scr_utils.get_collection_order()]
    df.to_csv(scr_utils.create_filename_from_url(url), sep="\t", index=False)
    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    custom_format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(
        description="Senscritique scraper for a top list/chart."
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
        "main_argument", nargs="?", type=str, help="URL to parse"
    )
    parser.add_argument(
        "-u", "--url", help="URL to parse (same as without argument)", type=str
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
