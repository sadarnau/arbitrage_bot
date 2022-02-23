def test_eth_flashloan(accounts, flashContract):
    print(flashContract.address)
    # FlashGordon.deploy("0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5", {
    #                    "from": accounts[0]})

    accounts[0].transfer(
        "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "2 ether")
    # WETH.transfer(FlashGordon, "2 ether", {"from": accounts[0]})
