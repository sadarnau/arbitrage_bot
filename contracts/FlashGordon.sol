//SPDX-License-Identifier: Unlicense
pragma solidity ^0.6.12;

import "hardhat/console.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {FlashLoanReceiverBase} from "@aave/protocol-v2/contracts/flashloan/base/FlashLoanReceiverBase.sol";
import {ILendingPool} from "@aave/protocol-v2/contracts/interfaces/ILendingPool.sol";
import {ILendingPoolAddressesProvider} from "@aave/protocol-v2/contracts/interfaces/ILendingPoolAddressesProvider.sol";

// make Withdrawable and onlyOwner
contract FlashGordon is FlashLoanReceiverBase {
    // using SafeERC20 for IERC20;

    constructor(ILendingPoolAddressesProvider _addressProvider)
        public
        FlashLoanReceiverBase(_addressProvider)
    {}

    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        console.log(IERC20(assets[0]).balanceOf(address(this)));

        for (uint256 i = 0; i < assets.length; i++) {
            uint256 amountOwing = amounts[i].add(premiums[i]);
            console.log(amountOwing);
            IERC20(assets[i]).approve(address(LENDING_POOL), amountOwing);
        }

        return true;
    }

    function _flashloan(address[] memory coins, uint256[] memory amounts)
        internal
    {
        address receiverAddress = address(this);
        address onBehalfOf = address(this);
        uint16 referralCode = 0;
        bytes memory params = "";

        // 0 = no debt, 1 = stable, 2 = variable
        uint256[] memory modes = new uint256[](coins.length);
        for (uint256 i = 0; i < coins.length; i++) {
            modes[i] = 0;
        }

        LENDING_POOL.flashLoan(
            receiverAddress,
            coins,
            amounts,
            modes,
            onBehalfOf,
            params,
            referralCode
        );
    }

    function flashloan(address coin) public {
        address[] memory coins = new address[](1);
        coins[0] = address(coin);

        uint256[] memory amounts = new uint256[](1);
        amounts[0] = 1 ether;

        _flashloan(coins, amounts);
    }

    function flashloan(address[] memory coins, uint256[] memory amounts)
        public
    {
        _flashloan(coins, amounts);
    }

    receive() external payable {}
}
