from monster_class import Monster
from student_monster_class import Student_Monster
from random import randint


studentmonster_mike = Student_Monster(uni_id=randint(10000, 99999), scary_subjects='Shout class')
monster_dan = Monster(name='Dan', strength=10, scary_skills='lifting heavy objects')


print(f"Student Mike's uni id is {studentmonster_mike.uni_id}. He attends {studentmonster_mike.scary_subjects}.")
print(f"Student {monster_dan.name} has a strength of {monster_dan.strength}, which makes him good at {monster_dan.scary_skills}.")

