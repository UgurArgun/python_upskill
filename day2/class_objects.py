"""
in Java:

class Item{

    String itemName;
    int itemPrice;

    Item(String itemName, int itemPrice){
        this.itemName = itemName;
        this.itemPrice = itemPrice;
    }
}

"""



class Item:
    made_in = "China"  #static variable
    tariffs = "%100"   #static variable

    def __init__(self, item_name: str, item_price: float):
        self.item_name = item_name
        self.item_price = item_price

#    def __str__(self):
#        return f"Item Name: {self.item_name}, Item Price: {self.item_price}"

    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'

    @staticmethod  # static method cannot interact with any instance or class variables
    def static_method():
        print(f"This is a static method")

    @classmethod # class method can access class variables and only accept static variables
    def class_method(cls):
        print(f"This is a class method of {cls.made_in}")


item1 = Item("Laptop", 1500.00)
item2 = Item("Phone", 800.00)

print(item1)
print(item2)

print(item1.made_in)
print(item2.tariffs)

"""
Create Employee class:
    instance variables: employee_name, job_title, salary
    static_variables: pay_tax

    instance methods: 
        __init()__: declares and initalizes all the isnace variables
        __str()__: creates string version of the object
        work(): displaye  ${employee_name} is working

    class method:
        display_employee_tax_rate()


"""
class Employee:
    pay_tax = 0.2  # static/class variable representing tax rate

    def __init__(self, employee_name, job_title, salary):
        self.employee_name = employee_name
        self.job_title = job_title
        self.salary = salary

    def __str__(self):
        return f"Employee(Name: {self.employee_name}, Job Title: {self.job_title}, Salary: ${self.salary})"

    def work(self):
        print(f"{self.employee_name} is working")

    @classmethod
    def display_employee_tax_rate(cls):
        print(f"Current employee tax rate is {cls.pay_tax * 100}%")

# Example usage:
employee1 = Employee("John Doe", "Software Engineer", 80000)
employee2 = Employee("Jane Smith", "Data Scientist", 90000)

print(employee1)                # Employee(Name: John Doe, Job Title: Software Engineer, Salary: $80000)
employee1.work()                # John Doe is working
Employee.display_employee_tax_rate()  # Current employee tax rate is 20.0%
