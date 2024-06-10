class CharacterMain:
	def __init__(self,name,skills: dict):
		self.name = name
		self.skills = skills
	
	def set_skill_xp(self,skill,level):
		self.skill[skill] = level
	
	def find_skill_xp(self,skill):
		return(self.skills[skill])

	def train_character(self,skill,level):
		self.skills[skill] = self.skills[skill] + level


class CharacterTrainer:
	def __init__(self,name,skill,level):
		self.name = name
		self.skill = skill
		self.level = level
	
	def train_character(self):
		return self.skill, self.level * 1000

trainer1 = CharacterTrainer("Steve","STR",3)
character1 = CharacterMain("Steven",{"STR":0,"STM":3000,"ATT":5000})

print("Your strength is:", character1.find_skill_xp("STR"))

character1.train_character(trainer1.train_character()[0], trainer1.train_character()[1])

print("Your stamina is:", character1.find_skill_xp("STR"))