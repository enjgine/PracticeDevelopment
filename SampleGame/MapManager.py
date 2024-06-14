import json

# 8=========================================================================================================D

class MapManager():

	def __init__(self, boundaryid):
		self.map = []
		self.boundaryid = boundaryid


	def save_map(self,file):
		json.dump(self.map,open(file,'w+'))


	def load_map(self,file):
		self.map = json.load(open(file,'r'))


	def create_map(self,xlen,ylen,zlen=3,blankval=1):
		try:
			if len(self.map) != 0:
				print(self.map)
				raise Exception("Map is not empty (MapManager)")
		except AttributeError:
			self.map = []
		for z in range(zlen):
			layer = []
			for y in range(ylen):
				row = []
				for x in range(xlen):
					row.append(blankval)
				layer.append(row)
			self.map.append(layer)


	def return_map_val(self,x,y,z=1):
		return self.map[z][y][x]


	def set_map_val(self,val,x,y,z=1):
		if self.map[z][y][x] == self.boundaryid:
			raise Exception("Boundary reached, value not set (MapManager)")
		self.map[z][y][x] = val


	def get_map_size(self):
		return len(self.map[0][0]) , len(self.map[0]) , len(self.map)


	def find_neighbours(self,y,x,z=False):
		if z == False:
			return {0:self.map[z][y-1][x],1:self.map[z][y][x+1],2:self.map[z][y+1][x],3:self.map[z][y][x-1]}
		else:
			return {0:self.map[z][y-1][x],1:self.map[z][y][x+1],2:self.map[z][y+1][x],3:self.map[z][y][x-1],4:self.map[z+1][y][x],5:self.map[z-1][y][x]}

# 8=========================================================================================================D

class TerrainMapManager(MapManager):

	def set_terrain_boundary(self):
		if len(self.map) == 0:
			raise Exception("Map is empty, no limits to set (TerrainMapManager)")

		xlim , ylim , zlim = self.get_map_size()
		xlim , ylim , zlim = xlim-1 , ylim-1 , zlim-1
		
		for z in range(len(self.map)):
			for y in range(len(self.map[z])):
				for x in range(len(self.map[z][y])):
					if z == zlim or x == xlim or y == ylim or z == 0 or x == 0 or y == 0:
						self.map[z][y][x] = self.boundaryid

# 8=========================================================================================================D

class ObjectMapManager(MapManager):

	def __init__(self, TerrainParent):
		self.boundaryid = TerrainParent.boundaryid
		self.TerrainParent = TerrainParent


	def put_obj(self,object,x,y,z=1):
		if self.map[z][y][x] != 0 and object != 0:
			raise Exception("Space is occupied (ObjectMapManager)")
		elif self.TerrainParent.return_map_val(x,y,z) != self.boundaryid:
			self.map[z][y][x] = object
			return f"{object} placed at {z},{y}.{x}"
		else:
			raise Exception("Cannot place on boundary (ObjectMapManager)")


	def create_map(self,blankval=1):
		try:
			if len(self.map) != 0:
				print(self.map)
				raise Exception("Map is not empty (MapManager)")
		except AttributeError:
			self.map = []
		xlen,ylen,zlen = self.TerrainParent.get_map_size()
		for z in range(zlen):
			layer = []
			for y in range(ylen):
				row = []
				for x in range(xlen):
					row.append(blankval)
				layer.append(row)
			self.map.append(layer)




""" Terrain = TerrainMapManager(999)
Terrain.create_map(10,10,3)
Terrain.set_terrain_boundary()
ObjectMap = ObjectMapManager(Terrain)
Terrain.set_map_val(99,5,5)
ObjectMap.put_obj(121,4,4) """