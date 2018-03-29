###############################################################################
#   ChandrasekharDynamicalFrictionForce: Class that implements the 
#                                        Chandrasekhar dynamical friction
###############################################################################
import hashlib
import numpy
from scipy import special
from galpy.potential_src.DissipativeForce import DissipativeForce
from galpy.potential_src.Potential import _APY_LOADED, evaluateDensities
from galpy.potential_src.Potential import flatten as flatten_pot
if _APY_LOADED:
    from astropy import units
_INVSQRTTWO= 1./numpy.sqrt(2.)
_INVSQRTPI= 1./numpy.sqrt(numpy.pi)
def isothermalsigmar(r):
    return _INVSQRTTWO
class ChandrasekharDynamicalFrictionForce(DissipativeForce):
    """Class that implements the Chandrasekhar dynamical friction force

    .. math::


       \\mathbf{F}(\\mathbf{x},\\mathbf{v}) = -2\\pi\\,[G\\,M]\\,[G\\,\\rho(\\mathbf{x})]\\,\\ln[1+\\Lambda^2] \\,\\left[\\mathrm{erf}(X)-\\frac{2X}{\\sqrt{\\pi}}\\exp\\left(-X^2\\right)\\right]\\,\\frac{\\mathbf{v}}{|\\mathbf{v}|^3}\\,

    on a mass (e.g., a satellite galaxy or a black hole) :math:`M` at position :math:`\\mathbf{x}` moving at velocity :math:`\\mathbf{v}` through a background density :math:`\\rho`. The factor :math:`\\Lambda` that goes into the Coulomb logarithm is taken to be

    .. math::

       \\Lambda = \\frac{R/\\gamma}{\\mathrm{max}\\left(r_{\\mathrm{hm}},GM/|\\mathbf{v}|^2\\right)}\\,,

    where :math:`\\gamma` is a constant. This :math:`\\gamma` should be the absolute value of the logarithmic slope of the density :math:`\\gamma = |\\mathrm{d} \\ln \\rho / \\mathrm{d} \\ln r|`, although for :math:`\\gamma<1` it is advisable to set :math:`\\gamma=1`. Implementation here roughly follows `2016MNRAS.463..858P <http://adsabs.harvard.edu/abs/2016MNRAS.463..858P>`__ and earlier work.

    """
    def __init__(self,amp=1.,GMs=.1,gamma=1.,rhm=0.,
                 dens=None,sigmar=isothermalsigmar,
                 const_lnLambda=False,
                 ro=None,vo=None):
        """
        NAME:

           __init__

        PURPOSE:

           initialize a Chandrasekhar Dynamical Friction force

        INPUT:

           amp - amplitude to be applied to the potential (default: 1)

           GMs - satellite mass; can be a Quantity with units of mass or Gxmass

           rhm - half-mass radius of the satellite (set to zero for a black hole; can be a Quantity)

           gamma - Free-parameter in :math:`\\Lambda`

           dens - Potential instance or list thereof that represents the density [default: LogarithmicHaloPotential(normalize=1.,q=1.)]

           sigmar - function that gives the velocity dispersion as a function of r (has to be in natural units!)

           cont_lnLambda= (False) if set to a number, use a constant ln(Lambda) instead with this value

        OUTPUT:

           (none)

        HISTORY:

           2011-12-26 - Started - Bovy (NYU)

           2018-03-18 - Re-started: updated to r dependent Lambda form and integrated into galpy framework - Bovy (UofT)

        """
        DissipativeForce.__init__(self,amp=amp*GMs,ro=ro,vo=vo,
                                  amp_units='mass')
        if _APY_LOADED and isinstance(rhm,units.Quantity):
            rhm= rhm.to(units.kpc).value/self._ro
        self._gamma= gamma
        self._ms= self._amp/amp # from handling in __init__ above, should be ms in galpy units
        self._rhm= rhm
        # Parse density
        if dens is None:
            from galpy.potential_src.LogarithmicHaloPotential import \
                LogarithmicHaloPotential
            dens= LogarithmicHaloPotential(normalize=1.,q=1.)
        dens= flatten_pot(dens)
        self._dens_pot= dens
        self._dens=\
            lambda R,z,phi=0.,t=0.: evaluateDensities(self._dens_pot,
                                                      R,z,phi=phi,t=t)
        self._sigmar= sigmar
        if const_lnLambda:
            self._lnLambda= const_lnLambda
        else:
            self._lnLambda= False
        self._amp*= 4.*numpy.pi
        self._force_hash= None
        return None

    def lnLambda(self,r,v):
        """
        """
        if self._lnLambda:
            lnLambda= self._lnLambda
        else:
            GMvs= self._ms/v**2.
            if GMvs < self._rhm:
                Lambda= r/self._gamma/self._rhm
            else:
                Lambda= r/self._gamma/GMvs
            lnLambda= 0.5*numpy.log(1.+Lambda**2.) 
        return lnLambda

    def _calc_force(self,R,phi,z,v,t):
        vs= numpy.sqrt(v[0]**2.+v[1]**2.+v[2]**2.)
        r= numpy.sqrt(R**2.+z**2.)
        X= vs*_INVSQRTTWO/self._sigmar(r)
        Xfactor= special.erf(X)-2.*X*_INVSQRTPI*numpy.exp(-X**2.)
        lnLambda= self.lnLambda(r,vs)
        self._cached_force=\
            -self._dens(R,z,phi=phi,t=t)/vs**3.\
            *Xfactor*lnLambda

    def _Rforce(self,R,z,phi=0.,t=0.,v=None):
        """
        NAME:
           _Rforce
        PURPOSE:
           evaluate the radial force for this potential
        INPUT:
           R - Galactocentric cylindrical radius
           z - vertical height
           phi - azimuth
           t - time
           v= current velocity in cylindrical coordinates
        OUTPUT:
           the radial force
        HISTORY:
           2018-03-18 - Started - Bovy (UofT)
        """
        new_hash= hashlib.md5(numpy.array([R,phi,z,v[0],v[1],v[2],t]))\
            .hexdigest()
        if new_hash != self._force_hash:
            self._calc_force(R,phi,z,v,t)
        return self._cached_force*v[0]

    def _phiforce(self,R,z,phi=0.,t=0.,v=None):
        """
        NAME:
           _phiforce
        PURPOSE:
           evaluate the azimuthal force for this potential
        INPUT:
           R - Galactocentric cylindrical radius
           z - vertical height
           phi - azimuth
           t - time
           v= current velocity in cylindrical coordinates
        OUTPUT:
           the azimuthal force
        HISTORY:
           2018-03-18 - Started - Bovy (UofT)
        """
        new_hash= hashlib.md5(numpy.array([R,phi,z,v[0],v[1],v[2],t]))\
            .hexdigest()
        if new_hash != self._force_hash:
            self._calc_force(R,phi,z,v,t)
        return self._cached_force*v[1]*R

    def _zforce(self,R,z,phi=0.,t=0.,v=None):
        """
        NAME:
           _zforce
        PURPOSE:
           evaluate the vertical force for this potential
        INPUT:
           R - Galactocentric cylindrical radius
           z - vertical height
           phi - azimuth
           t - time
           v= current velocity in cylindrical coordinates
        OUTPUT:
           the vertical force
        HISTORY:
           2018-03-18 - Started - Bovy (UofT)
        """
        new_hash= hashlib.md5(numpy.array([R,phi,z,v[0],v[1],v[2],t]))\
            .hexdigest()
        if new_hash != self._force_hash:
            self._calc_force(R,phi,z,v,t)
        return self._cached_force*v[2]