import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def simulated_annealing(func, x0, T, alpha, n_iterations):
    best = x0
    current = x0
    best_cost = func(best)
    cost_history = []

    for i in range(n_iterations):
        # Generate a neighbor by random perturbation
        candidate = current + np.random.normal(0, .5)
        candidate_cost = func(candidate)
        current_cost = func(current)
        delta_cost = candidate_cost - current_cost

        # Accept candidate if it's better, or with a probability if it's worse
        if delta_cost < 0 or np.random.rand() < np.exp(-delta_cost / T):
            current = candidate
            current_cost = candidate_cost

        # Record the best solution found so far
        if current_cost < best_cost:
            best = current
            best_cost = current_cost

        cost_history.append(current)
        T *= alpha  # Cooling schedule

    return best, best_cost, cost_history

def objective(x):
    # Simple quadratic function; the minimum is at x = [0, 0]
    return .1*x**4 + .2*x**3 - x**2 - x*np.cos(x**2)

np.random.seed(42)
def gradient_descent(func, grad, x0, learning_rate, n_iterations):
    x = x0
    history = [x]
    for i in range(n_iterations):
        x = x - learning_rate * grad(x)
        history.append(x)
    best = x
    best_cost = func(x)
    return best, best_cost, history

def grad_objective(x):
    # Derivative of: 0.1*x^4 + 0.2*x^3 - x^2 - x*cos(x^2)
    # f'(x) = 0.4*x^3 + 0.6*x^2 - 2*x - cos(x^2) + 2*x**2*sin(x**2)
    return (objective(x+.001) - objective(x-.001)) / (.002)

x0 = 4
learning_rate = 0.001
iterations = 1000

best_solution, best_value, g_history = gradient_descent(objective, grad_objective, x0, learning_rate, iterations)
T_initial = 1.0
cooling_rate = 0.999
iterations = 1000

best_solution, best_value, history = simulated_annealing(
    objective, x0, T_initial, cooling_rate, iterations
)

fig, ax = plt.subplots()
x_n = np.linspace(-5, 5, 1000)
ax.set_title("Simulated Annealing vs Gradient Descent")

sascat = ax.scatter(np.array([x0]), np.array([objective(x0)]), c="r", s=20, label=f'Current Point (Simulated Annealing, T = {T_initial})')
gscat = ax.scatter(np.array([x0]), np.array([objective(x0)]), c="black", s=20, label=f'Current Point (Gradient)')
line2 = ax.plot(x_n, objective(x_n), label=f'Cost Function')[0]
ax.set(xlim=[-5, 5], ylim=[-20, 20], xlabel='X', ylabel='Cost')
ax.legend()

def update(frame):
    # for each frame, update the data stored on each artist.
    x = history[frame]
    y = objective(x)
    x2 = g_history[frame]
    y2 = objective(x2)
    # update the scatter plot:
    data = np.stack([x, y]).T
    sascat.set_offsets(data)
    sascat.set_label(f'Current Point (Simulated Annealing, T = {round(T_initial * cooling_rate**frame, 3)})')
    gscat.set_offsets(np.stack([x2,y2]).T)

    legend = plt.legend()
    return (sascat, gscat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=10)
plt.show()