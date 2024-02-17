n1_inp = int(input())
n1_lst = set(map(int, input().split()))
n2_inp = int(input())
n2_lst = set(map(int, input().split()))

print(len(n1_lst.difference(n2_lst)))
