import math3d

def OperatorDecorator(func):
		def inner(self, other):
			if(isinstance(other, math3d.Vector4D) or isinstance(other, math3d.Vector3D) or
				isinstance(other, math3d.Vector2D) or isinstance(other, math3d.Matrix4x4) or isinstance(other, math3d.Quaternion)):
				return func(self, other.value)
			else:
				return func(self, other)
		return inner