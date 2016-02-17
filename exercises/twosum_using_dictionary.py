def twosum(nums, target):
	check ={};
	j = 0;
	index_list = range(len(nums))
	for i in index_list:
		if target-nums[i] not in check:
			check[nums[i]]=j;
		else:
			return [check[target-nums[i]], i]
		j+=1;
	return "Not Found"