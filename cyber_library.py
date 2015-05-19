import re
from random import random
from topia.termextract import tag

def prefix(word):
	"""Prefixes the word while preserving its case."""
	if word[0].islower():
		return "cyber" + word
	elif len(word) == 1 or word[0].isupper() and word[1].islower():
		return "Cyber" + word[0].lower() + word[1:]
	elif word.isupper():
		return "CYBER" + word
	else:
		return word

def is_replaceable(word):
	"""Determines if a word is replaceable.
	This will only replace 3/4 of replaceable words"""
	if not word:
		return False
	return word[0][1] in ['NN', 'NNS', 'NNP', 'NNPS'] and random() < .75

def replace_words(text):
	"""Parses each word, and replaces it if possible."""
	replaced = ""
	tagger = tag.Tagger()
	tagger.initialize()
	split = re.split('(\W+)', text)
	for word in split:
		if is_replaceable(tagger(word)):
			replaced += prefix(word)
		else:
			replaced += word
	return replaced

def generate_novel():
	"""Reads a novel, replaces the words, and writes a new novel."""
	infile = open('the_art_of_war.txt', 'r')
	text = infile.read()
	replaced = replace_words(text)
	outfile = open('the_cyberart_of_cyberwar.txt', 'w')
	outfile.write(replaced)

if __name__ == '__main__':
	generate_novel()
