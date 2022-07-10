
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        # definir los atributos
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_provation = is_on_probation
        pass

        # usar una funcion de una clase
    def on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False
