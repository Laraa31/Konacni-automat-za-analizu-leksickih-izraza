from ganit import Parser

parameters = {}
for letter in "abcdefghijklmnopqrstuvwxyz":
    x = input(f"Unesite vrijednost za parametar {letter} (Za izalaz unesite EXIT): ")
    if x == "EXIT":
        break
    parameters[letter] = int(x)

parser = Parser()
izraz = input("Unesite izraz: ")
izraz_postfix = parser.convert(izraz, parameters)
print(f"RPN: {izraz_postfix}")
print(f"Rezultat: {parser.evaluate(izraz, parameters)}")
