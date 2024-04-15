import matplotlib.pyplot as plt

def show(ordered_request, algorithm):
    order = list(range(1, len(ordered_request) + 1))

    # Create a new figure for each plot
    plt.figure()

    # Create the line plot
    plt.plot(ordered_request, order, marker='o', color='b')

    # Set plot labels and title
    plt.xlabel("Request")
    plt.ylabel("Order")
    plt.title(algorithm + str(ordered_request))

    # Display the plot
    plt.show()
