#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Hack to use specified compiler
os.environ['CC'] = 'clang++'
os.environ['OPT'] = ''

extensions = [
    Extension(
        '*',
        ['owl/*.pyx', 'owl/minerva_utils.cpp'],
        language='c++',
        include_dirs=[
            'minerva',
            'third_party',
            '/usr/local/cuda/include',
            '/home/yutian/cpp/cudnn-6.5-linux-x64-v2'
        ],
        extra_compile_args=[
            '-std=c++11',
            '-Wall',
            '-O2',
            '-g'
        ],
        define_macros=[
            ('HAS_CUDA', None),
        ],
        libraries=[
            'minerva'
        ],
        library_dirs=[
            'release/lib'
        ],
        runtime_library_dirs=[
            'release/lib'
        ],
    )
]

setup(
    name='owl',
    package_dir={'': 'owl'},
    ext_modules=cythonize(extensions)
)
