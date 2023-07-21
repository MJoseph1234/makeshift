
import random

from utils import pluralize, gerund

class Shrine():
	"""
	Name:
		The {descriptor} {place},
		{place} of {diety},
		Place where the pluralize({animal}) {action},
		{place} of the {number} pluralize({animal})
	
	Place:
		Shrine
		{building}
		{natural_feature}

	Descriptor:
		{adjective}
		{gerund(action)}

	Diety:
		the {person}
		the {descriptor} {person}
		the {animal}
		the {descriptor} {animal}
		{concept}
		{descriptor} {concept}
	"""
	def generate():
		rand = random.randrange(10)
		if 0 <= rand < 4:
			return(f'The {descriptor()} {place()}')
		elif 4 <= rand < 8:
			return(f'{place()} of {diety()}')
		elif rand == 8:
			return(f'Place where the {"".join(pluralize(animal()))} {action()}')
		elif rand == 9:
			return(f'{place()} of the {number()} {"".join(pluralize(animal()))}')

def diety():
	rand = random.randrange(10)
	if 0 <= rand < 2:
		return(f'the {person()}')
	elif rand == 2:
		return(f'the {descriptor()} {person()}')
	elif 3 <= rand < 5:
		return(f'the {animal()}')
	elif rand == 5:
		return(f'the {descriptor()} {animal()}')
	elif 6 <= rand < 9:
		return(f'{concept()}')
	elif rand == 9:
		return(f'{descriptor()} {concept()}')

def place():
	rand = random.randrange(6)
	if 0 <= rand < 2:
		return('Shrine')
	elif 2 <= rand < 5:
		return(building())
	else:
		return(natural_feature())

def descriptor():
	rand = random.randrange(3)
	if rand < 2:
		return(adjective())
	else:
		return(gerund(action()))

def adjective():
	adjectives = [
	"Amaranthine","Ancestral","Ancient","Astral",
	"Blessed","Blue","Bright","Celestial","Corrupted","Dark",
	"Divine","Elder","Eternal","Ethereal","Exalted","Foul","Golden","Guilty","Hallowed",
	"Heavenly","Immortal","Impure","Ivory","Shining","Lucent","Pale","Primal","Putrid",
	"Radiant","Red","Rusted","Sacred","Sanctified","Sanguine","Silver","Tainted",
	"Timeless","Tribal","White","Wicked","Still","Alabaster", "Blight",
	"Death","Ghost","Honor","Pearl","Phantom","Spirit",
	"Soul","Iron",
	]
	return(random.choice(adjectives))

def action():
	actions = [
	"Dance","Whisper","Shiver","Rot","Rise","Fall","Laugh","Travel","Creep",
	"Sing","Fade","Glow","Shine","Stand","Weep","Drown","Howl","Smile","Hunt",
	"Burn","Return","Dream","Wake","Slumber"
	]
	return(random.choice(actions))

def animal():
	animals = [
	"Bear","Beetle","Carp","Cat","Cormorant","Cow","Deer","Dog","Fox",
	"Frog","Goat","Hart","Hawk","Heron","Horse","Hound","Lion","Magpie",
	"Owl","Panther","Peacock","Phoenix", "Rabbit","Ram","Rat","Raven","Salamander",
	"Scorpion","Rat","Rabbit","Snake","Spider","Squirrel","Stag","Tiger",
	"Toad","Tortoise","Turtle","Vulture","Wolf","Beetle","Locust"
	]
	return(random.choice(animals))

def building():
	buildings = [
	"Altar", "Pagoda", "Gate", "Obelisk", "Pagoda", "Pillar", "Pillars",
	]
	return(random.choice(buildings))

def natural_feature():
	natural_features = [
	"Basin","Cavern","Grove","Pond","Pool","Menhir",
	"Grotto","Cenote", "Tree", "Stones", "Cave"
	]
	return(random.choice(natural_features))

def person():
	persons = [
	"Father","Mother","Parent","Sibling","Hunter","Emperor","Empress","Warrior","Sage","Ancestor"
	]
	return(random.choice(persons))

def concept():
	concepts = [
	"Love","Knowledge","Wisdom","Truth","Justice","Mercy","Protection","Healing","Strength","Courage",
	"Fortune","Prosperity","Storms","Fire","Water","Earth","Air","Dreams","Music","Poetry","Dance",
	"Ancestors","Transcendence","Anguish","Blight","Confessions","Connections","Courage","Decay",
	"Lore","Silence","Triumph","Wisdom","Mending","Healing","Judgement","Forgiveness","Justice","Textiles", 
	]
	return(random.choice(concepts))

def number():
	numbers = [
	"Two","Three","Four","Five","Six","Seven","Eight","Eight-and-a-Half","Nine",
	"Twelve","Thirty-Six", "Forty","Seventy-Two","Nine-and-Twenty", "Ninety-Nine","Thousand","Thousand-Thousand"
	]
	return(random.choice(numbers))