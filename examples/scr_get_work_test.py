"""scr_get_list_work

This script will export in a csv file an user list_work.
Launch the script with the -h flag to see available options.
"""

import logging
import time
import argparse
from senscritiquescraper import Senscritique

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()

    ufilm = "https://www.senscritique.com/film/Avatar/371239"
    userie = "https://www.senscritique.com/serie/The_Handmaid_s_Tale/21032442"
    ujeu = "https://www.senscritique.com/jeuvideo/Verdun/10624321"
    ulivre = "https://www.senscritique.com/livre/Soif/39651063"
    ubd = "https://www.senscritique.com/bd/La_Fille_de_Vercingetorix_Asterix_tome_38/17954654"
    ualbum = "https://www.senscritique.com/album/Spiritual_Instinct/40163973"

    dfilm = Senscritique.get_work_details(ufilm)
    dserie = Senscritique.get_work_details(userie)
    djeu = Senscritique.get_work_details(ujeu)
    dlivre = Senscritique.get_work_details(ulivre)
    dbd = Senscritique.get_work_details(ubd)
    dalbum = Senscritique.get_work_details(ualbum)

    print(f"FILM : {dfilm}")
    print(f"SERIE : {dserie}")
    print(f"JEU : {djeu}")
    print(f"LIVRE : {dlivre}")
    print(f"BD : {dbd}")
    print(f"ALBUM : {dalbum}")
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
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
