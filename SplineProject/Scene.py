from Mesh import Mesh
from Camera import Camera
import copy

class Scene(object):
	__camera = Camera()
	__entities = []

	def __iadd__(self, mesh=Mesh):
		self.__entities.append(mesh)
		return self

	def __isub__(self, mesh=Mesh):
		self.__entities.remove(mesh)
		return self

	@property
	def camera(self) -> Camera:
		return self.__camera

	@camera.setter
	def camera(self, camera=Camera):
		self.__camera = camera

	def __getitem__(self, key) -> Mesh:
		return self.__entities[key]

