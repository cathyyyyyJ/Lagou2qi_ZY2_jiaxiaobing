import pytest

#需要再考虑等价类和边界值#
class Calculator:
    @pytest.mark.add
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return 0
        else:
            return a/b