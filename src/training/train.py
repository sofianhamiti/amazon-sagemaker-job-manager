import os
import logging
import argparse


logging.basicConfig(level=logging.INFO)


def train(args):
    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hyperparameters", type=str, default=os.environ["SM_HPS"])
    args, _ = parser.parse_known_args()

    # train model
    model = train(args)
