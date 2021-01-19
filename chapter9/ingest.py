"""
This is a script that accompanies Chapter 9
from the Packt book Machine Learning with Elastic, 2nd Edition.
Please see the README for more information.
"""

import argparse
from datetime import datetime
import os
import random

from elasticsearch import Elasticsearch, helpers

USERNAMES = ['josh98', 'flowers', 'natalie_porter', 'johnny', 'Amelia', 'Jenny']
START_EPOCH_TIME = 1577919740
INDEX_NAME = 'social-media-feed'

def parse_args():
    """
    Helper method for parsing CLI args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--es', type=str, help="URL of ES instance")
    parser.add_argument('--num', type=int, help="Number of documents to ingest")
    return parser.parse_args()

def main():

    args = parse_args()

    # credentials for your ES instance
    es_username = os.environ['ES_USERNAME']
    es_password = os.environ['ES_PASSWORD']

    es_client = Elasticsearch(args.es, http_auth=(es_username, es_password))
    for i in range(args.num):
        data = {"username": random.choice(USERNAMES), "statistics": {"likes":
            random.randint(0,1000), "shares": random.randint(0,10000)},
            "timestamp":datetime.fromtimestamp(START_EPOCH_TIME+random.randint(60,2592000))}
        es_client.index(index=INDEX_NAME, body=data)




if __name__ == '__main__':
    main()
