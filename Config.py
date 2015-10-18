import configparser, re

class OgarConfig:
    def __init__(self,configfile):
        self.configf  = open(configfile)
        self.contents = self.configf.read()
        self.contents = self.contents.replace('// [','[')
        self.contents = re.sub(r'(^[(\/)].*)*','',self.contents,flags=re.M)
        self.config = configparser.ConfigParser()
        self.config.read_string(self.contents)

    def getVal(self,key):
        for s in self.config.sections():
            for k in self.config[s]:
                if k == key:
                    return self.config[s][k]

    def setVal(self,key,val):
        for s in self.config.sections():
            for k in self.config[s]:
                if k == key:
                    self.config[s][k] = val

if __name__ == '__main__':
    c = OgarConfig('gameserver.ini')
