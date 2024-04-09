def centered_average(nums):
    return round( (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2))
    
print(centered_average([-10,-4,-2,-4,0]))