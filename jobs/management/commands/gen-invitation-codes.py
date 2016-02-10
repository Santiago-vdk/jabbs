from django.core.management import BaseCommand
import time

from jobs.models import InvitationCode

import argparse

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    
    # Show this when the user types help
    help = "invitation generator"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('ammount', nargs='+', type=int)
        
    # A command must define handle()
    def handle(self, *args, **options):
        ammount = options['ammount'][0]
        print('\x1b[0m' + "Generating " + str(ammount) + " tokens...")
       
        ammount = int(ammount)
        start = time.time()
        i = ammount
        while i > 0:
            code = InvitationCode()
            code.save()
            i -= 1
        end = time.time()
        O = int(end) - int(start)
        print("Generated " + str(ammount) + " tokens in aprox. " + str(O) + " seconds." + '\x1b[0m')
            
