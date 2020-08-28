# -*- coding: utf-8 -*-
import requests, json
from consts import endpoint, headers
from get_languages import get_language_name

def detect_language(text):
    body = [{
        'text': text
    }]
    path = '/detect?api-version=3.0'
    constructed_url = endpoint + path

    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    language = response[0]['language']
    name = get_language_name(language)
    score = response[0]['score']
    return [name, score]