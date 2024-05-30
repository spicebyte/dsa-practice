def findDuplicate(nums) :
  slow = nums[0]
  fast = nums[nums[0]]
  while(slow != fast):
    slow = nums[slow]
    fast = nums[nums[fast]]
  
  last = 0
  while(nums[last] != nums[slow]):
    last = nums[last]
    slow = nums[slow]
    
  return nums[slow]
