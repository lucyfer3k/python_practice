#!/usr/bin/env python3
from acronyms import acronym
import unittest

class TestAcronym(unittest.TestCase):
    def test_basic(self):
        testcase = "World Health Organization"
        expected = "WHO"
        self.assertEqual(acronym(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = 1
        self.assertEqual(acronym(testcase), expected)

    def test_one_word(self):
        testcase = "World"
        expected = 1
        self.assertEqual(acronym(testcase), expected)

    def test_spaces(self):
        testcase = "       World     Health     Organization     "
        expected = "WHO"
        self.assertEqual(acronym(testcase), expected)

unittest.main()


