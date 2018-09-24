from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NOMALIZE_ZERO_VECTOR_MESSAGE = 'Cannot normalize the zero vector.'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def magnitude(self):
        '''computes the magnitude of a vector'''
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        ''' normalizes a vector after checking to ensure that it is not the zero vector '''
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/Decimal(magnitude))

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NOMALIZE_ZERO_VECTOR_MESSAGE)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        ''' check if two vectors have a dot product of zero and check for precision of dot product '''
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        ''' check if two vectors are parallel '''
        return (self.is_zero() or 
                v.is_zero() or 
                self.angle_with(v) == 0 or 
                self.angle_with(v) == pi)

    def is_zero(self, tolerance=1e-10):
        '''check if a vector's magnitude is smaller than some tolerance'''
        return self.magnitude() < tolerance

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self,v,in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(round(u1.dot(u2),3))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NOMALIZE_ZERO_VECTOR_MESSAGE:
                raise Exception('Cannot compute an angle with the zero vector.')
            else:
                raise e

    def plus(self,v):
        '''vector addition'''
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def minus(self,v):
        '''vector subtraction'''
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self,c):
        '''scalar multiplication'''
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

