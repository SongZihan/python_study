class Restuarant():
    def __init__(self,name,style):
        self.name = name
        self.style = style

    def describe_Restuarant(self):
        print("餐馆的名字是"+self.name+"\n餐馆的风格是"+self.style)

class Icecreamstand(Restuarant):
    def _init_(self,name,style):
        super().__init__(name,style)

    def flavors(self):
        special_type = ["apple","banana","orange"]
        print("我们提供的冰淇淋口味如下")
        print(special_type)

my_restuarant = Icecreamstand("水果","冰淇淋店")
my_restuarant.describe_Restuarant()
my_restuarant.flavors()









