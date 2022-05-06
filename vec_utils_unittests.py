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


    def test_4_angle(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        vec_angle = vec1.angle(vec2)
        self.assertAlmostEqual(vec_angle, 0.01110238844)
        
        
    def test_5_angle(self):
        vec1 = mathutils.Vector((0., 0., 1.))
        vec2 = mathutils.Vector((0., 0., 1.))
        vec_angle = vec1.angle(vec2)
        self.assertAlmostEqual(vec_angle, 0.)
    

    def test_6_cross(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        product = vec1.cross(vec2)
        assert product == mathutils.Vector((0., -15., 0.))
        
        
    def test_7_cross(self):
        vec1 = mathutils.Vector((30., 0., 1.))
        vec2 = mathutils.Vector((30., 90., 20.))
        product = vec1.cross(vec2)
        assert product == mathutils.Vector((-90., -570., 2700.))


    def test_8_dot(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((30., 0., 1.))
        product = vec1.dot(vec2)
        self.assertAlmostEqual(product, 1351.)
        
        
    def test_9_dot(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec2 = mathutils.Vector((0., 0., 0.))
        product = vec1.dot(vec2)
        self.assertAlmostEqual(product, 0.)

    
    def test_10_lerp(self):
        vec1 = mathutils.Vector((30., 0., 1.))
        vec2 = mathutils.Vector((30., 90., 1.))
        lerp_vector = vec1.lerp(vec2, .5)
        assert lerp_vector == mathutils.Vector((30., 45., 1.))
        
    def test_11_lerp(self):
        vec1 = mathutils.Vector((30., 0., 1.))
        vec2 = mathutils.Vector((-30., -90., 1.))
        lerp_vector = vec1.lerp(vec2, .2)
        assert lerp_vector == mathutils.Vector((18., -18., 1.))
    

    def test_12_negate(self):
        vec1 = mathutils.Vector((45., 0., 1.))
        vec1.negate()
        assert vec1 == mathutils.Vector((-45., 0., -1.))
        
    
    def test_13_negate(self):
        vec1 = mathutils.Vector((0., 0., 0.))
        vec1.negate()
        assert vec1 == mathutils.Vector((0., 0., 0.))

    
    def test_14_orthogonal(self):
        vec1 = mathutils.Vector((0., 30., 3.))
        new_vector = vec1.orthogonal()
        assert new_vector == mathutils.Vector((30., -3., 30.))
        
    def test_15_orthogonal(self):
        vec1 = mathutils.Vector((0., 0., 0.))
        new_vector = vec1.orthogonal()
        assert new_vector == mathutils.Vector((0., 0., 0.))


    def test_16_project(self):
        vec1 = mathutils.Vector((80., 60., 1.))
        vec2 = mathutils.Vector((10., 120., 1.))
        new_vector = vec1.project(vec2)
        self.assertAlmostEqual(new_vector.x, 5.51755046)
        self.assertAlmostEqual(new_vector.y, 66.2106094)
        self.assertAlmostEqual(new_vector.z, 0.55175507)
        #assert new_vector == mathutils.Vector((5.5176, 66.2106, 0.5518)), f"{new_vector} != {mathutils.Vector((5.5176, 66.2106, 0.5518))}"
        
        
    def test_17_project(self):
        vec1 = mathutils.Vector((-15., -60., 3.))
        vec2 = mathutils.Vector((10., 60., 1.))
        new_vector = vec1.project(vec2)
        self.assertAlmostEqual(new_vector.x, -10.12429141)
        self.assertAlmostEqual(new_vector.y, -60.74574661)
        self.assertAlmostEqual(new_vector.z, -1.012429118)
        
    
    def test_18_reflect(self):
        vec1 = mathutils.Vector((30., 0., 1.))
        vec2 = mathutils.Vector((5., 90., 2.))
        new_vector = vec1.reflect(vec2)
        self.assertAlmostEqual(new_vector.x, 29.81301498)
        self.assertAlmostEqual(new_vector.y, -3.36572766)
        
        
    def test_19_reflect(self):
        vec1 = mathutils.Vector((4., 7.))
        vec2 = mathutils.Vector((-5., -3.))
        new_vector = vec1.reflect(vec2)
        self.assertAlmostEqual(new_vector.x, -8.05882549)
        self.assertAlmostEqual(new_vector.y, -0.23529529)
        
        
    def test_20_magnitude(self):
        vec2d = mathutils.Vector((1.0, 2.0))
        mag = vec2d.magnitude
        self.assertAlmostEqual(mag, 2.2360679775)


if __name__ == '__main__':
   try:
      unittest.main()
   except SystemExit:
      pass
   except:
      raise
