from ursina import *
from ursina.shaders import basic_lighting_shader

app = Ursina()

newMesh = Mesh(vertices=[[0, 0, 0],  # 0
                         [1, 0, 0],  # 1
                         [1, 0, 1],  # 2
                         [0, 0, 1],  # 3
                         [0, 1, 0],  # 4
                         [1, 1, 0],  # 5
                         [1, 1, 1],  # 6
                         [0, 1, 1]],  # 7
               triangles=[[3, 2, 1, 0],
                          [0, 1, 5, 4],
                          [1, 2, 6, 5],
                          [2, 3, 7, 6],
                          [3, 0, 4, 7],
                          [4, 5, 6, 7]],
               normals=[[-1, -1, -1],  # 0
                        [1, -1, -1],  # 1
                        [1, -1, 1],  # 2
                        [-1, -1, 1],  # 3
                        [-1, 1, -1],  # 4
                        [1, 1, -1],  # 5
                        [1, 1, 1],  # 6
                        [-1, 1, 1]],  # 7
               uvs=[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0], [1, 0], [1, 1], [0, 1]],
               # mode='point',
               # thickness=0.1
               )
newMesh.vertices = [[i*2 for i in j] for j in newMesh.vertices]

newMesh.generate()
newEntity = Entity(model=newMesh, texture='brick')
EditorCamera()

app.run()
