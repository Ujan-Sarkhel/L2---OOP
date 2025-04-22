class pair_elements:
    def twoSum(self, nums, target):
        lookup={}
        for i,num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
x=int(input("Enter the required sum"))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70),x))

