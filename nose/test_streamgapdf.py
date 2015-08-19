import numpy
numpy.random.seed(1)

# Test the routine that rotates vectors to an arbitrary vector
def test_rotate_to_arbitrary_vector():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.]])
    # Rotate to 90 deg off
    ma= streamgapdf._rotate_to_arbitrary_vector(v,[0,1.,0])
    assert numpy.fabs(ma[0,0,1]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    # Rotate to 90 deg off
    ma= streamgapdf._rotate_to_arbitrary_vector(v,[0,0,1.])
    assert numpy.fabs(ma[0,0,2]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    # Rotate to same should be unit matrix
    ma= streamgapdf._rotate_to_arbitrary_vector(v,v[0])
    assert numpy.all(numpy.fabs(numpy.diag(ma[0])-1.) < 10.**tol), \
        'Rotation matrix to same vector is not unity'
    assert numpy.fabs(numpy.sum(ma**2.)-3.)< 10.**tol, \
        'Rotation matrix to same vector is not unity'
    # Rotate to -same should be -unit matrix
    ma= streamgapdf._rotate_to_arbitrary_vector(v,-v[0])
    assert numpy.all(numpy.fabs(numpy.diag(ma[0])+1.) < 10.**tol), \
        'Rotation matrix to minus same vector is not minus unity'
    assert numpy.fabs(numpy.sum(ma**2.)-3.)< 10.**tol, \
        'Rotation matrix to minus same vector is not minus unity'
    return None

# Test that the rotation routine works for multiple vectors
def test_rotate_to_arbitrary_vector_multi():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.],[0.,1.,0.]])
    # Rotate to 90 deg off
    ma= streamgapdf._rotate_to_arbitrary_vector(v,[0,0,1.])
    assert numpy.fabs(ma[0,0,2]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    # 2nd
    assert numpy.fabs(ma[1,1,2]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,2,1]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,0,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,0,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,0,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,1,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,1,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,2,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,2,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    return None

# Test the inverse of the routine that rotates vectors to an arbitrary vector
def test_rotate_to_arbitrary_vector_inverse():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.]])
    # Rotate to random vector and back
    a= numpy.random.uniform(size=3)
    a/= numpy.sqrt(numpy.sum(a**2.))
    ma= streamgapdf._rotate_to_arbitrary_vector(v,a)
    ma_inv= streamgapdf._rotate_to_arbitrary_vector(v,a,inv=True)
    ma= numpy.dot(ma[0],ma_inv[0])
    assert numpy.all(numpy.fabs(ma-numpy.eye(3)) < 10.**tol), 'Inverse rotation matrix incorrect'
    return None

# Test that rotating to vy in particular works as expected
def test_rotation_vy():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.]])
    # Rotate to 90 deg off
    ma= streamgapdf._rotation_vy(v)
    assert numpy.fabs(ma[0,0,1]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'

# Test the Plummer calculation for a perpendicular impact, B&T ex. 8.7
def test_impulse_deltav_plummer_subhalo_perpendicular():
    from galpy.df_src import streamgapdf
    tol= -10.
    kick= streamgapdf.impulse_deltav_plummer(numpy.array([[0.,numpy.pi,0.]]),
                                             numpy.array([0.]),
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             1.5,4.)
    # Should be B&T (8.152)
    assert numpy.fabs(kick[0,0]-2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    assert numpy.fabs(kick[0,2]+2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    # Same for along z
    kick= streamgapdf.impulse_deltav_plummer(numpy.array([[0.,0.,numpy.pi]]),
                                             numpy.array([0.]),
                                             3.,
                                             numpy.array([0.,0.,numpy.pi/2.]),
                                             1.5,4.)
    # Should be B&T (8.152)
    assert numpy.fabs(kick[0,0]-2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    assert numpy.fabs(kick[0,1]-2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    return None

# Test the Plummer curved calculation for a perpendicular impact
def test_impulse_deltav_plummer_curved_subhalo_perpendicular():
    from galpy.df_src import streamgapdf
    tol= -10.
    kick= streamgapdf.impulse_deltav_plummer(numpy.array([[3.4,0.,0.]]),
                                             numpy.array([4.]),
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             1.5,4.)
    curved_kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        numpy.array([[3.4,0.,0.]]),
        numpy.array([[4.,0.,0.]]),
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        1.5,4.)
    # Should be equal
    assert numpy.all(numpy.fabs(kick-curved_kick) < 10.**tol), 'curved Plummer kick does not agree with straight kick for straight track'
    # Same for a bunch of positions
    v= numpy.zeros((100,3))
    v[:,0]= 3.4
    xpos= numpy.random.normal(size=100)
    kick= streamgapdf.impulse_deltav_plummer(v,
                                             xpos,
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             1.5,4.)
    xpos= numpy.array([xpos,numpy.zeros(100),numpy.zeros(100)]).T
    curved_kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        v,
        xpos,
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        1.5,4.)
    # Should be equal
    assert numpy.all(numpy.fabs(kick-curved_kick) < 10.**tol), 'curved Plummer kick does not agree with straight kick for straight track'
    return None

# Test general impulse vs. Plummer
def test_impulse_deltav_general():
    from galpy.df_src import streamgapdf
    from galpy.potential import PlummerPotential
    tol= -10.
    kick= streamgapdf.impulse_deltav_plummer(numpy.array([[3.4,0.,0.]]),
                                             numpy.array([4.]),
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             1.5,4.)
    pp= PlummerPotential(amp=1.5,b=4.)
    general_kick=\
        streamgapdf.impulse_deltav_general(numpy.array([[3.4,0.,0.]]),
                                           numpy.array([4.]),
                                           3.,
                                           numpy.array([0.,numpy.pi/2.,0.]),
                                           pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Plummer calculation for a Plummer potential'
    # Same for a bunch of positions
    v= numpy.zeros((100,3))
    v[:,0]= 3.4
    xpos= numpy.random.normal(size=100)
    kick= streamgapdf.impulse_deltav_plummer(v,
                                             xpos,
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             numpy.pi,numpy.exp(1.))
    pp= PlummerPotential(amp=numpy.pi,b=numpy.exp(1.))
    general_kick=\
        streamgapdf.impulse_deltav_general(v,
                                           xpos,
                                           3.,
                                           numpy.array([0.,numpy.pi/2.,0.]),
                                           pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Plummer calculation for a Plummer potential'
    return None

# Test general impulse vs. Plummer for curved stream
def test_impulse_deltav_general_curved():
    from galpy.df_src import streamgapdf
    from galpy.potential import PlummerPotential
    tol= -10.
    kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        numpy.array([[3.4,0.,0.]]),
        numpy.array([[4.,0.,0.]]),
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        1.5,4.)
    pp= PlummerPotential(amp=1.5,b=4.)
    general_kick= streamgapdf.impulse_deltav_general_curvedstream(\
        numpy.array([[3.4,0.,0.]]),
        numpy.array([[4.,0.,0.]]),
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Plummer calculation for a Plummer potential, for curved stream'
    # Same for a bunch of positions
    v= numpy.zeros((100,3))
    v[:,0]= 3.4
    xpos= numpy.random.normal(size=100)
    xpos= numpy.array([xpos,numpy.zeros(100),numpy.zeros(100)]).T
    kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        v,
        xpos,
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        numpy.pi,numpy.exp(1.))
    pp= PlummerPotential(amp=numpy.pi,b=numpy.exp(1.))
    general_kick=\
        streamgapdf.impulse_deltav_general_curvedstream(\
        v,
        xpos,
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Plummer calculation for a Plummer potential, for curved stream'
    return None

# Test general impulse vs. Hernquist
def test_impulse_deltav_general_hernquist():
    from galpy.df_src import streamgapdf
    from galpy.potential import HernquistPotential
    GM = 1.5
    tol= -10.
    kick= streamgapdf.impulse_deltav_hernquist(numpy.array([[3.4,0.,0.]]),
                                             numpy.array([4.]),
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             GM,4.)
    # Note factor of 2 in definition of GM and amp
    pp= HernquistPotential(amp=2.*GM,a=4.)
    general_kick=\
        streamgapdf.impulse_deltav_general(numpy.array([[3.4,0.,0.]]),
                                           numpy.array([4.]),
                                           3.,
                                           numpy.array([0.,numpy.pi/2.,0.]),
                                           pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Hernquist calculation for a Hernquist potential'
    # Same for a bunch of positions
    GM = numpy.pi
    v= numpy.zeros((100,3))
    v[:,0]= 3.4
    xpos= numpy.random.normal(size=100)
    kick= streamgapdf.impulse_deltav_hernquist(v,
                                             xpos,
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             GM,numpy.exp(1.))
    pp= HernquistPotential(amp=2.*GM,a=numpy.exp(1.))
    general_kick=\
        streamgapdf.impulse_deltav_general(v,
                                           xpos,
                                           3.,
                                           numpy.array([0.,numpy.pi/2.,0.]),
                                           pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Hernquist calculation for a Hernquist potential'
    return None

# Test general impulse vs. Hernquist for curved stream
def test_impulse_deltav_general_curved_hernquist():
    from galpy.df_src import streamgapdf
    from galpy.potential import HernquistPotential
    GM = 1.5
    tol= -10.
    kick= streamgapdf.impulse_deltav_hernquist_curvedstream(\
        numpy.array([[3.4,0.,0.]]),
        numpy.array([[4.,0.,0.]]),
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        GM,4.)
    # Note factor of 2 in definition of GM and amp
    pp= HernquistPotential(amp=2.*GM,a=4.)
    general_kick= streamgapdf.impulse_deltav_general_curvedstream(\
        numpy.array([[3.4,0.,0.]]),
        numpy.array([[4.,0.,0.]]),
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Hernquist calculation for a Hernquist potential, for curved stream'
    # Same for a bunch of positions
    GM = numpy.pi
    v= numpy.zeros((100,3))
    v[:,0]= 3.4
    xpos= numpy.random.normal(size=100)
    xpos= numpy.array([xpos,numpy.zeros(100),numpy.zeros(100)]).T
    kick= streamgapdf.impulse_deltav_hernquist_curvedstream(\
        v,
        xpos,
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        GM,numpy.exp(1.))
    pp= HernquistPotential(amp=2.*GM,a=numpy.exp(1.))
    general_kick=\
        streamgapdf.impulse_deltav_general_curvedstream(\
        v,
        xpos,
        3.,
        numpy.array([0.,numpy.pi/2.,0.]),
        numpy.array([0.,0.,0.]),
        numpy.array([3.4,0.,0.]),
        pp)
    assert numpy.all(numpy.fabs(kick-general_kick) < 10.**tol), 'general kick calculation does not agree with Hernquist calculation for a Hernquist potential, for curved stream'
    return None

from nose.tools import raises
@raises(ValueError)
def test_hernquistX_negative():
    from galpy.df_src import streamgapdf
    streamgapdf.HernquistX(-1.)
    return None

def test_hernquistX_unity():
    from galpy.df_src import streamgapdf
    assert streamgapdf.HernquistX(1.)==1., 'Hernquist X function not returning 1 with argument 1'
    return None

# Test general impulse vs. full orbit integration for zero force
def test_impulse_deltav_general_orbit_zeroforce():
    from galpy.df_src import streamgapdf
    from galpy.potential import PlummerPotential
    tol= -6.
    rcurv=10.
    vp=220.
    x0 = numpy.array([rcurv,0.,0.])
    v0 = numpy.array([0.,vp,0.])
    w = numpy.array([1.,numpy.pi/2.,0.])
    plummer_kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        v0,
        x0,
        3.,
        w,
        x0,
        v0,
        1.5,4.)
    pp= PlummerPotential(amp=1.5,b=4.)
    vang=vp/rcurv
    angrange=numpy.pi
    maxt=5.*angrange/vang
    galpot = constantPotential()
    orbit_kick= streamgapdf.impulse_deltav_general_orbitintegration(\
        v0,
        x0,
        3.,
        w,
        x0,
        v0,
        pp,
        maxt,
        galpot)
    assert numpy.all(numpy.fabs(orbit_kick-plummer_kick) < 10.**tol), \
        'general kick with acceleration calculation does not agree with Plummer calculation for a Plummer potential, for straight'
    # Same for a bunch of positions
    tol= -5.
    pp= PlummerPotential(amp=numpy.pi,b=numpy.exp(1.))
    theta = numpy.linspace(-numpy.pi/4.,numpy.pi/4.,100)
    xc,yc = rcurv*numpy.cos(theta),rcurv*numpy.sin(theta)
    Xc = numpy.zeros((100,3))
    Xc[:,0]=xc
    Xc[:,1]=yc
    vx,vy = -vp*numpy.sin(theta),vp*numpy.cos(theta)
    V = numpy.zeros((100,3))
    V[:,0]=vx
    V[:,1]=vy
    plummer_kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        V,
        Xc,
        3.,
        w,
        x0,
        v0,
        numpy.pi,numpy.exp(1.))
    orbit_kick=streamgapdf.impulse_deltav_general_orbitintegration(\
        V,
        Xc,
        3.,
        w,
        x0,
        v0,
        pp,
        maxt,
        galpot)
    assert numpy.all(numpy.fabs(orbit_kick-plummer_kick) < 10.**tol), \
            'general kick calculation does not agree with Plummer calculation for a Plummer potential, for curved stream'
    return None

# Test general impulse vs. full stream and halo integration for zero force
def test_impulse_deltav_general_fullintegration_zeroforce():
    from galpy.df_src import streamgapdf
    from galpy.potential import PlummerPotential
    tol= -4.
    rcurv=10.
    vp=220.
    GM=1.5
    rs=4.
    x0 = numpy.array([rcurv,0.,0.])
    v0 = numpy.array([0.,vp,0.])
    w = numpy.array([1.,numpy.pi/2.,0.])
    plummer_kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        v0,
        x0,
        3.,
        w,
        x0,
        v0,
        GM,rs)
    galpot = constantPotential()
    orbit_kick= streamgapdf.impulse_deltav_general_fullplummerintegration(\
        v0,
        x0,
        3.,
        w,
        x0,
        v0,
        galpot,
        GM,
        rs,
        tmaxfac=10.,
        N=1000)
    assert numpy.all(numpy.fabs(orbit_kick-plummer_kick) < 10.**tol), \
        'general kick with acceleration calculation does not agree with Plummer calculation for a Plummer potential, for straight'
    # Same for a bunch of positions
    tol= -4.
    GM=numpy.pi
    rs=numpy.exp(1.)
    theta = numpy.linspace(-numpy.pi/4.,numpy.pi/4.,10)
    xc,yc = rcurv*numpy.cos(theta),rcurv*numpy.sin(theta)
    Xc = numpy.zeros((10,3))
    Xc[:,0]=xc
    Xc[:,1]=yc
    vx,vy = -vp*numpy.sin(theta),vp*numpy.cos(theta)
    V = numpy.zeros((10,3))
    V[:,0]=vx
    V[:,1]=vy
    plummer_kick= streamgapdf.impulse_deltav_plummer_curvedstream(\
        V,
        Xc,
        3.,
        w,
        x0,
        v0,
        GM,rs)
    orbit_kick=streamgapdf.impulse_deltav_general_fullplummerintegration(\
        V,
        Xc,
        3.,
        w,
        x0,
        v0,
        galpot,
        GM,
        rs,
        tmaxfac=20.)
    print plummer_kick,orbit_kick
    assert numpy.all(numpy.fabs(orbit_kick-plummer_kick) < 10.**tol), \
            'full stream+halo integration calculation does not agree with Plummer calculation for a Plummer potential, for curved stream'
    return None

from galpy.potential import Potential
class constantPotential(Potential):
    def __init__(self):
        Potential.__init__(self,amp=1.)
        self.hasC= False
        return None
    def _Rforce(self,R,z,phi=0.,t=0.):
        return 0.
    def _zforce(self,R,z,phi=0.,t=0.):
        return 0.
