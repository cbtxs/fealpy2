

from typing import Optional

from ..backend import backend_manager as bm
from ..typing import TensorLike, Index, _S

from ..mesh import HomogeneousMesh
from ..functionspace.space import FunctionSpace as _FS
from ..utils import process_coef_func
from ..functional import bilinear_integral, linear_integral, get_semilinear_coef
from .integrator import (
    LinearInt, OpInt, CellInt,
    enable_cache,
    assemblymethod,
    CoefLike
)


class CurlIntegrator(LinearInt, OpInt, CellInt):
    """
    @note (c curl u, curl v)
    """    
    def __init__(self, coef: Optional[CoefLike]=None, q: Optional[int]=None) -> None:
        super().__init__()
        self.coef = coef
        self.q = q

    @enable_cache
    def to_global_dof(self, space: _FS) -> TensorLike:
        return space.cell_to_dof()

    def assembly(self, space, index: Index = _S, 
                             cellmeasure=None, out=None):
        mesh = space.mesh
        NC = mesh.number_of_cells()
        GD = space.mesh.geo_dimension()

        ldof = space.dof.number_of_local_dofs()
        gdof = space.dof.number_of_global_dofs()
        cm = space.cellmeasure if cellmeasure is None else cellmeasure
        q = space.p+3 if self.q is None else self.q
        qf = mesh.quadrature_formula(q, 'cell')
        bcs, ws = qf.get_quadrature_points_and_weights()

        cphi = space.curl_basis(bcs) #(NQ, NC, ldof)
        if GD==2:
            cphi = cphi[..., None]
        A = self.coef*bm.einsum("cqli, cqdi, c, q->cld", cphi, cphi, cm, ws)
        if out is None:
            return A
        else:
            out += A
