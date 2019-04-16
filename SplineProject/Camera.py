import numpy as np

class Camera(object):
	__dirty = False

	__fov = 0.0
	__aspect = 0.0
	__nearZ = 0.0
	__farZ = 0.0		

	__eye = np.zeros(3)
	__at = np.zeros(3)
	__up = np.zeros(3)

	__view_Matrix = np.eye(4, 4)
	__perspective_Matrix = np.eye(4, 4)

	__VP = np.eye(4, 4);

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

	def UpdateView(self, eye = np.zeros(3), at = np.zeros(3), up =  np.zeros(3)):
		self.__eye = eye
		self.__at = at
		self.__up = up
		self.__BuildView();
		self.__dirty = True

	def __BuildView(self):
		dir = self.__eye - self.__at
		zc = dir / np.linalg.norm(dir, ord=1);
		cross = np.cross(self.__up, zc)
		xc = cross / np.linalg.norm(cross, ord=1);
		yc = np.cross(zc, xc);
		self.__view_Matrix = np.array([[xc[0], xc[1], xc[2], np.dot(-self.__eye, xc)],
						 [yc[0], yc[1], yc[2], np.dot(-self.__eye, yc)],
						 [zc[0], zc[1], zc[2], np.dot(-self.__eye, zc)],
						 [0,0,0,1]])

	def __BuildPerspective(self):
		tanHalfFov = np.tan(np.radians(self.__fov * 0.5));
		inv_tan = 1.0 / tanHalfFov;
		inv_fsubn = -1.0 / (self.__farZ - self.__nearZ);
		self.__perspective_Matrix = np.array([[inv_tan / self.__aspect, 0.0, 0.0, 0.0],
										[0.0, inv_tan, 0.0, 0.0],
										[0.0, 0.0, inv_fsubn * (self.__farZ + self.__nearZ), inv_fsubn * (self.__farZ * self.__nearZ) * 2.0],
										[0.0, 0.0, -1.0, 0.0]]);

	def __BuildVP(self):
		self.__VP = np.matmul(self.__perspective_Matrix, self.__view_Matrix)

	def TransformPoint(self, point=np.zeros(4)):
		return np.matmul(self.ViewPerspective(), point)

	def From3DSpaceToScreen(self, point=np.zeros(4)):
		#point = np.matmul(np.linalg.inv(self.ViewPerspective()), point)
		return np.array([point[0] / point[2], point[1] / point[2]])
		


