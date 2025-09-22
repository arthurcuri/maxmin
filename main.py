def max_min_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    mid = (left + right) // 2
    
    min_left, max_left = max_min_select(arr, left, mid)
    min_right, max_right = max_min_select(arr, mid + 1, right)
    
    return min(min_left, min_right), max(max_left, max_right)


if __name__ == "__main__":
    seq = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    minimo, maximo = max_min_select(seq, 0, len(seq) - 1)
    print("Min:", minimo)
    print("Max:", maximo)