#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pyqr

CONTENT = 'HTTPS://QR.ALIPAY.COM/FKX06972YEJOYZ4PSDWCBA'
IMAGE_PATH = '/tmp/demo.png'


def test_encode():
    import os
    if os.path.exists(IMAGE_PATH):
        os.remove(IMAGE_PATH)
    assert not os.path.exists(IMAGE_PATH)

    pyqr.encode(CONTENT, IMAGE_PATH)
    assert os.path.exists(IMAGE_PATH)


def test_decode():
    assert os.path.exists(IMAGE_PATH)
    _decoded = pyqr.decode(IMAGE_PATH)
    assert _decoded == CONTENT
