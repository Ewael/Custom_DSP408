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
[134] = 0x01 si inverse sinon 0x00
[138] = link on 4 bits
    0001 => InA alone
    0101 => InA & InC linked
    1000 => InD alone
    0000 => already linked to another In

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
[98] = 0x01 si inverse sinon 0x00
[102] = link on 8 bits
    00000001 => Out1 alone
    01000101 => Out1 & Out3 & Out7 linked
    00000000 => already linked to another Out

après les channel Out

[0x58e] = mute sur 4 bits, 0 is muted and 1 is not
    0001 = InA unmuted
    0010 = InB unmuted
    1010 = InB & InD unmuted
[0x590] = mute sur 8 bits
    11110101 = InB & InD unmuted
    00001000 = InD muted
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

    a = 0
    b = 2
    for i in range(IN_SIZE):
        if ins[a][i] != ins[b][i]:
            print(f"{i=}, {ins[a][i]=}, {ins[b][i]=}")

    a = 1
    b = 2
    for i in range(OUT_SIZE):
        if outs[a][i] != outs[b][i]:
            print(f"{i=}, {outs[a][i]=}, {outs[b][i]=}")
