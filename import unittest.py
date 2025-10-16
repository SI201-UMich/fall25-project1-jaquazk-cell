import unittest

from Project_my import (  # replace 'your_module_name' with the actual python file name without .py
    calculate_total_profit,
    revenue_per_category,
    calculate_profitability_per_category,
)

class TestAnalysisFunctions(unittest.TestCase):
    def setUp(self):
        # Sample data mimicking dataset rows as dicts (strings for numeric fields)
        self.sample_data = [
            {'Category': 'Furniture', 'Sales': '100.0', 'Profit': '20.0'},
            {'Category': 'Furniture', 'Sales': '200.0', 'Profit': '-15.0'},
            {'Category': 'Technology', 'Sales': '150.0', 'Profit': '30.0'},
            {'Category': 'Office Supplies', 'Sales': '0', 'Profit': '0'},
            {'Category': 'Technology', 'Sales': '100.0', 'Profit': '-10.0'},
        ]

    def test_calculate_total_profit(self):
        result = calculate_total_profit(self.sample_data)
        expected = 20.0 - 15.0 + 30.0 + 0 - 10.0  # = 25.0
        self.assertEqual(result, expected)

    def test_revenue_per_category(self):
        result = revenue_per_category(self.sample_data)
        expected = {
            'Furniture': 300.0,
            'Technology': 250.0,
            'Office Supplies': 0.0,
        }
        self.assertEqual(result, expected)

    def test_calculate_profitability_per_category(self):
        result = calculate_profitability_per_category(self.sample_data)
        expected = {
            'Furniture': (20.0 - 15.0) / 300.0,  # 5/300 = 0.016666...
            'Technology': (30.0 - 10.0) / 250.0,  # 20/250 = 0.08
            'Office Supplies': 0 / 0 if 0 != 0 else 0,
        }
        # Since office supplies sales is 0, profitability is 0
        # Use almost equal for floating point comparison
        self.assertAlmostEqual(result['Furniture'], expected['Furniture'])
        self.assertAlmostEqual(result['Technology'], expected['Technology'])
        self.assertEqual(result['Office Supplies'], 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)