import os
import logging
import argparse

logging.basicConfig(level=logging.INFO)


def train(args):
    print(args.parameters)
    # ==================================================
    # =============== DO TRAINING HERE =================
    # ==================================================


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters", type=str, default=os.environ["SM_HPS"])
    args, _ = parser.parse_known_args()

    # train model
    train(args)
