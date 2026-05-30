import math

def gainToHex(gain: int) -> str:
    """Return hex code with given decimal gain in dB

    Args:
        gain (int): gain in dB

    Returns:
        str: hex value without the "0x"
    """

    if gain < -20:
        return "0000"
    elif gain > 12:
        gain = 12

    BASE_GAIN = 24  # 0dB -> 0x22
    gainBase = int(gain * 10) + BASE_GAIN
    gainHex = f"{hex(gainBase & 0xff)[2:]:02s}"
    gainHexSigned = gainHex + "01" if gainBase >= 0 else gainHex + "00"

    return gainHexSigned

print(gainToHex(0))
print(f"{gainToHex(0.0)=}")
print(f"{gainToHex(0.1)=}")
print(f"{gainToHex(0.2)=}")
print(f"{gainToHex(10)=}")
print(f"{gainToHex(12)=}")
print(f"{gainToHex(-0.1)=}")
print(f"{gainToHex(-0.2)=}")
print(f"{gainToHex(-20)=}")
print(f"{gainToHex(-60)=}")