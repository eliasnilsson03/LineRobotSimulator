class PID:
  def __init__(self, Kp, Ki, Kd, setpoint):
    self.Kp = Kp
    self.Ki = Ki
    self.Kd = Kd
    self.setpoint = setpoint
    self.e_prev = 0
    self.integral = 0

  def reset(self):
    self.e_prev = 0.0
    self.integral = 0.0

  def set_setpoint(self, new_setpoint):
    self.setpoint = new_setpoint

  def compute(self, process_variable, dt):
    e = self.setpoint - process_variable
    P_out = self.Kp * e
    self.integral += e * dt
    self.integral = max(min(self.integral, 100), -100) # anti-windup
    I_out = self.Ki * self.integral
    derivative = (e - self.e_prev) / dt if dt > 0 else 0.0
    D_out = self.Kd * derivative
    self.e_prev = e
    u = P_out + I_out + D_out
    return u
