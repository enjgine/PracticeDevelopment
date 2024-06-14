import MapManager, CharacterManager, json
import os
clear = lambda: os.system('cls')

class FileManager():

	def __init__(self, folder):
		self.folder = folder

	def create_state(self):
		self.folder = input("Folder Name: ")
		self.prefix = input("Save Name: ")
		self.file = f"{self.folder}/{self.prefix}"
		x,y,z = int(input("X Tiles: "))+2, int(input("Y Tiles: "))+2, int(input("Number of layers: "))+2
		self.Terrain = MapManager.TerrainMapManager(0)
		self.Terrain.create_map(x,y,z,1)
		self.Terrain.set_terrain_boundary()
		self.Objects = MapManager.ObjectMapManager(self.Terrain)
		self.Objects.create_map()
		self.Character = CharacterManager.Character(self.Terrain)
		self.Character.create_char("Steve",1,self.Terrain,[1,1,1])

	def load_state(self):
		self.folder = input("Folder name: ")
		Loader = json.load(open(f"{self.folder}/loader.json",'r+'))
		self.prefix = Loader[1]
		self.file = f"{self.folder}/{self.prefix}"
		self.Terrain = MapManager.TerrainMapManager(0)
		TerrainFile = f"{self.file}_terrain.json"
		self.Terrain.load_map(TerrainFile)
		self.Objects = MapManager.ObjectMapManager(self.Terrain)
		ObjectFile = f"{self.file}_objects.json"
		self.Objects.load_map(ObjectFile)
		self.Character = CharacterManager.Character(self.Terrain)
		CharacterFile = f"{self.file}_character.json"
		self.Character.load_char(CharacterFile)


	def save_state(self):
		if os.path.exists(self.folder) != True:
			os.mkdir(self.folder)
		self.Terrain.save_map(f"{self.file}_terrain.json")
		self.Objects.save_map(f"{self.file}_objects.json")
		self.Character.save_char(f"{self.file}_character.json")
		json.dump([self.folder,self.prefix],open(f"{self.folder}/loader.json",'w+'))


	def file_menu(self):
		while True:
			if hasattr(self,'Terrain') == False:
				print("There is no current state. Run create_state or load_state")
			match int(input("Press to run:\n1. Create state\n2. Load state\n3. Save state\n4. Check environment\n5. Exit\n: ")):

				case 1:
					self.create_state()

				case 2:
					self.load_state()

				case 3:
					self.save_state()

				case 4:
					self.check_env()

				case _:
					break


	def check_env(self):
		while True:
			if self.Terrain == None:
				print("There is no current state. Run create_state or load_state")
				break
			match int(input("Press to run:\n1. Print the terrain map\n2.Print the object map\n3. Print character details\n4. Exit")):

				case 1:
					z = int(input("Enter z layer to render: "))
					clear()
					for y in range(self.Terrain.get_map_size()[1]):
						ylayer = []
						for x in range(self.Terrain.get_map_size()[0]):
							ylayer.append(self.Terrain.return_map_val(x,y,z))
						print(ylayer)
					input("Enter to continue")
					clear()

				case 2:
					z = int(input("Enter z layer to render: "))
					clear()
					for y in range(self.Objects.get_map_size()[1]):
						ylayer = []
						for x in range(self.Objects.get_map_size()[0]):
							ylayer.append(self.Objects.return_map_val(x,y,z))
						print(ylayer)
					input("Enter to continue")
					clear()

				case 3:
					clear()
					print(f"Name:{self.Character.name}\nEntity ID:{self.Character.id}\nLocation:{self.Character.loc}")
					input("Enter to continue")
					clear()

				case _:
					break