try:
        width = float(input("Enter retangle width: "))
        length = float(input("Enter retangle length: "))

        if width == length:
             exit("That looks like a square.")
        area = width * length
        print(area)
except ValueError:
        print("Please enter a number.") 