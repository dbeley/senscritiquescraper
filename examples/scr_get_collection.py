import logging
import time
import argparse
from senscritiquescraper import Senscritique

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()

    if args.main_argument:
        user = args.main_argument
    elif args.user:
        user = args.user
    else:
        logger.error("ERREUR")
        exit()

    user_collection = Senscritique.get_user_collection(user)

    user_collection.to_csv(
        Senscritique.create_collection_filename(user), sep="\t", index=False
    )
    logger.info("Runtime : %.2f seconds." % (time.time() - temps_debut))


def parse_args():
    custom_format = "%(levelname)s :: %(message)s"
    parser = argparse.ArgumentParser(
        description="Senscritique scraper for an user collection"
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
        "main_argument", nargs="?", type=str, help="Name of the user"
    )
    parser.add_argument(
        "-u",
        "--user",
        help="Name of the user (same as without argument)",
        type=str,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format=custom_format)
    return args


if __name__ == "__main__":
    main()
