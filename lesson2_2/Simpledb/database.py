from os import replace


class Simpledb:
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return "<%s file='%s'>" % (self.__class__.__name__, self.filename)

    def insert(self, name, number):
        f = open(self.filename, 'a')
        f.write(name + '\t' + number + '\n')
        f.close()
        return 'Inserted'

    def select(self, name):
        f = open(self.filename, 'r')
        for line in f:
            (k, v) = line.split('\t', 1)
            if k.lower() == name.lower():
                f.close()
                return v[:-1]
        f.close()
        return 'NULL'

    def delete(self, name):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        nameFound = False
        for line in f:
            (k, v) = line.split('\t', 1)
            if k.lower() != name.lower():
                result.write(line)
            elif k.lower() == name.lower():
                nameFound = True
        f.close()
        result.close()
        replace('result.txt', self.filename)

        if not nameFound:
            return 'NULL'
        else:
            return 'Deleted'

    def update(self, name, number):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        nameFound = False
        for line in f:
            (k, v) = line.split('\t', 1)
            if k.lower() != name.lower():
                result.write(line)
            elif k.lower() == name.lower():
                result.write(name + '\t' + number + '\n')
                nameFound = True
        f.close()
        result.close()
        replace('result.txt', self.filename)

        if not nameFound:
            return 'NULL'
        else:
            return 'Updated'
