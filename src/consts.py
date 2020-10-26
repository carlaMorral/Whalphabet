import os, uuid

key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': 'eastus',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

LANGUAGES = {
    "af": {
        "dir": "ltr",
        "name": "Afrikaans",
        "nativeName": "Afrikaans"
    },
    "ar": {
        "dir": "rtl",
        "name": "Arabic",
        "nativeName": "العربية"
    },
    "bg": {
        "dir": "ltr",
        "name": "Bulgarian",
        "nativeName": "Български"
    },
    "bn": {
        "dir": "ltr",
        "name": "Bangla",
        "nativeName": "বাংলা"
    },
    "bs": {
        "dir": "ltr",
        "name": "Bosnian",
        "nativeName": "bosanski (latinica)"
    },
    "ca": {
        "dir": "ltr",
        "name": "Catalan",
        "nativeName": "Català"
    },
    "cs": {
        "dir": "ltr",
        "name": "Czech",
        "nativeName": "Čeština"
    },
    "cy": {
        "dir": "ltr",
        "name": "Welsh",
        "nativeName": "Welsh"
    },
    "da": {
        "dir": "ltr",
        "name": "Danish",
        "nativeName": "Dansk"
    },
    "de": {
        "dir": "ltr",
        "name": "German",
        "nativeName": "Deutsch"
    },
    "el": {
        "dir": "ltr",
        "name": "Greek",
        "nativeName": "Ελληνικά"
    },
    "en": {
        "dir": "ltr",
        "name": "English",
        "nativeName": "English"
    },
    "es": {
        "dir": "ltr",
        "name": "Spanish",
        "nativeName": "Español"
    },
    "et": {
        "dir": "ltr",
        "name": "Estonian",
        "nativeName": "Eesti"
    },
    "fa": {
        "dir": "rtl",
        "name": "Persian",
        "nativeName": "Persian"
    },
    "fi": {
        "dir": "ltr",
        "name": "Finnish",
        "nativeName": "Suomi"
    },
    "fil": {
        "dir": "ltr",
        "name": "Filipino",
        "nativeName": "Filipino"
    },
    "fj": {
        "dir": "ltr",
        "name": "Fijian",
        "nativeName": "Fijian"
    },
    "fr": {
        "dir": "ltr",
        "name": "French",
        "nativeName": "Français"
    },
    "ga": {
        "dir": "ltr",
        "name": "Irish",
        "nativeName": "Gaeilge"
    },
    "gu": {
        "dir": "ltr",
        "name": "Gujarati",
        "nativeName": "ગુજરાતી"
    },
    "he": {
        "dir": "rtl",
        "name": "Hebrew",
        "nativeName": "עברית"
    },
    "hi": {
        "dir": "ltr",
        "name": "Hindi",
        "nativeName": "हिंदी"
    },
    "hr": {
        "dir": "ltr",
        "name": "Croatian",
        "nativeName": "Hrvatski"
    },
    "ht": {
        "dir": "ltr",
        "name": "Haitian Creole",
        "nativeName": "Haitian Creole"
    },
    "hu": {
        "dir": "ltr",
        "name": "Hungarian",
        "nativeName": "Magyar"
    },
    "id": {
        "dir": "ltr",
        "name": "Indonesian",
        "nativeName": "Indonesia"
    },
    "is": {
        "dir": "ltr",
        "name": "Icelandic",
        "nativeName": "Íslenska"
    },
    "it": {
        "dir": "ltr",
        "name": "Italian",
        "nativeName": "Italiano"
    },
    "ja": {
        "dir": "ltr",
        "name": "Japanese",
        "nativeName": "日本語"
    },
    "kk": {
        "dir": "ltr",
        "name": "Kazakh",
        "nativeName": "Kazakh"
    },
    "kn": {
        "dir": "ltr",
        "name": "Kannada",
        "nativeName": "ಕನ್ನಡ"
    },
    "ko": {
        "dir": "ltr",
        "name": "Korean",
        "nativeName": "한국어"
    },
    "lt": {
        "dir": "ltr",
        "name": "Lithuanian",
        "nativeName": "Lietuvių"
    },
    "lv": {
        "dir": "ltr",
        "name": "Latvian",
        "nativeName": "Latviešu"
    },
    "mg": {
        "dir": "ltr",
        "name": "Malagasy",
        "nativeName": "Malagasy"
    },
    "mi": {
        "dir": "ltr",
        "name": "Maori",
        "nativeName": "Māori"
    },
    "ml": {
        "dir": "ltr",
        "name": "Malayalam",
        "nativeName": "മലയാളം"
    },
    "mr": {
        "dir": "ltr",
        "name": "Marathi",
        "nativeName": "मराठी"
    },
    "ms": {
        "dir": "ltr",
        "name": "Malay",
        "nativeName": "Melayu"
    },
    "mt": {
        "dir": "ltr",
        "name": "Maltese",
        "nativeName": "Il-Malti"
    },
    "mww": {
        "dir": "ltr",
        "name": "Hmong Daw",
        "nativeName": "Hmong Daw"
    },
    "nb": {
        "dir": "ltr",
        "name": "Norwegian",
        "nativeName": "Norsk"
    },
    "nl": {
        "dir": "ltr",
        "name": "Dutch",
        "nativeName": "Nederlands"
    },
    "or": {
        "dir": "ltr",
        "name": "Odia",
        "nativeName": "Odia"
    },
    "otq": {
        "dir": "ltr",
        "name": "Querétaro Otomi",
        "nativeName": "Querétaro Otomi"
    },
    "pa": {
        "dir": "ltr",
        "name": "Punjabi",
        "nativeName": "ਪੰਜਾਬੀ"
    },
    "pl": {
        "dir": "ltr",
        "name": "Polish",
        "nativeName": "Polski"
    },
    "pt": {
        "dir": "ltr",
        "name": "Portuguese (Brazil)",
        "nativeName": "Português (Brasil)"
    },
    "pt-pt": {
        "dir": "ltr",
        "name": "Portuguese (Portugal)",
        "nativeName": "Português (Portugal)"
    },
    "ro": {
        "dir": "ltr",
        "name": "Romanian",
        "nativeName": "Română"
    },
    "ru": {
        "dir": "ltr",
        "name": "Russian",
        "nativeName": "Русский"
    },
    "sk": {
        "dir": "ltr",
        "name": "Slovak",
        "nativeName": "Slovenčina"
    },
    "sl": {
        "dir": "ltr",
        "name": "Slovenian",
        "nativeName": "Slovenščina"
    },
    "sm": {
        "dir": "ltr",
        "name": "Samoan",
        "nativeName": "Samoan"
    },
    "sr-Cyrl": {
        "dir": "ltr",
        "name": "Serbian (Cyrillic)",
        "nativeName": "srpski (ćirilica)"
    },
    "sr-Latn": {
        "dir": "ltr",
        "name": "Serbian (Latin)",
        "nativeName": "srpski (latinica)"
    },
    "sv": {
        "dir": "ltr",
        "name": "Swedish",
        "nativeName": "Svenska"
    },
    "sw": {
        "dir": "ltr",
        "name": "Swahili",
        "nativeName": "Kiswahili"
    },
    "ta": {
        "dir": "ltr",
        "name": "Tamil",
        "nativeName": "தமிழ்"
    },
    "te": {
        "dir": "ltr",
        "name": "Telugu",
        "nativeName": "తెలుగు"
    },
    "th": {
        "dir": "ltr",
        "name": "Thai",
        "nativeName": "ไทย"
    },
    "tlh-Latn": {
        "dir": "ltr",
        "name": "Klingon (Latin)",
        "nativeName": "Klingon (Latin)"
    },
    "tlh-Piqd": {
        "dir": "ltr",
        "name": "Klingon (pIqaD)",
        "nativeName": "Klingon (pIqaD)"
    },
    "to": {
        "dir": "ltr",
        "name": "Tongan",
        "nativeName": "lea fakatonga"
    },
    "tr": {
        "dir": "ltr",
        "name": "Turkish",
        "nativeName": "Türkçe"
    },
    "ty": {
        "dir": "ltr",
        "name": "Tahitian",
        "nativeName": "Tahitian"
    },
    "uk": {
        "dir": "ltr",
        "name": "Ukrainian",
        "nativeName": "Українська"
    },
    "ur": {
        "dir": "rtl",
        "name": "Urdu",
        "nativeName": "اردو"
    },
    "vi": {
        "dir": "ltr",
        "name": "Vietnamese",
        "nativeName": "Tiếng Việt"
    },
    "yua": {
        "dir": "ltr",
        "name": "Yucatec Maya",
        "nativeName": "Yucatec Maya"
    },
    "yue": {
        "dir": "ltr",
        "name": "Cantonese (Traditional)",
        "nativeName": "粵語 (繁體中文)"
    },
    "zh-Hans": {
        "dir": "ltr",
        "name": "Chinese Simplified",
        "nativeName": "简体中文"
    },
    "zh-Hant": {
        "dir": "ltr",
        "name": "Chinese Traditional",
        "nativeName": "繁體中文"
    }
}

TAGS = "TAG   :   VALUE\n" + '\n'.join(f"{tag}   :   {name['name']}" for tag, name in LANGUAGES.items())