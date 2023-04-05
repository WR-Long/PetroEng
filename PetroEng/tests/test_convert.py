"""
Tests for the PetroEng convert module.
"""

import PetroEng as pe
import numpy as np
import pandas as pd

tempF = np.array([32.0, 212.0])
tempC = np.array([0.0, 100.0])

dfF = pd.DataFrame(tempF)
dfC = pd.DataFrame(tempC)

def test_scalar():
    assert pe.convert(5280, 'ft', 'mi') == 1.0

def test_array():
    assert np.all(pe.convert(tempF, 'degF', 'degC') == tempC)

def test_dataframe():
    assert dfF.equals(pe.convert(dfC, 'degC', 'degF'))