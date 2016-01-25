# XTRACE(u"hello, world\n")
# XTRACE_COLOR(0xff, u"red\n")
# XTRACE_COLOR(0xff00, u"green\n")
# XTRACE_COLOR(0xff0000, u"blue\n")
import tempfile
import os
import sys
import platform
from ctypes import *

if "64" in platform.architecture()[0]:
    _dll_filename = tempfile.gettempdir() + "\\xTrace64.dll"
else:
    _dll_filename = tempfile.gettempdir() + "\\xTrace.dll"
__dll_handle = None

if os.path.exists(_dll_filename):
    __dll_handle = cdll.LoadLibrary(_dll_filename)
    pass

def XTRACE(str_output):
    if None == __dll_handle:
        return
    __dll_handle.MagicTraceProc(0, 0, str_output)
    pass

def XTRACE_COLOR(color, str_output):
    if None == __dll_handle:
        return
    __dll_handle.MagicTraceProc(0, color, str_output)
    pass
