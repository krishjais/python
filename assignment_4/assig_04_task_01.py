try:
    with open("sample.txt") as f:

        print("reading the file content:")
        line1 = f.readline()
        print(f"line 1:{line1}")
        line2 = f.readline()
        print(f"line 2:{line2}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")