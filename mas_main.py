import random
import numpy as np
import matplotlib.pyplot as plt
def predict(inputs, weights):
    z = weights[0] + inputs[0] * weights[1] + inputs[1] * weights[2] + inputs[2] * weights[3]
    return 1 if z >= 0 else 0
def train(data, eta):
    weights = [random.uniform(-0.1, 0.1) for _ in range(4)]
    acc_history = []
    epoch = 0
    while True:
        errors = 0
        for inputs, target in data:
            y = predict(inputs, weights)
            diff = target - y
            if diff != 0:
                errors += 1
                weights[0] += eta * diff  # w0 (x0 всегда 1)
                weights[1] += eta * diff * inputs[0]
                weights[2] += eta * diff * inputs[1]
                weights[3] += eta * diff * inputs[2]
        accuracy = 1 - (errors / len(data))
        acc_history.append(accuracy)
        epoch += 1
        if errors == 0:
            break
    return weights, acc_history
if __name__ == "__main__":
    dataset = [
        ([0, 0, 0], 1), ([0, 0, 1], 1), ([0, 1, 0], 1), ([0, 1, 1], 1),
        ([1, 0, 0], 1), ([1, 0, 1], 1), ([1, 1, 0], 1), ([1, 1, 1], 0)
    ]
    w, history = train(dataset, eta=0.7)
    print(f"Обучение завершено за {len(history)} эпох.")
    print(f"Уравнение плоскости: {w[0]:.2f} + {w[1]:.2f}*x1 + {w[2]:.2f}*x2 + {w[3]:.2f}*x3 = 0")
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history, marker='o')
    plt.title("Точность обучения")
    plt.xlabel("Эпоха")
    plt.ylabel("Точность")
    plt.grid(True)
    ax = plt.subplot(1, 2, 2, projection='3d')
    for inp, target in dataset:
        color = 'blue' if target == 1 else 'red'
        ax.scatter(inp[0], inp[1], inp[2], c=color, s=100)
    x1_vals = np.array([0, 1])
    x2_vals = np.array([0, 1])
    X1, X2 = np.meshgrid(x1_vals, x2_vals)
    X3 = -(w[0] + w[1] * X1 + w[2] * X2) / w[3]
    ax.plot_surface(X1, X2, X3, alpha=0.5, color='gray')
    ax.set_title("Разделяющая плоскость")
    ax.set_xlabel('X1');
    ax.set_ylabel('X2');
    ax.set_zlabel('X3')
    plt.show()
