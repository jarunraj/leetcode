class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max, result = max(candies), []

        for candy in candies:
            #print(candy)
            #print(candy + extraCandies >= current_max)
            result.append(candy + extraCandies >= current_max)

        return result