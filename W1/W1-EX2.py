str = "8200123;Ana Maria;931221012;12/05/2000"

arr = str.split(";")

print(arr)
print(len(arr))
arr.append("SOL")
print(arr)

new_str = ", ".join(arr)
print(new_str)
