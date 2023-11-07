import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

def limpiar_parrafo(parrafo):

    stemmer = PorterStemmer()

    signos_puntuacion = string.punctuation + "''“”– .. `` ' - — ' "

    palabras = word_tokenize(parrafo)

    palabras_limpias = [stemmer.stem(palabra) for palabra in palabras if palabra not in signos_puntuacion]

    texto_limpiado = ' '.join(palabras_limpias)

    return texto_limpiado

parrafo_entrada = "Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. Data with many entries (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate"
texto_output = limpiar_parrafo(parrafo_entrada)

print("Texto output:")
print(texto_output)