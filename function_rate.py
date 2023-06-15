# ttowG

def darcy_rate(perm, area, p_in, p_out, visc, interval, cf = 0.001127):
    rate = (cf*perm*area*(p_in - p_out))/(visc*interval)
    rate = round(rate, 4)
    return rate


