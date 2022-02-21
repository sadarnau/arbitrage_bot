import { expect } from "chai";
import { ethers } from "hardhat";
import { WETHAbi } from "../helpers/abi";

describe("Greeter", function () {
  it("Should lend weth and repay", async function () {
    const [owner] = await ethers.getSigners();

    const FlashGordon = await ethers.getContractFactory("FlashGordon");
    const flash = await FlashGordon.deploy(
      "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"
      // Aave registry
    );

    await flash.deployed();

    const wethContract = new ethers.Contract(
      "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
      WETHAbi
    );

    await wethContract
      .connect(owner)
      .deposit({ value: ethers.utils.parseEther("10").toString() });

    await wethContract
      .connect(owner)
      .transfer(flash.address, ethers.utils.parseEther("10").toString());

    const balBefore = await wethContract
      .connect(owner)
      .balanceOf(flash.address);
    console.log("Balance before :", balBefore.toString());

    // Multiple flashloan functions so harhat need to know which one
    await flash["flashloan(address)"](
      "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    );

    const balAfter = await wethContract.connect(owner).balanceOf(flash.address);
    console.log("Balance after :	", balAfter.toString());

    expect(balAfter).to.be.below(balBefore);
  });
});
