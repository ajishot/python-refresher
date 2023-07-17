import unittest
import physics

import numpy as np


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(5, 100), 5 * 100 * 9.81)
        self.assertNotEqual(physics.calculate_buoyancy(23, 1), 52)
        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(0, 1000)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(5, 100), True)
        self.assertNotEqual(physics.will_it_float(23, 22), False)
        self.assertEqual(physics.will_it_float(1, 1000), None)
        with self.assertRaises(ValueError):
            physics.will_it_float(500, 0)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(20), 196200 + 101325)
        self.assertNotEqual(physics.calculate_pressure(22), 501 + 101325)
        with self.assertRaises(ValueError):
            physics.calculate_pressure(-5)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(20, 5), 4)
        self.assertNotEqual(physics.calculate_acceleration(20, 5), 3)
        with self.assertRaises(ValueError):
            physics.calculate_acceleration(20, 0)
        with self.assertRaises(ValueError):
            physics.calculate_acceleration(20, -5)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(16, 4), 4)
        self.assertNotEqual(physics.calculate_angular_acceleration(16, 4), 3)
        self.assertEqual(physics.calculate_angular_acceleration(0, 20), 0)
        with self.assertRaises(ValueError):
            physics.calculate_angular_acceleration(-2, 3)
        with self.assertRaises(ValueError):
            physics.calculate_angular_acceleration(20, 0)

    def test_calculate_torque(self):
        self.assertAlmostEqual(physics.calculate_torque(20, 45, 5), 70.71067812)
        self.assertNotEqual(physics.calculate_torque(20, 45, 5), 70.71067812)
        self.assertNotEqual(physics.calculate_torque(20, 45, 5), 23)
        with self.assertRaises(ValueError):
            physics.calculate_torque(-5, 5, 3)
        with self.assertRaises(ValueError):
            physics.calculate_torque(20, 45, -10)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(5, 10), 500)
        self.assertNotEqual(physics.calculate_moment_of_inertia(5, 10), 200)
        self.assertEqual(physics.calculate_moment_of_inertia(20, 0), 0)
        with self.assertRaises(ValueError):
            physics.calculate_moment_of_inertia(-5, 20)
        with self.assertRaises(ValueError):
            physics.calculate_moment_of_inertia(20, -3)

    def test_calculate_auv_acceleration(self):
        self.assertTrue(
            np.allclose(
                physics.calculate_auv_acceleration(50, np.pi), np.array([-0.5, 0])
            )
        )
        self.assertFalse(
            np.allclose(physics.calculate_auv_acceleration(50, np.pi), np.array([0, 0]))
        )
        with self.assertRaises(ValueError):
            physics.calculate_auv_acceleration(-3, 23, 0)
        with self.assertRaises(ValueError):
            physics.calculate_auv_acceleration(100, 36, -3)

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv_angular_acceleration(20, np.pi), 0)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(20, np.pi), 20)
        with self.assertRaises(ValueError):
            physics.calculate_auv_angular_acceleration(-3, 20)
        with self.assertRaises(ValueError):
            physics.calculate_auv_angular_acceleration(20, np.pi, 5, -3)


if __name__ == "__main__":
    unittest.main()
