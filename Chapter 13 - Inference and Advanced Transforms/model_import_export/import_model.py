"""
Script to import an Elasticsearch model from a file into a cluster
"""

import argparse

from elasticsearch import Elasticsearch
from elasticsearch.client import MlClient


def parse_args():
   parser = argparse.ArgumentParser()
   parser.add_argument('--es_url', type=str, help="Elasticsearch URL to connect to")
   parser.add_argument('--filename', type=str, help="The file that contains the exported model")
   return parser.parse_args()


def main():
   # parse commandline arguments
   args = parse_args()

   # create the required client objects 
   es_client = Elasticsearch(args.es_url, http_auth=(ES_USERNAME, ES_PASSWORD)
   ml_client =  MlClient(es_client)

   # read in the imported modelfile
   with open(args.filename, 'r') as handle:
       model_definition = json.loads(handle.read())
   # import the model with the MlClient object

   
   


if __name__ == '__main__':
    main()
