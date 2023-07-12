import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(20, 5), 25)
        self.assertEqual(hello.add(-30, 53), 23)

    def test_sub(self):
        self.assertEqual(hello.sub(20, 5), 15)
        self.assertEqual(hello.sub(-15, -23), 8)

    def test_mul(self):
        self.assertEqual(hello.mul(20, 0), 0)
        self.assertEqual(hello.mul(-5, 2), -10)

    def test_div(self):
        self.assertEqual(hello.div(5, 3), 5/3)
        self.assertEqual(hello.div(20, -5), -4)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(25), 5)
        self.assertEqual(hello.sqrt(9), 3)

    def test_power(self):
        self.assertEqual(hello.power(2, 5), 32)
        self.assertEqual(hello.power(23, 0), 1)

    def test_log(self):
        self.assertAlmostEqual(hello.log(12), 2.4849066497)
        self.assertAlmostEqual(hello.log(32), 3.465735903)

    def test_exp(self):
        self.assertAlmostEqual(hello.exp(5), 148.4131591)
        self.assertAlmostEqual(hello.exp(-1), 0.3678794412)

    def test_sin(self):
        self.assertAlmostEqual(hello.sin(0), 0)
        self.assertAlmostEqual(hello.sin(1), 0.8414709848)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
