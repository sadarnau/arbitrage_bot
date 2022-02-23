import pytest
import abi


@pytest.fixture(autouse=True)
def setup(fn_isolation):
    pass


@pytest.fixture
def aave_lending_pool(Contract):
    test = Contract("0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5")
    print(test)
    # Contract.from_abi(
    # "aave_lending_pool", "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5", abi.aave_lending)
    # yield Contract("0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5")


@pytest.fixture
def flashContract(FlashGordon, aave_lending_pool, accounts):
    yield FlashGordon.deploy(aave_lending_pool, {"from": accounts[0]})


# @pytest.fixture(scope="module")
# def WETH(Contract):
#     yield Contract("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
