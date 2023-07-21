import random


from utils import pluralize, gerund

class Inn():
	"""
	Name:
		Inn of the {descriptor} {thing}
		The {descriptor} {noun}
		The {creature}'s {place}
		The {creature}'s {item}
		The {item} {place}
		{noun} and {noun}
	
	descriptor:
		{adjective}
		{gerund(action)}
	
	thing:
		{creature}
		{item}

	creature:
		{person}
		{animal}

	noun:
		{thing}
		{place}

	"""
	def generate():
		rand = random.randrange(10)
		if rand == 0:
			return(f'Inn of the {descriptor()} {thing()}')
		elif rand == 1:
			des = descriptor()
			return(f'Inn of the {des} {thing(des)}')
		
		elif rand == 2:
			return(f'The {descriptor()} {noun()}')
		elif rand in {3, 4}:
			des = descriptor()
			return(f'The {des} {noun(des)}')

		elif rand == 5:
			cre = creature()
			return(f'The {cre}\'s {place(cre)}')
		elif rand == 6:
			cre = creature()
			return(f'The {cre}\'s {item(cre)}')

		elif rand == 7:
			itm = item()
			return(f'The {itm} {place(itm)}')
		elif rand == 8:
			itm = item()
			return(f'The {itm} {place(itm)}')

		elif rand == 9:
			thing1 = thing()
			return(f'{thing1} and {thing(thing1)}')

def descriptor(alliterate_word = None):
	rand = random.randrange(3)
	if rand < 2:
		return(adjective(alliterate_word))
	else:
		return(gerund(action(alliterate_word)))

def thing(alliterate_word = None):
	rand = random.randrange(3)
	if rand < 2:
		return(creature(alliterate_word))
	else:
		return(item(alliterate_word))

def creature(alliterate_word = None):
	rand = random.randrange(2)
	if rand == 0:
		return(animal(alliterate_word))
	elif rand == 1:
		return(person(alliterate_word))

def noun(alliterate_word = None):
	rand = random.randrange(4)
	if rand == 0:
		return(animal(alliterate_word))
	if rand == 1:
		return(person(alliterate_word))
	if rand == 2:
		return(item(alliterate_word))
	if rand == 3:
		return(place(alliterate_word))


def adjective(alliterate_word = None):
	adjectives = [
	'Amaranthine','Ancestral','Ancient','Astral',
	'Blessed','Blue','Bright','Celestial','Corrupted','Dark',
	'Divine','Elder','Eternal','Ethereal','Exalted','Foul','Golden','Guilty','Hallowed',
	'Heavenly','Immortal','Impure','Ivory','Shining','Lucent','Pale','Primal','Putrid',
	'Radiant','Red','Rusted','Sacred','Sanctified','Sanguine','Silver','Tainted',
	'Timeless','Tribal','White','Wicked','Still','Alabaster', 'Blight',
	'Deathly','Ghostly','Honor','Pearl','Phantom','Spirit',
	'Soul','Iron','Holy', "Bronze", "Brown", "Burgundy", "Driven", "Enchanted", "Gold", "Green", "Grey",
	"Grouchy", "Hallowed", "Happy", "Hidden", "Hungry", "Jovial", "Lone", "Lost", "Lucky",
	"Merry", "Moody", "Morose", "Orange", "Purple", "Silent", "Thirsty",
	"Wasted", "Wild",
	]
	if alliterate_word:
		temp = [adj for adj in adjectives if adj.startswith(alliterate_word[0])]
		if len(temp) > 0:
			adjectives = temp
	return(random.choice(adjectives))

def person(alliterate_word = None):
	persons = [
	'Beggar','Harper','Hunter','Emperor','Warrior','Sage','Widow',
	"Adventurer", "Baker", "Blacksmith", "Brewer", "Bricklayer", "Builder",
	"Butcher", "Carpenter", "Conjurer", "Cooper", "Diviner", "Enchanter", "Evoker", "Farrier",
	"Ferryman", "Fisherman", "Glazier", "Illusionist", "Knight", "Mage", "Magician", "Mason",
	"Miller", "Plumber", "Porter", "Printer", "Roper", "Sailor", "Shipwright", "Smith",
	"Soldier", "Waterman", "Wizard",
	]
	if alliterate_word:
		temp = [per for per in persons if per.startswith(alliterate_word[0])]
		if len(temp) > 0:
			persons = temp
	return(random.choice(persons))

def place(alliterate_word = None):
	places = [
	'Lounge','Library','Pub','Tavern', 'Inn', 'Hangout', 'Den', 
	'Resting Place', 'Barroom', 'Barrelhouse', 'House', 'Grogshop',
	'Public House', 'Roadhouse', 'Saloon', 'Lodge', 'Hostel'
	]
	if alliterate_word:
		temp = [pla for pla in places if pla.startswith(alliterate_word[0])]
		if len(temp) > 0:
			places = temp
	return(random.choice(places))

def item(alliterate_word = None):
	items = [
	'Cask', 'Spear', 'Barrel', 'Keg', 'Scroll', 'Cup', 'Pipe',
	"Abbey", "Anchor", "Anvil", "Arrow", "Axe", "Belfry", "Bell", "Book", "Buckle", "Cap",
	"Castle", "Column", "Crescent", "Crown", "Drum", "Feather", "Foil", "Hammer", "Harp",
	"Harrow", "Helmet", "Horseshoe", "Key", "Lance", "Lance", "Locket", "Mace", "Mill",
	"Mitre", "Moon", "Nail", "Oar", "Rake", "Rook", "Scale", "Sceptre", "Scythe",
	"Ship", "Shovel", "Spur", "Star", "Steeple", "Sun", "Sword", "Thunderbolt",
	"Tower", "Trumpet", "Wand", "Wheel","Tankard"
	]
	if alliterate_word:
		temp = [itm for itm in items if itm.startswith(alliterate_word[0])]
		if len(temp) > 0:
			items = temp
	return(random.choice(items))

def animal(alliterate_word = None):
	animals = [
	'Bear','Beetle','Carp','Cat','Cormorant','Cow','Deer','Dog','Fox',
	'Frog','Goat','Hart','Hawk','Heron','Horse','Hound','Lion','Magpie',
	'Owl','Panther','Peacock','Phoenix', 'Rabbit','Ram','Rat','Raven','Salamander',
	'Scorpion','Rat','Rabbit','Snake','Spider','Squirrel','Stag','Tiger',
	'Toad','Tortoise','Turtle','Vulture','Wolf','Beetle','Locust',
	"Antelope", "Ape", "Baboon", "Badger", "Bat", "Beaver", "Bee", "Beetle", "Boar",
	"Camel", "Carp", "Cat", "Cod", "Cormorant", "Cow", "Crab", "Deer", "Dog", "Dolphin",
	"Donkey", "Dove", "Dragonfly", "Duck", "Eagle", "Eel", "Elephant", "Elk", "Ermine", "Fox",
	"Frog", "Goat", "Goose", "Hare", "Hart", "Hawk", "Hedgehog", "Heron", "Herring", "Horse",
	"Hound", "Hyena", "Jackal", "Lamb", "Leopard", "Lion", "Magpie", "Mermaid", "Mole",
	"Octopus", "Osprey", "Otter", "Owl", "Panther", "Peacock", "Pelican", "Perch", "Phoenix",
	"Pony", "Porcupine", "Rabbit", "Ram", "Rat", "Raven", "Salamander", "Salmon", "Scorpion",
	"Seagull", "Seal", "Shark", "Sheep", "Snake", "Spider", "Squid", "Squirrel", "Stag",
	"Stoat", "Stork", "Swan", "Tiger", "Toad", "Tortoise", "Trout", "Turkey", "Turtle",
	"Unicorn", "Weasel", "Whale", "Whelk",
	]
	if alliterate_word:
		temp = [ani for ani in animals if ani.startswith(alliterate_word[0])]
		if len(temp) > 0:
			animals = temp
	return(random.choice(animals))

def action(alliterate_word = None):
	actions = [
	'Dance','Whisper','Shiver','Prance','Rise','Fall','Laugh','Travel','Creep',
	'Sing','Fade','Glow','Shine','Stand','Weep','Drown','Howl','Smile','Hunt',
	'Burn','Return','Dream','Wake','Slumber'
	]
	if alliterate_word:
		temp = [act for act in actions if act.startswith(alliterate_word[0])]
		if len(temp) > 0:
			actions = temp
	return(random.choice(actions))




#OK!