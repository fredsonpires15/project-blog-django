from random import SystemRandom
import string
from django.utils.text import slugify

def random_string(length=5):  
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=length
    ))

def slogify_new(text, k=4):
    return slugify(text) + '-' + random_string(k)


