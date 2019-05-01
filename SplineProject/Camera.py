import numpy as np
from math3d import Matrix4x4, Vector3D, Vector4D, Vector2D
import math3d
import math

class Camera(object):
	__dirty = False

	__fov = 0.0
	__aspect = 0.0
	__nearZ = 0.0
	__farZ = 0.0		

	__eye = Vector3D()
	__at = Vector3D()
	__up = Vector3D()

	__view_Matrix = Matrix4x4()
	__perspective_Matrix = Matrix4x4()

	__VP = Matrix4x4();

	@property
	def view_perspective(self) -> Matrix4x4:
		if(self.__dirty):
			self.__BuildVP()
			self.__dirty = False
		return self.__VP

	def update_perspective(self, fov = 0.0, aspect = 0.0, nearZ = 0.0, farZ = 0.0):
		self.__fov = fov
		self.__aspect = aspect
		self.__nearZ = nearZ
		self.__farZ = farZ
		self.__BuildPerspective()
		self.__dirty = True

	def update_view(self, eye=Vector3D, at=Vector3D, up=Vector3D):
		self.__eye = eye
		self.__at = at
		self.__up = up
		self.__BuildView();
		self.__dirty = True

	@property
	def eye(self) -> Vector3D:
		return self.__eye

	@property
	def at(self) -> Vector3D:
		return self.__at

	@property
	def up(self) -> Vector3D:
		return self.__up

	@eye.setter
	def eye(self, value=Vector3D) -> Vector3D:
		self.__eye = value
		self.__dirty = True

	@at.setter
	def at(self, value=Vector3D) -> Vector3D:
		self.__at = value
		self.__dirty = True

	@up.setter
	def up(self, value=Vector3D) -> Vector3D:
		self.__up = value
		self.__dirty = True

	def __BuildView(self) -> Matrix4x4:
		minusEye = -self.eye
		zc = (self.eye - self.__at).normalize()
		xc = math3d.Cross(self.up, zc).normalize()
		yc = math3d.Cross(zc, xc);
		self.__view_Matrix = Matrix4x4([[xc.x, xc.y, xc.z, minusEye.dot(xc)],
						 [yc.x, yc.y, yc.z, minusEye.dot(yc)],
						 [zc.x, zc.y, zc.z, minusEye.dot(zc)],
						 [0,0,0,1]])
		return self.__view_Matrix

	def __BuildPerspective(self) -> Matrix4x4:
		tanHalfFov = np.tan(np.radians(self.__fov * 0.5));
		inv_tan = 1.0 / tanHalfFov;
		inv_fsubn = -1.0 / (self.__farZ - self.__nearZ);
		self.__perspective_Matrix = Matrix4x4([[inv_tan / self.__aspect, 0.0, 0.0, 0.0],
										[0.0, inv_tan, 0.0, 0.0],
										[0.0, 0.0, inv_fsubn * (self.__farZ + self.__nearZ), inv_fsubn * (self.__farZ * self.__nearZ) * 2.0],
										[0.0, 0.0, -1.0, 0.0]]);
		return self.__perspective_Matrix

	def __BuildVP(self):
		self.__VP = self.__BuildPerspective() * self.__BuildView()

def From3DSpaceToScreen(point=Vector3D, width=int, height=int) -> Vector2D:
	x = math.floor((point.x / -point.z) * width + width * 0.5)
	y = math.floor((point.y / point.z) * height + height * 0.5)
	return Vector2D([x, y])
		


