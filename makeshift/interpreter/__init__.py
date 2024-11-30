
from makeshift.interpreter.lexer import Lexer
from makeshift.interpreter.parser import Parser
from makeshift.interpreter.interpreter import TreeWalkInterpreter

def generate(source, title = '', count = 1):	#, unique = True):

	tokens = Lexer(source).tokenize()
	ast = Parser(tokens).generator("")
	results = []

	for i in range(0, count):
		results.append(TreeWalkInterpreter().visit_generator_node(ast))

	return(results)

