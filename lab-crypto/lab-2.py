f = open('animals.txt','r')
f2 = open('passwords.txt','w')

animal_list = []

for line in f.readlines():
    animal_list.append(line.replace("\n",""))

# only 7 or more letters, then 2 random letters
for animal in animal_list:
    if len(animal) >= 7:
        for j in range(10):
            for k in range(10):
                text = str(animal) + str(j) + str(k) + "\n"
                f2.write(text)

for animal1 in animal_list:
    for animal2 in animal_list:
        text = str(animal1) + str(animal2) + "\n"
        f2.write(text)

for animal1 in animal_list:
    for animal2 in animal_list:
        text = str(animal1)[0:3] + str(animal2)[0:3] + "\n"
        f2.write(text)
