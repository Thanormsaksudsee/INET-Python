import matplotlib.pyplot as plt

def main():
    leftEdges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    barWidth = 5
    plt.bar(leftEdges,heights,barWidth,color=('g'))
    plt.show()

main()
