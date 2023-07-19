"""
Functions for translating from english to french and french to english
"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Convert english to french, return the french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)

    return french_text


def frenchToEnglish(french_text):
    """Convert french to english, return the english"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
