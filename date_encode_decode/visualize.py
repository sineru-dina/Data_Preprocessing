import matplotlib.pyplot as plt

def plot_encoded_dates(encoded_dates):
    # Extract sine and cosine values
    sine_values = [encoded[0] for encoded in encoded_dates]
    cosine_values = [encoded[1] for encoded in encoded_dates]

    # Create a scatter plot
    plt.scatter(sine_values, cosine_values, color='green', label='Encoded Date')

    # Optionally, you can also connect the points to visualize the circular pattern
    plt.plot(sine_values, cosine_values, color='black', linestyle='--', alpha=0.5)

    # Add labels and title
    plt.xlabel('Sine')
    plt.ylabel('Cosine')
    plt.title('Encoded Date Plot (Sine and Cosine)')

    # Add a grid
    plt.grid(True)

    # Show the plot
    plt.legend()
    plt.show()