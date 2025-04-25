import random
import string

def generate_id(tamanho=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))
