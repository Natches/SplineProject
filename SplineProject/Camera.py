import numpy as np
from math3d import Matrix4x4, Vector3D, Vector4D, Vector2D

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

	def ViewPerspective(self):
		if(self.__dirty):
			self.__BuildVP()
		return self.__VP

	def UpdatePerspective(self, fov = 0.0, aspect = 0.0, nearZ = 0.0, farZ = 0.0):
		self.__fov = fov
		self.__aspect = aspect
		self.__nearZ = nearZ
		self.__farZ = farZ
		self.__BuildPerspective()
		self.__dirty = True

	def UpdateView(self, eye=Vector3D, at=Vector3D, up=Vector3D):
		self.__eye = eye
		self.__at = at
		self.__up = up
		self.__BuildView();
		self.__dirty = True

	def __BuildView(self):
		zc = (self.__eye - self.__at).normalize();
		xc = self.__up.cross(zc).normalize()
		yc = zc.cross(xc);
		self.__view_Matrix = Matrix4x4([[xc.x(), xc.y(), xc.z(), (-self.__eye).dot(xc)],
						 [yc.x(), yc.y(), yc.z(), (-self.__eye).dot(yc)],
						 [zc.x(), zc.y(), zc.z(), (-self.__eye).dot(zc)],
						 [0,0,0,1]])

	def __BuildPerspective(self):
		tanHalfFov = np.tan(np.radians(self.__fov * 0.5));
		inv_tan = 1.0 / tanHalfFov;
		inv_fsubn = -1.0 / (self.__farZ - self.__nearZ);
		self.__perspective_Matrix = Matrix4x4([[inv_tan / self.__aspect, 0.0, 0.0, 0.0],
										[0.0, inv_tan, 0.0, 0.0],
										[0.0, 0.0, inv_fsubn * (self.__farZ + self.__nearZ), inv_fsubn * (self.__farZ * self.__nearZ) * 2.0],
										[0.0, 0.0, -1.0, 0.0]]);

	def __BuildVP(self):
		self.__VP = self.__perspective_Matrix * self.__view_Matrix

def From3DSpaceToScreen(point=Vector3D, width=int, height=int) -> Vector2D:
	return Vector2D((point.x() / point.z()) * width, (point.y() / point.z()) * height)
		


