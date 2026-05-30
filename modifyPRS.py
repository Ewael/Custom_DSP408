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

IN_PAD = 0x1E
IN_SIZE = 140


with open(basePRS, "rb") as fin:
    baseData = fin.read()
    newData = list(baseData)

    inA = newData[IN_PAD + IN_SIZE * 0 : IN_PAD + IN_SIZE * 1]
    inB = newData[IN_PAD + IN_SIZE * 1 : IN_PAD + IN_SIZE * 2]
    inC = newData[IN_PAD + IN_SIZE * 2 : IN_PAD + IN_SIZE * 3]
    inD = newData[IN_PAD + IN_SIZE * 3 : IN_PAD + IN_SIZE * 4]

    for i in range(IN_SIZE):
        if inA[i] != inB[i]:
            print(f"{i=}, {inA[i]=}, {inB[i]=}")
