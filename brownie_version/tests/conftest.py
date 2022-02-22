import pytest


@pytest.fixture(autouse=True)
def setup(fn_isolation):
    """
    Isolation setup fixture.
    This ensures that each test runs against the same base environment.
    """
    pass


# @pytest.fixture(scope="module")
# def WETH(Contract):
#     yield Contract("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
