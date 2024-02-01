

import unittest

from makeshift.interpreter.lexer import Lexer
from makeshift.interpreter.parser import Parser
from makeshift.interpreter.token import Token, TokenType


class TestParserMethods(unittest.TestCase):
	def setUp(self):
		self.lexer = Lexer('abc\n\t123')
		self.tokens = self.lexer.lexv2()
		self.parser = Parser(self.tokens)

	def test_init(self):
		self.assertEqual(self.parser.tokens, self.tokens)
		self.assertEqual(self.parser.pos, 0)

	def test_consume(self):
		expected_tokens = [
			Token(TokenType.STRING, 'abc', 1, 0),
			Token(TokenType.NEWLINE, '\n', 1, 3),
			Token(TokenType.TAB, '\t', 2, 0),
			Token(TokenType.NUMBER, '123', 2, 1)
		]
		# "len(tokens) -1" for EOF token, which is not emitted by parser"
		self.assertEqual(len(self.parser.tokens) - 1, len(expected_tokens))

		for i in range(0, len(self.parser.tokens) - 1):
			with self.subTest(i=i):
				self.assertEqual(self.parser.consume(), expected_tokens[i])

	def test_peek(self):
		expected_tokens = [
			Token(TokenType.STRING, 'abc', 1, 0),
			Token(TokenType.NEWLINE, '\n', 1, 3),
			Token(TokenType.TAB, '\t', 2, 0),
			Token(TokenType.NUMBER, '123', 2, 1)
		]
		# "len(tokens) -1" for EOF token, which is not emitted by parser"
		self.assertEqual(len(self.parser.tokens) - 1, len(expected_tokens))

		for i in range(0, len(self.parser.tokens) - 1):
			with self.subTest(i=i):
				self.assertEqual(self.parser.peek(i), expected_tokens[i])

	def test_check(self):
		expected_tokens = [
			Token(TokenType.STRING, 'abc', 1, 0),
			Token(TokenType.NEWLINE, '\n', 1, 3),
			Token(TokenType.TAB, '\t', 2, 0),
			Token(TokenType.NUMBER, '123', 2, 1)
		]
		# "len(tokens) -1" for EOF token, which is not emitted by parser"
		self.assertEqual(len(self.parser.tokens) - 1, len(expected_tokens))

		for i in range(0, len(self.parser.tokens) - 1):
			with self.subTest(i=i):
				self.assertTrue(self.parser.check(expected_tokens[i].type))
				self.parser.consume()

	# def test_match

	# def test_expect

	def test_is_at_end(self):
		self.assertFalse(self.parser.is_at_end())
		self.parser.consume()
		self.assertFalse(self.parser.is_at_end())
		self.parser.consume()
		self.assertFalse(self.parser.is_at_end())
		self.parser.consume()
		self.assertFalse(self.parser.is_at_end())
		self.parser.consume()
		self.assertTrue(self.parser.is_at_end())
		self.parser.consume()
		self.assertTrue(self.parser.is_at_end())

	# def test_previous

	# def test_name

	# def test_method_name

	# def test_string_literal

	# def test_reference

	# def test_resolvable

	# def test_expression

	# def test_option

	# def test_definition

	# def test_generator
