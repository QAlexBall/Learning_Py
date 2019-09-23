cmake_minimum_required(VERSION 3.14)
project(use_cython C)

set(CMAKE_C_STANDARD 99)
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})


add_executable(use_cython main.c src/cpython_module/get_index.h src/cpython_module/get_index.h)
target_include_directories(use_cython PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_libraries(use_cython PRIVATE ${PYTHON_LIBRARIES})