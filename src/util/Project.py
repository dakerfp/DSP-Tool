from Signal import Signal
import os
import pickle

class Project(object):
    '''
    '''
    def __init__(self, path, name, platform): 
        
        object.__init__(self)
        
        self.experimentProperties = []
        self.horizontalLabels = ["Original Signal"]
        self.verticalLabels = []
        self.path = path
        if platform == "win32":
            self.filePath = self.path + "\\" + name + ".dsp"
	elif platform == "linux2":
            self.filePath = self.path + "/" + name + ".dsp"
			
        self.signalList = []     
        
    def save(self):
          
        f = open (self.filePath, "w")
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        
        f = open (self.filePath, "r")
        test = pickle.load(f)
        f.close() 
           
    def addSignal (self, name, path, commentary, sampleRate):
        sig = Signal(name, path, commentary, self, sampleRate)
        self.signalList.append([sig])
        self.verticalLabels.append(name)
    
    def addPropertie(self, Name, Value):
        self.experimentProperties.append((Name, Value))

