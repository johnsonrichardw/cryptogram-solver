import pytest
from cryptogram_wordlist import cryptogram_wordlist as wl

def test_init_class():
    assert wl() != None

def test_load_wordlist():
    wordlist = wl()
    wordlist.load_list('test-list.txt')
    assert len(wordlist.words.keys()) == 6

def test_upper_case():
    wordlist = wl()
    wordlist.load_list('test-list.txt')
    assert wordlist.is_word('RICHARD')
    assert wordlist.is_word('SPARK')
    assert wordlist.is_word('FOOD')
