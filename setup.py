#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os
import shutil

dist_path = os.path.join(os.path.dirname(__file__), 'dist')
if os.path.exists(dist_path):
    shutil.rmtree(dist_path)
setup(
    name='qtpyeditor',
    version='0.2.12',
    description=(
            'An simple editor in pure Python-Qt binding for both PyQt5 and PySide2 to sove the problem that PySide2 lacks QScintilla bindings.\n' +
            'This package is developed by PyMiner developing team.'
    ),
    author='hzy15610046011',
    author_email='1295752786@qq.com',
    license='LGPL',
    packages=find_packages(),
    platforms=["all"],
    url='https://gitee.com/hzy15610046011/pyminer_comm',
    install_requires=[
        'qtpy',
        'jedi'
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ], include_package_data=True
)
