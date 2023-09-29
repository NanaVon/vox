class Chunk:
  def __init__(self,ChunkId,CantContent=None,CantChildren=None, header=None, version=None):
    self.chunkId = ChunkId
    self.versionVox = version
    self.cantContent = CantContent
    self.cantChildren = CantChildren
    self.content = None
    self.children = None
    self.header = header
  def len(self):
    return self.CantContent + self.CantContent
  def addChildren(self, children):
       self.children.append(children)
  def addContent(self, content):
    self.content.append(content)
      

class Vox:
  def __init__(self):
    self.header = None
    self.main = None
  def 
