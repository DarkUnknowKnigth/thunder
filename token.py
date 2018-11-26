import re
class token:
    RESERVED={
        "directive":r"^(add|make|delete|a|m|d)$",
        "component":r"^(route|view|controller|model|all|ro|vw|cn|md)$",
        "action":r"^(serve|reset|stop|s|rs|st)$",
        "key":r"^(t|thunder)$",
        "control":r"^(init|exit|i|e)$",
        "parameter":r"^(--help|--version|--browser|--h|--v|--b)$",
        "generate":r"^(new|n)$"
    }  
    def name(self, _string):
        if len(_string)>0:
            if re.match("[a-zA-Z]",_string[0]):
                if len(_string)>1:
                    x=_string[1:len(_string)]
                    for _x in x:
                        if re.match("[a-zA-Z0-9]",_x):
                            None
                        else:
                            return False
                    return True
                return True
            else:
                return False
        else:
            return False

    def path(self,_string):
        if len(_string)>0:
            if re.match(r"[a-zA-Z]",_string[0]):
                if len(_string)>4:
                    x=_string[4:len(_string)]
                    if _string[1]==":":
                        if _string[2]=="/":
                            for _x in x:
                                if re.match("[a-zA-Z0-9]|/|-|_",_x):
                                    None
                                else:
                                    return False
                            return True
                        else:
                            return False
                    else:
                        return False
                return True
            else:
                return False
        else:
            return False
    def tokenize(self, _string):
        token=[]
        index=1  
        x=_string.split(" ")
        for _x in x:
            if len(_x)>0:
                if re.match(self.RESERVED['directive'],_x) != None :
                    token.append([index,'directive',_x])
                    index+=1
                elif re.match(self.RESERVED['component'],_x) != None :
                    token.append([index,'component',_x])
                    index+=1
                elif re.match(self.RESERVED['action'],_x) != None :
                    token.append([index,'action',_x])
                    index+=1
                elif re.match(self.RESERVED['key'],_x) != None :
                    token.append([index,'key',_x])
                    index+=1
                elif re.match(self.RESERVED['control'],_x) != None :
                    token.append([index,'control',_x])
                    index+=1
                elif re.match(self.RESERVED['parameter'],_x) != None :
                    token.append([index,'parameter',_x])
                    index+=1
                elif re.match(self.RESERVED['generate'],_x) != None :
                    token.append([index,'generate',_x])
                    index+=1
                elif self.name(_x):
                    token.append([index,'name',_x])
                    index+=1
                elif self.path(_x):
                    token.append([index,'path',_x])
                    index+=1
                else:
                    token.append([index,'error',_x])
                    index+=1
            
        return token