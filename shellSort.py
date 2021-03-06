from typing import MutableSequence

def shell_sort(a:MutableSequence)->None:
    n=len(a)
    h=n//2


    while h<n//9:
        h=h*3+1

    while h>0:
        for i in range(h,n):
            j=i-h
            temp=a[i]
            while j>=0 and temp<a[j]:
                a[j+h]=a[j]
                j-=h
            a[j+h]=temp
        h//=3


if __name__=="__main__":
    print('셸 정렬을 수행합니다.(h*3+1의 수열 사용')
    num=int (input('원소 수를 입력하세요.:'))
    x=[None]*num

    for i in range(num):
        x[i]=int (input(f'x[{i}]:'))

    shell_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}]:{x[i]}')