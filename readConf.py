import sys

class CFile:
    def __init__(self,filename):
        self.filename = filename

    def read(self):
        fh = None
        content = None
        fh = self.__open(self.filename, 'r')
        if None != fh:
            content = fh.read()
        self.__close(fh)
        return content

    def readLine(self):
        lines = []
        fh = self.__open(self.filename, 'r')
        if None != fh:
            lines = fh.readlines()
        self.__close(fh)
        return lines

    def __close(self, fh):
        if None != fh:
            fh.close()

    def __open(self, filename, model):
        fh = None
        if None != filename:
            try:
                fh = open(filename, model)
            except Exception, e:
                print "open file error: ",e
                sys.exit()
        return fh

def readConf():
    try:
        confFile =  str(sys.argv[1])
    except IndexError:
        print "confFile is null, sample: python checkData.py checkData.ini "
        sys.exit()
    return confFile

if __name__ == '__main__':
    conffile = CFile(readConf())
    map = eval(conffile.read())
    for file in map:
        print map[file]
