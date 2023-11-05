import decimal

import numpy as np
import math


# 삼각형의 무게중심
def get_triangle_gravity(arr: np.ndarray):
    return np.sum(arr[:, 0])/3, np.sum(arr[:, 1])/3


def get_polygon_gravity(nth_arr: np.ndarray):
    if nth_arr.shape[0] == 3:
        return get_triangle_gravity(nth_arr)
    else:
        # points_arr = sort_unclockwise(nth_arr)
        points_arr = nth_arr

        x_1, y_1 = get_triangle_gravity(points_arr[0:3])
        x_2, y_2 = get_polygon_gravity(np.delete(points_arr, 1, axis=0))
        # 두 점 지나는 직선(일차방정식)
        solution_1 = np.array([y_2 - y_1, x_1 - x_2, y_2 * x_1 - x_2 * y_1])

        x_3, y_3 = get_triangle_gravity(points_arr[-3:])
        x_4, y_4 = get_polygon_gravity(np.delete(points_arr, -2, axis=0))

        solution_2 = np.array([y_4 - y_3, x_3 - x_4, x_3 * y_4 - x_4 * y_3])

        return solve_equation(solution_1, solution_2)


# 반시계방향으로 정렬 -> 삼각 분할 위해
def sort_unclockwise(arr: np.ndarray):
    center = np.average(arr[:,0]), np.average(arr[:,1])
    key_arr = np.array([])

    for point in arr:
        key = math.atan2(decimal.Decimal(point[1] - center[1]), decimal.Decimal(point[0] - center[0]))
        key_arr = np.append(key_arr, [key, point[0], point[1]])
    key_arr = key_arr.reshape((int(key_arr.size/3), 3))
    key_arr = np.sort(key_arr, axis=0)

    sorted_arr = key_arr[:,1:]

    return sorted_arr


'''
일차방정식의 근 리턴함
[   [a b c]             ax + by = c
    [d e f]    ] =>     dx + ey = f
'''
# 값 0일 때 예외처리 필요
def solve_equation(sol_1: np.ndarray, sol_2: np.ndarray):
    if sol_2[0] != 0:
        sol_1 = sol_1 - sol_2 * (sol_1[0] / sol_2[0])

    if sol_1[1] != 0:
        sol_2 = sol_2 - sol_1 * (sol_2[1] / sol_1[1])

    return np.array([sol_2[2] / sol_2[0], sol_1[2] / sol_1[1]])
