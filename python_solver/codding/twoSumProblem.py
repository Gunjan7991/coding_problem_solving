def twoSum(nums: list[int], target: int) -> list[int]:
        num_map = {}
        for enum, num in enumerate(nums):
            complement = target-num
            if complement in num_map:
                return [num_map[complement], enum]
            num_map[nums[enum]] = enum
        return []
