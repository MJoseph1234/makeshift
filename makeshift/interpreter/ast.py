class Visitor():
	def __init__(self):
		return

	def visit_generator_node(self):
		raise NotImplementedError

	def visit_definition_node(self):
		raise NotImplementedError

	def visit_name_node(self):
		raise NotImplementedError

	def visit_option_node(self):
		raise NotImplementedError

	def visit_expression_node(self):
		raise NotImplementedError

	def visit_resolvable_node(self):
		raise NotImplementedError

	def visit_reference_node(self):
		raise NotImplementedError

	def visit_string_literal_node(self):
		raise NotImplementedError

	def visit_method_node(self):
		raise NotImplementedError

class Node():
	"""abstract base class representing
	a node in our AST. Subclass this into each
	node type"""
	def __init__(self):
		pass

	def __repr__(self):
		return(self.accept_visitor(visitor = Debug()))

	def __str__(self):
		return(self.accept_visitor(visitor = FilePrinter()))

	def accept_visitor(self, visitor):
		raise NotImplementedError

# The overall thing to be generated. Usually a singlular file that represents
# the thing to be made
class Generator(Node):
	def __init__(self, title, top_definition, definitions):
		super().__init__()
		self.title = title
		self.top_definition = top_definition #name of the primary thing this generates
		self.definitions = definitions

	def accept_visitor(self, visitor):
		return(visitor.visit_generator_node(self))

# A single term with a list of options that could be used to define that term
class Definition(Node):
	def __init__(self, name, options):
		super().__init__()
		self.name = name
		self.options = options

	def accept_visitor(self, visitor):
		return(visitor.visit_definition_node(self))

# A term or name for a definition. Usually a single-word string
class Name(Node):
	def __init__(self, value):
		super().__init__()
		self.value = value

	def accept_visitor(self, visitor):
		return(visitor.visit_name_node(self))

# a line of text under a term or name that is one of the choices for a definition
# for that name or term. Usually looks like a single sentence or phrase
class Option(Node):
	def __init__(self, expression, percent = None):
		super().__init__()
		self.expression = expression
		self.percent = percent

	def accept_visitor(self, visitor):
		return(visitor.visit_option_node(self))

# segments that make up an Option. Usually sentence fragments consisting
# of string literals and groups of other resovable options within curly brackets
class Expression(Node):
	def __init__(self, subexpressions): #string = None, resolvable = None, subexpressions = None):
		super().__init__()
		# self.string = string
		# self.resolvable = resolvable
		self.subexpressions = subexpressions
		#should be a list of strings and resolvables

	def accept_visitor(self, visitor):
		return(visitor.visit_expression_node(self))

# a segment of an expression between curly brackets that contains a list of 
# choices or a reference to another definition from which a choice should be made
class Resolvable(Node):
	def __init__(self, segments): #name = None, method = None, expression = None, segments = None):
		super().__init__()
		# self.name = name
		# self.method = method
		# self.expression = expression
		self.segments = segments
		#should be a list of references and expressions

	def accept_visitor(self, visitor):
		return(visitor.visit_resolvable_node(self))

# A string to use as-is. No choice/option/random roll to be made
class String_Literal(Node):
	def __init__(self, value):
		super().__init__()
		self.value = value

	def accept_visitor(self, visitor):
		return(visitor.visit_string_literal_node(self))

# a choice within an resolvable segment that indicates we should look to 
# another definition to make a choice from there. Possibly modify that choice
# with a method
class Reference(Node):
	def __init__(self, name, method = None):
		super().__init__()
		self.name = name
		self.method = method

	def accept_visitor(self, visitor):
		return(visitor.visit_reference_node(self))

# A function/macro to use to modify a value within a resolvable
class Method(Node):
	def __init__(self, method_name):
		super().__init__()
		self.method_name = method_name

	def accept_visitor(self, visitor):
		return(visitor.visit_method_node(self))