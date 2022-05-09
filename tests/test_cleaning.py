import unittest
import pandas as pd
import sys

sys.path.append("..")

from utils.cleaning import CleanData

df = pd.read_csv('../data/Week1_challenge_data_source.csv')

class TestCleanData(unittest.TestCase):
	def setUp(self)->pd.DataFrame:
		self.df = 

	def test_fill_with_mean(self):


