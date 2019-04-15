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
		return __VP

	def UpdatePerspective(self, fov = 0.0, aspect = 0.0, nearZ = 0.0, farZ = 0.0):
		self.__fov = fov
		self.__aspect = aspect
		self.__nearZ = nearZ
		self.__farZ = farZ
		__BuildPerspective()
		self.__dirty = True

	def UpdateView(self, eye = np.zeros(3), at = np.zeros(3), up =  np.zeros(3)):
		self.__eye = eye
		self.__at = at
		self.__up = up
		__BuildView();
		self.__dirty = True

	def __BuildView(self):
		zc = np.linalg.norm(self.__eye - self.__at, ord=1, axis=int);
		xc = np.linalg.norm(np.cross(self.__up, zc), ord=1, axis=int);
		yc = np.cross(zc, xc);
		self.__view_Matrix = array([[xc.x, xc.y, xc.z, np.dot(-self.__eye, xc)]
						 [yc.x, yc.y, yc.z, np.dot(-self.__eye, yc)]
						 [zc.x, zc.y, zc.z, np.dot(-self.__eye, zc)]
						 [0,0,0,1]])

	def __BuildPerspective(self):
		tanHalfFov = tan(np.radians(self.__fov * 0.5));
		inv_tan = 1.0 / tanHalfFov;
		inv_fsubn = -1.0 / (self.__farZ - self.__nearZ);
		self.__perspective_Matrix = np.array([[inv_tan / self.__aspect, 0.0, 0.0, 0.0]
										[0.0, inv_tan, 0.0, 0.0]
										[0.0, 0.0, inv_fsubn * (self.__farZ + self.__nearZ), inv_fsubn * (self.__farZ * self.__nearZ) * 2.0]
										[0.0, 0.0, -1.0, 0.0]]);

	def __BuildVP(self):
		__VP = np.matmul(self.__perspective_Matrix, self.__view_Matrix)
		
def TransformPoint(camera=Camera(), point=np.zeros(4)):
	return np.matmul(camera.ViewPerspective(), point)

