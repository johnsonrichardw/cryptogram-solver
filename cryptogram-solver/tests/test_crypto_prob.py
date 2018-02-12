import pytest
from cryptogram_problem import cryptogram_problem as cp
from cryptogram_solution import cryptogram_solution as cs

def test_init_class():
    assert cp() != None

def test_decipher_problem():
    solution = cs()
    expected_vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rot13 = [expected_vals[(i+13)%26] for i in range(len(expected_vals))]
    for i in range(len(expected_vals)):
        solution.set_deciphered_value(expected_vals[i],rot13[i])
    prob = cp()
    prob.set_ciphertext('EVPUNEQ')
    cleartext = prob.apply_solution(solution)
    assert cleartext == 'RICHARD'

def test_solution_score():
    solution = cs()
    expected_vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rot13 = [expected_vals[(i+13)%26] for i in range(len(expected_vals))]
    for i in range(len(expected_vals)):
        solution.set_deciphered_value(expected_vals[i],rot13[i])
    prob = cp()
    prob.set_ciphertext('EVPUNEQ AND EVPUNEQ')
    cleartext = prob.apply_solution(solution)
    assert cleartext == 'RICHARD NAQ RICHARD'
    assert prob.score_solution(cleartext,['JOLLIES','SPEED','RICHARD','NAME']) == 14
    assert prob.score_solution(cleartext,['RIC','HARD','A','TRUNKES']) == 0

