#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 == 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    if len(sys.argv) - 1 > 0:
        count = 0
        for x in sys.argv[1:]:
            count += 1
            print("{:d}: {:s}".format(count, x))
