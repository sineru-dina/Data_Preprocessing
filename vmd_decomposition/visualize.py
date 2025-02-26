import matplotlib.pyplot as plt

def plot_vmd(data, k):
    # Plot: Each VMD Mode + Reconstruction
    plt.figure(figsize=(12, 10))

    plt.subplot(k+2, 1, 1)
    plt.plot(data['price'], color='black', label='Original Price')
    plt.legend()

    for i in range(k):
        plt.subplot(k+2, 1, i+2)
        plt.plot(data[f'mode_{i+1}'], label=f'Mode {i+1}')
        plt.legend()

    # Plot Final VMD Reconstruction in the last subplot
    plt.subplot(k+2, 1, k+2)
    plt.plot(data['vmd_recon'], color='red', label='Final VMD Reconstruction', linestyle='dashed')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Plot: Original Price & VMD-Reconstructed Price
    plt.figure(figsize=(12, 6))
    plt.plot(data['price'], color='black', label='Original Price', alpha=0.7)
    plt.plot(data['vmd_recon'], color='red', label='VMD Reconstructed', linestyle='dashed', alpha=0.8)
    plt.legend()
    plt.title("Original Price vs. VMD-Reconstructed Price")
    plt.xlabel("Time Index")
    plt.ylabel("Price")
    plt.show()