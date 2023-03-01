class vector:

    def __init__(self, seq):
        self.__sequence = tuple(seq)

    def size(self):
        return len(self.__sequence)

    def values(self):
        return self.__sequence

    def get(self,index):
        if index <= self.size()-1:
            return self.values()[index]
        return None

    def __add__(self, other):
        if isinstance(other,vector):
            return vector([self.get(index) + other.get(index) for index in range(self.size())])

            #return vector(map(lambda i: self.get(i) + other.get(i),range(self.size())))

            # vals_1,vals_2 = self.values(),other.values()
            # return vector(map(lambda x,y: x+y,vals_1,vals_2))


    def __eq__(self, other):
        if isinstance(other,vector) and self.size() == other.size():
            return self.values() == other.values()
        return False
    def __str__(self):
        return "dim: " + str(self.size()) + " | " + str(self.values())

    def __mul__(self, factor):
        if isinstance(factor,int):
            return vector(map(lambda elem: elem*factor,self.values()))


    def scalar_product(self,other):
        return  sum(map(lambda index: self.get(index)*other.get(index),range(self.size())))

V1 = vector((3,7,2,4,-10,8))
V2 = vector((1,5,-2,8,6,3))

print(V1 + V2)

# difference = tuple(map(lambda index: V2.get(index) - V2.get(index+1),range(V2.size()-1)))
# index_exists = tuple(filter(lambda index: V1.get(index) in difference,range(V1.size()-1)))
# sums = tuple(map(lambda index: V1.get(index) + V2.get(index),index_exists))
#
# print(sums)