import onetimepad

msg1: str = input("1st message: ")
msg2: str = input("2nd message: ")
dec1: str = ""
dec2: str = ""
key: str = ""


def drag(m: str, n: str, d: str, e: str, g: str, k: str) -> list:
    a: int = len(d)
    b: int = a + 1
    d += g + "."
    x: str = m[a] + m[b]
    y: str = onetimepad.decrypt(x, g)
    k += y + "."
    e += (onetimepad.decrypt(n[a] + n[b], y) if len(n) > a else " ") + "."
    return [d, e, k]


while len(dec1) < len(msg1) or len(dec1) < len(msg2):
    guessing: int = int(input("guessing: "))
    guess: str = input("guess: ")
    if guessing == 1:
        res: list = drag(msg1, msg2, dec1, dec2, guess, key)
    else:
        res: list = drag(msg2, msg1, dec2, dec1, guess, key)
    dec1 = res[(guessing % 2) ^ 1]
    dec2 = res[guessing % 2]
    key = res[2]
    print(dec1)
    print(dec2)

print()
print(msg1)
print(msg2)
print()
print(key)
