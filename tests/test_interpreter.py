
import random
import unittest
from pathlib import Path


from makeshift.interpreter import generate


class TestInterpreter(unittest.TestCase):
	def test_seeded_random(self):
		random.seed(42)
		with open("./examples/gang.txt", "r") as f:
			source = f.read()

		expected = [
			"The Gang of Stoneforge's Light",
			'The Ruthless Council of The Uptown Corners',
			'Wicked Monk Union',
			'Eternal Alchemist Alliance',
			'Eternal Protectors of The Ruthless War'
		]

		for i in range(0, 5):
			with self.subTest(i = i):
				self.assertEqual(expected[i], generate(source)[0])

	def test_super_integrated(self):
		# just run 100 generates on each example file and make sure we don't 
		# fuck up

		p = Path("./examples")

		makeshift_files = 0
		for exampleFile in p.iterdir():
			if exampleFile.suffix not in {".txt", ".mksft"}:
				continue

			with open(exampleFile) as ex:
				source = ex.read()

			for i in range(0, 100):
				with self.subTest(file = exampleFile, iteration = i):
					val = generate(source)[0]
					#print(f'{exampleFile.name} iteration {i}: val')
					self.assertIsNotNone(val)





