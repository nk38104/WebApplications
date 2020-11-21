import base64
from os import urandom
from hashlib import pbkdf2_hmac


def hash_string(text):
    salt = urandom(32)
    key = pbkdf2_hmac('sha256', text.encode('utf-8'), salt, 100000)
    hash = salt + key 
    return hash


def verify_input(text, hash):
    salt = hash[:32]
    key = hash[32:]

    new_key = pbkdf2_hmac(
        'sha256',
        text.encode('utf-8'), 
        salt, 
        100000)
    return new_key == key 


