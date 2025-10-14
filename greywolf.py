import numpy as np

def solar_power(theta):
    power = - (theta - 30)**2 + 100
    return -power  # Minimization

n_wolves = 5
max_iter = 30
lb, ub = 0, 90

positions = lb + (ub - lb) * np.random.rand(n_wolves)

alpha_pos = 0
alpha_score = float('inf')
beta_pos = 0
beta_score = float('inf')
delta_pos = 0
delta_score = float('inf')

for iter in range(max_iter):
    for i in range(n_wolves):
        positions[i] = np.clip(positions[i], lb, ub)
        fitness = solar_power(positions[i])
        if fitness < alpha_score:
            alpha_score = fitness
            alpha_pos = positions[i]
        elif fitness < beta_score:
            beta_score = fitness
            beta_pos = positions[i]
        elif fitness < delta_score:
            delta_score = fitness
            delta_pos = positions[i]

    a = 2 - iter * (2 / max_iter)

    for i in range(n_wolves):
        r1, r2 = np.random.rand(), np.random.rand()
        A1 = 2 * a * r1 - a
        C1 = 2 * r2
        D_alpha = abs(C1 * alpha_pos - positions[i])
        X1 = alpha_pos - A1 * D_alpha

        r1, r2 = np.random.rand(), np.random.rand()
        A2 = 2 * a * r1 - a
        C2 = 2 * r2
        D_beta = abs(C2 * beta_pos - positions[i])
        X2 = beta_pos - A2 * D_beta

        r1, r2 = np.random.rand(), np.random.rand()
        A3 = 2 * a * r1 - a
        C3 = 2 * r2
        D_delta = abs(C3 * delta_pos - positions[i])
        X3 = delta_pos - A3 * D_delta

        positions[i] = (X1 + X2 + X3) / 3

    print(f"Iteration {iter+1:02d}: Best tilt angle = {alpha_pos:.2f} degrees, Max power = {-alpha_score:.2f}")

print("\nFinal Results:")
print(f"Best tilt angle found: {alpha_pos:.2f} degrees")
print(f"Maximum solar power (simulated): {-alpha_score:.2f}")
