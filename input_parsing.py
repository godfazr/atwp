def who_you_know():
# this function inputs list of names
    persons_list = []
    persons = input("Enter the list of names: ")
    l = len(persons)
    s = ""
    for i in range(0, l):
#        print(i)
        if persons[i] != " ":
            s = s + persons[i]
 #       elif persons[i] == " " or i == (l):
        else:
            persons_list.append(s)
            s = ""
    persons_list.append(s)
    return persons_list
    

def ask_user():
    known_persons = who_you_know()
    person = input("Enter person's name: ") 
    if person in known_persons:
        print("You know {}!".format(person))
    else:
        print("Who da fuck is that?")
# print("test")
ask_user()