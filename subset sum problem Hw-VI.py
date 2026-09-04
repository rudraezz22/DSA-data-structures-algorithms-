def subset_sum(arr, target, index, subset):
    if target == 0:
        print("Subset:", subset)
        return True

    if index == len(arr):
        return False

    if arr[index] <= target:
        subset.append(arr[index])

        if subset_sum(arr, target - arr[index], index + 1, subset):
            return True

        subset.pop()

    if subset_sum(arr, target, index + 1, subset):
        return True

    return False


arr = [3, 34, 4, 12, 5, 2]
target = 9

if not subset_sum(arr, target, 0, []):
    print("No subset found")