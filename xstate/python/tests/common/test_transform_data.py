from common import transform_data
import common.constants as cn
from common.data_provider import DataProvider
from common_python.testing import helpers

import numpy as np
import os
import pandas as pd
import unittest


IGNORE_TEST = True


class TestDataTransformer(unittest.TestCase):

  def setUp(self):
    if IGNORE_TEST:
      return
    self._init()

  def _init(self):
    self.provider = DataProvider()
    self.provider.do()

  def testMakeTrinaryData(self):
    if IGNORE_TEST:
      return
    df = transform_data.makeTrinaryData(
        df=self.provider.df_normalized)
    columns = self.provider.df_normalized.columns
    self.assertTrue(helpers.isValidDataFrame(df, columns))

  def testAggregateGenes(self):
    if IGNORE_TEST:
      return
    provider = DataProvider()
    provider.do()
    df = transform_data.aggregateGenes(provider=provider)
    self.assertTrue(helpers.isValidDataFrame(df,
        provider.df_normalized.columns))

  def testNormalizeSample(self):
    if IGNORE_TEST:
      return
    provider = DataProvider(is_normalize=False)
    provider.do()
    df = provider.dfs_data[0]

if __name__ == '__main__':
  unittest.main()
