"""
Unit test for translator.py
"""

import unittest
from translator import *


class TestTranslations(unittest.TestCase):
    #Poems for testing
    english_poem = "In the forests of the night"
    french_poem = "Dans les forêts de la nuit"

    #Methods are named for the langugage they are translating from
    #Greetings Tests for english and french
    def test_en_greeting(self):
        self.assertEqual(englishToFrench("hello"),"bonjour")

    def test_fr_greeting(self):
        self.assertEqual(frenchToEnglish("bonjour"),"hello")

    #Poem Tests for english and french
    def test_en_poem(self):
        self.assertEqual(englishToFrench(self.english_poem),self.french_poem)

    def test_fr_poem(self):
        self.assertEqual(frenchToEnglish(self.french_poem),self.english_poem)

    #Failed Asserts
    def test_en_dog(self):
        self.assertNotEqual(englishToFrench("dog"), "chat")

    def test_fr_dog(self):
        self.assertNotEqual(frenchToEnglish("chien"), "cat")


if __name__ == '__main__':
    unittest.main()
