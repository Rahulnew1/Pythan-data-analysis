class Human:
    def _init_(self,nm,age,h,w,g,cntry):
        self.name=nm
        self.age-age
        self.height=h
        self.weight=w
        self.gender=g
        self.country=cntry
    
    def show(self):
        print(f'Name:{self.name}')
        print(f'age:{self.age}')
        print(f'height:{self.height}')
        print(f'weight:{self.weight}')
        print(f'gender:{self.gender}')
        print(f'country:{self.country}')

#making object

h1=Human('Ram',23,5.6,67,'m','Nepal')
h2=Human('shyam',25,5.5,65,'M','India')
h3=Human('Gita',26,5,50,'f','NY')

print(h1)
print(h2)
print(h3)

print(h1.name)
print(h2.name)

h1.show()
print('_'*15)
h2.show()
print('_'*15)
h3.show()
print('_'*15)



              
