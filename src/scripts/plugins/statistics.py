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

@dsp.script("Max Value")
def max_value(signal):
    """ Gets the max amplitude of a signal.
    """
    import numpy as np
    return np.max(signal)

@dsp.script("Min Value")
def min_value(signal):
    """ Gets the min amplitude of a signal.
    """
    import numpy as np
    return np.min(signal)

@dsp.script("Average Value")
def avg_value(signal):
    """ Gets the average amplitude of a signal.
    """
    import numpy as np
    return np.average(signal)

