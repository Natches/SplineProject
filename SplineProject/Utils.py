from __future__ import annotations
import math3d
from enum import Enum
import copy
import math


class Edge(Enum):
	BOTTOM = 1
	TOP = 2
	LEFT = 3
	RIGHT = 4

def OperatorDecorator(func):
		def inner(self, other):
			if(isinstance(other, math3d.Vector4D) or isinstance(other, math3d.Vector3D) or
				isinstance(other, math3d.Vector2D) or isinstance(other, math3d.Quaternion)):
				return func(self, other.value)
			else:
				return func(self, other)
		return inner

def FindIntersection(vec1='math3d.Vector2D', vec2='math3d.Vector2D', width=int, height=int) -> [math3d.Vector2D]:
	vec1Outside = vec1.x > width or vec1.y > height or vec1.y < 0.0 or vec1.x < 0.0
	vec2Outside = vec2.x > width or vec2.y > height or vec2.y < 0.0 or vec2.x < 0.0
	if((vec1.x > width and vec2.x > width) or
		(vec1.y > height and vec2.y > height) or
		(vec1.y < 0.0 and vec2.y < 0.0) or
		(vec1.x < 0.0 and vec2.x < 0.0)):
		return []

	if(vec1 == vec2 or (not vec1Outside and not vec2Outside)):
		return [vec1, vec2]
	output = [vec1, vec2]
	input = []
	for edge in Edge:
		input.clear()
		input = output.copy()
		output.clear()

		if(input.__len__() > 0):
			S = input[input.__len__() - 1]
			for E in input:
				if(Inside(E, edge, width, height)):
					if (Inside(S, edge, width, height) == False):
						ComputeIntersection(E, S, edge, width, height, output)
					output.append(E)
				elif(Inside(S, edge, width, height)):
					ComputeIntersection(S, E, edge, width, height, output)
				S = E
	if(output.__len__() > 2):
		if(output[0] == output[1] and output[0] != output[2]):
			return [output[0], output[2]]
		elif(output[0] == output[2] and output[1] != output[2]):
			return [output[1], output[2]]
	return [output[0], output[1]]

def ComputeIntersection(vec1='math3d.Vector2D', vec2='math3d.Vector2D', edge=Edge, width=int, height=int, output=[]):
	if (edge == Edge.BOTTOM):
		ComputeHorizontalIntersection(vec1, vec2, math3d.Vector2D([width, height]))
	elif(edge == Edge.TOP):
		ComputeHorizontalIntersection(vec1, vec2, math3d.Vector2D([width, 0]))
	elif (edge == Edge.LEFT):
		ComputeVerticalIntersection(vec1, vec2,  math3d.Vector2D([0, height]))
	elif(edge == Edge.RIGHT):
		ComputeVerticalIntersection(vec1, vec2, math3d.Vector2D([width, height]))

	output.append(vec2)

def ComputeHorizontalIntersection(vec1='math3d.Vector2D', vec2='math3d.Vector2D', edge='math3d.Vector2D'):
	A = 0.0
	if(math.fabs(vec2.x - vec1.x) != 0.0):
		A = (vec2.y - vec1.y) / (vec2.x - vec1.x)
	if (A != 0.0):
		B = vec1.y - (A*vec1.x)
		vec2.x = (edge.y - B) // A
	vec2.y = edge.y

def ComputeVerticalIntersection(vec1='math3d.Vector2D', vec2='math3d.Vector2D', edge='math3d.Vector2D'):
	A = 0.0
	if(math.fabs(vec2.x - vec1.x) != 0.0):
		A = (vec2.y - vec1.y) / (vec2.x - vec1.x)
	B = vec1.y - (A*vec1.x)
	vec2.y = math.floor((A * edge.x + B));
	vec2.x = edge.x

def Inside(vec='math3d.Vector2D', edge=Edge, width=int, height=int):
	if(edge == Edge.BOTTOM):
		return vec.y <= height
	elif(edge == Edge.TOP):
		return vec.y >= 0.0
	elif(edge == Edge.LEFT):
		return vec.x >= 0.0
	elif(edge == Edge.RIGHT):
		return vec.x <= width

def From3DSpaceToScreen(point='math3d.Vector3D', width=int, height=int) -> math3d.Vector2D:
	x = (point.x / -point.z) * width + width * 0.5
	y = (point.y / -point.z) * height + height * 0.5
	return math3d.Vector2D([x, y])

def compute_3D_position(mvp, x, y, width, height) -> math3d.Vector4D:
	clip = math3d.Vector4D([(2.0 * x) / width - 1.0, 1.0 - (2.0 * y) / height, -1, 1])
	return math3d.Inverse(mvp) * clip

def compute_2D_position(pos, width, height):
	posy = ((1-pos.y) * height) / 2
	posx = ((pos.x + 1) * width) / 2 
	return math3d.Vector2D([posx, posy])