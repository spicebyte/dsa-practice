def search(nums, target):
  l, r = 0, len(nums) - 1
  while(l <= r):
    m = ((r-l)//2) + l
    print(m)
    if(nums[m] >target):
      if(nums[l] > target):
        if(nums[m] > nums[l]):
          l = m + 1
        else:
          r = m - 1
      else:
        r = m -1
    elif(nums[m] < target):
      if(nums[r] < target):
        if(nums[m] > nums[r]):
          l = m + 1
        else:
          r = m - 1
      else:
        l = m + 1
    else:
      return m
  return -1

test = [4,5,6,7,0,1,2]

print(search(test, 0))
