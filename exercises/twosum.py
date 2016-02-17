def twosum(nums, target):
	index_list = range(len(nums));
	for idx in index_list:
		first_num = nums[idx]
		for idx_j in range(idx+1, len(nums)):
			second_num = nums[idx_j]
			total = first_num + second_num
			if total == target:
				return [idx, idx_j]
	return "Not Found";