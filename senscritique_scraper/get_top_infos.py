import logging
import time
import argparse
import pandas as pd
from .utils import scr_utils

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()

    url = (
        args.url
        if args.url
        else "https://www.senscritique.com/films/tops/top111"
    )
    print(url)
    soup = scr_utils.get_soup(url)
    category = scr_utils.get_category_from_url(url)
    chart_infos = scr_utils.get_top_infos(soup, category)
    df = pd.DataFrame(chart_infos)
    df = df[scr_utils.get_order(category)]
    df.to_csv(f"file_{category}.csv", sep="\t", index=False)
    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(description="Python skeleton")
    parser.add_argument(
        "--debug",
        help="Display debugging information",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument(
        "positional_argument", nargs="?", type=str, help="Positional argument"
    )
    parser.add_argument("-u", "--url", help="URL", type=str)
    parser.add_argument(
        "-b",
        "--boolean_flag",
        help="Boolean flag",
        dest="boolean_flag",
        action="store_true",
    )
    parser.set_defaults(boolean_flag=False)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=format)
    return args


if __name__ == "__main__":
    main()
