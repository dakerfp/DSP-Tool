"""
DSP-Tool

This file is part of the DSP-Tool application.

This application is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or (at
your option) any later version.

This application is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this application;  If not, see <http://www.gnu.org/licenses/>.
"""
import scripts.dsp as dsp

@dsp.script("Fast Fourier Transform")
def fft_value(signal):
    """ Gets the fft of a signal.
    """
    import scipy.signal as sig
    return sig.fft(signal)

@dsp.script("Inverse Fast Fourier Transform")
def ifft_value(signal):
    """ Gets the inverse fft of a signal.
    """
    import scipy.signal as sig
    return sig.ifft(signal)

