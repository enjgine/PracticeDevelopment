# Import map layout from CSV and export to CSV
import csv, json

# =========================================================================================================D

class MapManager():

	def __init__(self, boundaryid):
		self.map = []
		self.boundaryid = boundaryid


	def save_map(self,file):
		self.__file_name = file
		json.dump(self.map,open(file,'w'))


	def load_map(self,file):
		self.__file_name = file
		self.map = json.load(open(file,'r'))


	def create_map(self,zlen,ylen,xlen):
		if len(self.map) != 0:
			raise Exception("Map is not empty")
		self.map = []
		for z in range(zlen):
			layer = []
			for y in range(ylen):
				row = []
				for x in range(xlen):
					row.append(0)
				layer.append(row)
			self.map.append(layer)


	def return_map_val(self,y,x):
		return self.map[y][x]


	def set_map_val(self,z,y,x,val):
		if self.map[z][y][x] == self.boundaryid:
			raise Exception("Boundary reached, value not set")
		self.map[z][y][x] = val


	def find_map_edges(self,y,x):
		return {0:self.map[y-1][x],1:self.map[y][x+1],2:self.map[y+1][x],3:self.map[y][x-1]}

# =========================================================================================================D

class TerrainMapManager(MapManager):

	def set_terrain_boundary(self):
		if len(self.map) == 0:
			raise Exception("Map is empty, no limits to set")

		zlim = len(self.map) - 1
		ylim = len(self.map[0]) - 1
		xlim = len(self.map[0][0]) - 1
		
		for z in range(len(self.map)):
			for y in range(len(self.map[z])):
				for x in range(len(self.map[z][y])):
					if z == zlim or x == xlim or y == ylim or z == 0 or x == 0 or y == 0:
						self.map[z][y][x] = self.boundaryid




CurrentMap = MapManager(999)

CurrentMap.create_map(5,5,5)
CurrentMap.set_map_val(1,3,3,[7,3,5])

CurrentMap.save_map("SampleGame/TestMap.csv")

CurrentMap = None

CurrentMap = TerrainMapManager(999)

CurrentMap.load_map("SampleGame/TestMap.csv")

CurrentMap.set_terrain_boundary()

print(CurrentMap.map)

CurrentMap.save_map("SampleGame/TestMap.csv")