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

import sys
import os

class DSPScript(object):
    """ A script to operate over signals.
    """
    def __init__(self, name, script, doc="", parent=None):
        self.name = name
        self.doc = doc
        self.parent = parent
        self.script = script

    def __call__(self, *args, **kwargs):
        return self.script(*args, **kwargs)

    def __repr__(self):
        return "<DSPScript: %s>" % self.name

    def __str__(self):
        return self.name

    def __len__(self):
        return 0


class DSPPlugin(object):
    """
    """
    def __init__(self, modulename, doc="", parent=None):
        self.name = modulename
        self.doc = doc
        self.parent = parent
        self.scripts = self.loadScripts()

    def loadScripts(self):
        """ Gets a module path and returns all the scripts on it.
        """
        module = __import__(self.name)
        members=[module.__getattribute__(member) for member in dir(module)]

        return [m for m in members if isinstance(m, DSPScript)]

    def __repr__(self):
        return "<DSP-Plugin %s: %s>" % (self.name, repr(self.scripts))

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.scripts)

    def __getitem__(self, index):
        return self.scripts[index]

    def __nonzero__(self):
        return len(self)



class DSPPluginModule(object):
    def __init__(self, path, parent=None):
        self.name = path.split("/")[-1]
        self.doc = ""
        self.parent = parent
        self.path = path
        self.modules = self.loadPlugins()

    def loadPlugins(self):
        sys.path.append(self.path)
        plugins = [DSPPlugin(mod[:-3]) for mod in
                   os.listdir(self.path) if mod.endswith(".py")]
        sys.path.pop()

        return filter(lambda plugin: len(plugin), plugins)

    def __repr__(self):
        return "<DSP-Module %s: %s>" % (self.name, repr(self.modules))

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.modules)

    def __getitem__(self, index):
        return self.modules[index]