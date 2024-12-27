import vtk
import numpy as np

# 创建一个多面体（例如：立方体作为示例）
# 立方体的8个顶点
points = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# 创建 vtkPoints 对象
vtk_points = vtk.vtkPoints()
for point in points:
    vtk_points.InsertNextPoint(point)

# 创建 vtkUnstructuredGrid 对象
unstructured_grid = vtk.vtkUnstructuredGrid()
unstructured_grid.SetPoints(vtk_points)

# 创建 vtkCellArray 来存储多面体的面
cell_array = vtk.vtkCellArray()

# 立方体的6个面（每个面为4个顶点）
faces = [
    [0, 1, 2, 3],  # 面 1
    [4, 5, 6, 7],  # 面 2
    [0, 1, 5, 4],  # 面 3
    [1, 2, 6, 5],  # 面 4
    [2, 3, 7, 6],  # 面 5
    [3, 0, 4, 7]   # 面 6
]

# 创建 vtkIdList 来存储顶点索引并插入面
for face in faces:
    id_list = vtk.vtkIdList()
    id_list.InsertNextId(4)  # 四个顶点定义一个面
    for vertex in face:
        id_list.InsertNextId(vertex)
    # 插入每个面
    cell_array.InsertNextCell(id_list)

# 通过 vtkUnstructuredGrid 插入多面体单元
unstructured_grid.InsertNextCell(vtk.VTK_POLYHEDRON, cell_array)

# 写入 .vtu 文件
writer = vtk.vtkXMLUnstructuredGridWriter()
writer.SetFileName("polyhedron_output.vtu")
writer.SetInputData(unstructured_grid)
writer.Write()

print("VTU file has been written.")

