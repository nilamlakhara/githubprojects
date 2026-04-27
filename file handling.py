f = open("data.txt", "w")
data = input("enter data to write in file \n")
f.write(data)
f.close()

try:
    with open("data.txt", "w") as f:
        f.write("hello python \n")

except FileNotFoundError:
    print("file not found")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)