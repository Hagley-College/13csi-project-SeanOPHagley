import json
from game import Game
# j = {
#     "tile_size": 32,
#     "texture_paths": ["\\assets\\textures\\default-floor.png","\\assets\\textures\\default-wall.png"],
#     "player": {"x": 1, "y":0, "texture": 0},
#     "map": [
#             [{"texture": 1, "collisions": True},{"texture": 0, "collisions": False},{"texture": 1, "collisions": True},{"texture": 1, "collisions": True}],
#             [{"texture": 1, "collisions": True},{"texture": 0, "collisions": False},{"texture": 0, "collisions": False},{"texture": 1, "collisions": True}],
#             [{"texture": 1, "collisions": True},{"texture": 1, "collisions": True},{"texture": 0, "collisions": False},{"texture": 1, "collisions": True}],
#             [{"texture": 1, "collisions": True},{"texture": 0, "collisions": False},{"texture": 0, "collisions": False},{"texture": 1, "collisions": True}]
            
#             ]
# }


# f = open(".\\maps\\default\\map.json","w")
# f.write(json.dumps(j, indent=4))
# f.close()
m = Game()
print(m.Map)
