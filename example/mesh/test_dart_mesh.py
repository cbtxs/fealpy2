
import numpy as np
import sys

from fealpy.mesh import DartMesh3d, TetrahedronMesh

filename = sys.argv[1]

mesh = DartMesh3d.from_polyhedron_files(filename)
mesh.celldata['cidx'] = np.arange(mesh.number_of_cells())
mesh.to_vtk(fname='cube.vtu')

