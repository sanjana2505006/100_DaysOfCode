def merged_sort(arr1, arr2):
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    merged = []
    while i < n and j < m :
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < n:
        merged.append(arr1[i])
        i += 1
    while j < m:
        merged.append(arr2[j])
        j += 1
    return merged 

def merge_parity(arr1, arr2):
    merge = merged_sort(arr1, arr2)
    even = [x for x in merge if x % 2 == 0]
    odd = [x for x in merge if x % 2 != 0]
    return even + odd

N, M = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
result = merge_parity(arr1, arr2)
print(*result)