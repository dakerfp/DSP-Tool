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

class DSPScript(object):
    """ A script to operate over signals.
    """
    def __init__(self, name, script, doc=""):
        self.name = name
        self.script = script
        self.doc = doc

    def __call__(self, *args, **kwargs):
        return self.script(*args, **kwargs)

    def __repr__(self):
        return "<DSPScript: %s>" % self.name

    def __str__(self):
        return self.name


def script(script_name):
    """ Decorator to export a funtion as a plugin
    to the DSP-Tool.
    """

    def script_decorator(script):
        return DSPScript(script_name, script, script.__doc__)

    return script_decorator

