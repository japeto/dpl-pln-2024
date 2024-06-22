
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import post_tag
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Descargar punkt
nltk.download("punkt") # tokenizacion considerando puntuacion
# Descargar punkt
nltk.download("wordnet") # red semantica para POSTag y Lematizacion
# Descargar diccionarion de stopwords
nltk.download("stopwords")
# Open Multilingual wordnet -- red semantica multilingue
nltk.download("omw-1.4")

## Creo los procesadores que voy a utilizar
stemmer = SnowballStemmer('spanish')
lemmatizer = WordNetLemmatizer()

def preprocessing(paragraphs:str, do_stem:bool=False, do_post:bool=False) ->dict:
  # Segmentation -- Cuando es un parrafo debo separar las oraciones
  lsentences = sent_tokenize(paragraphs)
  # Tokenization  
  lltokens = [word_tokenize(a_sentence) for a_sentence in lsentences]
  ## Stemming (Optional)
  if do_stem: 
    stemmed = [[stemmer.stem(a_token) for a_token in a_sentence] for a_sentence in lltokens]
  ## Postagging (Optional)
  if do_post:
    tagged = [post_tag(a_sentence) for a_sentence in lltokens]
  # Lemmatization
  lemmatized = [[lemmatizer.lemmatize(a_token) for a_token in a_sentence] for a_sentence in lltokens]
  # Remove Stop words
  # Remove punctuation


## testing preprocessing
a_paragraph = "Un párrafo es una unidad de un texto compuesta por una o varias oraciones"\
  ", que comienza con una mayúscula y que termina con un punto y aparte. Los textos se "\
  "organizan de manera tal que cada párrafo trata sobre una idea central. "\
  "Generalmente, la primera oración de cada párrafo suele explicitar cuál es el "\
  "punto principal que se desarrollará."

result= preprocessing(a_paragraph)
print(result)