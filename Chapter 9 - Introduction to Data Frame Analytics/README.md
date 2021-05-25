# Chapter 9

## Continuous Transforms

### Instructions for Populating the Index with Data on Unix like systems

1. Make sure you have Python 3.6 installed on your system. 
2. Create a virtual environment by running 
```
python3 -m venv <nameofyourenv>
```
3. Activate your virtual environment

```
source <nameofyourenv>/bin/activate
```
4. Install the Python dependencies listed in the `requirements.txt` file
```
pip install -r requirements.txt
```

Now you should be ready to run the ingest script `ingest.py` that is included in this chapter.

5. To view the commandline arguments you need to supply to the script, run 

```
python ingest.py --help
```

6. The script requires your Elasticsearch username and password to be stored as environment variables ES_USERNAME and ES_PASSWORD

