class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fb_len = len(flowerbed)

        for i in xrange(fb_len):
            if  flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == fb_len-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1

            if n <= 0:
                return True
            
        return False