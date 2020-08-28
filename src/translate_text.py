# -*- coding: utf-8 -*-
import requests, json
from consts import endpoint, headers, LANGUAGES
from get_languages import is_language_supported, get_language_name

def translator(text, language):
    if not is_language_supported(language): 
        return "Sorry, this language is not supported for translation"

    body = [{
        'text': text
    }]
    path = '/translate?api-version=3.0'
    params = '&to=' + language
    constructed_url = endpoint + path + params
    
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    return response

def detect_translate(text, language):
    response = translator(text, language)
    if isinstance(response, str): return response

    detected = response[0]['detectedLanguage']['language']
    name = get_language_name(detected)
    score = response[0]['detectedLanguage']['score']
    translated = response[0]['translations'][0]['text']
    return [name, score, translated]

def translate(text, language):
    response = translator(text, language)
    if isinstance(response, str): return response

    translated = response[0]['translations'][0]['text']
    return translated
    