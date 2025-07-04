# Directly computes the maximum value over a sliding window (kernel) of size k
def maxOverKernel(num_list, k):
    if len(num_list) == 0 or k <= 0:
        return []
    if k > len(num_list):
        return []
    
    max_list = []
    for i in range(len(num_list) - k + 1):
        max_value = max(num_list[i:i+k])
        max_list.append(max_value)
    
    return max_list


# With a sublist that is always full (i.e., the size of the kernel is always k)
def maxOverKernelFull(num_list, k):
    if len(num_list) == 0 or k <= 0:
        return []
    if k > len(num_list):
        return []
    
    max_list = []
    tmp_list = []
    for element in num_list:
        tmp_list.append(element)
        if len(tmp_list) == k:
            max_value = max(tmp_list)
            max_list.append(max_value)
            tmp_list.pop(0)
    
    return max_list

# Using slicing to compute the maximum over a sliding window
def maxOverKernelSlice(num_list, k):
    if len(num_list) == 0 or k <= 0:
        return []
    if k > len(num_list):
        return []
    
    max_list = []
    sub_list = []
    start_index = list(range(0, len(num_list) - k + 1))
    end_index = list(range(k, len(num_list) + 1))
    
    for start_index, end_index in zip(start_index, end_index):
        sub_list = num_list[start_index:end_index]
        max_value = max(sub_list)
        max_list.append(max_value)
    
    return max_list

# Example usage:
if __name__ == "__main__":
    nums = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    
    k = 3
    result = maxOverKernelSlice(nums, k)
    print(f"Max over kernel of size {k}: {result}")
    