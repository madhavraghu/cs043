from database import Simpledb

programRunning = True

print('Enter the name of the database file(without file extension),')
print("or type 'q' to quit the program.")
filename = input()
if filename == 'q':
    programRunning = False
else:
    db = Simpledb(filename + '.txt')

while programRunning:
    print('''Type 'a', 'f', 'd', or 'u' to add, find,
delete, or update database entries.
Type 'q' to quit the program.''')
    command = input()
    if command == 'a':
        print('Enter a name.')
        name = input()
        print('Enter a phone number.')
        number = input()
        print(db.add(name, number))
    elif command == 'f':
        print('Enter a name to search for.')
        name = input()
        print(db.find(name))
    elif command == 'd':
        print('Enter a name to delete.')
        name = input()
        print(db.delete(name))
    elif command == 'u':
        print('Enter a name to update.')
        name = input()
        print('Enter the new number.')
        number = input()
        print(db.update(name, number))
    elif command == 'q':
        programRunning = False
