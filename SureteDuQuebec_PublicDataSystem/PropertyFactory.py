from SureteDuQuebec_PublicDataSystem import __KeyDictAttribute__

from SureteDuQuebec_PublicDataSystem import decorator
from SureteDuQuebec_PublicDataSystem.decorator import DecoratorSQ

class DictPropertyFactory( object ):

  ASdQc={
    'PersonnesDisparues':{
      'Object':None,
          'url':'http://www.sq.gouv.qc.ca/personnes-disparues/personnes-disparues-surete-du-quebec.jsp#pageDemandee=1',
          'web':{
            'image':None,
            'link':None } },
    'PersonnesRecherches':{
      'Object':None,
          'url':'http://www.sq.gouv.qc.ca/suspect-recherches/suspects-recherches-sq.jsp#pageDemandee=1',
          'web':{
            'image':None,
            'link':None } } }

  IntNodeLevel=0
  CurrentNodeLevel=None
  TreeNode=[ ] 

  RootNode=None
  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def GetRootNode( self ):
    return self.RootNode

  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def SetRootNode( self, value ):
    self.RootClassName, self.RootClassNode = value
    self.RootNode=getattr( self.RootClassName, self.RootClassNode )
  
  PropertyRootNode=property( GetRootNode, SetRootNode)
  
  ParentKey=None
  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def GetParentKey( self ):
    return self.ParentKey

  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def SetParentKey( self, value ):
    Value = value
    self.ParentKey=self.DictReferences[ Value ]

  PropertyParentKey=property( GetParentKey, SetParentKey)
  
  ChildKey=None
  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def GetChildKey( self ):
    return [self.ChildKey]

  @DecoratorSQ.GlobalKeyNameAssertion( __KeyDictAttribute__ )
  def SetChildKey( self, value ):
    Value = value
    self.ChildKey=self.DictReferences[ Value ]

  PropertyChildKey=property( GetChildKey, SetChildKey )
