def operatorDecorator(func):
		def inner(other):
			if(other == 'Vector4D' or other == 'Vector3D' or other == 'Vector2D' or other == 'Matrix4x4' or other == 'Quaternion'):
				return func(other.value)
			elif(other == float):
				return func(other)