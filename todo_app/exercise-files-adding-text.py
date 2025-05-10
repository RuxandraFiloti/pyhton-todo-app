filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename in filenames:
    file = open(f"files/{filename}", 'w')
    # file = open(f"../files/{filename}", 'w') -> daca acest fisier se afla in alt folder
    file.write("Hello")
    file.close()