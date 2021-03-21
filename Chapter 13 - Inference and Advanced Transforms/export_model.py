"""
This script demonstrates how to export a trained model from an Elasticsearch cluster
"""

import argparse



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--es_url', type=str, help="URL of the Elasticsearch cluster")
    parser.add_argument('--output', type=str, help="Name of the output file to write model to")
    return parser.parse_args()





def main():
    pass



if __name__ == '__main__':
    main()
