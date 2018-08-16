import ctypes
import numpy as np

hllDll = ctypes.windll.LoadLibrary("python_dll.dll")

test_print_console = hllDll.test_print_console # need the extern!!
# test_print_console.argtypes = ()
# test_print_console.restype = ctypes.c_int
print(test_print_console())

test_vector_add = hllDll.test_vector_add # need the extern!!
# test_vector_add.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int,)
# test_vector_add.restype = ctypes.c_int

length = 10
a = np.ones((length, 1), dtype=np.float32)
b = np.ones((length, 1), dtype=np.float32) * 2
c = np.zeros((length, 1), dtype=np.float32)

print(
	test_vector_add(
		ctypes.c_void_p(c.ctypes.data), 
		ctypes.c_void_p(a.ctypes.data), 
		ctypes.c_void_p(b.ctypes.data),
		ctypes.c_int(length))
	)

print(a)
print(b)
print(c)