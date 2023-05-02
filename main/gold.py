from pymem import *
from pymem.process import *
 
pm = pymem.Pymem("Stardew Valley.exe")
 
gameModule = module_from_name(pm.process_handle, "coreclr.dll").lpBaseOfDll
 
def GetPtrAddr (base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_longlong(int(addr + i))
    return addr + offsets[-1]
 
#read_bytes(self, address, length)

tmp = GetPtrAddr(gameModule + 0x004A82C8, [0x18, 0xC8, 0x28, 0x8, 0x10, 0x450, 0xD8, 0x44])
print(hex(tmp))

while True:
    pm.write_int(tmp,500000)
    print(pm.read_int(tmp))

#"coreclr.dll"+004A82C8