import Tool
import Protocol

class Member:
    def __init__(self):
        self.id = 0
        self.n = 0
        self.t = 0
        self.circuit = []

    def set_n_t(self, n, t):
        self.n = n
        self.t = t

    def setCircuit(self, circuit):
        self.circuit = circuit

    def ShareSecret(self, party_id_list, secret, E):
        newPoly = Tool.CreatePoly(self.t, E, secret)
        SS = [Tool.CalcPoly(newPoly, number) for number in party_id_list]
        return SS

class Publisher(Member):
    def __init__(self, secret: list):
        super().__init__()
        self.secret = secret

class Party(Member):
    def __init__(self, _id):
        super().__init__()
        self.id = _id
        self.stored_secret = {}

    def Step(self):
        pass


class NetWork:
    def __init__(self, publisher, party_list, n, t, E):
        self.publisher = publisher
        self.party_list = party_list
        self.n = n
        self.t = t
        self.E = E
        self.publisher.set_n_t(n, t)
        self.party_id_list = []
        for party in self.party_list:
            party.setCircuit(publisher.circuit)
            party.set_n_t(n, t)
            self.party_id_list.append(party.id)
        B = [[each_id ** i for each_id in self.party_id_list] for i in range(n)]
        P = [[1 if i == j and i <= t else 0 for j in range(n)] for i in range(n)]
        self.matrix_A = Tool.CalcA(B, P)

    def Solve(self):
        output = ''
        ret = []
        for idx, secret in enumerate(self.publisher.secret):
            SS = self.publisher.ShareSecret(self.party_id_list, secret, self.E)
            for jdx, party in enumerate(self.party_list):
                party.stored_secret['x'+str(idx+1)] = SS[jdx]
        for idx, gate in enumerate(self.publisher.circuit):
            if gate[2] == '+':
                Protocol.AddProtocol(self.party_list, gate, self.E)
            elif gate[2] == '*':
                Protocol.MulProtocol(self.party_list, gate, self.E, self.matrix_A)
            else:
                pass
            if idx == len(self.publisher.circuit) - 1:
                output = gate[3]
        for party in self.party_list:
            ret.append(party.stored_secret[output])
        return ret
