class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1=0
        index2=len(numbers)-1 
        while True:
            sum = numbers[index1]+numbers[index2]
            if sum == target:
                break
            elif sum > target:
                index2 -= 1
            else:
                index1 +=1
        return index1+1,index2+1



        


        