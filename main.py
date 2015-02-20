import random
import re
import sys
import flask


def get_random_line(rsv):
    file_h = open(rsv)
    limit = file_h.readline()
    limit = limit.replace('\n', '' )
    limit = int(limit)
    line = random.randint(0, limit - 1)
    
    for x in range(line):
        file_h.readline()
    phrase = file_h.readline()
    phrase = phrase.replace('\n', '')
    
    return(phrase)
	

def main():
	flask.flash("Base: " + get_random_line('Base.txt'))
	flask.flash("Theme: " + get_random_line('Theme.txt'))