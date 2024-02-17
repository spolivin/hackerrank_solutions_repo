if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(list(arr))
    max_val = max(arr)
    final = 0
    for item in arr:
        if item < max_val:
            final = item
    print(final)
