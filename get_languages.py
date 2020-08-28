# -*- coding: utf-8 -*-
import requests, json
from consts import endpoint, headers
from consts import LANGUAGES

def get_supported_languages():
    path = '/languages?api-version=3.0'
    params = '&scope=translation'
    constructed_url = endpoint + path + params

    request = requests.get(constructed_url, headers=headers)
    response = request.json()

    return response

def is_language_supported(language):
    if language in LANGUAGES: return True
    return False

def get_language_name(language):
    return LANGUAGES[language]["name"]
