import numpy as np
import decimal
import math


# 삼각형의 무게중심
def get_triangle_gravity(arr: np.ndarray):
    return np.array([np.sum(arr[:0])/3, np.sum(arr[:1])/3])

# 사각형의 무게중심
# 점선택 알고리즘 -> 무게중심 두 번 구함
def get_square_gravity(square_arr: np.ndarray):
    points_arr = sort_unclockwise(square_arr)
    print("Sorted:", points_arr)

    x_1, y_1 = get_triangle_gravity(np.delete(points_arr, 3, axis=0))
    x_2, y_2 = get_triangle_gravity(np.delete(points_arr, 1, axis=0))
    # 두 점 지나는 직선(일차방정식)
    solution_1 = np.array([y_2 - y_1, x_1 - x_2, y_2 * x_1 - x_2 * y_1])
    print(f"Sol1: {solution_1[0]} X {solution_1[1]} Y = {solution_1[2]}")


    x_3, y_3 = get_triangle_gravity(np.delete(points_arr, 2, axis=0))
    x_4, y_4 = get_triangle_gravity(np.delete(points_arr, 0, axis=0))

    solution_2 = np.array([y_4 - y_3, x_3 - x_4, x_3 * y_4 - x_4 * y_3])
    print(f"Sol1: {solution_2[0]} X {solution_2[1]} Y = {solution_2[2]}")

    return solve_equation(solution_1, solution_2)


#반시계방향으로 정렬 -> 삼각 분할 위해
def sort_unclockwise(arr: np.ndarray):
    center_x, center_y = 0.0, 0.0
    for point in arr:
        center_x += point[0]
        center_y += point[1]
    center = np.array([center_x / arr.size * 2, center_y / arr.size * 2])

    key_arr = np.array([])
    sorted_arr = np.array([])

    for point in arr:
        key = math.atan2(point[1] - center[1], point[0] - center[0])
        key_arr = np.append(key_arr, key)
    index_arr = np.argsort(key_arr, axis=0)

    for i in range(0, index_arr.size):
        sorted_arr = np.append(sorted_arr, arr[np.where(index_arr == i)])

    return sorted_arr.reshape((int(arr.size/2), 2))


# 안 써도 돌아갈 거 같음
'''
# 거리^2 행렬
# 행렬의 첫 번째 점을 기준으로 거리 구함
def get_distance(arr: np.ndarray):
    dist_array = np.array([])
    for nth_arr in arr:
        # (x-x_n)^2 + (y-y_n)^2
        dist_array = np.append(dist_array, np.sum((nth_arr - arr[0])**2))

    print("Distance:", dist_array[1:])
    return dist_array[1:]
'''

'''
일차방정식의 근 리턴함
[   [a b c]             ax + by = c
    [d e f]    ] =>     dx + ey = f
'''
# 값 0일 때 예외처리 필요
def solve_equation(sol_1: np.ndarray, sol_2: np.ndarray):
    sol_1 -= sol_2 * (sol_1[0] / sol_2[0])
    sol_2 -= sol_1 * (sol_2[1] / sol_1[1])

    return np.array([sol_2[2] / sol_2[0], sol_1[2] / sol_1[1]])


if __name__ == "__main__":
    pass