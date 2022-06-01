from ganit import Parser

parameters = {}
for letter in "abcdefghijklmnopqrstuvwxyz":
    x = input(f"Unesite vrijednost za parametar {letter}: ")
    if x == "EXIT":
        break
    parameters[letter] = int(x)

print("RPN: " + Parser().convert(input("Unesite izraz: "), parameters))