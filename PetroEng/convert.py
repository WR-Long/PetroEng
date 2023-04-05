#!/usr/bin/env python
# Copyright 2022-2023 William Long
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Unit conversion using Energistics_Unit_of_Measure_Dictionary_V1.0
"""
from pathlib import Path
import json

def convert(fromQuantity, fromUnit, toUnit):
    
    # Convert to base unit unless fromUnit is Base
    if UoM['unit'][fromUnit]['base'] == True:
        baseQty = fromQuantity
    else:
        x = fromQuantity
        A = float(UoM['unit'][fromUnit]['A'])
        B = float(UoM['unit'][fromUnit]['B'])
        C = float(UoM['unit'][fromUnit]['C'])
        D = float(UoM['unit'][fromUnit]['D'])
        baseQty = (A + B*x) / (C + D*x)
    
    # Convert from base unit unless toUnit is Base
    if UoM['unit'][toUnit]['base'] == True:
        toQty = baseQty
    else:
        y = baseQty
        A = float(UoM['unit'][toUnit]['A'])
        B = float(UoM['unit'][toUnit]['B'])
        C = float(UoM['unit'][toUnit]['C'])
        D = float(UoM['unit'][toUnit]['D'])
        toQty = (A - C*y) / (D*y - B)
    return toQty

def UoMdict():
    return UoM

folder = Path(__file__).parent
file = folder / 'Energistics_Unit_of_Measure_Dictionary_V1.0.json'
with file.open() as f:
    UoM = json.load(f)
