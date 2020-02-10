# Do monster class here

class Monster():
    def __init__(self, name, strength, scary_skills):
        self.name = name
        self.strength = strength
        self.scary_skills = scary_skills
        
    def eat(self):          # we have access to the instance of the Class via the self. Self is the instance.
        return 'Nom nom'
    def sleep(self):
        return 'Zzzz'
    def pay_taxes(self):
        return "Ain't nobody got time for that"
    def shout_strength(self):
        return 'ASDIJFASDFASDF!!!'

# sullivan = Monster('Sullivan', 10, 'Good at shouting')
# print(sullivan.name)