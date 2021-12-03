import sys
with open(sys.argv[1], encoding="utf-8"):
    line = file.read().rstrip()
    storage ={}
for word in line:
    person, uni= word.split(":")
    storage[person]= str(uni)
for student in sys.argv[2].split(","):
    try:
        print(("Name:{}, University:{}".format(student,storage[student])))
    except:
        print("No record of {} was found!".format(student))
