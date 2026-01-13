# Morse code dictionary
morse = {
    '._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E',
    '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J',
    '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O',
    '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T',
    '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X', '_.__': 'Y',
    '__..': 'Z'
}

s = input("Enter encrypted message: ").strip()

results = []

def decode(index, current):
    if index == len(s):
        results.append(current)
        return

    for length in range(1, 5):
        if index + length <= len(s):
            part = s[index:index+length]
            if part in morse:
                decode(index + length, current + morse[part])

decode(0, "")

results.sort()
for word in results:
    print(word)
