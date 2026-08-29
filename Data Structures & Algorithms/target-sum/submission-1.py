class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Bottom Up 
        # create a hashmap where
            # key represents possible sum
            # value represents number of ways to form the sum
        # initialize dp[0][0] = 1 since only one way to form sum 0 using no numbers
        # iterate through index of nums
        # for each exisiting (sum, count) in dp[i]
            # add the current num and update
            # add the current num and update
        # return dp[n][target]

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1 # (0 elements, 0 sum) -> 1 way
                    # 1 way to sum to zero with first 0 elements
        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count
        return dp[len(nums)][target]


        # T: O(n * sum(nums))
        # S: O(n * sum(nums))
        