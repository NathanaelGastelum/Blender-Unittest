import mathutils
import unittest
# testing the Python API mathutils.Vector class methods...
 
class TestVectorClass(unittest.TestCase):
   def test_1_constructor(self):
    vec1 = mathutils.Vector((2.0, 0.0, 1.0))
    vec2 = mathutils.Vector((2.0, 0.0, 1.0))
    self.assertAlmostEqual(vec1.x, vec2.x)
    self.assertAlmostEqual(vec1.y, vec2.y)
    self.assertAlmostEqual(vec1.z, vec2.z)
      
   def test_2_length(self):
    vec = mathutils.Vector((45., 0., 0.))
    l = vec.length
    self.assertAlmostEqual(45.0, l)
      
   def test_3_normalize(self):
    vec = mathutils.Vector((2, 0, 0))
    norm = vec.normalized()
    norm_tup = norm.to_tuple()
    self.assertAlmostEqual(norm_tup, (1, 0, 0))
 
    # TODO: get clarification on "2 tests per operation" like does that mean 2 asserts in each test function? So 10 functions total
    # Also do we need to write 20 tests or 17?
    def test_4_angle(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        vec_angle = vec1.angle(vec2)
        self.assertAlmostEqual(vec_angle, )
        vec_angle = vec1.angle(vec3)
        self.assertAlmostEqual(vec_angle, )
    

    def test_5_cross(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        product = vec1.cross(vec2)
        self.assertAlmostEqual(vec_angle, )
        product = vec1.cross(vec3)
        self.assertAlmostEqual(vec_angle, )


    def test_6_dot(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        product = vec1.dot(vec2)
        self.assertAlmostEqual(vec_angle, )
        product = vec1.dot(vec3)
        self.assertAlmostEqual(vec_angle, )

    
    def test_7_lerp(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        lerp_vector = vec1.lerp(vec2)
        self.assertAlmostEqual(lerp_vector, )
        lerp_vector = vec1.lerp(vec3)
        self.assertAlmostEqual(lerp_vector, )
    

    def test_8_negate(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        vec1.negate()
        self.assertAlmostEqual(vec1, (-45., 0., -1.))
        vec2.negate()
        self.assertAlmostEqual(vec2, (-30., 0., -1.))

    
    def test_9_orthogonal(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        new_vector = vec1.orthogonal()
        self.assertAlmostEqual(vec1, (-45., 0., -1.))
        new_vector = vec2.orthogonal()
        self.assertAlmostEqual(vec2, (-30., 0., -1.))

    
    def test_10_reflect(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec3 = mathutils.Vector((30., 90., 1.))
        new_vector = vec1.reflect(vec2)
        self.assertAlmostEqual(vec1, )
        new_vector = vec3.reflect(vec2)
        self.assertAlmostEqual(vec2, )

 
if __name__ == '__main__':
   try:
      unittest.main()
   except SystemExit:
      pass
   except:
      raise