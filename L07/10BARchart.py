import matplotlib.pyplot as plt

def main():
    leftEdges = [0, 10, 20, 30, 40]

    heights = [100, 200, 300, 400, 500]
    barWidth = 10

    plt.bar(leftEdges,heights,barWidth,color=('g','r','b','y','g'))
    plt.title

    plt.xlabel('Year')
    plt.ylabel('Sales')

    plt.xticks([0, 1, 2, 3, 4],
                ['2016','2017','2018','2019','2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
                ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    

    plt.show()

main()