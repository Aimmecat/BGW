import numpy as np
import Tool

def AddProtocol(party_list, gate, E):
    for party in party_list:
        party.stored_secret[gate[3]] = (party.stored_secret[gate[0]] + party.stored_secret[gate[1]]) % E

def MulProtocol(party_list, gate, E, A):
    if str.isdigit(gate[0]):
        for party in party_list:
            party.stored_secret[gate[3]] = (int(gate[0]) * party.stored_secret[gate[1]]) % E
    elif str.isdigit(gate[1]):
        for party in party_list:
            party.stored_secret[gate[3]] = (int(gate[1]) * party.stored_secret[gate[0]]) % E
    else:
        S = []
        for party in party_list:
            S.append((party.stored_secret[gate[0]] * party.stored_secret[gate[1]]))
        R = Tool.Reduction(S, A)
        R = [r % E for r in R]
        for idx, party in enumerate(party_list):
            party.stored_secret[gate[3]] = R[idx] % E
