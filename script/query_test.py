#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State

import django
django.setup()

# states = State.objects.all().order_by('capital')

#states = State.objects.all().exclude(name_startwith="C").order_by('name')

#states = State.object.all().filter(name_startwith="C").order_by('name')

states = State.object.all().values_list('name','abbreviation', 'population')

for state in states:
	print state  
	

# for state in states:
# print "%s | %s | %s" % (state.name, state.capital, state.population)