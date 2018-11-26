
class table:
    data=[]  #index, token, lexema
    def top(self):
        top= self.data
        self.data=[]
        return top
    def add(self,value):
            self.data.append([value[0],value[1],value[2]])