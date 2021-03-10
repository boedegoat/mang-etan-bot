


class Interactions :
  def __init__(self) :
    pass

  @property
  def help(self) :
    return ['tulung','tolong']

  @property
  def toxic(self) :
    return ['bacot', 'anjing', 'goblok', 'tolol', 'bangsat', 'kontol', 'asu', 'asw', 'jancuk', 'jancok']

  @property
  def replyToxic(self) :
    return [
      'sing sabar broo',
      'ada pegerangan apa si kawan ?',
    ]

  @property
  def capsExcepts(self) :
    return ['HA','AWOK','WK','KWOK', 'GG', 'GEGE', 
    'MANTAP', 'KEREN', 'IRI BILANG BOS', 'MAKASIH', 'THANK YOU', 'THANKS', 
    'WOKE', 'MABAR KUY'
    ]

class Formatting :
  def __init__(self) :
    pass

  def bold(self, str) :
    return f'**{str}**'

  def italic(self,str) :
    return f'*{str}*'

  def bold_italic(self,str) :
    return f'***{str}***'

  def quote_bold_italic(self,str) :
    return f'>>> ***{str}***'


