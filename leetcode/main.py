from Running_Sum_of_1d_Array import Solution

def main():
    print('hello');
    solution = Solution()
    nums = solution.runningSum([1, 2, 3])
    for i in range(0, len(nums)):
        print(nums[i])

if __name__ == '__main__':
    main();