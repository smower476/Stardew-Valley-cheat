from tkinter import *
from tkinter import ttk
from pymem import *
from pymem.process import *
import re
import threading
import random

pm = pymem.Pymem("Stardew Valley.exe")
def is_valid(newval):
    result=  re.match("\d{0,9}$", newval) is not None
    if not result:
        errmsg.set("the field can only contain numbers, and no more than 9")
    elif len(newval) == 0:
        errmsg.set("The field must contain at least 1 number")
    else:
        errmsg.set("")
    return result

class Pointer():
    def __init__(self, dll, dll_offset, offsets, process_module, read_method, write_method):
        self.dll_offset = dll_offset
        self.offsets = offsets
        self.gamemodule = module_from_name(pm.process_handle, dll).lpBaseOfDll
        self.address = GetPtrAddr(self.gamemodule + self.dll_offset, self.offsets)
        self.read_method = read_method
        self.write_method = write_method
    def readValue(self):
        return self.read_method(self.address)
    
    def WriteValue(self, value):
        return self.write_method(self.address, value)
 
def GetPtrAddr (base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_longlong(int(addr + i))
    return addr + offsets[-1]


dll = "System.Linq.dll"
dll_offset = 0x00003048
offsets = [0x8, 0x30, 0x78, 0x10, 0x174, 0x18, 0x458, 0x44]
#read_bytes(self, address, length)
stamina = Pointer(dll, dll_offset, offsets, pm, pm.read_float, pm.write_float)

dll = "System.Private.Xml.dll" 
dll_offset = 0x22D48
offsets = [0x0, 0x20, 0x60, 0x88, 0xC0, 0x60, 0x1C]
visual_money = Pointer(dll, dll_offset, offsets, pm, pm.read_int, pm.write_int)

dll = "coreclr.dll" 
dll_offset = 0x004A82C8
offsets = [0x18, 0xC8, 0x28, 0x8, 0x10, 0x450, 0xD8, 0x44]
real_money = Pointer(dll, dll_offset, offsets, pm, pm.read_int, pm.write_int)




window = Tk()
window.title('Stardew Valley Trainer +2')
window.geometry('400x300')

check = (window.register(is_valid), "%P")

enabled = False
HHH = 0
def checkbutton_changed():
    global HHH
    while True:
        if HHH == 1:
            break
        if enabled: 
                #real_money.WriteValue((max(real_money.readValue() + random.randint(-102,100),0)))
                stamina.WriteValue(270.0)
                #print(real_money.readValue())    
#         else:
#             print('off')
            
def switch():
    global enabled
    enabled = not enabled

    
    
var = IntVar()
enabled_checkbutton = ttk.Checkbutton(text="stamina hack", command = switch, variable=var)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)

entry = ttk.Entry(validate="all", validatecommand=check)
entry.pack(anchor=NW, padx=6, pady=6)



btn = ttk.Button(text="Change Money", command=lambda: real_money.WriteValue(int(entry.get())) if is_valid(entry.get()) else False)
btn.pack(anchor=NW, padx=6, pady=6)

errmsg = StringVar()
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5, anchor=NW)

th = threading.Thread(target=checkbutton_changed)
th.start()
window.mainloop()
HHH = 1