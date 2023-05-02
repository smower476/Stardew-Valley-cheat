from pymem import *
from pymem.process import *
 
pm = pymem.Pymem("Stardew Valley.exe")
 
gameModule = module_from_name(pm.process_handle, "System.Linq.dll").lpBaseOfDll
 
def GetPtrAddr (base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_longlong(int(addr + i))
    return addr + offsets[-1]
 
#read_bytes(self, address, length)

tmp = GetPtrAddr(gameModule + 0x00003048, [0x8, 0x30, 0x78, 0x10, 0x174, 0x18, 0x458, 0x44])
print(hex(tmp))
k=0


while True:
    pm.write_float(tmp,500.0)
    print(pm.read_float(tmp))
#"System.Collections.dll"+00001000
#"System.Linq.dll"+00003048