"""
The lexer turns the raw input into a series of defined Tokens

TODO: get rid of match method, because we don't ever use it. Clean up tests too
TODO: don't require input when initializing. do it all through .tokenize method
"""


from makeshift.interpreter.utils import GeneratorSyntaxError
from makeshift.interpreter.token import TokenType, Token

KEYS = {
	'OPEN_BRACE': '{',
	'CLOSE_BRACE': '}',
	'COLON': ':',
	'OPEN_BRACKET': '[',
	'CLOSE_BRACKET': ']',
	'OPEN_PARENTHESIS': '(',
	'CLOSE_PARENTHESIS': ')',
	'BAR': '|',
	'DOT': '.',
	'NEWLINE': '\n',
	'TAB': '\t',
	'PERCENT': '%',
	'SLASH': '/',
	'EQUALS': '='
	}

def is_string_char(char):
	return(char.isalpha() or char in " !\'\"#$&'`()*,+-_/:;<>?@[]\\^_~")
	
	if ord(char) in {ord(x) for x in " !\'\"#$&'`()*,+-_/:;<>?@[]\\^_~"}:
		return(True)
	else:
		return(char.isalpha())

class Lexer():
	def __init__(self, inp):
		self.inp = inp.strip() #leading/trailing whitespace in file doesn't affect the grammar
		self.index = 0
		self.line = 1
		self.offset = 0
		self.tokens = []

	def add_token(self, token_type, literal = None, line = None, offset = None):
		if token_type.name in KEYS and literal is None:
			literal = KEYS.get(token_type.name)

		if offset is None:
			offset = self.offset - len(literal)
		if line is None:
			line = self.line
		
		self.tokens.append(Token(token_type, literal, line, offset))
		return

	def advance(self):
		self.index += 1
		self.offset += 1
		return(self.inp[self.index - 1])

	def is_at_end(self):
		return(self.index >= len(self.inp))

	def match(self, expected):
		if self.is_at_end():
			return(False)
		elif self.inp[self.index] != expected:
			return(False)

		self.index += 1
		self.offset += 1
		return(True)

	def peek(self, ct = 0):
		if self.is_at_end():
			return(False)
		return(self.inp[self.index + ct])

	def handle_number(self):
		start_index = self.index - 1
		start_offset = self.offset - 1

		while not self.is_at_end() and self.peek().isdigit():
			self.advance()

		self.add_token(TokenType.NUMBER, self.inp[start_index:self.index], offset = start_offset)
		return

	def handle_string(self):
		start_index = self.index - 1
		start_offset = self.offset - 1
		
		# while (not self.is_at_end()) and (self.peek().isalpha() or self.peek() in {'_', ' ', '\t', '\''}):
		# 	self.advance()
		while not self.is_at_end() and is_string_char(self.peek()):
			self.advance()

		self.add_token(TokenType.STRING, self.inp[start_index:self.index], offset = start_offset)
		return

	def tokenize(self):
		while not self.is_at_end():
			start = self.index

			char = self.advance()

			if char == '{':
				self.add_token(TokenType.OPEN_BRACE)
			elif char == '}':
				self.add_token(TokenType.CLOSE_BRACE)
			elif char == '|':
				self.add_token(TokenType.BAR)
			elif char == '.':
				self.add_token(TokenType.DOT)
			elif char == '\t':
				self.add_token(TokenType.TAB)
			elif char == '%':
				self.add_token(TokenType.PERCENT)

			# Handle comments
			elif char == '/' and self.peek() == '/':
				self.advance()
				while self.peek() != '\n' and not self.is_at_end():
					self.advance()

			elif char == '\n' or (char == '\r' and self.peek() == '\n'):
				self.add_token(TokenType.NEWLINE)
				if char == '\r' and self.peek() == '\n':
					self.advance()
				self.line += 1
				self.offset = 0
				while not self.is_at_end() and (self.peek() == '\n' or (self.peek() == '\r' and self.peek(1) == '\n')):
					if self.peek() == '\r' and self.peek(1) == '\n':
						self.advance()
					self.advance()
					self.line += 1
					self.offset = 0

			elif char.isdigit():
				self.handle_number()

			elif is_string_char(char):
				self.handle_string()

			else:
				raise GeneratorSyntaxError(f'Unknown character at line {self.line} position {self.offset}')

		self.add_token(TokenType.EOF, offset = self.offset)

		return(self.tokens)

	def __iter__(self):
		return(self)

	def __next__(self):
		pass
