
import argparse
from pathlib import Path

from interpriter.lexer import Lexer
from interpriter.parser import Parser
from interpriter.interpriter import TreeWalkInterpriter

def main():
	cli_parser = argparse.ArgumentParser(
		description = "Run a Random Generator")

	cli_parser.add_argument('infile',
		help = 'Generator file to run')
	cli_parser.add_argument('-c', '--count',
		help = 'Number of examples to generate',
		type = int, default = 1)

	args = cli_parser.parse_args()
	if args.infile == '' or args.infile is None:
		cli_parser.print_help()
		return

	filename = find_file(args.infile)
	with open(filename) as gen_file:
		x = Lexer(gen_file.read())

	x.lexv2()

	pr = Parser(x.tokens)
	ast = pr.generator(args.infile)

	interp = TreeWalkInterpriter()
	if args.count == 1:
		print(f'{interp.visit_generator_node(ast)}')
		return
	
	for x in range(0,args.count):
		print(f'{x+1:>2}. {interp.visit_generator_node(ast)}')

def find_file(filename):
	if Path(filename).exists():
		return(filename)
	elif Path('examples', filename).exists():
		return(Path('examples', filename))