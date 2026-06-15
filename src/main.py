# 문제 1.
#
# 서보모터 각도를 PWM pulse width 값으로 변환하세요.
#
# angle 값은 0 ~ 180 범위입니다.
#
# 0도   -> 500
# 90도  -> 1500
# 180도 -> 2500
#
# 선형 비례 관계로 계산하세요.
def servo_angle_to_pulse_width(angle):
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    
    pulse = 500 + (angle*2000.0) / 180.0
    return int(round(pulse))
#    raise NotImplementedError


# 문제 2.
#
# 부저로 출력할 음계 이름을 주파수 값으로 변환하세요.
#
# C4, D4, E4, F4, G4, A4, B4, C5 음계를 지원해야 합니다.
def note_to_frequency(note):
    NOTE = {
    "C4": 262,  # 도
    "D4": 294,  # 레
    "E4": 330,  # 미
    "F4": 349,  # 파
    "G4": 392,  # 솔
    "A4": 440,  # 라
    "B4": 494,  # 시
    "C5": 523,  # 높은 도
    "REST": 0,  # 쉼표
    }

    key = note.strip().upper()
    return NOTE.get(key,0)

#    raise NotImplementedError


# 문제 3.
#
# 여러 개의 음계를 부저 주파수 리스트로 변환하세요.
#
# notes 인자는 음계 이름이 들어있는 리스트입니다.
# 각 음계를 주파수 값으로 변환한 리스트를 반환하세요.
def melody_to_frequencies(notes):
    
    NOTE = {
    "C4": 262,  # 도
    "D4": 294,  # 레
    "E4": 330,  # 미
    "F4": 349,  # 파
    "G4": 392,  # 솔
    "A4": 440,  # 라
    "B4": 494,  # 시
    "C5": 523,  # 높은 도
    "REST": 0,  # 쉼표
    }
    
    if notes is None:
        return []
    
    try:
        iterator = iter(notes)
    except TypeError:
        return []


    freq = []
    for n in iterator:
        key = n.strip().upper()
        freq.append(NOTE.get(key,0))
    return freq
#    raise NotImplementedError


# 문제 4.
#
# 로봇 이동 방향 문자열을 ROS2 Twist 값으로 변환하세요.
#
# direction 인자는 이동 방향 문자열입니다.
#
# 지원해야 하는 방향은 아래와 같습니다.
#
# - forward
# - backward
# - left
# - right
# - stop
#
# 반환값은 (linear_x, angular_z) 튜플입니다.
def direction_to_twist(direction):

    d= direction.strip().lower()

    if d == "forward":
        return (1.0, 0.0)
    elif d == "backward":
        return (-1.0, 0.0)
    elif d == "left":
        return (0.0, 1.0)
    elif d == "right":
        return (0.0, -1.0)
    else:
        return (0.0, 0.0)
    
    


# 문제 5.
#
# ROS2 Twist 값을 좌우 바퀴 속도로 변환하세요.
#
# linear_x는 전진/후진 속도입니다.
# angular_z는 회전 속도입니다.
#
# 좌우 바퀴 속도는 -100 ~ 100 범위로 제한되어야 합니다.
#
# 반환값은 (left_speed, right_speed) 튜플입니다.
def twist_to_wheel_speed(linear_x, angular_z):
    try:
        lx = float(linear_x)
        az = float(angular_z)
    except(TypeError,ValueError):
        return (0,0)

    left_raw = lx-az
    right_raw = lx +az
    
    left_scaled = left_raw * 100.0
    right_scaled = right_raw * 100.0

    def clamp(v, lo=-100.0, hi=100.0):
        if v <lo:
            return lo
        if v>hi:
            return hi
        return v
    
    left_clamped = clamp(left_scaled)
    right_clamped = clamp(right_scaled)

    return(int(round(left_clamped)),int(round(right_clamped)))
#    raise NotImplementedError
