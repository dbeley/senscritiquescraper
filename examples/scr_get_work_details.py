"""scr_get_work

This script will export in a csv file one or several works from senscritique.
The -f option will use the "URL" field of a csv file.
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
        file = args.main_argument
    elif args.file:
        file = args.file
    else:
        logger.error("No file entered. Exiting.")
        exit()

    df = pd.read_csv(file, sep="\t")

    list_work_details = []
    for index, row in df.iterrows():
        if work_details := Senscritique.get_work_details(row["URL"]):
            # list_work_details.append(Senscritique.get_work_details(row['URL']))
            list_work_details.append(work_details)

    df_topchart = pd.DataFrame(list_work_details)
    df_topchart.to_csv(f"export_works_{file}", sep="\t", index=False)

    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    custom_format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(
        description="This script will export in a csv file one or several works from senscritique. The -f option will use the 'URL' field of a csv file."
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
        "main_argument", nargs="?", type=str, help="File to parse."
    )
    parser.add_argument("-f", "--file", type=str, help="File to parse.")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
