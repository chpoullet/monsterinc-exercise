from monster_class import Monster

# inherit from monster_class

# methods

# read_me_other

class Student_Monster(Monster):
    def __init__(self, uni_id, scary_subjects, name, strength, scary_skills):
        super().__init__(self, name, strength, scary_skills)
        self.uni_id = uni_id
        self.scary_subjects = scary_subjects

    def study(self):
        return "I'm studying"

    def drink(self):
        return 'Woooo'

    def party(self):
        return 'Woooo x2'
