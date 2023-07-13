import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(5, 100), 5 * 100 * 9.81)
        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(0, 1000)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(5, 100), True)
        self.assertEqual(physics.will_it_float(1, 1000), None)
        with self.assertRaises(ValueError):
            physics.will_it_float(500, 0)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(20), 196200)
        with self.assertRaises(ValueError):
            physics.calculate_pressure(-5)


if __name__ == "__main__":
    unittest.main()
