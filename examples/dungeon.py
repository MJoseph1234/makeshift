import random


from utils import pluralize, gerund

class Dungeon():
"""
The {adjective} {place}
The {adjective} {place} of {owner}


"""

def place():
	place = [
	'dungeon', 'crypt', 'caves', 'prison', 'ruins', 'sanctum',
	'vault', 'pit', 'catacombs', 'den', 'cavern', 'maze', 'hive',
	'mines', 'monestary', 'tower', 'labrynth'
	]
	return(random.choice(place))

def adjective():
	adjective = [
	'Horror', 'Dark', 'Forsaken', 'Abandoned', 'Unholy', 'Overgrown',
	'Clockwork'
	]
	return(random.choice(adjective))