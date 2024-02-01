
import argparse
import sys
from pathlib import Path

from makeshift.interpreter import generate

def parse_cli_args():
	parser = argparse.ArgumentParser(
		description = "Run a Random Generator")

	parser.add_argument('input_file',
		help = 'MakeShift template file to run')
	parser.add_argument('-c', '--count',
		help = 'Number of examples to generate',
		type = int, default = 1)

	args = parser.parse_args()

	if args.input_file == '' or args.input_file is None:
		parser.print_help()
		return(None)

	return(args)

def main():
	args = parse_cli_args()
	if args is None:
		sys.exit(2)

	filename = find_file(args.input_file)

	with open(filename) as template_file:
		source = template_file.read()

	results = generate(source, count = args.count)

	if args.count == 1:
		print(results[0])
		return

	for i in range(0, args.count):
		print(f'{i+1:>2}. {results[i]}')
	return

def find_file(filename):
	if Path(filename).exists():
		return(filename)
	elif Path('examples', filename).exists():
		return(Path('examples', filename))

if __name__ == "__main__":
	main()