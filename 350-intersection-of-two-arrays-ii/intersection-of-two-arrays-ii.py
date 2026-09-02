class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set(nums1) & set(nums2))
        c = []
        count = Counter(nums1)
        for i in nums2:
            #print(count)
            if count[i]>0:
                c.append(i)
                #print(c)
                count[i]-=1
                #print(count)
        return c

        