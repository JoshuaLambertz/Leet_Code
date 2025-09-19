nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]

def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
            nums1[:n] = nums2[:n]
    
    print(nums1)
    return

merge(nums1, len(nums1)-len(nums2), nums2, len(nums2))