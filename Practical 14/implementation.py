import xml.dom.minidom
import pandas as pd

DOM=xml.dom.minidom.parse('go_obo.xml')
obo=DOM.documentElement
terms=obo.getElementsByTagName('term')

ID=[]
NAME=[]
DEFSTR=[]
NUM=[]


for term in terms:
    id=term.getElementsByTagName('id')[0]
    name=term.getElementsByTagName('name')[0]
    DEF=term.getElementsByTagName('def')[0]
    defstr=DEF.getElementsByTagName('defstr')[0]
    if 'autophagosome' in defstr.childNodes[0].data:
        ID.append(id.childNodes[0].data)
        NAME.append(name.childNodes[0].data)
        DEFSTR.append(defstr.childNodes[0].data)
        kids=term.getElementsByTagName('is_a')
        NUM.append(len(kids))
       
df=pd.DataFrame({'id':ID,'name':NAME,'definition':DEFSTR,'childNodes':NUM})
df.to_excel('output.xlsx')
print('seccess!')