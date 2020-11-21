#custom iterator starting at 1 with a built-in stop after 100 iterations

class Zähler:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x= self.a
        self.a += 1
        return x

zähler = Zähler()
iterz = iter(zähler)

runcounter = 1

while runcounter < 100:
    print(next(iterz))
    runcounter += 1
