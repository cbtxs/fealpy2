
import jax.numpy as jnp
from .quadrature import Quadrature

# http://keisan.casio.com/exec/system/1280801905


class GaussLobattoQuadrature(Quadrature):
    def make(self, k: int):
        if k == 2:
            A = jnp.array([[-1, 1], [1, 1]], dtype=jnp.float64)
        elif k == 3:
            A = jnp.array([
                [-1,  0.3333333333333333333333333],
                [ 0,  1.3333333333333333333333333],
                [ 1,  0.3333333333333333333333333]], dtype=jnp.float64)
        elif k == 4:
            A = jnp.array([
                [-1,                       0.1666666666666666666667],
                [-0.447213595499957939282, 0.8333333333333333333333],
                [ 0.447213595499957939282, 0.8333333333333333333333],
                [ 1,                       0.1666666666666666666667]], dtype=jnp.float64)
        elif k == 5:
            A = jnp.array([
                [-1,                          0.1],
                [-0.6546536707079771437983,   0.5444444444444444444444],
                [ 0,                          0.7111111111111111111111],
                [ 0.654653670707977143798,    0.5444444444444444444444], [ 1,   0.1]], dtype=jnp.float64)
        elif k == 6:
            A = jnp.array([
                [-1,                         0.06666666666666666666667],
                [-0.765055323929464692851,   0.3784749562978469803166],
                [-0.2852315164806450963142,  0.5548583770354863530167],
                [ 0.2852315164806450963142,  0.5548583770354863530167],
                [ 0.765055323929464692851,   0.3784749562978469803166],
                [ 1,                         0.06666666666666666666667]], dtype=jnp.float64)
        elif k == 7:
            A = jnp.array([
                [-1,                         0.04761904761904761904762],
                [-0.830223896278566929872,   0.276826047361565948011],
                [-0.4688487934707142138038,  0.4317453812098626234179],
                [ 0,                         0.487619047619047619048],
                [ 0.468848793470714213804,   0.431745381209862623418],
                [ 0.830223896278566929872,   0.2768260473615659480107],
                [ 1,                         0.04761904761904761904762]], dtype=jnp.float64)
        elif k == 8:
            A = jnp.array([
                [-1,                          0.03571428571428571428571],
                [-0.8717401485096066153375,   0.210704227143506039383],
                [-0.5917001814331423021445,   0.3411226924835043647642],
                [-0.2092992179024788687687,   0.4124587946587038815671],
                [ 0.2092992179024788687687,   0.412458794658703881567],
                [ 0.5917001814331423021445,   0.341122692483504364764],
                [ 0.8717401485096066153375,   0.210704227143506039383],
                [ 1,                          0.03571428571428571428571]], dtype=jnp.float64)
        elif k == 9:
            A = jnp.array([
                [-1,                          0.02777777777777777777778],
                [-0.8997579954114601573124,   0.1654953615608055250463],
                [-0.6771862795107377534459,   0.274538712500161735281],
                [-0.3631174638261781587108,   0.3464285109730463451151],
                [ 0,                          0.3715192743764172335601],
                [ 0.3631174638261781587108,   0.3464285109730463451151],
                [ 0.6771862795107377534459,   0.2745387125001617352807],
                [ 0.8997579954114601573124,   0.165495361560805525046],
                [ 1,                          0.02777777777777777777778]], dtype=jnp.float64)
        elif k == 10:
            A = jnp.array([
                [-1,                          0.02222222222222222222222],
                [-0.9195339081664588138289,   0.1333059908510701111262],
                [-0.7387738651055050750031,   0.2248893420631264521195],
                [-0.4779249498104444956612,   0.2920426836796837578756],
                [-0.1652789576663870246262,   0.3275397611838974566565],
                [ 0.1652789576663870246262,   0.3275397611838974566565],
                [ 0.4779249498104444956612,   0.292042683679683757876],
                [ 0.7387738651055050750031,   0.224889342063126452119],
                [ 0.9195339081664588138289,   0.133305990851070111126],
                [ 1,                          0.02222222222222222222222]], dtype=jnp.float64)
        elif k == 11 :
            A = jnp.array([
                [-1,                          0.01818181818181818181818],
                [-0.9340014304080591343323,   0.1096122732669948644614],
                [-0.7844834736631444186224,   0.187169881780305204108],
                [-0.565235326996205006471,    0.2480481042640283140401],
                [-0.2957581355869393914319,   0.2868791247790080886792],
                [ 0,                          0.3002175954556906937859],
                [ 0.2957581355869393914319,   0.286879124779008088679],
                [ 0.565235326996205006471,    0.2480481042640283140401],
                [ 0.7844834736631444186224,   0.1871698817803052041081],
                [ 0.9340014304080591343323,   0.109612273266994864461],
                [ 1,                          0.01818181818181818181818]], dtype=jnp.float64)
        elif k == 12 :
            A = jnp.array([
                [-1.0,                      0.01515151515151515],
                [-0.9448992722228822234076, 0.091684517413196130668],
                [-0.8192793216440066783486, 0.1579747055643701151647],
                [-0.6328761530318606776624, 0.212508417761021145358],
                [-0.3995309409653489322643, 0.2512756031992012802932],
                [-0.1365529328549275548641, 0.2714052409106961770003],
                [0.1365529328549275548641,  0.2714052409106961770003],
                [0.3995309409653489322643,  0.251275603199201280293],
                [0.6328761530318606776624,  0.212508417761021145358],
                [0.8192793216440066783486,  0.1579747055643701151647],
                [0.9448992722228822234076,  0.0916845174131961306683],
                [1.0,                       0.01515151515151515151515]], dtype=jnp.float64)
        else:
            raise NotImplementedError('gauss lobatto quadrature order higher '
                                      'than 20 is not supported now.')

        A = jnp.true_divide(A, 2.0)
        return jnp.stack([(0.5 + A[:, 0]),
                          (0.5 - A[:, 0]),
                          A[:, 1]], axis=-1)
