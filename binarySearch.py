def binarySearch(seq,key):
    pl=0
    pr=len(seq)-1
    

    while True:
        pc=pl+pr//2
        if seq[pc]==key:
            return pc
        elif seq[pc]<key:
            pr=pc-1
        else:
             pl=pc+1

        if pl > pr:
            break
    return -1

if __name__=='__main__':
    num=int (input('원소 수를 입력하세요:'))
    x=[None]*num
    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0]=int (input('x[0]:'))

    for i in range(1,num):
        while True:
            x[i]=int (input(f'x[{i}]:'))
            if x[i]>x[i-1]:
                break
    
    ky=int (input('검색할 값을 입력하세요.:'))

    idx=binarySearch(x,ky)

    if idx==-1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

