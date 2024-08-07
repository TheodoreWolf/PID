import numpy as np

class PID:
    def __init__(self, kp, ki, kd, I = 0.):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0.
        self.Is = [I]

    def update(self, error, dt):
        P = self.kp * error
        self.Is.append(self.Is[-1] + self.ki * error * dt)
        D = self.kd * (error - self.prev_error) / dt
        self.prev_error = error
        return P + self.Is[-1] + D

class System:
    def __init__(self, x0: float, noise=0.1):
        self.x = x0
        self.noise = noise

    def update(self, u):
        self.x = self.x * 0.9 + u + np.random.randn() * self.noise
        return self.x

def run_pid(kp, ki, kd, noise, target=2., dt=0.1, init_state=1., integral=0., prev_error=0.):
    pid = PID(kp, ki, kd, I=integral)
    system = System(init_state, noise=noise)
    error = target - system.x
    u = pid.update(error, dt)
    system.update(u)
    return system.x, pid.Is[-1], pid.prev_error