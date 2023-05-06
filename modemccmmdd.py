#!c:\users\mpaka\appdata\local\programs\python\python38\python.exe
from __future__ import print_function
import sys
from modemcmd import modemcmd, ModemcmdTimeoutException


def main(argv):
    if len(argv) < 3:
        print('Usage: %s MODEM_DEVICE COMMAND [TIMEOUT]' % argv[0])
        exit(1)

    try:
        # argv[2] = str.encode(argv[2])
        print(modemcmd(*argv[1:]))
        exit(0)
    except ModemcmdTimeoutException as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main(sys.argv)
