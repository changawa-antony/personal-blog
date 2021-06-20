import urllib.request,json
from flask import config
from .models import Quote

QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
base_url = QUOTES_URL

def get_quotes():
    '''
    Function that gets responce to request
    '''
    with urllib.request.urlopen(base_url) as url:
        get_quotes_response = url.read()
        quote = json.loads(get_quotes_response)

    return quote