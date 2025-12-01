import sys

import makeshift.interpreter.ast as ast

class AstPrinter(ast.Visitor):
	def __init__(self, target = sys.stdout):
		self.target = target
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
		self.target.write(f'{" "*self.depth}definition: "{definition.name.value}"\n')
		self.indent()
		counter = 0
		for option in definition.options:
			counter += 1
			option.accept_visitor(self, count = counter)
		self.deindent()

	def visit_name_node(self, name):
		self.target.write(f'{" "*self.depth}name: "{name.value}"\n')

	def visit_option_node(self, option, count):
		if option.percent:
			self.target.write(f'{" "*self.depth}option {count}. Percent: {option.percent}\n')
		else:
			self.target.write(f'{" "*self.depth}option {count}\n')
		self.indent()
		option.expression.accept_visitor(self)
		self.deindent()

	def visit_expression_node(self, expr):
		self.target.write(f'{" "*self.depth}expression\n')
		self.indent()
		for subex in expr.subexpressions:
			subex.accept_visitor(self)
		self.deindent()

	def visit_resolvable_node(self, res):
		self.target.write(f'{" "*self.depth}resolvable\n')
		self.indent()
		for segment in res.segments:
			segment.accept_visitor(self)
		self.deindent()

	def visit_string_literal_node(self, string):
		self.target.write(f'{" "*self.depth}string literal: "{string.value}"\n')

	def visit_reference_node(self, reference):
		self.target.write(f'{" "*self.depth}reference\n')
		self.indent()
		reference.name.accept_visitor(self)
		if reference.method is not None:
			reference.method.accept_visitor(self)
		else:
			self.target.write(f'{" "*self.depth}method: None\n')
		self.deindent()

	def visit_method_node(self, method):
		self.target.write(f'{" "*self.depth}method: {method.method_name}\n')