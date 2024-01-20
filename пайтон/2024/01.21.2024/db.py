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
