
import random

from utils import pluralize, gerund

class WeaponShop():
	"""
	Name ::=
		The {animal|profession}'s {place|item[ "and" item]}
		The {animal} {profession}'s {place}
		{"The "|"By "|""}{item} and {item}
		{smith-name|animal}'s {descriptor} {place|item}
		{smith-name|animal}'s {item} and {item}
	"""
	def generate():
		rand = random.randrange(10)
		if 0 <= rand <= 2:
			return(f'The {animal_profession()}\'s {place_item_item()}')
		elif rand == 3:
			return(f'The {animal()} {profession()}\'s {place()}')
		elif 4 <= rand <= 5:
			item1 = item()
			return(f'{determiner()}{item1} and {item(item1)}')
		elif rand == 6:
			item1 = item()
			return(f'The {item1} and the {item(item1)}')
		elif rand == 7:
			return(f'{smith_animal()}\'s {descriptor()} {place_item()}')
		elif 8 <= rand <= 9:
			item1 = item()
			return(f'{smith_animal()}\'s {item1} and {item(item1)}')

def descriptor():
	return(adjective())
	# rand = random.randrange(3)
	# if rand < 2:
	# 	return(adjective())
	# else:
	# 	return(gerund(action()))


def animal_profession():
	rand = random.randrange(2)
	if rand == 0:
		return(animal())
	elif rand == 1:
		return(profession())

def place_item():
	rand = random.randrange(2)
	if rand == 0:
		return(place())
	if rand == 1:
		return(item())

def place_item_item():
	rand = random.randrange(3)
	if rand == 0:
		return(place())
	if rand == 1:
		return(item())
	if rand == 2:
		itm1 = item()
		return(f'{itm1} and {item(itm1)}')

def determiner():
	rand = random.randrange(3)
	if rand == 0:
		return('')
	if rand == 1:
		return('The ')
	if rand == 2:
		return('By ')

def smith_animal():
	rand = random.randrange(2)
	if rand == 0:
		return(smith_name())
	if rand == 1:
		return(animal())





"""
names I like:
	a fighting chance

action:
	fight, defend

concept:
	chance
"""
def item(avoid_word = None):
	items = [
	'Anvil', 'Armament', 'Armor', 'Arsenal', 'Blades', 
	'Fire', 'Forge', 'Hammer', 'Hand', 'Iron', 
	'Metal', 'Muscle', 'Shields', 'Steel', 'Thunder', 
	'Weaponry', "Tongs"
	]
	# Tongs, arcana
	if avoid_word:
		items = [itm for itm in items if itm != avoid_word]
	return(random.choice(items))

def place():
	places = [
	'Outfitter', 'Vault', 'Roost', 'Caravan', 'Bazaar', 'Exchange',
	'Emporium', 'Showroom'
	]
	return(random.choice(places))


def animal():
	animals = [
	'Armadillo', 'Ram', 'Griffon', 'Lion', 'Minotaur', 'Dragon', 'Fox', 'Scorpion',
	'Unicorn', 'Rhino', 'Naga', 'Hawk', 'Heron', 'Tiger', 'Wolf', 'Centaur', 'Giant', "Tuna"
	]
	# Tuna
	return(random.choice(animals))

def adjective():
	adjectives = [
	'Marvelous', 'Hot', 'Fiery', 'Majestic', 'Wonderous', 'Heavy', 'Mighty',
	'Trusty', 'Ancient'
	]
	return(random.choice(adjectives))

def smith_name():
	names = [
	'Haldor', 'Smith', 'Griffon', 'Ningal', 'Balthazar'
	]
	return(random.choice(names))

def profession():
	professions = [
	'Warrior', 'Armoror', 'Mercenary', 'Ranger', 'Soldier', 'Smith', 'Fighter', 
	'Defender', 'Blacksmith', 'Engineer', 'Craftswoman', 'Smithy'
	]
	return(random.choice(professions))



#OK!