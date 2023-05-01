from pymem import *
from pymem.process import *


pm = pymem.Pymem("Stardew Valley.exe")

gameModule = module_from_name(
    pm.process_handle, "System.Private.Xml.dll").lpBaseOfDll


def GetPtrAddr(base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_longlong(int(addr + i))
    return addr + offsets[-1]

# read_bytes(self, address, length)


tmp = GetPtrAddr(gameModule + 0x00022D48,
                 [0x0, 0x20, 0x60, 0x88, 0xC0, 0x60, 0x1C])
print(hex(tmp))

while True:
    pm.write_int(tmp, 54000)
    print(pm.read_int(tmp))




# "System.Private.Xml.dll"+00022D481
#WH