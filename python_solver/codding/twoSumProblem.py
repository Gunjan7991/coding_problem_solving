def twoSum(nums: list[int], target: int) -> list[int]:
        """
        - This is one of the easiest question in leetcode. 
        - We are trying to solve this problem in linear time. 
        Here we are using a map variable which is of type dict.
        We are traversing through the list only once.
        - We are calculating the complement of number->num as we are
        traversing through the list. We are chenking to see if the 
        complement already exist in the map, if so,  we return  the 
        list [position of complment, postion of element] by return
        map[complement], enum].  Where our map is map<value_of_num, position_of_num>.
        if we don't find the complement in maps, we add the data in 
        map: map[nums[enum]] = enum. 
        - In this problem, we know that their will exist a solution,
        So we can write a code accordingly.
        """
        map = {}
        for enum, num in enumerate(nums):
            complement = target-num
            if complement in map:
                return [map[complement], enum]
            map[nums[enum]] = enum
        return []
