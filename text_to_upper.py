print('Tento program vypise veskery obsah zadaneho souboru velkymi pismeny.')
name = input('Zadej jmeno souboru ke zpracovani:')

try:
    with open(name) as f:
        obsah = f.read()
except FileNotFoundError:
    print('Chyba')
print(obsah.upper())