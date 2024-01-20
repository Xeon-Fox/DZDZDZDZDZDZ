from db import database, new_employee, get_employee_id, getEmployeeRecord, fire_employee

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
