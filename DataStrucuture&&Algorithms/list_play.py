def reference_issus():
    refereced = [1,2,3,4]
    ob1 = [refereced, 5, 6]
    ob2 = [refereced, '?', 's']
    for t in ob2:
        print(t, end=' ')

    ob1[0].append('new')
    for t in ob2:
        print(t, end=' ')

if __name__=='__main__':
    reference_issus()