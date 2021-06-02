"""
This script demonstrates how to export a trained model from an Elasticsearch cluster
"""

import argparse
import json
import os


from elasticsearch import Elasticsearch
from elasticsearch.client import MlClient


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--es_url', type=str, help="URL of the Elasticsearch cluster")
    parser.add_argument('--filename', type=str, help="Name of the output file to write model to")
    parser.add_argument('--model_id', type=str, help="Name of the model to be exported")
    return parser.parse_args()





def main():
    # parser commandline arguments 
    args = parse_args()
   
    # read the username and password from env variables to avoid storing them in cleartext in the script
    ES_PASSWORD = os.environ['ES_PASSWORD']
    ES_USERNAME = os.environ['ES_USERNAME']

    # create the two clients needed to work with the API
    es_client = Elasticsearch(args.es_url, http_auth=(ES_USERNAME, ES_PASSWORD))
    ml_client = MlClient(es_client)

    # call the API to get the model 
    compressed_model = ml_client.get_trained_models(model_id, decompress_definition=False, include_model_definition=True)

    # write the model to a file
    with open(args.filename, 'r') as handle:
        handle.write(json.dumps(compressed_model))


if __name__ == '__main__':
    main()
