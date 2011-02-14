'''
'''
from :/ui/Signal import DSPToolSignal
import numpy as np
import scipy.signal as sig

def median_frequence(signal):
    ff = sig.fft(signal.signal_read())
    f = ff[len(ff)/2:] # splitting in half

    return np.median(np.abs(np.array(f)))
