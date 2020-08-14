
def linearSearch(a,key):
    """시퀀스 a 에서 key와 값이 같은 원소를 선형 검색"""    
    i=0

    while True:
        if i==len(a):
            return -1
        if a[i]==key:
            return a[i]
        i+=1

if __name__=='__main__':
    num=int(input('원소 수를 입력하세요'))
    x=[None]*num

    for i in range(num):
        x[i]=int (input(f'x[{i}]: '))
    ky=int(input ('검색할 값을 입력하세요:'))

    idx=linearSearch(x,ky)

    if idx==-1:
        print ('원소가 존재하지 않음')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')


