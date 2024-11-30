

import unittest

from makeshift.interpreter.lexer import Lexer, is_string_char
from makeshift.interpreter.token import Token, TokenType

class TestStringChar(unittest.TestCase):
	def test_valid_string_char(self):
		valid_chars = " !\'\"#$&'`()*,+-_/:;<>?@[]\\^_~ abcdABCD"
		for char in valid_chars:
			with self.subTest(i=char):
				self.assertTrue(is_string_char(char))

	def test_invalid_string_char(self):
		invalid_chars = "\t\n{}|.%1234"
		for char in invalid_chars:
			with self.subTest(i=char):
				self.assertFalse(is_string_char(char))

class TestLexerMethods(unittest.TestCase):
	#passing empty file
	#normal looking file
	def setUp(self):
		self.lexer = Lexer('abc\n\t123')

	def test_advance(self):
		# x = proclang.lexer.Lexer('abc\n\t123')
		x = self.lexer
		self.assertEqual(x.index, 0)
		self.assertEqual(x.offset, 0)
		self.assertEqual(x.advance(), 'a')
		self.assertEqual(x.index, 1)
		self.assertEqual(x.offset, 1)
		self.assertEqual(x.advance(), 'b')
		self.assertEqual(x.index, 2)
		self.assertEqual(x.offset, 2)
		self.assertEqual(x.advance(), 'c')
		self.assertEqual(x.index, 3)
		self.assertEqual(x.offset, 3)
		self.assertEqual(x.advance(), '\n')
		self.assertEqual(x.index, 4)
		self.assertEqual(x.offset, 4)
		self.assertEqual(x.advance(), '\t')
		self.assertEqual(x.index, 5)
		self.assertEqual(x.offset, 5)
		self.assertEqual(x.advance(), '1')
		self.assertEqual(x.index, 6)
		self.assertEqual(x.offset, 6)
		self.assertEqual(x.advance(), '2')
		self.assertEqual(x.advance(), '3')

	def test_is_at_end(self):
		x = self.lexer
		x.inp = 'a'
		self.assertFalse(x.is_at_end())
		x.advance()
		self.assertTrue(x.is_at_end())

	def test_match(self):
		x = self.lexer
		self.assertTrue(x.match('a'))
		self.assertTrue(x.match('b'))
		self.assertFalse(x.match('\n'))
		self.assertTrue(x.match('c'))
		self.assertTrue(x.match('\n'))
		self.assertTrue(x.match('\t'))
		self.assertTrue(x.match('1'))
		self.assertTrue(x.match('2'))
		self.assertTrue(x.match('3'))
		self.assertFalse(x.match('4'))

	def test_peek(self):
		x = self.lexer
		x.inp = 'abc\n\t1'
		self.assertEqual(x.peek(), 'a')
		x.advance()
		self.assertEqual(x.peek(), 'b')
		x.advance()
		self.assertEqual(x.peek(), 'c')
		x.advance()
		self.assertEqual(x.peek(), '\n')
		x.advance()
		self.assertEqual(x.peek(), '\t')
		x.advance()
		self.assertEqual(x.peek(), '1')
		x.advance()
		self.assertFalse(x.peek())

	def test_add_token(self):
		#TO DO: should check that string requires literal
		x = Lexer('')
		x.add_token(TokenType.STRING, 'abc', 1, 0)
		x.offset = 3
		
		# read the newline, increments offset by 1
		x.offset+= 1
		x.add_token(TokenType.NEWLINE)
		x.offset = 0
		x.line += 1
		
		x.offset += 1
		x.add_token(TokenType.TAB)
		x.offset = 1

		expected_tokens = [
			Token(TokenType.STRING, 'abc', 1, 0),
			Token(TokenType.NEWLINE, '\n', line = 1, offset = 3),
			Token(TokenType.TAB, '\t', 2, 0)
		]

		self.assertEqual(len(x.tokens), len(expected_tokens))

		for i in range(0, len(x.tokens)):
			with self.subTest(i=i):
				self.assertEqual(x.tokens[i], expected_tokens[i])

	def test_handle_number(self):
		x = Lexer('999a123')
		x.advance()
		x.handle_number()
		self.assertEqual(x.tokens,
			[Token(TokenType.NUMBER, '999', 1, 0)])

	def test_handle_string(self):
		x = Lexer('abc123')
		x.advance()
		x.handle_string()
		self.assertEqual(x.tokens,
			[Token(TokenType.STRING, 'abc', 1, 0)])
		
		x = Lexer("abc_ \\ /?'\'\'__ &3")
		x.advance()
		x.handle_string()
		self.assertEqual(x.tokens,
			[Token(TokenType.STRING, "abc_ \\ /?'\'\'__ &", 1, 0)])


class TestLexer(unittest.TestCase):
	
	def test_empty(self):
		#An empty file just returns an EOF
		#[Token(EOF, None, line 1 pos 1)]
		result = Token(TokenType.EOF, None, 1, 0)
		x = Lexer('')
		self.assertEqual(x.tokenize(), [result])
		x = Lexer(' ')
		self.assertEqual(x.tokenize(), [result])
		x = Lexer('\t')
		self.assertEqual(x.tokenize(), [result])
		x = Lexer('\n')
		self.assertEqual(x.tokenize(), [result])

	def test_lexer(self):
		x = Lexer('{}|.\t ():\t	\n%//comment\na/sd\\nf1234')
		#x = Lexer('{}|.\t \t	\n%//\nasdf1234')
		x.tokenize()
		expected_tokens = [
			Token(TokenType.OPEN_BRACE, '{', 1, 0),
			Token(TokenType.CLOSE_BRACE, '}', 1, 1),
			Token(TokenType.BAR, '|', 1, 2),
			Token(TokenType.DOT, '.', 1, 3),
			Token(TokenType.TAB, '\t', 1, 4),
			Token(TokenType.STRING, ' ():', 1, 5),
			#Token(TokenType.OPEN_PARENTHESIS, '(', 1, 7),
			#Token(TokenType.CLOSE_PARENTHESIS, ')', 1, 8),
			#Token(TokenType.COLON, ':', 1, 9),
			#Token(TokenType.EQUALS, '=', 1, 10),
			# Token(TokenType.BACKSLASH, '\', 1, 10),
			Token(TokenType.TAB, '\t', 1, 9),
			Token(TokenType.TAB, '\t', 1, 10),
			Token(TokenType.NEWLINE, '\n', 1, 11),
			Token(TokenType.PERCENT, '%', 2, 0),
			Token(TokenType.NEWLINE, '\n', 2, 10),
			Token(TokenType.STRING, 'a/sd\\nf', 3, 0),
			Token(TokenType.NUMBER, '1234', 3, 7),
			Token(TokenType.EOF, None, 3, 11)
			]

		self.assertEqual(len(x.tokens), len(expected_tokens))

		for i in range(0, len(x.tokens)):
			with self.subTest(i=i):
				self.assertEqual(x.tokens[i], expected_tokens[i])

	def test_newlines(self):
		# Newline strings "\n" and "\r\n" should be functionally equal
		string_pairs = [
			('\n', '\r\n'),
			('asdf\n1234', 'asdf\r\n1234'),
		]
		for ct, pair in enumerate(string_pairs):
			with self.subTest(i=ct):
				lf = Lexer(pair[0]).tokenize()
				crlf = Lexer(pair[1]).tokenize()
				self.assertEqual(lf, crlf)
		# lf = Lexer('asdf\n1234').tokenize()
		# crlf = Lexer('asdf\r\n1234').tokenize()
		# self.assertEqual(lf, crlf)

		# lf = Lexer('\n').tokenize()
		# crlf = Lexer('\r\n').tokenize()
		# self.assertEqual(lf, crlf)

	# def test_comments(self):
	# 	comment_file = 'x'
	# 	non_comment_file = 'y'
	# 	# inline comments before name
	# 	# inline comments after name
	# 	# comment on line before name
	# 	# comment on line after name but before any options
	# 	# comment on line after name after first option
	# 	# comment on line after name before first option
	# 	# comment before tab before first option
	# 	# comment after tab before first option
	# 	# comments after options (should strip off extra spaces )
	# 	# randomly between (newline separated on each end) definitions
	# 	# 	tab indented or not

if __name__ == '__main__':
	unittest.main()