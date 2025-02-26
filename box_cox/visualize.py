import matplotlib.pyplot as plt

def data_plot(data, lambdas, simple=True, sub=False, hist=False):
    if simple:
        plt.figure(figsize=(10,6))
        plt.plot(data.index, data)
        plt.title('Volume data')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.show()
    
    elif sub:
        fig, axes = plt.subplots(3, 5, figsize=(15, 9))
        axes = axes.flatten()

        for i, data in enumerate(data):
            ax = axes[i]
            ax.hist(data, bins=30, color='green', alpha=0.7)
            ax.set_title(f"λ = {lambdas[i]:.1f}")

        # Remove empty subplots if lambdas don't fill all 15 slots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()

    elif hist:
        plt.figure(figsize=(10,6))
        plt.hist(data, bins=100, color='green', alpha=0.7)
        plt.title('Volume data')
        plt.xlabel('Volume')
        plt.ylabel('Frequency')
        plt.show()
    
    
    