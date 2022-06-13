import NetWork
import Circuit
import random
import Tool

n, t = 5, 1
E = 97

f = 'x1▪x2 + 2▪x3'
secret = [23, 76, 85]


def main():
    circuit = Circuit.CreateCircuit(f)
    newPublisher = NetWork.Publisher(secret)
    newPublisher.setCircuit(circuit)
    random_sel_idx = random.sample(range(E), n)
    newPartyList = [NetWork.Party(idx) for idx in random_sel_idx]
    newNetWork = NetWork.NetWork(newPublisher, newPartyList, n, t, E)
    ret = newNetWork.Solve()
    sel = random.sample(range(n), t+1)
    x = []
    y = []
    for each_sel in sel:
        x.append(newPartyList[each_sel].id)
        y.append(ret[each_sel])
    reconstruction = Tool.CalcLagrange(x, y, E, t+1)
    print(reconstruction)
    print((secret[0] * secret[1] + 2 * secret[2]) % E)


if __name__ == "__main__":
    main()
