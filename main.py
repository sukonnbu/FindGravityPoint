import numpy as np

#삼각형의 무게중심
def get_triangle_gravity(arr: np.ndarray) :
    x, y = 0.0, 0.0
    for i,j in arr :
        x += i
        y += j
    x /= 3
    y /= 3

    return np.array([x, y])

#사각형의 무게중심
def get_square_gravity(arr: np.ndarray) :
    x, y = 0.0, 0.0

    x_1, y_1 = get_triangle_gravity()
    x_2, y_2 = get_triangle_gravity()
    # 두 점 지나는 직선(일차방정식)
    solution_1 = np.array([y_2 -y_1, -x_2 +x_1, x_2*y_1 -y_2*x_1])
    print(solution_1)

    return np.array([x, y])

#거리^2 행렬
def get_distance(arr: np.ndarray) :
    dist_array = np.array([])
    for nth_arr in arr :
        # (x-x_n)^2 + (y-y_n)^2
        dist_array = np.append(dist_array, np.sum((nth_arr - arr[0])**2))

    return dist_array
