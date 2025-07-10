from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """Define the Student DAO API"""

    @abstractmethod
    def insert(self, student):
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, student_id, student):
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, student_id):
        raise NotImplementedError()
    
    @abstractmethod
    def get_one(self, student_id):
        raise NotImplementedError()
    
    class StudentImpl(AbstractStudentDAO): #TODO na dw ti ftaiei
        def __init__(self):
            self.students = {}

        def insert(self, student):
            student_id = student["id"]
            self.students[student_id] = student
            print(f"Inserted student with ID: {student_id}")

        def update(self, student_id, student):
            if student_id in self.students:
                self.students[student_id] = student
                print(f"Updated student with ID: {student_id} with value: {student}")
            else:
                print(f"Student with {student_id} not found")

        def delete(self, student_id):
            if student_id in self.students:
                del self.students[student_id]
                print(f"Deleted student with ID: {student_id}")
            else:
                print(f"Student with {student_id} not found")
        
        def getOne(self, student_id):  # TODO na dw giati to grapsame se camel case
            return self.students.get(student_id, None)
        
class ABCInventory(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        pass

class Inventory(ABCInventory):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item_name_to_remove):
        for item in self.items:
            if item.name == item_name_to_remove:
                self.items.remove(item)  # tha borousa na perasw kai to item_name_to_remove alla einai to idio TODO na to skeutw
                print(f"Removed item: {item}")
                return
        print(f"Item not found: {item_name_to_remove}")  #TODO na dw an ginetai me for else kalytera



class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
def main():
    student_d = StudentImpl()
    student_d.insert({'id': 1, 'name':"Bob"})
    student_d.insert({'id': 2, 'name':"Alice"})

    student_d.update(1, {'id': 1, 'name':"Bob"})
    st = student_d.get_one(1)

if __name__ == "__main__":
    main()