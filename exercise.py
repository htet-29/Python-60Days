file = open('members.txt', 'r')
members = file.readlines()
file.close()

name = input("Enter a new member: ") + '\n'

file = open('members.txt', 'w')
members.append(name)
file.writelines(members)
file.close()




