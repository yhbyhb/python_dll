// python_dll.cpp : Defines the exported functions for the DLL application.
//

#include <Windows.h>
#include <iostream>

#include "python_dll.h"


int test_print_console()
{
    std::cout << "test_print_console()" << std::endl;
    return 1;
}