import pytest
from cryptogram_solution import cryptogram_solution
import string

def test_init_class():
    assert cryptogram_solution() != None

def test_get_map():
    cs = cryptogram_solution()
    cmap = cs.gen_initial_solution()
    keys = sorted(cmap.keys())
    assert len(keys) == 26
    expected_vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    assert keys == expected_vals
    for k,v in cmap.items():
        assert v in expected_vals
        expected_vals.remove(v)
    assert len(expected_vals) == 0

def test_map_randomness():
    expected_vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    cs = cryptogram_solution()
    cmap = cs.gen_initial_solution()
    val_list = [cmap[k] for k in sorted(cmap.keys())]
    assert len(val_list) == 26
    different = 0
    #Test that the randomized list is actually randomized. So as a simple
    #heuristic assume the list is randomized if at least 5 elements are
    #different between the two lists.
    for i in range(len(expected_vals)):
        if expected_vals[i] != val_list[i]:
            different += 1
    assert different >= 5

def test_swap():
    cs = cryptogram_solution()
    a_val = cs.get_deciphered_value('A')
    b_val = cs.get_deciphered_value('B')
    assert a_val != b_val
    cs.swap_values('A','B')
    assert a_val == cs.get_deciphered_value('B')
    assert b_val == cs.get_deciphered_value('A')

def test_random_chars():
    cs = cryptogram_solution()
    for i in range(100):
        a, b = cs.get_random_swap_chars()
        assert a != b

def test_mutate():
    cs = cryptogram_solution()
    val_list = [cs.solution[k] for k in sorted(cs.solution.keys())]
    cs.mutate()
    new_val_list = [cs.solution[k] for k in sorted(cs.solution.keys())]
    different = 0
    for i in range(26):
        if val_list[i] != new_val_list[i]:
            different += 1
    assert different == 2

def test_simple_decipher():
    expected_vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rot13 = [expected_vals[(i+13)%26] for i in range(len(expected_vals))]
    cs = cryptogram_solution()
    for i in range(len(expected_vals)):
        cs.set_deciphered_value(expected_vals[i],rot13[i])
    assert cs.decipher('EVPUNEQ') == 'RICHARD'

def test_non_letter_decipher():
    garbage_string = "A  -G343,.Y!#[]"
    cleartext = cryptogram_solution().decipher(garbage_string)
    assert len(garbage_string) == len(cleartext)
    for i in range(len(garbage_string)):
        if garbage_string[i] not in string.ascii_uppercase:
            assert garbage_string[i] == cleartext[i]

def test_case():
    expected_vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rot13 = [expected_vals[(i+13)%26] for i in range(len(expected_vals))]
    cs = cryptogram_solution()
    for i in range(len(expected_vals)):
        cs.set_deciphered_value(expected_vals[i],rot13[i])
    assert cs.decipher('evpuneq') == 'RICHARD'

def test_copy():
    cs_a = cryptogram_solution()
    cs_b = cs_a.copy()
    for c in string.ascii_uppercase:
        assert cs_a.get_deciphered_value(c) == cs_b.get_deciphered_value(c)

def test_deep_copy():
    cs_a = cryptogram_solution()
    cs_b = cs_a.copy()
    cs_b.mutate()
    different = 0
    for c in string.ascii_uppercase:
        if cs_a.get_deciphered_value(c) != cs_b.get_deciphered_value(c):
            different += 1
    assert different == 2
