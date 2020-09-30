names = ["Husna", "Theodore", "Emmanuel", "Solomon", "Amarachi"]

reversedName = []

counter = len(names) - 1
while(counter >= 0):
    reversedName.append(names[counter])
    counter = counter - 1

for name in reversedName:
    print(name)

