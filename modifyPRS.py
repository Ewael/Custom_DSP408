import os

"""
[0x00:0x1e] = ***DSP408V010***Default Preset

padding channel In = 0x1e bytes (avant InA)
taille d'un channel In = 140 bytes

[0x1e:0x26] = name of InA
[0xa2] = gain en signed hex
[0xa3] = 0x01 si gain > -2.4dB sinon 0x00
"""

basePRS = "./test.prs"
newPRS = "./newPRS.prs"

N_IN = 4
N_OUT = 8

IN_PAD = 0x1E
IN_SIZE = 140
OUT_PAD = 0x24E
OUT_SIZE = 104

with open(basePRS, "rb") as fin:
    baseData = fin.read()
    newData = list(baseData)

    ins = [
        newData[IN_PAD + IN_SIZE * i : IN_PAD + IN_SIZE * (i + 1)] for i in range(N_IN)
    ]
    outs = [
        newData[OUT_PAD + OUT_SIZE * i : OUT_PAD + OUT_SIZE * (i + 1)]
        for i in range(N_OUT)
    ]

    for i in range(IN_SIZE):
        if ins[0][i] != ins[1][i]:
            print(f"{i=}, {ins[0][i]=}, {ins[1][i]=}")

    for i in range(OUT_SIZE):
        if outs[0][i] != outs[1][i]:
            print(f"{i=}, {outs[0][i]=}, {outs[1][i]=}")
