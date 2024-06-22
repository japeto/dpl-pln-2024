from flask import Flask, jsonify, request
from flask_cors import CORS

from preproces_nltk import preprocessing as pnltk
from preproces_spacy import preprocessing as pspacy