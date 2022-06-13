"""
    Give:
        f(x1,x2,x3) = x1▪x2 + 2▪x3
    Create circuit as follow:
        x1 ------
                |
                ×  -----y1
                |        |
        x2 ------        |
                         |
                         + ------ y3
        2  ------        |
                |        |
                ×  -----y2
                |
        x3 ------
"""


def CreateCircuit(s: str):
    circuit = [['x1', 'x2', '*', 'y1'], ['2', 'x3', '*', 'y2'], ['y1', 'y2', '+', 'y3']]
    return circuit
