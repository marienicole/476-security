'''
Marie Morin
Security Assignment #2
To use: run program in the same directory as the memorydump.dmp file.

This is written in Python (rather than Java), as per approval of Dr. Binhai Zhu.
'''
with open("memorydump.dmp", "rb") as f:
    dump = f.read()
    dump = "".join(chr(x) for x in bytearray(dump))

dump = dump.split("%")
cards = []
for entry in dump:
    if len(entry) > 0 and entry[0] == 'B':  # alphabet only
        entry = entry[1:]
        current = entry.split("^") # split on field separators
        if len(current[0]) > 19 or len(current[1]) > 26:
            continue
        card_no_temp = current[0]
        card_no = ""
        for i in range(len(card_no_temp)):
            if i % 4 == 0:
                card_no += ' '
            card_no += card_no_temp[i]

        name = current[1].replace("/", ", ")
        year = current[2][:2]
        month = current[2][2:4]
        cvv = current[2] [4:7]
        cc_info = "\tCardholder's Name: %s\n\tCard Number: %s\n\tExpiration Date: %s/20%s\n\tCVV Number: %s" % (
            name, card_no, month, year, cvv)
        cards.append(cc_info)
i = 1
with open("morin.output", "w+") as f:
    f.write("There are %s track records in the memory data.\n" % len(cards))
    for card in cards:
        f.write("< Information of record #%i >\n" % i)
        f.write(card)
        f.write("\n")
        i += 1
