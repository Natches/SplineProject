import numpy as np
import math3d
import math

class Camera(object):
	__dirty = False

	__fov = 0.0
	__aspect = 0.0
	__nearZ = 0.0
	__farZ = 0.0		

	__eye = math3d.Vector3D()
	__at = math3d.Vector3D()
	__up = math3d.Vector3D()

	__orthoR = 0
	__orthoH = 0

	__view_Matrix = math3d.Matrix4x4()
	__perspective_Matrix = math3d.Matrix4x4()
	__orthographic_Matrix = math3d.Matrix4x4()

	__VP = math3d.Matrix4x4();

	__mode = 'persp'

	def __init__(self, mode='persp'):
		self.__mode = mode

	@property
	def mode(self):
		return self.__mode

	@mode.setter
	def mode(self, value=''):
		self.__mode = value

	@property
	def view_perspective(self) -> math3d.Matrix4x4:
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

	def update_ortho(self, width = 0.0, height = 0.0, nearZ = 0.0, farZ = 0.0):
		self.__orthoR = width * 0.5
		self.__orthoH = height * 0.5
		self.__nearZ = nearZ
		self.__farZ = farZ
		self.__BuildOrtho()
		self.__dirty = True

	def update_view(self, eye=math3d.Vector3D, at=math3d.Vector3D, up=math3d.Vector3D):
		self.__eye = eye
		self.__at = at
		self.__up = up
		self.__BuildView();
		self.__dirty = True

	@property
	def eye(self) -> math3d.Vector3D:
		return self.__eye

	@property
	def at(self) -> math3d.Vector3D:
		return self.__at

	@property
	def up(self) -> math3d.Vector3D:
		return self.__up

	@eye.setter
	def eye(self, value=math3d.Vector3D) -> math3d.Vector3D:
		self.__eye = value
		self.__dirty = True

	@at.setter
	def at(self, value=math3d.Vector3D) -> math3d.Vector3D:
		self.__at = value
		self.__dirty = True

	@up.setter
	def up(self, value=math3d.Vector3D) -> math3d.Vector3D:
		self.__up = value
		self.__dirty = True

	def __BuildView(self) -> math3d.Matrix4x4:
		minusEye = -self.eye
		zc = (self.eye - self.__at).normalize()
		xc = math3d.Cross(self.up, zc).normalize()
		yc = math3d.Cross(zc, xc);
		self.__view_Matrix = math3d.Matrix4x4([[xc.x, xc.y, xc.z, minusEye.dot(xc)],
						 [yc.x, yc.y, yc.z, minusEye.dot(yc)],
						 [zc.x, zc.y, zc.z, minusEye.dot(zc)],
						 [0,0,0,1]])
		return self.__view_Matrix

	def __BuildPerspective(self) -> math3d.Matrix4x4:
		tanHalfFov = np.tan(np.radians(self.__fov * 0.5));
		inv_tan = 1.0 / tanHalfFov;
		inv_fsubn = -1.0 / (self.__farZ - self.__nearZ);
		self.__perspective_Matrix = math3d.Matrix4x4([[inv_tan / self.__aspect, 0.0, 0.0, 0.0],
										[0.0, inv_tan, 0.0, 0.0],
										[0.0, 0.0, inv_fsubn * (self.__farZ + self.__nearZ), inv_fsubn * (self.__farZ * self.__nearZ) * 2.0],
										[0.0, 0.0, -1.0, 0.0]]);
		return self.__perspective_Matrix

	def __BuildOrtho(self) -> math3d.Matrix4x4:
		inv_fsubn = -1.0 / (self.__farZ - self.__nearZ);
		self.__orthographic_Matrix = math3d.Matrix4x4([[1.0 / self.__orthoR, 0.0, 0.0, 0.0],
										[0.0, 1.0 / self.__orthoH, 0.0, 0.0],
										[0.0, 0.0, inv_fsubn * 2, 0.0],
										[0.0, 0.0, inv_fsubn * (self.__farZ + self.__nearZ), 1.0]]);
		return self.__orthographic_Matrix

	def __BuildVP(self):
		if(self.mode == 'persp'):
			self.__VP = self.__BuildPerspective() * self.__BuildView()
		elif(self.mode == 'ortho'):
			self.__VP = self.__BuildOrtho() * self.__BuildView()
		


