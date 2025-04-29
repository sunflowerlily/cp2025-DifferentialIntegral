import numpy as np

def trapezoid(f, a, b, N):
    h = (b - a) / N
    s = 0.5 * f(a) + 0.5 * f(b)
    for k in range(1, N):
        s += f(a + k * h)
    return h * s

def adaptive_trapezoidal(f, a, b, tol=1e-5, n=5, N=10):
    area = trapezoid(f, a, b, N)
    check = trapezoid(f, a, b, n)
    if abs(area - check) > tol:
        m = (b + a) / 2.0
        area = adaptive_trapezoidal(f, a, m, tol) + adaptive_trapezoidal(f, m, b, tol)
    return area

def integrand(theta, theta0_rad):
    return 1 / np.sqrt(1 - (np.sin(theta0_rad / 2)) ** 2 * (np.sin(theta)) ** 2)

def compute_period_ratio(theta0_deg, tol=1e-5):
    theta0_rad = np.deg2rad(theta0_deg)
    f = lambda theta: integrand(theta, theta0_rad)
    integral_result = adaptive_trapezoidal(f, 0, np.pi / 2, tol=tol)
    return (2 / np.pi) * integral_result

def find_critical_angle(target_relative_error=0.05, tol=1e-5):
    left, right = 0.0, 90.0
    while right - left > tol:
        mid = (left + right) / 2
        ratio = compute_period_ratio(mid, tol=tol)
        rel_error = ratio - 1.0
        if rel_error < target_relative_error:
            left = mid
        else:
            right = mid
    return (left + right) / 2

def main():
    angles_deg = [1, 3, 5, 7, 10, 15, 20, 25]
    print("计算不同角度下单摆周期比值 T/T0：")
    for angle in angles_deg:
        ratio = compute_period_ratio(angle)
        print(f"θ0 = {angle}°, T/T0 = {ratio:.5f}")

    critical_angle = find_critical_angle()
    print("\n周期相对误差达到5%时的临界角度为：")
    print(f"θ0 ≈ {critical_angle:.5f}°")

if __name__ == "__main__":
    main()