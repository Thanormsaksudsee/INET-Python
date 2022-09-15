#2.ให้เขียนโปรแกรมรับจำนวนเต็ม N และ K จากนั้นพิมพ์เลขตั้งแต่ 1 ถึง N ที่ K หารลงตัว


N = int(input('Enter N:'))
K = int(input('Enter K'))

for i in range(1,N):
    if i % K == 0 :
        print(i)
    