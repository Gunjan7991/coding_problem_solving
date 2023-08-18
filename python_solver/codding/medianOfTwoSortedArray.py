def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        n,m=0,0
        new_list  = []
        counter, counted = 0, len(nums1)
        counted += len(nums2)
        while n < len(nums1) or m <len(nums2):
            counter += 1
            if  m >= len(nums2):
                new_list.append(nums1[n])
                n +=1
            elif n>= len(nums1):
                new_list.append(nums2[m])
                m +=1
            else:
                if nums1[n] > nums2[m]:
                    new_list.append(nums2[m])
                    m +=1
                elif nums1[n] <= nums2[m]:
                    new_list.append(nums1[n])
                    n +=1
            if counter >= counted:
                 break
        med = len(new_list)-1
        if med % 2 == 0:
            med  = float(med/2)
            return float(new_list[int(med)])
        else:
            med  = float(med/2)   
            return float((new_list[int(med-0.5)]+new_list[int(med+0.5)])/2)
        

def findMedianSortedArraysFast(nums1: list[int], nums2: list[int]) -> float:
    newList = sorted(nums1 + nums2)
    l = len(newList)
    if l % 2 == 0:
        idx = l // 2
        return (newList[idx - 1] + newList[idx]) / 2
    return newList[l // 2]   

if __name__ == "__main__":
    print(findMedianSortedArrays([1,2], [3,4]))