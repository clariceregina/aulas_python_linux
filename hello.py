#!/usr/bin/env python3

# The comment below indicates where python is in my Linux. This type of comment is a SHEBANG

"""Hello World in multiple languages

Based on the language set in the environment, the corresponding message is shown.

Usage:

Make sure the LANG variable is properly set. Ex:

    export LANG=en_US

Running the project:

    python3 hello.py
    or
    ./hello.py
"""
# Dunder variables
__version__ = "0.0.1"
__author__ = "Clarice Regina"
__license__ = "Unlicense"

import os

# if the OS does not have the LANG variable, we can put a default value "en_US"
# [:5] means we only want the first 5 characters from the LANG variable, which usually has more characters, for example "en_US.utf8"
current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)
