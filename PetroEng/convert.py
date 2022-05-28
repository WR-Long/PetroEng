"""
Unit conversion using Energistics_Unit_of_Measure_Dictionary_V1.0
"""

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

import json

with open('data/Energistics_Unit_of_Measure_Dictionary_V1.0.json') as f:
    UoM = json.load(f)