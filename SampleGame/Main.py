import MapManager, CharacterManager, FileManager

""" def map_printer(map,z):

	for y in range(map.get_map_size()[1]):
		ylayer = []
		for x in range(map.get_map_size()[0]):
			ylayer.append(map.return_map_val(x,y,z))
		print(ylayer) """

File = FileManager.FileManager("test")
File.file_menu()

