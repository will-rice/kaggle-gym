"""
This script memoizes BERT embeddings
for training of small footprint NLU models
"""
import os
import random
import argparse

import numpy as np
import tensorflow as tf


# set random seeds
random.seed(1234)
np.random.seed(1234)
tf.random.set_seed(1234)


def main():
    """ program entry point """

    parser = argparse.ArgumentParser(description="Hydra Model Preprocessing")
    parser.add_argument('data_path',
                        help="path to the training data directory")
    parser.add_argument('name',
                        help="name of this training run")
    parser.add_argument('--log_path',
                        default='./logs',
                        help="path to the tensorflow output logs")
    parser.add_argument('--config',
                        default='./config/hparams.json',
                        help='path to hparams config file')

    args = parser.parse_args()

    _prep(args)


def _prep(args):
    log_path = os.path.join(args.log_path, args.name)


if __name__ == '__main__':
    main()
