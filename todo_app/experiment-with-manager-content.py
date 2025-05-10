with open ("files/doc.txt") as file: # argumentul "r" este by default, doar "w" este scris
   content = file.read()
print(content) #nu da eroare chiar daca este in afara blocului de executie deoarece avem stocare date in variabila, iar ea poate fi folosita oriunde in cod

# file.read() -> eroare deoarece este in afara blocului de executie