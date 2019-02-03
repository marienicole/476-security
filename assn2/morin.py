import base64
from pprint import pprint
with open("memorydump.dmp", "rb") as f:
    dump = f.read()
    dump = "".join(chr(x) for x in bytearray(dump))

dump = dump.split("%")
cards = []
for entry in dump:
    if len(entry) > 0 and entry[0] == 'B':  # alphabet only
        entry = entry[1:]
        current = entry.split("^") # split on field separators
        print(current)
        print()
        if len(current[0]) > 19 or len(current[1]) > 26:
            continue
        card_no = current[0]
        name = current[1].replace("/", " ")
        year = current[2][:2]
        month = current[2][2:4]
        cvv = current[2] [4:7]
        cc_info = "\tCardholder's Name: %s\n\tCard Number: %s\n\tExpiration Date: %s/%s\n\tCVV Number: %s" % (
            name, card_no, month, year, cvv)
        cards.append(cc_info)
i = 1
for card in cards:
    print("<Information of record #%i>" % i)
    print(card)
    i += 1
