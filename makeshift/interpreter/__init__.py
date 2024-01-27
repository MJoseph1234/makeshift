
from makeshift.interpreter.lexer import Lexer
from makeshift.interpreter.parser import Parser
from makeshift.interpreter.interpreter import TreeWalkInterpreter

def run(source, title = '', count = 1):	#, unique = True):

	tokens = Lexer(source).lexv2()
	ast = Parser(tokens).generator("")

	results = set()
	while len(results) < count:
		result = TreeWalkInterpreter().visit_generator_node(ast)
		results.add(result)

	return(list(results))
