"""
This is a script that accompanies Chapter 9
from the Packt book Machine Learning with Elastic, 2nd Edition.
Please see the README for more information.
"""

import argparse
import os

from elasticsearch import Elasticsearch, helpers

def parse_args():
    """
    Helper method for parsing CLI args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--es', type=str, help="URL of ES instance")
    return parser.parse_args()

def main():
    args = parse_args()
    # credentials for your ES instance
    es_username = os.env['ES_USERNAME']
    es_password = os.env['ES_PASSWORD']

    es_client = Elasticsearch(args.es, http_auth=(es_username, es_password))


if __name__ == '__main__':
    main()
