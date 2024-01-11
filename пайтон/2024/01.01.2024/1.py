database = []

def new_employee(full_name: str, birth_date, position, salary):
    if not full_name:
        return {"id": -1, "errorDesc": "Full Name not specified"}
    if not birth_date:
        return {"id": -1, "errorDesc": "Birth Date not specified"}
    if not position:
        return {"id": -1, "errorDesc": "Position not specified"}
    if salary <= 0:
        return {"id": -1, "errorDesc": "Salary not valid"}
    first_name, last_name = full_name.split(" ", 1)
    newcome = {
        "id": len(database),
        "firstName": first_name,
        "lastName": last_name,
        "birthDate": birth_date,
        "hiredDate": "yesterday",
        "firedDate": "",
        "position": position,
        "salary": salary
    }   
    database.append(newcome)
    return {"id": newcome["id"], "errorDesc": ""}

def fire_employee(id: int) -> dict:
    if not(0 <= id < len(database)):
        return {"id": -1, "errorDesc": "No such an employee exists"}
    if database[id]["firedDate"]:
        return {"id": -1, "errorDesc": "Employee is already fired"}
    database[id]["firedDate"] = "tommorow"
    return {"id": id, "errorDesc": ""}


def get_employee_id(name: str) -> int:
    for employee in database:
        if name == (employee["firstName"] + " " + employee["lastName"]):
            return employee["id"]
    return {"id": -1, "errorDesc": "No such a person here"}
    
def getEmployeeRecord(id: int) -> dict:
    if not(0 <= id < len(database)):
        return {"id": -1, "errorDesc": "No such an employee exists"}
    return database[id]


r1 = new_employee("Алексей Шевцов", "1488-05-01", "продавец говна",  14881488)
r2 = new_employee("Игорь Линк", "1776-04-04", "Неподкупный обозреватель", 123121)
r3 = new_employee("Виктор Слидовский", "1984-04-02", "русофоб", 3)
r4 = new_employee("Lorem Ipsum", "0000-01-01", "черная дыра", 0)
r5 = new_employee("П П", "1981-04-12", "пистолет пулемет", 123)

print(get_employee_id("Алексей Шевцов"))
print(getEmployeeRecord(1))
fire_employee(3)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(database)

for employee in database:
    if employee["firedDate"]:
        print(employee)

salaries = []
for employee in database:
    salaries.append(employee["salary"])
total_salary = sum(salaries)
min_salary = min(salaries)
max_salary = max(salaries)
max_id=0
for id in database:
    max_id = id["id"]
avg_salary = total_salary/max_id

print(total_salary)
print(min_salary)
print(max_salary)
print(avg_salary)

# median_salary = 
# print(median_salary)