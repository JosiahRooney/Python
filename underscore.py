class Underscore(object):
    def map(self, arr, callback):
        output = []
        for n in arr:
            output.append(callback(n))
        return output

    def reduce(self, arr, callback, identity):
        output = callback(arr[0], identity)
        for n in arr[1:]:
            output = callback(n, output)
        return output

    def find(self, arr, callback):
        for n in arr:
            if callback(n):
                return n
        return "undefined"

    def filter(self, arr, callback):
        output = []
        for n in arr:
            if callback(n):
                output.append(n)
        return output

    def reject(self, arr, callback):
        output = []
        for n in arr:
            if not callback(n):
                output.append(n)
        return output

_ = Underscore()

print(_.map([4,2,4], lambda x: 2 * x))
print(_.reduce([4,2,4], lambda x, y: x + y, 0))
print(_.find([1,2,3,4,5,6], lambda x: x / 2 == 2))
print(_.filter([1,2,3,4,5,6], lambda x: x % 2 == 0))
print(_.reject([1,2,3,4,5,6], lambda x: x % 2 == 0))