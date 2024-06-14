import json

class Character():

	def __init__(self, parent):
		self.Parent = parent


	def create_char(self,name,entityid,parentmap,xyz):
		self.name = name
		self.loc = xyz
		self.id = entityid


	def set_parent_map(self,map):
		self.map = map


	def change_loc(self,xyz):
		x,y,z = xyz
		self.loc = [sum(a) for a in zip(self.loc,[x,y,z])]


	def save_char(self,file):
		dumplist = [self.name, self.id, self.loc]
		json.dump(dumplist,open(file,'w+'))


	def load_char(self,file):
		self.name, self.id, self.loc = json.load(open(file,'r'))

""" Protag = Character("Steve", 100, 3,3,1)
print(Protag.loc)
Protag.save_char("SampleGame/Character1.json")
Protag = None
Protag = Character("x",0,0,0,0)
Protag.load_char("SampleGame/Character1.json")

Protag.change_loc(2,1,0)
print(Protag.loc) """
