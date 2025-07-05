def maxOverKernel(num_list, k):
    if len(num_list) == 0 or k <= 0:
        return []        
    if k > len(num_list):
        return max(num_list)
    
    max_list = []
    
    for i in range(len(num_list) - k + 1):
        max_list.append(max(num_list[i:i + k]))
        
    return max_list


if __name__ == "__main__":
    