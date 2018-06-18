import ctypes

hllDll = ctypes.WinDLL ("python_dll.dll")


test_print_console = hllDll['test_print_console'] # need the extern!!
test_print_console.argtypes = ()
test_print_console.restype = None
test_print_console()

mydll = ctypes.cdll.LoadLibrary("python_dll.dll")
print(mydll)

mydll.test_print_console()