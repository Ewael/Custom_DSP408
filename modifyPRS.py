import os

# Step 1 - extract and save In and Out presets in a bank
# Step 2 - rebuild an interface to modify them easily
# Step 3 - try network app from Yoann's reddit link

"""
[0x00:0x1e] = ***DSP408V010***Default Preset

padding channel In = 0x1e bytes (avant InA)
taille d'un channel In = 140 bytes

[0:8] = name of InA
[132] = gain en signed hex
[133] = 0x01 si gain > -2.4dB sinon 0x00

padding channel Out = 0x24e bytes (avant Out1)
taille d'un channel Out = 104 bytes

[0:8] = name of Out1
[8] = matrix on 4 bits
    0001 => InA
    0010 => InB
    0101 => InA & InC
    1010 => InB & InD
[96] = gain en signed hex
[97] = 0x01 si gain > -2.4dB sinon 0x00
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

    # for i in range(IN_SIZE):
    #     if ins[0][i] != ins[1][i]:
    #         print(f"{i=}, {ins[0][i]=}, {ins[1][i]=}")

    a = 0
    b = 1
    for i in range(OUT_SIZE):
        if outs[a][i] != outs[b][i]:
            print(f"{i=}, {outs[a][i]=}, {outs[b][i]=}")
