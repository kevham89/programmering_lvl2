from mina_funktioner import namn, pnamn, pnummer, save_file, read_file
for x in range(5):
    input_namn = namn()
    pnamn(input_namn)
    input_nummer = pnummer()
    save_file(input_namn, input_nummer)
read_file()