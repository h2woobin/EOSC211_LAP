import math

def grav_acc(s_x, s_y, Mp):
    """""
    Calculates the gravitational acceleration acting on the spacecraft using its position and the mass of the planet. 
    (Applies Newton's Law of Universal Gravitation and Newton's Second Law of Motion.)

    Inputs:
        - s_x (float): x components of a single position vector in m.
        - s_y (float): y components of a single position vector in m.
        - Mp (float): the mass of the planet in kg.

    Outputs:
        tuple: (a_x, a_y)
            - a_x: x components of instantaneous spacecraft acceleration in m s^{-2}.
            - a_y: y components of instantaneous spacecraft acceleration in m s^{-2}.
    """""
    # 우주선과 행성간의 거리 계산 
    s = math.sqrt(s_x**2 + s_y**2)

    # 중력 상수 
    gravity = (6.67e-11)

    # 가속도의 크기               
    acceleration = gravity * Mp / s**2

    # 가속도의 방향 성분
    sinB = -s_x/s
    cosB = -s_y/s

    # 가속도 성분 계산 
    a_x = acceleration * sinB
    a_y = acceleration * cosB

    return a_x,a_y