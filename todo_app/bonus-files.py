contents = ["All carrots are to be sliced longitudinally.", 
            "The carrots are reportedly sliced.", 
            "The slicing process was well presented."]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    # file = open(f"../files/{filename}", 'w') -> daca acest fisier se afla in alt folder
    file.write(content)