import matplotlib.pyplot as plt

def plot_wma(data):
    plt.figure(figsize=(15, 10))
    plt.subplot(3, 1, 1)
    plt.plot(data['price'], label='Original Price', color='black')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')

    plt.subplot(3, 1, 2)
    plt.plot(data['wma'], label='WMA Price', color='green')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')

    plt.subplot(3, 1, 3)
    plt.plot(data['price'], label='Original Price', color='black')
    plt.plot(data['wma'], label='WMA Price', color='green')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')

    plt.title('Weighted Moving Average')
    plt.tight_layout()
    plt.show()