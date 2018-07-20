import pandas as pd
import string
import secrets
import requests
import random
from zxcvbn import zxcvbn


def pw_gen_all(size, chars=string.ascii_letters + string.digits + string.punctuation + string.whitespace):
    return ''.join(secrets.choice(chars) for i in range(size))

def pw_gen_word(size):
    f = open('words.txt', 'r')
    all_words = f.read()
    words = all_words.split('\n')
    password = ' '.join(secrets.choice(words) for i in range(size))
    return password.replace(' ','-')

pw_chars = input('How many characters should your password have?')
print("You've picked:", pw_chars)

new_pw_chars = (pw_gen_all(int(pw_chars)))
new_pw_chars = new_pw_chars
print('This is your new password:', '"' + str(new_pw_chars)+ '"')

print('How long it will take to crack your password?')
pw_check = zxcvbn(new_pw_chars)
print(pw_check['crack_times_display']['offline_fast_hashing_1e10_per_second'])

import hashlib
hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()
