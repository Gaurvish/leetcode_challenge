class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = [i for i in str(int(''.join(map(str,digits)))+1)]
        return dig
        