# A Bresenham 3D line algorithm
# Adapted from https://gist.github.com/yamamushi/5823518


def bresenham_3d_line(x1, y1, z1, x2, y2, z2):
    point_list = []

    point = list()

    point.append(x1)
    point.append(y1)
    point.append(z1)
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    if dx < 0:
        x_inc = -1
    else:
        x_inc = 1
    abs_dx = abs(dx)

    if dy < 0:
        y_inc = -1
    else:
        y_inc = 1
    m = abs(dy)

    if dz < 0:
        z_inc = -1
    else:
        z_inc = 1
    n = abs(dz)

    dx2 = abs_dx * 2
    dy2 = m * 2
    dz2 = n * 2

    if (abs_dx >= m) and (abs_dx >= n):
        err_1 = dy2 - abs_dx
        err_2 = dz2 - abs_dx
        for i in range(0, abs_dx):
            new_point = [point[0], point[1], point[2]]
            point_list.append(new_point)
            # print 'Point {},{},{}'.format(point[0], point[1], point[2])
            if err_1 > 0:
                point[1] += y_inc
                err_1 -= dx2

            if err_2 > 0:
                point[2] += z_inc
                err_2 -= dx2

            err_1 += dy2
            err_2 += dz2
            point[0] += x_inc

    elif (m >= abs_dx) and (m >= n):
        err_1 = dx2 - m
        err_2 = dz2 - m
        for i in range(0, m):
            new_point = [point[0], point[1], point[2]]
            point_list.append(new_point)
            # print 'Point {},{},{}'.format(point[0], point[1], point[2])
            if err_1 > 0:
                point[0] += x_inc
                err_1 -= dy2

            if err_2 > 0:
                point[2] += z_inc
                err_2 -= dy2

            err_1 += dx2
            err_2 += dz2
            point[1] += y_inc

    else:
        err_1 = dy2 - n
        err_2 = dx2 - n
        for i in range(0, n):
            new_point = [point[0], point[1], point[2]]
            point_list.append(new_point)
            # print 'Point {},{},{}'.format(point[0], point[1], point[2])
            if err_1 > 0:
                point[1] += y_inc
                err_1 -= dz2

            if err_2 > 0:
                point[0] += x_inc
                err_2 -= dz2

            err_1 += dy2
            err_2 += dx2
            point[2] += z_inc

    new_point = [point[0], point[1], point[2]]
    point_list.append(new_point)
    # print 'Point {},{},{}'.format(point[0], point[1], point[2])
    return point_list
