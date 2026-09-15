#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""获取当前时间的小脚本"""

from datetime import datetime
import time


def main() -> None:
    now = datetime.now()
    print("本地时间:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("UTC 时间:", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    print("Unix 时间戳:", int(time.time()))


if __name__ == "__main__":
    main()
