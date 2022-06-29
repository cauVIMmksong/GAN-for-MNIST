import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from typing import List, Tuple

def plot_values(
    train_values: List[float], 
    val_values: List[float],
    title: str
) -> None:
    x = list(range(1, len(train_values)+1))
    plt.figure()
    plt.title(title)
    plt.plot(x, train_values, marker='o', label='Training')
    plt.plot(x, val_values, marker='x', label='Validataion')
    plt.xlabel('Epoch')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.legend()
    plt.savefig(title + '.png')