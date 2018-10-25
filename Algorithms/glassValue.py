def hourglassSum(arr):
    leng = len(arr)-1
    sum = 0
    n = 0
    for x in range(1,leng):
        for y in range(1,leng):
            groupsum = arr[x][y]+arr[x-1][y-1]+arr[x-1][y]+arr[x-1][y+1]+arr[x+1][y+1] + arr[x+1][y-1]+arr[x+1][y]
            if n == 0:
                sum = groupsum
            elif groupsum > sum:
                sum = groupsum
            n +=1

    return sum

if __name__=='__main__':
    test = [[-1,-2,-3,-4],[-1,-2,-3,-4],[-1,-2,-3,-4],[-1,-2,-3,-4]]
    print(hourglassSum(test))