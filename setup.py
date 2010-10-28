# -*- coding: utf-8 -*-

from distutils.core import setup
import SureteDuQuebec_PublicDataSystem
from SureteDuQuebec_PublicDataSystem import  __version__
from SureteDuQuebec_PublicDataSystem.decorator import  DecoratorSQ

#from SureteDuQuebec_PublicDataSystem import PersonnesRecherches
#from SureteDuQuebec_PublicDataSystem import PersonnesDisparues
#from SureteDuQuebec_PublicDataSystem import decorator
#from SureteDuQuebec_PublicDataSystem.decorator import DecoratorSQ
#from SureteDuQuebec_PublicDataSystem import Exceptions
#from SureteDuQuebec_PublicDataSystem.Exceptions import ErrorSureteDuQuebec
#from SureteDuQuebec_PublicDataSystem import PropertyFactory


setup(
    name="SureteDuQuebec_PublicDataSystem",
    version=__version__,
    description="Structure intended for the Public Access of Visual Information, to provide tools to accelerate search or enhance content into harmonic-identification of << dudits recherches >>...",
    license="BSD NEW LICENCE",
    url="http://github.com/priendeau/SureteDuQuebec",
    long_description="This structure is intended for the Public Access of Visual Information, to provide tools to accelerate search or enhance content into harmonic-identification of << dudits recherches >>...This is provided by third non-private party's and is out of any remuneration form or contribution form to provide the information under false-reason, abussive form or gangsterism-form listed in Canada. This Tools is provided as-is and beleive in evolution of tools to provide accurate information to help our security systems being wiser...",
    packages=["SureteDuQuebec_PublicDataSystem"]
)
