// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("Group_Currency_DAO Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployTokenFixture(){
    const [owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7] = await ethers.getSigners();
    const Group_Currency_DAO = await ethers.deployContract("Group_Currency_DAO");
    await Group_Currency_DAO.waitForDeployment();

    return{Group_Currency_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7};
 }

  describe("Deployment", function (){
    it("Should set the right owner", async function (){
      const{Group_Currency_DAO, owner} = await loadFixture(deployTokenFixture);
      expect(await Group_Currency_DAO.hasRole(owner.address)).to.equal(259);
   });
 });

  describe("Control relations", function (){
    before(async function () {});

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Group_Currency_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7} = await loadFixture(deployTokenFixture);

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(259, owner);
      
      addressesByEntityValue.set(320, addr1);
      
      addressesByEntityValue.set(1281, addr2);
      
      addressesByEntityValue.set(258, addr3);
      
      addressesByEntityValue.set(1348, addr4);
      
      addressesByEntityValue.set(2309, addr5);
      
      addressesByEntityValue.set(4358, addr6);
      
      addressesByEntityValue.set(263, addr7);
      

      // Connect to contract with the owner's wallet
      const ownerAddr = Group_Currency_DAO.connect(owner);

      // Iterate over the mapping and assign roles
      for (const [roleValue, addr] of addressesByEntityValue.entries()){
        try{
          console.log(`Assigning role ${roleValue} to address ${addr.address}`);
          const tx = await ownerAddr.assignRole(addr.address, roleValue);
          await tx.wait();
          console.log(`Role ${roleValue} successfully assigned to address ${addr.address}`);
       } catch (error){
          console.error(`Failed to assign role ${roleValue} to address ${addr.address}:`, error);
          throw error; // Stop execution if there's an error
       }
     }

      // Validate control relations
      let result = null;
      
      result = await Group_Currency_DAO.canControl(320, 320);
      console.log(`Result of canControl(320, 320):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 1281);
      console.log(`Result of canControl(320, 1281):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 258);
      console.log(`Result of canControl(320, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 259);
      console.log(`Result of canControl(320, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 1348);
      console.log(`Result of canControl(320, 1348):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 2309);
      console.log(`Result of canControl(320, 2309):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 4358);
      console.log(`Result of canControl(320, 4358):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(320, 263);
      console.log(`Result of canControl(320, 263):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1281, 320);
      console.log(`Result of canControl(1281, 320):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(1281, 1281);
      console.log(`Result of canControl(1281, 1281):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1281, 258);
      console.log(`Result of canControl(1281, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1281, 259);
      console.log(`Result of canControl(1281, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1281, 1348);
      console.log(`Result of canControl(1281, 1348):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(1281, 2309);
      console.log(`Result of canControl(1281, 2309):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1281, 4358);
      console.log(`Result of canControl(1281, 4358):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1281, 263);
      console.log(`Result of canControl(1281, 263):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 320);
      console.log(`Result of canControl(258, 320):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 1281);
      console.log(`Result of canControl(258, 1281):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 258);
      console.log(`Result of canControl(258, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 259);
      console.log(`Result of canControl(258, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 1348);
      console.log(`Result of canControl(258, 1348):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 2309);
      console.log(`Result of canControl(258, 2309):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 4358);
      console.log(`Result of canControl(258, 4358):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(258, 263);
      console.log(`Result of canControl(258, 263):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(259, 320);
      console.log(`Result of canControl(259, 320):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 1281);
      console.log(`Result of canControl(259, 1281):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 258);
      console.log(`Result of canControl(259, 258):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 259);
      console.log(`Result of canControl(259, 259):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 1348);
      console.log(`Result of canControl(259, 1348):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 2309);
      console.log(`Result of canControl(259, 2309):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 4358);
      console.log(`Result of canControl(259, 4358):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(259, 263);
      console.log(`Result of canControl(259, 263):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(1348, 320);
      console.log(`Result of canControl(1348, 320):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 1281);
      console.log(`Result of canControl(1348, 1281):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 258);
      console.log(`Result of canControl(1348, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 259);
      console.log(`Result of canControl(1348, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 1348);
      console.log(`Result of canControl(1348, 1348):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 2309);
      console.log(`Result of canControl(1348, 2309):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 4358);
      console.log(`Result of canControl(1348, 4358):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(1348, 263);
      console.log(`Result of canControl(1348, 263):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(2309, 320);
      console.log(`Result of canControl(2309, 320):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(2309, 1281);
      console.log(`Result of canControl(2309, 1281):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(2309, 258);
      console.log(`Result of canControl(2309, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(2309, 259);
      console.log(`Result of canControl(2309, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(2309, 1348);
      console.log(`Result of canControl(2309, 1348):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(2309, 2309);
      console.log(`Result of canControl(2309, 2309):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(2309, 4358);
      console.log(`Result of canControl(2309, 4358):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(2309, 263);
      console.log(`Result of canControl(2309, 263):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 320);
      console.log(`Result of canControl(4358, 320):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 1281);
      console.log(`Result of canControl(4358, 1281):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 258);
      console.log(`Result of canControl(4358, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 259);
      console.log(`Result of canControl(4358, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 1348);
      console.log(`Result of canControl(4358, 1348):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 2309);
      console.log(`Result of canControl(4358, 2309):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(4358, 4358);
      console.log(`Result of canControl(4358, 4358):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(4358, 263);
      console.log(`Result of canControl(4358, 263):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 320);
      console.log(`Result of canControl(263, 320):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 1281);
      console.log(`Result of canControl(263, 1281):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 258);
      console.log(`Result of canControl(263, 258):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 259);
      console.log(`Result of canControl(263, 259):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 1348);
      console.log(`Result of canControl(263, 1348):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 2309);
      console.log(`Result of canControl(263, 2309):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.canControl(263, 4358);
      console.log(`Result of canControl(263, 4358):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.canControl(263, 263);
      console.log(`Result of canControl(263, 263):`, result);
      expect(result).to.equal( false );
      
   });
 });
});
