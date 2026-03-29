#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: packmemo.py
from evernotecontroller import EvernoteController
from memo import Memo

MEMO_NAME = '备忘录'
MEMO_DIR = 'Memo'
# MEMO_STORAGE_DIR = 'S-Memo'


def f(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except:
        pass


m = Memo()
e = EvernoteController()
f(e.create_notebook, MEMO_DIR)
# f(e.create_notebook, MEMO_STORAGE_DIR)
f(e.move_note, MEMO_DIR + '/' + MEMO_NAME, MEMO_DIR + '/' + MEMO_NAME)
e.create_note(MEMO_NAME, m.raw_memo(), MEMO_DIR)
