import math

steps_per_degree = 6400.0 / 360.0

def calculate_elbow(x, y, l1, l2):
    d = math.sqrt(x**2 + y**2)

    if d > (l1 + l2) or d < abs(l1 - l2):
        print("Ziel ist außerhalb der Reichweite.")
        return None

    cos_elbow = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    cos_elbow = max(-1.0, min(1.0, cos_elbow))

    angle_elbow = math.acos(cos_elbow)
    steps_elbow = math.degrees(angle_elbow) * steps_per_degree

    return angle_elbow, steps_elbow
    
def calculate_shoulder(x, y, l1, l2, angle_elbow): 
    alpha = math.atan2(y, x)
    beta = math.atan2(l2 * math.sin(angle_elbow), l1 + l2 * math.cos(angle_elbow))

    angle_shoulder = alpha - beta
    steps_shoulder = math.degrees(angle_shoulder) * steps_per_degree

    return angle_shoulder, steps_shoulder