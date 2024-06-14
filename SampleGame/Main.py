import MapManager

def map_printer(map,z):

	for y in range(map.get_map_size()[1]):
		ylayer = []
		for x in range(map.get_map_size()[0]):
			ylayer.append(map.return_map_val(x,y,z))
		print(ylayer)

TerrainMap = MapManager.TerrainMapManager(0)
TerrainMap.create_map(10,10)

map_printer(TerrainMap,1)

TerrainMap.set_terrain_boundary()

map_printer(TerrainMap,1)