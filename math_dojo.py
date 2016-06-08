class MathDojo(object):
    def __init__(self, result=0):
        self.result = result

    def add(self, *rest):
        for i in rest:
            if type(i) == list or type(i) == tuple:
                for n in i:
                    self.result += n
                    self.result = round(self.result, 2)
            else:
                self.result += i
                self.result = round(self.result, 2)
        return self

    def subtract(self, *rest):
        for i in rest:
            if type(i) == list or type(i) == tuple:
                for n in i:
                    self.result -= n
                    self.result = round(self.result, 2)
            else:
                self.result -= i
                self.result = round(self.result, 2)
        return self

md = MathDojo()
print(md.add([1], 3, 4).add([3, 5, 7, 8], [2, 9.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result)
