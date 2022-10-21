from FromInt import Solution
from testdata import ROAMANDATA_SET
import pytest

Sol = Solution()
@pytest.mark.parametrize("Int,Roman",list(ROAMANDATA_SET.items()))
def test_toroman_test(Int,Roman):
    assert Roman==Sol.intToRoman(Int)


