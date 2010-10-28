# -*- coding: utf-8 -*-

#from SureteDuQuebec_PublicDataSystem import decorator
#import decorator
#from SureteDuQuebec_PublicDataSystem.decorator import DecoratorSQ
#from decorator import DecoratorSQ

class ErrorSureteDuQuebec:

  class ExceptionOverwritingNotAllowed( Exception ):
    MsgShow='Base Classe Variable/Attribute implicitly claimed to not overwrite variable, with transfert techniques, while using Func: %s. '
    ExceptionValue=None
    WarnValue=None
    def __init__(self, value):
      if self.WarnAttributeOverwriting.WarnValue in DecoratorSQ.DictReference.keys():
        if ErrorSureteDuQuebec.DictReference[ErrorSureteDuQuebec.WarnAttributeOverwriting.WarnValue] == False :
          Exception.__init__( self, self.MsgShow % ( self.ExceptionValue ) )
      else:
        pass

  class WarnAttributeOverwriting( Warning ):
    MsgShow='Raised an Class Exception %s '
    WarnValue=None
    def __init__(self, value):
      if len( value ) == 1:
        self.WarnValue=value
        ErrorSureteDuQuebec.ExceptionOverwritingNotAllowed.ExceptionValue='None'
      if len( value ) == 2:
        self.WarnValue, ErrorSureteDuQuebec.ExceptionOverwritingNotAllowed.ExceptionValue = value
      try:
        raise ErrorSureteDuQuebec.ExceptionOverwritingNotAllowed, ErrorSureteDuQuebec.ExceptionOverwritingNotAllowed.ExceptionValue
      except ErrorSureteDuQuebec.ExceptionOverwritingNotAllowed:
        Warning.__init__( self, self.MsgShow % ( self.__class__.__name__ ) )
      else:
        pass 
