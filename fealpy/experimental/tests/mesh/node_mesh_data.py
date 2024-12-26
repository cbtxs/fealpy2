import numpy as np

# 定义多个典型的 NodeMesh 对象
mesh_data = [
    {
        "node": np.array([[0, 0], [1, 0], [0, 1]], dtype=np.float64),
        "num": 3,
        "geo_dim": 2,
        "top": 0,
        "temperature": np.array([300.0, 350.0, 400.0], dtype=np.float32),
        "pressure": np.array([100.0, 200.0, 300.0], dtype=np.float32),
        "node_box": np.array([[0.5, 0.5], [0.2, 0.1], [0.2, 0.3], [0.3, 0.5], [0.8, 0.4],[0.4, 0.5], [0.7, 0.3], [0.9, 0.2], [0.3, 0.6], [0.6, 0.2], \
            [0.4, 0.4], [0.5, 0.8], [0.3, 0.8], [0.9, 0.3], [0.2, 0.5], [0.2, 0.9], [0.7, 0.1], [0.6, 0.3], [0.8, 0.1]], dtype=np.float64),
        "cutoff": 0.2,
        "box_size": 1.0,
        "index": np.array([5, 10, 0, 2, 15, 1, 14, 1, 2, 8, 14, 0, 5, 10, 3, 13, 6, 4, 0, 10, 3, 8, 5, 4, 9, 17, 16, 6, 13, 18, 7, 3, 14, 5,\
                 8, 17, 6, 16, 9, 0, 5, 3, 10, 11, 15, 11, 12, 7, 4, 13, 3, 8, 5, 14, 12, 1, 15, 6, 9, 18, 16, 9, 6, 17, 7, 16, 18], dtype=np.int32),
        "indptr": np.array([0, 3, 6, 9, 15, 18, 23, 28, 31, 35, 39, 43, 44, 47, 50, 54, 57, 61, 64, 67], dtype=np.int32),
        "tgv_num": 2500,
        "ht_num": 800,
        "fht_num": 1200,
        "lrc_num": 4994,
        "db_num": 6202
    }
]