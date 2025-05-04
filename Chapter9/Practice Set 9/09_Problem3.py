# Problem 3
# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.


# Function Definition
def generate_Table(n):
    result = ""
    for i in range(1, 11):
        result += f"{n} * {i} = {n * i}\n"

    with open(f"./Practice Set 9/tables/Table_{n}.txt", "w") as f:
        f.write(result)


for i in range(2, 21):
    generate_Table(i)
