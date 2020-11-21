#iterator incorporation a loop raising StopIteration when the condition is met
class Zähler:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

zähler = Zähler()
iterate = iter(zähler)
for x in iterate:
    print (x)
