from Signal import Signal
import os
import pickle

class Project(object):
    '''
    '''
    def __init__(self, path, name): 
        
        object.__init__(self)
        
        self.path = path
        self.filePath = self.path + "/" + name + ".dsp"
        self.signalList = []     
        
    def save(self):
        
        print "save"
             
        f = open (self.filePath, "w")
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        
        f = open (self.filePath, "r")
        test = pickle.load(f)
        f.close()
        
        print test.signalList
    
    def addSignal (self, name, path, commentary):
        sig = Signal(name, path, commentary, self)
        self.signalList.append([sig])

