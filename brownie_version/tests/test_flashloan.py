from brownie import network


def test_eth_flashloan(accounts, FlashGordon):
    print(accounts[0].balance())
    print(accounts[0].address)
    FlashGordon.deploy("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", {
                       "from": accounts[0]})
    # accounts[0].transfer(WETH, "2 ether", network.priority_fee("auto"))
    # WETH.transfer(FlashGordon, "2 ether", {"from": accounts[0]})
