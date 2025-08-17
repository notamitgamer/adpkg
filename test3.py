# test_triangle_calculator.py
import unittest
import math
from triangle import areaoftriangle

class TestAreaOfTriangle(unittest.TestCase):

    def setUp(self):
        pass

    # --- Test Cases for Valid Triangles ---

    def test_right_triangle_3_4_5(self):
        self.assertAlmostEqual(areaoftriangle(3, 4, 5), 6.0, places=9)
        self.assertAlmostEqual(areaoftriangle(4, 3, 5), 6.0, places=9)
        self.assertAlmostEqual(areaoftriangle(5, 3, 4), 6.0, places=9)

    def test_equilateral_triangle(self):
        self.assertAlmostEqual(areaoftriangle(2, 2, 2), math.sqrt(3), places=9)
        self.assertAlmostEqual(areaoftriangle(10, 10, 10), (math.sqrt(3)/4) * 100, places=9)

    def test_scalene_triangle(self):
        self.assertAlmostEqual(areaoftriangle(7, 8, 9), math.sqrt(720), places=9) # approx 26.83281573
        self.assertAlmostEqual(areaoftriangle(6, 8, 10), 24.0, places=9)

    def test_float_inputs(self):
        self.assertAlmostEqual(areaoftriangle(3.0, 4.0, 5.0), 6.0, places=9)
        self.assertAlmostEqual(areaoftriangle(7.5, 10.0, 12.5), 37.5, places=9)

    # --- Test Cases for Degenerate Triangles (Area should be 0) ---

    def test_degenerate_triangle_straight_line(self):
        self.assertAlmostEqual(areaoftriangle(1, 2, 3), 0.0, places=9)
        self.assertAlmostEqual(areaoftriangle(2.5, 2.5, 5.0), 0.0, places=9)
        self.assertAlmostEqual(areaoftriangle(10, 20, 30), 0.0, places=9)
        self.assertAlmostEqual(areaoftriangle(1, 1, 2), 0.0, places=9)


    # --- Test Cases for Invalid Inputs (should return None) ---

    def test_invalid_triangle_inequality(self):
        self.assertIsNone(areaoftriangle(1, 2, 5))
        self.assertIsNone(areaoftriangle(10, 1, 2))
        self.assertIsNone(areaoftriangle(1, 10, 2))

    def test_zero_side_length(self):
        self.assertIsNone(areaoftriangle(0, 4, 5))
        self.assertIsNone(areaoftriangle(3, 0, 5))
        self.assertIsNone(areaoftriangle(3, 4, 0))
        self.assertIsNone(areaoftriangle(0, 0, 0))

    def test_negative_side_length(self):
        self.assertIsNone(areaoftriangle(-3, 4, 5))
        self.assertIsNone(areaoftriangle(3, -4, 5))
        self.assertIsNone(areaoftriangle(3, 4, -5))

    def test_non_numeric_inputs(self):
        self.assertIsNone(areaoftriangle("a", 4, 5))
        self.assertIsNone(areaoftriangle(3, "b", 5))
        self.assertIsNone(areaoftriangle(3, 4, "c"))
        self.assertIsNone(areaoftriangle(None, 4, 5))
        self.assertIsNone(areaoftriangle([1,2], 4, 5))

    # --- Test Cases for Unit Parameter ---

    def test_unit_parameter(self):
        self.assertEqual(areaoftriangle(3, 4, 5, 'sq units'), "6.0 sq units")
        self.assertEqual(areaoftriangle(7, 8, 9, 'm^2'), f"{math.sqrt(720)} m^2")
        self.assertEqual(areaoftriangle(10, 10, 10, 'cm²'), f"{ (math.sqrt(3)/4) * 100 } cm²")

    # Corrected syntax here:
    def test_no_unit_parameter(self):
        self.assertIsInstance(areaoftriangle(3, 4, 5), float)
        self.assertAlmostEqual(areaoftriangle(3, 4, 5), 6.0, places=9)

    def test_empty_unit_parameter(self):
        self.assertIsInstance(areaoftriangle(3, 4, 5, ''), float)
        self.assertAlmostEqual(areaoftriangle(3, 4, 5, ''), 6.0, places=9)

    # --- Refined Test for precision around degenerate cases ---
    # This test focuses on cases where the mathematical area is exactly 0,
    # but floating point arithmetic *might* produce a slightly negative `pre_result`.
    # Your function's `pre_result > -0.09` tolerance should handle these.
    def test_degenerate_triangle_zero_area_precision(self):
        # A perfectly degenerate triangle where s-c is exactly 0.
        # This is the primary case where floating point might yield pre_result < 0 but near 0.
        self.assertAlmostEqual(areaoftriangle(1.0, 1.0, 2.0), 0.0, places=9)
        self.assertAlmostEqual(areaoftriangle(3.0, 4.0, 7.0), 0.0, places=9)
        # Add cases that might cause tiny negative pre_result for true degeneracy
        # (These are hard to force consistently without knowing specific float quirks)
        # For perfectly degenerate: a=1,b=1,c=2 => s=2, s-c=0, pre_result=0.
        # If the internal calculation for (s-a)*(s-b)*(s-c) is slightly negative,
        # your function's tolerance should catch it and return 0.0.

    # This test verifies that genuinely invalid triangles (violating inequality) still return None.
    # This was previously part of 'test_nearly_degenerate_triangle' that caused TypeError.
    def test_invalid_triangle_exceeding_tolerance(self):
        # These are clearly invalid and should return None
        self.assertIsNone(areaoftriangle(1.0, 2.0, 3.0000000001)) # 1+2 < 3.0000000001
        self.assertIsNone(areaoftriangle(1.0, 1.0, 2.0000000001)) # 1+1 < 2.0000000001
        self.assertIsNone(areaoftriangle(10, 10, 25)) # Sum of two sides is less than third (pre_result would be very negative)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)