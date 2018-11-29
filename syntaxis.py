import re
class syntaxis:
    hierarchy={
        1:r'^(key)$',
        2:r'^(control|generate|parameter|directive|action)$',
        3:r'^(name|component|parameter)$',
        4:r'^(path|name)$'
         }
    valid={
        'kc':['key','control'],
        'kgn':['key','generate','name'],
        'kgnp':['key','generate','name','path'],
        'kp':['key','parameter'],
        'kdp':['key','directive','parameter'],
        'kdcn':['key','directive','component','name'],
        'ka':['key','action'],
        'kap':['key','action','parameter']
    }
    def syntaxize(self,table):
        keys=self.valid.keys()#arreglo de llaves
        instruction=[]
        if len(table)>1:
            for data in table:
                if data[0]<=4 and data[0]>0:
                    if re.match(self.hierarchy[data[0]],data[1]) != None:
                        instruction.append(data[1])
                    else:
                        instruction.append('error')
                else:
                    print()
            for key in keys:
                if ' '.join(str(x) for x in self.valid[key]) == ' '.join(str(x) for x in instruction):
                    return [key,table]
                else:
                    if ' '.join(str(x) for x in self.valid[key][0:len(self.valid[key])-1]) == ' '.join(str(x) for x in instruction):
                        print("(r_r) try whit: \n\t>"+' >'.join(str(x) for x in self.valid[key]))
            return None              



