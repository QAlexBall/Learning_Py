cmake_minimum_required(VERSION 3.14)
project(c_extensions C)

set(CMAKE_C_STANDARD 99)
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})


add_executable(c_extensions main.c)
target_include_directories(c_extensions PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_libraries(c_extensions PRIVATE ${PYTHON_LIBRARIES})
