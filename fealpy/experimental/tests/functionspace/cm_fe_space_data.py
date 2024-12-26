import numpy as np
cell_to_dof = [{
    "c2d" :np.array([[ 18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,   0,
          1,   2,   3,   4,   5,  68,  69,  70,  71,  72,  73,  74,  61,
         62,  63,  64,  65,  66,  67, 103, 104, 105, 106, 107, 108, 109,
        166, 167, 168, 169, 170, 171],
       [ 36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,  18,
         19,  20,  21,  22,  23, 117, 118, 119, 120, 121, 122, 123, 110,
        111, 112, 113, 114, 115, 116, 152, 153, 154, 155, 156, 157, 158,
        172, 173, 174, 175, 176, 177],
       [ 24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,   6,
          7,   8,   9,  10,  11,  89,  90,  91,  92,  93,  94,  95,  82,
         83,  84,  85,  86,  87,  88, 124, 125, 126, 127, 128, 129, 130,
        178, 179, 180, 181, 182, 183],
       [ 42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  24,
         25,  26,  27,  28,  29, 138, 139, 140, 141, 142, 143, 144, 131,
        132, 133, 134, 135, 136, 137, 159, 160, 161, 162, 163, 164, 165,
        184, 185, 186, 187, 188, 189],
       [  6,   7,   8,   9,  10,  11,   0,   1,   2,   3,   4,   5,  24,
         25,  26,  27,  28,  29,  70,  69,  68,  74,  73,  72,  71,  84,
         83,  82,  88,  87,  86,  85,  54,  55,  56,  57,  58,  59,  60,
        190, 191, 192, 193, 194, 195],
       [ 24,  25,  26,  27,  28,  29,  18,  19,  20,  21,  22,  23,  42,
         43,  44,  45,  46,  47, 119, 118, 117, 123, 122, 121, 120, 133,
        132, 131, 137, 136, 135, 134, 105, 104, 103, 109, 108, 107, 106,
        196, 197, 198, 199, 200, 201],
       [ 12,  13,  14,  15,  16,  17,   6,   7,   8,   9,  10,  11,  30,
         31,  32,  33,  34,  35,  91,  90,  89,  95,  94,  93,  92,  96,
         97,  98,  99, 100, 101, 102,  75,  76,  77,  78,  79,  80,  81,
        202, 203, 204, 205, 206, 207],
       [ 30,  31,  32,  33,  34,  35,  24,  25,  26,  27,  28,  29,  48,
         49,  50,  51,  52,  53, 140, 139, 138, 144, 143, 142, 141, 145,
        146, 147, 148, 149, 150, 151, 126, 125, 124, 130, 129, 128, 127,
        208, 209, 210, 211, 212, 213]], dtype=np.int32)
    }]
is_boundary_dof = [{
    "isBdDof":np.array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True, False,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True, False, False, False, False,
       False, False, False,  True,  True,  True,  True,  True, False,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True, False,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True, False, False, False, False,
       False, False, False,  True,  True,  True,  True,  True,  True,
        True, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False,  True,  True,  True,
        True,  True,  True,  True, False, False, False, False, False,
       False, False,  True,  True,  True,  True,  True,  True,  True,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False],dtype=np.bool)
    }]
