// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("dao0 Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployTokenFixture(){
    const [owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20] = await ethers.getSigners();
    const dao0 = await ethers.deployContract("dao0");
    await dao0.waitForDeployment();

    return{dao0, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20};
 }
    
    it("Should set the right owner", async function (){
      const{dao0, owner} = await loadFixture(deployTokenFixture);
      expect(await dao0.hasRole(owner.address)).to.equal(20);
      // Initialize committees
      const tx = await ownerConnect.initializeCommittees();
      await tx.wait();
      expect(tx).to.not.be.reverted;
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{dao0, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20} = await loadFixture(deployTokenFixture);

    ownerConnect = dao0.connect(owner);
    
    addr1Connect = dao0.connect(addr1);
    
    addr2Connect = dao0.connect(addr2);
    
    addr3Connect = dao0.connect(addr3);
    
    addr4Connect = dao0.connect(addr4);
    
    addr5Connect = dao0.connect(addr5);
    
    addr6Connect = dao0.connect(addr6);
    
    addr7Connect = dao0.connect(addr7);
    
    addr8Connect = dao0.connect(addr8);
    
    addr9Connect = dao0.connect(addr9);
    
    addr10Connect = dao0.connect(addr10);
    
    addr11Connect = dao0.connect(addr11);
    
    addr12Connect = dao0.connect(addr12);
    
    addr13Connect = dao0.connect(addr13);
    
    addr14Connect = dao0.connect(addr14);
    
    addr15Connect = dao0.connect(addr15);
    
    addr16Connect = dao0.connect(addr16);
    
    addr17Connect = dao0.connect(addr17);
    
    addr18Connect = dao0.connect(addr18);
    
    addr19Connect = dao0.connect(addr19);
    
    addr20Connect = dao0.connect(addr20);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(20, owner);
      
      addressesByEntityValue.set(0, addr1);
      
      addressesByEntityValue.set(1, addr2);
      
      addressesByEntityValue.set(2, addr3);
      
      addressesByEntityValue.set(3, addr4);
      
      addressesByEntityValue.set(4, addr5);
      
      addressesByEntityValue.set(5, addr6);
      
      addressesByEntityValue.set(6, addr7);
      
      addressesByEntityValue.set(7, addr8);
      
      addressesByEntityValue.set(8, addr9);
      
      addressesByEntityValue.set(9, addr10);
      
      addressesByEntityValue.set(10, addr11);
      
      addressesByEntityValue.set(11, addr12);
      
      addressesByEntityValue.set(12, addr13);
      
      addressesByEntityValue.set(13, addr14);
      
      addressesByEntityValue.set(14, addr15);
      
      addressesByEntityValue.set(15, addr16);
      
      addressesByEntityValue.set(16, addr17);
      
      addressesByEntityValue.set(17, addr18);
      
      addressesByEntityValue.set(18, addr19);
      
      addressesByEntityValue.set(19, addr20);
      

      // Iterate over the mapping and assign roles
      for (const [roleValue, addr] of addressesByEntityValue.entries()){
        try{
          console.log(`Assigning role ${roleValue} to address ${addr.address}`);
          const tx = await ownerConnect.assignRole(addr.address, roleValue);
          await tx.wait();
          console.log(`Role ${roleValue} successfully assigned to address ${addr.address}`);
       } catch (error){
          console.error(`Failed to assign role ${roleValue} to address ${addr.address}:`, error);
          throw error; // Stop execution if there's an error
       }
     }

      // Validate control relations
      let result = null;
      
      result = await dao0.canControl(0, 0);
      console.log(`Result of canControl(0, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 1);
      console.log(`Result of canControl(0, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 2);
      console.log(`Result of canControl(0, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 3);
      console.log(`Result of canControl(0, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 4);
      console.log(`Result of canControl(0, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 5);
      console.log(`Result of canControl(0, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 6);
      console.log(`Result of canControl(0, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 7);
      console.log(`Result of canControl(0, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 8);
      console.log(`Result of canControl(0, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 9);
      console.log(`Result of canControl(0, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 10);
      console.log(`Result of canControl(0, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 11);
      console.log(`Result of canControl(0, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 12);
      console.log(`Result of canControl(0, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 13);
      console.log(`Result of canControl(0, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 14);
      console.log(`Result of canControl(0, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 15);
      console.log(`Result of canControl(0, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 16);
      console.log(`Result of canControl(0, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 17);
      console.log(`Result of canControl(0, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 18);
      console.log(`Result of canControl(0, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 19);
      console.log(`Result of canControl(0, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(0, 20);
      console.log(`Result of canControl(0, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 0);
      console.log(`Result of canControl(1, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 1);
      console.log(`Result of canControl(1, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 2);
      console.log(`Result of canControl(1, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 3);
      console.log(`Result of canControl(1, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 4);
      console.log(`Result of canControl(1, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 5);
      console.log(`Result of canControl(1, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 6);
      console.log(`Result of canControl(1, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 7);
      console.log(`Result of canControl(1, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 8);
      console.log(`Result of canControl(1, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 9);
      console.log(`Result of canControl(1, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 10);
      console.log(`Result of canControl(1, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 11);
      console.log(`Result of canControl(1, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 12);
      console.log(`Result of canControl(1, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 13);
      console.log(`Result of canControl(1, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 14);
      console.log(`Result of canControl(1, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 15);
      console.log(`Result of canControl(1, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 16);
      console.log(`Result of canControl(1, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 17);
      console.log(`Result of canControl(1, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 18);
      console.log(`Result of canControl(1, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 19);
      console.log(`Result of canControl(1, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(1, 20);
      console.log(`Result of canControl(1, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 0);
      console.log(`Result of canControl(2, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 1);
      console.log(`Result of canControl(2, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 2);
      console.log(`Result of canControl(2, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 3);
      console.log(`Result of canControl(2, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 4);
      console.log(`Result of canControl(2, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 5);
      console.log(`Result of canControl(2, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 6);
      console.log(`Result of canControl(2, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 7);
      console.log(`Result of canControl(2, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 8);
      console.log(`Result of canControl(2, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 9);
      console.log(`Result of canControl(2, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 10);
      console.log(`Result of canControl(2, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 11);
      console.log(`Result of canControl(2, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 12);
      console.log(`Result of canControl(2, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 13);
      console.log(`Result of canControl(2, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 14);
      console.log(`Result of canControl(2, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 15);
      console.log(`Result of canControl(2, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 16);
      console.log(`Result of canControl(2, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 17);
      console.log(`Result of canControl(2, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 18);
      console.log(`Result of canControl(2, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 19);
      console.log(`Result of canControl(2, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(2, 20);
      console.log(`Result of canControl(2, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 0);
      console.log(`Result of canControl(3, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 1);
      console.log(`Result of canControl(3, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 2);
      console.log(`Result of canControl(3, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 3);
      console.log(`Result of canControl(3, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 4);
      console.log(`Result of canControl(3, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 5);
      console.log(`Result of canControl(3, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 6);
      console.log(`Result of canControl(3, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 7);
      console.log(`Result of canControl(3, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 8);
      console.log(`Result of canControl(3, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 9);
      console.log(`Result of canControl(3, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 10);
      console.log(`Result of canControl(3, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 11);
      console.log(`Result of canControl(3, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 12);
      console.log(`Result of canControl(3, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 13);
      console.log(`Result of canControl(3, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 14);
      console.log(`Result of canControl(3, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 15);
      console.log(`Result of canControl(3, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 16);
      console.log(`Result of canControl(3, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 17);
      console.log(`Result of canControl(3, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 18);
      console.log(`Result of canControl(3, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 19);
      console.log(`Result of canControl(3, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(3, 20);
      console.log(`Result of canControl(3, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 0);
      console.log(`Result of canControl(4, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 1);
      console.log(`Result of canControl(4, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 2);
      console.log(`Result of canControl(4, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 3);
      console.log(`Result of canControl(4, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 4);
      console.log(`Result of canControl(4, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 5);
      console.log(`Result of canControl(4, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 6);
      console.log(`Result of canControl(4, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 7);
      console.log(`Result of canControl(4, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 8);
      console.log(`Result of canControl(4, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 9);
      console.log(`Result of canControl(4, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 10);
      console.log(`Result of canControl(4, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 11);
      console.log(`Result of canControl(4, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 12);
      console.log(`Result of canControl(4, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 13);
      console.log(`Result of canControl(4, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 14);
      console.log(`Result of canControl(4, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 15);
      console.log(`Result of canControl(4, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 16);
      console.log(`Result of canControl(4, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 17);
      console.log(`Result of canControl(4, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 18);
      console.log(`Result of canControl(4, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 19);
      console.log(`Result of canControl(4, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(4, 20);
      console.log(`Result of canControl(4, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 0);
      console.log(`Result of canControl(5, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 1);
      console.log(`Result of canControl(5, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 2);
      console.log(`Result of canControl(5, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 3);
      console.log(`Result of canControl(5, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 4);
      console.log(`Result of canControl(5, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 5);
      console.log(`Result of canControl(5, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 6);
      console.log(`Result of canControl(5, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 7);
      console.log(`Result of canControl(5, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 8);
      console.log(`Result of canControl(5, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 9);
      console.log(`Result of canControl(5, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 10);
      console.log(`Result of canControl(5, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 11);
      console.log(`Result of canControl(5, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 12);
      console.log(`Result of canControl(5, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 13);
      console.log(`Result of canControl(5, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 14);
      console.log(`Result of canControl(5, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 15);
      console.log(`Result of canControl(5, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 16);
      console.log(`Result of canControl(5, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 17);
      console.log(`Result of canControl(5, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 18);
      console.log(`Result of canControl(5, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 19);
      console.log(`Result of canControl(5, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(5, 20);
      console.log(`Result of canControl(5, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 0);
      console.log(`Result of canControl(6, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 1);
      console.log(`Result of canControl(6, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 2);
      console.log(`Result of canControl(6, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 3);
      console.log(`Result of canControl(6, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 4);
      console.log(`Result of canControl(6, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 5);
      console.log(`Result of canControl(6, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 6);
      console.log(`Result of canControl(6, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 7);
      console.log(`Result of canControl(6, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 8);
      console.log(`Result of canControl(6, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 9);
      console.log(`Result of canControl(6, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 10);
      console.log(`Result of canControl(6, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 11);
      console.log(`Result of canControl(6, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 12);
      console.log(`Result of canControl(6, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 13);
      console.log(`Result of canControl(6, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 14);
      console.log(`Result of canControl(6, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 15);
      console.log(`Result of canControl(6, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 16);
      console.log(`Result of canControl(6, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 17);
      console.log(`Result of canControl(6, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 18);
      console.log(`Result of canControl(6, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 19);
      console.log(`Result of canControl(6, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(6, 20);
      console.log(`Result of canControl(6, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 0);
      console.log(`Result of canControl(7, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 1);
      console.log(`Result of canControl(7, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 2);
      console.log(`Result of canControl(7, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 3);
      console.log(`Result of canControl(7, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 4);
      console.log(`Result of canControl(7, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 5);
      console.log(`Result of canControl(7, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 6);
      console.log(`Result of canControl(7, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 7);
      console.log(`Result of canControl(7, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 8);
      console.log(`Result of canControl(7, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 9);
      console.log(`Result of canControl(7, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 10);
      console.log(`Result of canControl(7, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 11);
      console.log(`Result of canControl(7, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 12);
      console.log(`Result of canControl(7, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 13);
      console.log(`Result of canControl(7, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 14);
      console.log(`Result of canControl(7, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 15);
      console.log(`Result of canControl(7, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 16);
      console.log(`Result of canControl(7, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 17);
      console.log(`Result of canControl(7, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 18);
      console.log(`Result of canControl(7, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 19);
      console.log(`Result of canControl(7, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(7, 20);
      console.log(`Result of canControl(7, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 0);
      console.log(`Result of canControl(8, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 1);
      console.log(`Result of canControl(8, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 2);
      console.log(`Result of canControl(8, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 3);
      console.log(`Result of canControl(8, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 4);
      console.log(`Result of canControl(8, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 5);
      console.log(`Result of canControl(8, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 6);
      console.log(`Result of canControl(8, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 7);
      console.log(`Result of canControl(8, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 8);
      console.log(`Result of canControl(8, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 9);
      console.log(`Result of canControl(8, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 10);
      console.log(`Result of canControl(8, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 11);
      console.log(`Result of canControl(8, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 12);
      console.log(`Result of canControl(8, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 13);
      console.log(`Result of canControl(8, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 14);
      console.log(`Result of canControl(8, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 15);
      console.log(`Result of canControl(8, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 16);
      console.log(`Result of canControl(8, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 17);
      console.log(`Result of canControl(8, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 18);
      console.log(`Result of canControl(8, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 19);
      console.log(`Result of canControl(8, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(8, 20);
      console.log(`Result of canControl(8, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 0);
      console.log(`Result of canControl(9, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 1);
      console.log(`Result of canControl(9, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 2);
      console.log(`Result of canControl(9, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 3);
      console.log(`Result of canControl(9, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 4);
      console.log(`Result of canControl(9, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 5);
      console.log(`Result of canControl(9, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 6);
      console.log(`Result of canControl(9, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 7);
      console.log(`Result of canControl(9, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 8);
      console.log(`Result of canControl(9, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 9);
      console.log(`Result of canControl(9, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 10);
      console.log(`Result of canControl(9, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 11);
      console.log(`Result of canControl(9, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 12);
      console.log(`Result of canControl(9, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 13);
      console.log(`Result of canControl(9, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 14);
      console.log(`Result of canControl(9, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 15);
      console.log(`Result of canControl(9, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 16);
      console.log(`Result of canControl(9, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 17);
      console.log(`Result of canControl(9, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 18);
      console.log(`Result of canControl(9, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 19);
      console.log(`Result of canControl(9, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(9, 20);
      console.log(`Result of canControl(9, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 0);
      console.log(`Result of canControl(10, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 1);
      console.log(`Result of canControl(10, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 2);
      console.log(`Result of canControl(10, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 3);
      console.log(`Result of canControl(10, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 4);
      console.log(`Result of canControl(10, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 5);
      console.log(`Result of canControl(10, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 6);
      console.log(`Result of canControl(10, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 7);
      console.log(`Result of canControl(10, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 8);
      console.log(`Result of canControl(10, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 9);
      console.log(`Result of canControl(10, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 10);
      console.log(`Result of canControl(10, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 11);
      console.log(`Result of canControl(10, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 12);
      console.log(`Result of canControl(10, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 13);
      console.log(`Result of canControl(10, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 14);
      console.log(`Result of canControl(10, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 15);
      console.log(`Result of canControl(10, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 16);
      console.log(`Result of canControl(10, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 17);
      console.log(`Result of canControl(10, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 18);
      console.log(`Result of canControl(10, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 19);
      console.log(`Result of canControl(10, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(10, 20);
      console.log(`Result of canControl(10, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 0);
      console.log(`Result of canControl(11, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 1);
      console.log(`Result of canControl(11, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 2);
      console.log(`Result of canControl(11, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 3);
      console.log(`Result of canControl(11, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 4);
      console.log(`Result of canControl(11, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 5);
      console.log(`Result of canControl(11, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 6);
      console.log(`Result of canControl(11, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 7);
      console.log(`Result of canControl(11, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 8);
      console.log(`Result of canControl(11, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 9);
      console.log(`Result of canControl(11, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 10);
      console.log(`Result of canControl(11, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 11);
      console.log(`Result of canControl(11, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 12);
      console.log(`Result of canControl(11, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 13);
      console.log(`Result of canControl(11, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 14);
      console.log(`Result of canControl(11, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 15);
      console.log(`Result of canControl(11, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 16);
      console.log(`Result of canControl(11, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 17);
      console.log(`Result of canControl(11, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 18);
      console.log(`Result of canControl(11, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 19);
      console.log(`Result of canControl(11, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(11, 20);
      console.log(`Result of canControl(11, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 0);
      console.log(`Result of canControl(12, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 1);
      console.log(`Result of canControl(12, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 2);
      console.log(`Result of canControl(12, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 3);
      console.log(`Result of canControl(12, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 4);
      console.log(`Result of canControl(12, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 5);
      console.log(`Result of canControl(12, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 6);
      console.log(`Result of canControl(12, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 7);
      console.log(`Result of canControl(12, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 8);
      console.log(`Result of canControl(12, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 9);
      console.log(`Result of canControl(12, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 10);
      console.log(`Result of canControl(12, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 11);
      console.log(`Result of canControl(12, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 12);
      console.log(`Result of canControl(12, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 13);
      console.log(`Result of canControl(12, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 14);
      console.log(`Result of canControl(12, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 15);
      console.log(`Result of canControl(12, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 16);
      console.log(`Result of canControl(12, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 17);
      console.log(`Result of canControl(12, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 18);
      console.log(`Result of canControl(12, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 19);
      console.log(`Result of canControl(12, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(12, 20);
      console.log(`Result of canControl(12, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 0);
      console.log(`Result of canControl(13, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 1);
      console.log(`Result of canControl(13, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 2);
      console.log(`Result of canControl(13, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 3);
      console.log(`Result of canControl(13, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 4);
      console.log(`Result of canControl(13, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 5);
      console.log(`Result of canControl(13, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 6);
      console.log(`Result of canControl(13, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 7);
      console.log(`Result of canControl(13, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 8);
      console.log(`Result of canControl(13, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 9);
      console.log(`Result of canControl(13, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 10);
      console.log(`Result of canControl(13, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 11);
      console.log(`Result of canControl(13, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 12);
      console.log(`Result of canControl(13, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 13);
      console.log(`Result of canControl(13, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 14);
      console.log(`Result of canControl(13, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 15);
      console.log(`Result of canControl(13, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 16);
      console.log(`Result of canControl(13, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 17);
      console.log(`Result of canControl(13, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 18);
      console.log(`Result of canControl(13, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 19);
      console.log(`Result of canControl(13, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(13, 20);
      console.log(`Result of canControl(13, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 0);
      console.log(`Result of canControl(14, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 1);
      console.log(`Result of canControl(14, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 2);
      console.log(`Result of canControl(14, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 3);
      console.log(`Result of canControl(14, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 4);
      console.log(`Result of canControl(14, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 5);
      console.log(`Result of canControl(14, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 6);
      console.log(`Result of canControl(14, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 7);
      console.log(`Result of canControl(14, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 8);
      console.log(`Result of canControl(14, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 9);
      console.log(`Result of canControl(14, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 10);
      console.log(`Result of canControl(14, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 11);
      console.log(`Result of canControl(14, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 12);
      console.log(`Result of canControl(14, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 13);
      console.log(`Result of canControl(14, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 14);
      console.log(`Result of canControl(14, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 15);
      console.log(`Result of canControl(14, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 16);
      console.log(`Result of canControl(14, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 17);
      console.log(`Result of canControl(14, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 18);
      console.log(`Result of canControl(14, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 19);
      console.log(`Result of canControl(14, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(14, 20);
      console.log(`Result of canControl(14, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 0);
      console.log(`Result of canControl(15, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 1);
      console.log(`Result of canControl(15, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 2);
      console.log(`Result of canControl(15, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 3);
      console.log(`Result of canControl(15, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 4);
      console.log(`Result of canControl(15, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 5);
      console.log(`Result of canControl(15, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 6);
      console.log(`Result of canControl(15, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 7);
      console.log(`Result of canControl(15, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 8);
      console.log(`Result of canControl(15, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 9);
      console.log(`Result of canControl(15, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 10);
      console.log(`Result of canControl(15, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 11);
      console.log(`Result of canControl(15, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 12);
      console.log(`Result of canControl(15, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 13);
      console.log(`Result of canControl(15, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 14);
      console.log(`Result of canControl(15, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 15);
      console.log(`Result of canControl(15, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 16);
      console.log(`Result of canControl(15, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 17);
      console.log(`Result of canControl(15, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 18);
      console.log(`Result of canControl(15, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 19);
      console.log(`Result of canControl(15, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(15, 20);
      console.log(`Result of canControl(15, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 0);
      console.log(`Result of canControl(16, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 1);
      console.log(`Result of canControl(16, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 2);
      console.log(`Result of canControl(16, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 3);
      console.log(`Result of canControl(16, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 4);
      console.log(`Result of canControl(16, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 5);
      console.log(`Result of canControl(16, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 6);
      console.log(`Result of canControl(16, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 7);
      console.log(`Result of canControl(16, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 8);
      console.log(`Result of canControl(16, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 9);
      console.log(`Result of canControl(16, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 10);
      console.log(`Result of canControl(16, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 11);
      console.log(`Result of canControl(16, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 12);
      console.log(`Result of canControl(16, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 13);
      console.log(`Result of canControl(16, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 14);
      console.log(`Result of canControl(16, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 15);
      console.log(`Result of canControl(16, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 16);
      console.log(`Result of canControl(16, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 17);
      console.log(`Result of canControl(16, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 18);
      console.log(`Result of canControl(16, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 19);
      console.log(`Result of canControl(16, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(16, 20);
      console.log(`Result of canControl(16, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 0);
      console.log(`Result of canControl(17, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 1);
      console.log(`Result of canControl(17, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 2);
      console.log(`Result of canControl(17, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 3);
      console.log(`Result of canControl(17, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 4);
      console.log(`Result of canControl(17, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 5);
      console.log(`Result of canControl(17, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 6);
      console.log(`Result of canControl(17, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 7);
      console.log(`Result of canControl(17, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 8);
      console.log(`Result of canControl(17, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 9);
      console.log(`Result of canControl(17, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 10);
      console.log(`Result of canControl(17, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 11);
      console.log(`Result of canControl(17, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 12);
      console.log(`Result of canControl(17, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 13);
      console.log(`Result of canControl(17, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 14);
      console.log(`Result of canControl(17, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 15);
      console.log(`Result of canControl(17, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 16);
      console.log(`Result of canControl(17, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 17);
      console.log(`Result of canControl(17, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 18);
      console.log(`Result of canControl(17, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 19);
      console.log(`Result of canControl(17, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(17, 20);
      console.log(`Result of canControl(17, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 0);
      console.log(`Result of canControl(18, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 1);
      console.log(`Result of canControl(18, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 2);
      console.log(`Result of canControl(18, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 3);
      console.log(`Result of canControl(18, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 4);
      console.log(`Result of canControl(18, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 5);
      console.log(`Result of canControl(18, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 6);
      console.log(`Result of canControl(18, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 7);
      console.log(`Result of canControl(18, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 8);
      console.log(`Result of canControl(18, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 9);
      console.log(`Result of canControl(18, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 10);
      console.log(`Result of canControl(18, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 11);
      console.log(`Result of canControl(18, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 12);
      console.log(`Result of canControl(18, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 13);
      console.log(`Result of canControl(18, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 14);
      console.log(`Result of canControl(18, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 15);
      console.log(`Result of canControl(18, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 16);
      console.log(`Result of canControl(18, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 17);
      console.log(`Result of canControl(18, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 18);
      console.log(`Result of canControl(18, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 19);
      console.log(`Result of canControl(18, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(18, 20);
      console.log(`Result of canControl(18, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 0);
      console.log(`Result of canControl(19, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 1);
      console.log(`Result of canControl(19, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 2);
      console.log(`Result of canControl(19, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 3);
      console.log(`Result of canControl(19, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 4);
      console.log(`Result of canControl(19, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 5);
      console.log(`Result of canControl(19, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 6);
      console.log(`Result of canControl(19, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 7);
      console.log(`Result of canControl(19, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 8);
      console.log(`Result of canControl(19, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 9);
      console.log(`Result of canControl(19, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 10);
      console.log(`Result of canControl(19, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 11);
      console.log(`Result of canControl(19, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 12);
      console.log(`Result of canControl(19, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 13);
      console.log(`Result of canControl(19, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 14);
      console.log(`Result of canControl(19, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 15);
      console.log(`Result of canControl(19, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 16);
      console.log(`Result of canControl(19, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 17);
      console.log(`Result of canControl(19, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 18);
      console.log(`Result of canControl(19, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 19);
      console.log(`Result of canControl(19, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(19, 20);
      console.log(`Result of canControl(19, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 0);
      console.log(`Result of canControl(20, 0):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 1);
      console.log(`Result of canControl(20, 1):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 2);
      console.log(`Result of canControl(20, 2):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 3);
      console.log(`Result of canControl(20, 3):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 4);
      console.log(`Result of canControl(20, 4):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 5);
      console.log(`Result of canControl(20, 5):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 6);
      console.log(`Result of canControl(20, 6):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 7);
      console.log(`Result of canControl(20, 7):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 8);
      console.log(`Result of canControl(20, 8):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 9);
      console.log(`Result of canControl(20, 9):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 10);
      console.log(`Result of canControl(20, 10):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 11);
      console.log(`Result of canControl(20, 11):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 12);
      console.log(`Result of canControl(20, 12):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 13);
      console.log(`Result of canControl(20, 13):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 14);
      console.log(`Result of canControl(20, 14):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 15);
      console.log(`Result of canControl(20, 15):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 16);
      console.log(`Result of canControl(20, 16):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 17);
      console.log(`Result of canControl(20, 17):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 18);
      console.log(`Result of canControl(20, 18):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 19);
      console.log(`Result of canControl(20, 19):`, result);
      expect(result).to.equal( false );
      
      result = await dao0.canControl(20, 20);
      console.log(`Result of canControl(20, 20):`, result);
      expect(result).to.equal( false );
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      result = await addr1Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 0):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 0):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 0):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 1):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 1):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 1):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 2):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 2):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 2):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 3):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 3):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 3):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 5):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 5):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 5):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 6):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 6):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 6):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr8Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 7):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 7):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 7):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr8Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 9):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 9):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 9):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 10):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 10):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 10):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 11):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 11):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 11):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 12):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 12):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 12):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr14Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 13):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 13):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 13):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr15Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 14):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr15Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 14):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr15Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 14):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr15Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr15Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr16Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 15):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr16Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 15):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr16Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 15):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr16Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr16Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr17Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 16):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr17Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 16):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr17Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 16):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr17Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr17Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr18Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 17):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr18Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 17):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr18Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 17):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr18Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr18Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr19Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 18):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr19Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 18):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr19Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 18):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr19Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr19Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr20Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 19):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr20Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 19):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr20Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 19):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr20Connect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr20Connect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission0()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission1()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission2()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission3()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission4()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission5()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission6()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission7()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission8()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission9()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission10()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission11()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission12()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission13()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission14()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission15()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission16()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission17()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission18()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission19()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission20()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission21()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission22()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission23()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission24()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission25()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission26()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission27()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission28()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission29()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission30()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission31()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission32()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission33()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(ownerConnect.permission34()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
});
});
