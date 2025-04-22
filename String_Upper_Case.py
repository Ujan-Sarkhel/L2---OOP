class str_upper:
    def initial(self,str):
        self.str=''
    def inp(self):
        self.str=input("Enter your string")
    def res(self):
        print("Result:", self.str.upper())
ob=str_upper()

ob.inp()
ob.res()