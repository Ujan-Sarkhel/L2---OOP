class emp_in():
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee deleted")
def create_employee():
    print("employee created")
    ob=emp_in()
    print("function end...")
    return ob

create_employee()