def array123(nums):
'''
If set of nums, regardless of what orders, is equal to the set with the
sequence of 1, 2, and 3  return True. if that fails then return False.
'''
  if set(nums) == set([1,2,3]):
    return True
  else:
    return False
  
