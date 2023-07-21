import interpriter.ast as ast

class AstPrinter(ast.Visitor):
	def __init__(self):
		self.depth = 0
		self.increment = 3

	def indent(self):
		self.depth += self.increment

	def deindent(self):
		self.depth -= self.increment

	def print_ast(self, node):
		node.accept_visitor(self)

	def visit_generator_node(self, gen):
		print(f'{" "*self.depth}generator: {gen.title}')
		for definition in gen.definitions:
			definition.accept_visitor(self)

	def visit_definition_node(self, definition):
		print(f'{" "*self.depth}definition')
		self.indent()
		definition.name.accept_visitor(self)
		for option in definition.options:
			option.accept_visitor(self)
		self.deindent()

	def visit_name_node(self, name):
		print(f'{" "*self.depth}name: {name.value}')

	def visit_option_node(self, option):
		print(f'{" "*self.depth}option percent: {option.percent}')
		self.indent()
		option.expression.accept_visitor(self)
		self.deindent()

	def visit_expression_node(self, expr):
		print(f'{" "*self.depth}expression')
		self.indent()
		for subex in expr.subexpressions:
			subex.accept_visitor(self)
		self.deindent()

	def visit_resolvable_node(self, res):
		print(f'{" "*self.depth}resolvable')
		self.indent()
		for segment in res.segments:
			segment.accept_visitor(self)
		self.deindent()

	def visit_string_literal_node(self, string):
		print(f'{" "*self.depth}string literal: "{string.value}"')

	def visit_reference_node(self, reference):
		print(f'{" "*self.depth}reference')
		self.indent()
		reference.name.accept_visitor(self)
		if reference.method is not None:
			reference.method.accept_visitor(self)
		else:
			print(f'{" "*self.depth}method: None')
		self.deindent()

	def visit_method_node(self, method):
		print(f'{" "*self.depth}method: {method.method_name}')