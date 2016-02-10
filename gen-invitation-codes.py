import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'jabbs'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jabbs.settings")
from django.conf import settings

from django.db import models
from jobs.models import InvitationCode
import time



def generate_codes(ammount):
    print('\x1b[0m' + "Generating " + ammount + " tokens...")
    ammount = int(ammount)

    start = time.time()
    i = ammount
    while i > 0:
        code = InvitationCode()
        code.save()
        i -= 1
    end = time.time()
    O = int(end) - int(start)
    print("Generated " + str(ammount) + " tokens in aprox. " + str(O) + " seconds.")

if __name__ == '__main__':
    ammount = sys.argv[1]
    generate_tokens(ammount)
