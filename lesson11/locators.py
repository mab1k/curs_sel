
data = ("Aleksei", "QA")

def print_person_data(first_name, last_name):
    first_name = first_name.strip()
    last_name = last_name.strip()
    print(first_name + " " + last_name)

print_person_data(*data)
print(*data)