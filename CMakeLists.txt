cmake_minimum_required(VERSION 3.14)
project(Python_Module C)

set(CMAKE_C_STANDARD 99)
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})




add_executable(test_single_c.c test_single_c)