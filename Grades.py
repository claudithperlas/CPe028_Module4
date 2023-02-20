class Grades:
    def __init__(self,code,unit,grade):
        self.code = code
        self.unit = unit
        self.grade = grade
    def __str__(self):
        return f"{self.code}({self.unit}({self.grade}))"