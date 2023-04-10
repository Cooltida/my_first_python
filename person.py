import sys

print("Hello!")
banned_names = ["Maria", "bob", "phontida"]
person = dict(
    name="anon",
    lastname="",
    second_lastname=""
)
if len(sys.argv) > 1:
    person["name"] = sys.argv[1]
if len(sys.argv) > 2:
    person["lastname"] = sys.argv[2]
if len(sys.argv) > 3:
    person["second_lastname"] = sys.argv[3]


# print(person)

for key, value in person.items():
    if value in banned_names:
        person[key] = "ERROR"
# print(person.values())
# person["second_lastname"] = "martin"
# print(person)


print(person["name"] + " " + person["lastname"] + " " + person["second_lastname"])

# print(sys.argv)

# if name in banned_names:
#     name = "ERROR"
# if lastname in banned_names:
#     lastname = "ERROR"
# if second_lastname in banned_names:
#     second_lastname = "ERROR"
# if len(sys.argv)>1:
#     name = sys.argv[1]
# if len(sys.argv)>2:
#     lastname = sys.argv[2]
# if len(sys.argv)>3:
#     second_lastname = sys.argv[3]
