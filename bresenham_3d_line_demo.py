from bresenham_3d_line import bresenham_3d_line


def main(argv):
    result = bresenham_3d_line(5, 5, 5, 20, 20, 20)
    for point in result:
        print('Point {},{},{}'.format(point[0], point[1], point[2]))


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
