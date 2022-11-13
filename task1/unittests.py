import pandas as pd
import unittest
from sessionsetter import setSession
from datetime import datetime

colnames = ['customer_id', 'product_id', 'timestamp', 'session_id']


class DfTests(unittest.TestCase):
    def setUp(self):
        try:
            data = pd.read_csv("task1/data.csv", names=['customer_id', 'product_id', 'timestamp'])
            self.df = data
        except IOError as e:
            print(e)

    def test_colum_names(self):
        self.assertListEqual(list(setSession(self.df).columns), colnames)

    def test_timestamp_format(self):
        ts = self.df["timestamp"]
        [self.assertRegex(i, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}") for i in ts]

    def test_null_values(self):
        count_nulls = setSession(self.df).isnull().values.sum()
        self.assertEqual(0, count_nulls)

    def test_sessionSeter_output(self):
        inp = pd.DataFrame({
            'customer_id': [1, 1, 1, 2],
            'product_id': [23, 24, 56, 23],
            'timestamp': ['2022-11-09 13:00:00',
                         '2022-11-09 13:03:00', 
                         '2022-11-09 13:23:00', 
                         '2022-11-09 13:00:00'],
        })

        expected = pd.DataFrame({
            'customer_id': [1, 1, 1, 2],
            'product_id': [23, 24, 56, 23],
            'timestamp': [datetime.fromisoformat('2022-11-09 13:00:00'), 
                        datetime.fromisoformat('2022-11-09 13:03:00'), 
                        datetime.fromisoformat('2022-11-09 13:23:00'),
                        datetime.fromisoformat('2022-11-09 13:00:00')],
            'session_id': [1, 1, 2, 1]
        })
        pd.testing.assert_frame_equal(expected, setSession(inp), check_dtype=False)


if __name__ == '__main__':
    unittest.main()