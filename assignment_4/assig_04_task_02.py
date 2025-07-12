text1 = input("enter  text to write in the file: ")

with open("output.txt", "w") as f:
    f.write(text1)
print("data successfully appended")

text2 = input(f"enter additoinal text to append:")

with open("output.txt", "a") as f:
    f.write(f"\n{text2}")
print("data successfully appended")