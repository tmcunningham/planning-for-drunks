# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:50:51 2021

@author: c27028tc
"""

drunks[13].id
# 140
drunk = drunks[13]
drunk.history
"""
[(129, 142),
 (129, 145),
 (129, 148),
 (129, 151),
 (126, 151),
 (126, 154),
 (126, 157),
 (126, 154),
 (126, 157),
 (126, 154),
 (123, 154),
 (120, 154),
 (120, 157),
 (120, 160),
 (120, 157),
 (123, 157),
 (126, 157),
 (126, 154)]
"""
for hist in drunk.history:
    print(hist in drunk.other_building_coords)
"""
True
True
True
True
False
False
False
False
False
False
False
False
False
False
False
False
False
False
"""