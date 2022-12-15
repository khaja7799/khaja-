def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3
nums = [19,19,15,5,5,5,1,2]
print("Original list:")
print(nums)
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))



a=[19,19,15,5,5,5,1,2]
b=a.count(5)
c=a.__len__()
if (b<=3 and c<=8):
    print(True)
else:
    print(False)


a="Twinkle, twinkle, little star,\n How I wonder what you are!\n Up above the world so high,\n Like a diamond in the sky."
print(a)


import datetime
a=datetime.datetime.now()
print(a)


import py_compile
a=py_compile
print(a)


 