# -*- coding: utf-8 -*-
import sys

from resources.libs.common.router import Router

if __name__ == '__main__':
    handle = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    params = sys.argv[2][1:] if len(sys.argv) > 2 else ''
    Router().dispatch(handle, params)
