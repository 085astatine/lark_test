#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import lark


def main() -> None:
    with open('./expr.lark') as file:
        parser = lark.Lark(file.read(), start='expr')
    tree = parser.parse(sys.argv[1])
    print(tree)


if __name__ == '__main__':
    main()
