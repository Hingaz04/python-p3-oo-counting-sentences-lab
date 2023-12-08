#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):

        cleaned_value = " ".join(self.value.split())

        abbreviations = ["Mr.", "Mrs.", "Ms.", "Dr.", "etc.", "e.g.", "i.e."]
        for abbreviation in abbreviations:
            cleaned_value = cleaned_value.replace(
                abbreviation, f"{abbreviation[:-1]} ")

        sentences = [sentence.strip()
                     for sentence in cleaned_value.split(".") if sentence.strip()]
        return len(sentences)
