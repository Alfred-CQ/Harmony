import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

stemmer = PorterStemmer()

archivo_entrada = "contenido.txt"
archivo_salida = "texto_limpio.txt"

signos_puntuacion = string.punctuation + "''“”– .. `` ' - — ' "

with open(archivo_entrada, 'r') as entrada:
    texto = entrada.read()

palabras = word_tokenize(texto)

palabras_limpias = [stemmer.stem(palabra) for palabra in palabras if palabra not in signos_puntuacion]

texto_limpiado = ' '.join(palabras_limpias)

with open(archivo_salida, 'w') as salida:
 
    salida.write(texto_limpiado)

print("Texto limpiado y guardado en", archivo_salida)
