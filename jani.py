from datetime import datetime

class person():
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    def get_age(self):
        dob = datetime.strptime(self.dob,"%Y-%m-%d")
        today = datetime.today()
        age = today.date - dob