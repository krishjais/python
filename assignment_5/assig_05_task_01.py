dict={"krish":80 ,"john":78 , "rohit":99}

a = input("enter the name to know the marks:")
x = dict.get(a)
if a in dict:
    print(f"{a}'s marks: {dict.get(a)}")
else:
    print("student not found")