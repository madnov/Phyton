# uncomplited
def find_uniq(arr):
    uniq = None
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            uniq = arr[i]
    return uniq