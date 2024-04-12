import matplotlib.pyplot as plt

def show (ordered_request,algorithm):
    order=[]
    for i in range(len(ordered_request)):
        order.append(i+1)

    # print("plot ", algorithm, ordered_request)
    plt.cla()
    # Create the line plot
    plt.plot(ordered_request, order, marker='o', color='b')

    # Set plot labels and title
    plt.xlabel("Request")
    plt.ylabel("Order")
    plt.title(algorithm)

    # Display the plot
    plt.show()