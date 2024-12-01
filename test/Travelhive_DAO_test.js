// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("Travelhive_DAO Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployTokenFixture(){
    const [owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14] = await ethers.getSigners();
    const Travelhive_DAO = await ethers.deployContract("Travelhive_DAO", ["Travelhive_DAO", owner.address, addr1.address  , addr2.address  , addr3.address  , addr4.address  , addr5.address ]);
    await Travelhive_DAO.waitForDeployment();

    return{Travelhive_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14};
 }
    
    it("Should set the right owner", async function (){
      const{Travelhive_DAO, owner} = await loadFixture(deployTokenFixture);
      expect(await Travelhive_DAO.hasRole(owner.address)).to.equal(10);
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Travelhive_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14} = await loadFixture(deployTokenFixture);

    ownerConnect = Travelhive_DAO.connect(owner);
    
    addr1Connect = Travelhive_DAO.connect(addr1);
    
    addr2Connect = Travelhive_DAO.connect(addr2);
    
    addr3Connect = Travelhive_DAO.connect(addr3);
    
    addr4Connect = Travelhive_DAO.connect(addr4);
    
    addr5Connect = Travelhive_DAO.connect(addr5);
    
    addr6Connect = Travelhive_DAO.connect(addr6);
    
    addr7Connect = Travelhive_DAO.connect(addr7);
    
    addr8Connect = Travelhive_DAO.connect(addr8);
    
    addr9Connect = Travelhive_DAO.connect(addr9);
    
    addr10Connect = Travelhive_DAO.connect(addr10);
    
    addr11Connect = Travelhive_DAO.connect(addr11);
    
    addr12Connect = Travelhive_DAO.connect(addr12);
    
    addr13Connect = Travelhive_DAO.connect(addr13);
    
    addr14Connect = Travelhive_DAO.connect(addr14);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(10, owner);
      
      addressesByEntityValue.set(1, addr1);
      
      addressesByEntityValue.set(2, addr2);
      
      addressesByEntityValue.set(3, addr3);
      
      addressesByEntityValue.set(4, addr4);
      
      addressesByEntityValue.set(5, addr5);
      
      addressesByEntityValue.set(6, addr6);
      
      addressesByEntityValue.set(7, addr7);
      
      addressesByEntityValue.set(8, addr8);
      
      addressesByEntityValue.set(9, addr9);
      
      addressesByEntityValue.set(11, addr10);
      
      addressesByEntityValue.set(12, addr11);
      
      addressesByEntityValue.set(13, addr12);
      
      addressesByEntityValue.set(14, addr13);
      
      addressesByEntityValue.set(15, addr14);
      

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
      
      try{
      console.log(`Result of can_control(addr1, addr1):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr2):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr3):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr4):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr5):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr6):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr7):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr8):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr9):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, owner):`);
      result = await Travelhive_DAO.can_control(addr1.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr10):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr11):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr12):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr13):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr1, addr14):`);
      result = await Travelhive_DAO.can_control(addr1.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 1 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr1):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr2):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr3):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr4):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr5):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr6):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr7):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr8):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr9):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, owner):`);
      result = await Travelhive_DAO.can_control(addr2.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr10):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr11):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr12):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr13):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr2, addr14):`);
      result = await Travelhive_DAO.can_control(addr2.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 2 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr1):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr2):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr3):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr4):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr5):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr6):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr7):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr8):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr9):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, owner):`);
      result = await Travelhive_DAO.can_control(addr3.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr10):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr11):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr12):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr13):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr3, addr14):`);
      result = await Travelhive_DAO.can_control(addr3.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 3 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr1):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr2):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr2.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr3):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr3.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr4):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr4.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr5):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr5.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr6):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr6.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr7):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr7.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr8):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr8.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr9):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr9.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, owner):`);
      result = await Travelhive_DAO.can_control(addr4.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr10):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr11):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr12):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr13):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr4, addr14):`);
      result = await Travelhive_DAO.can_control(addr4.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 4 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr1):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr2):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr3):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr4):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr5):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr6):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr7):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr8):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr9):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, owner):`);
      result = await Travelhive_DAO.can_control(addr5.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr10):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr11):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr12):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr13):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr5, addr14):`);
      result = await Travelhive_DAO.can_control(addr5.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 5 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr1):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr2):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr3):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr4):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr5):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr6):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr7):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr8):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr9):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, owner):`);
      result = await Travelhive_DAO.can_control(addr6.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr10):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr11):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr12):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr13):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr6, addr14):`);
      result = await Travelhive_DAO.can_control(addr6.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 6 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr1):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr2):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr3):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr4):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr5):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr6):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr7):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr8):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr9):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, owner):`);
      result = await Travelhive_DAO.can_control(addr7.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr10):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr11):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr12):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr13):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr7, addr14):`);
      result = await Travelhive_DAO.can_control(addr7.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 7 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr1):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr2):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr3):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr4):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr5):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr6):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr7):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr8):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr9):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, owner):`);
      result = await Travelhive_DAO.can_control(addr8.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr10):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr11):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr12):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr13):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr8, addr14):`);
      result = await Travelhive_DAO.can_control(addr8.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 8 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr1):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr2):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr3):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr4):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr5):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr6):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr7):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr8):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr9):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, owner):`);
      result = await Travelhive_DAO.can_control(addr9.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr10):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr11):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr12):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr13):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr9, addr14):`);
      result = await Travelhive_DAO.can_control(addr9.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 9 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr1):`);
      result = await Travelhive_DAO.can_control(owner.address, addr1.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr2):`);
      result = await Travelhive_DAO.can_control(owner.address, addr2.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr3):`);
      result = await Travelhive_DAO.can_control(owner.address, addr3.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr4):`);
      result = await Travelhive_DAO.can_control(owner.address, addr4.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr5):`);
      result = await Travelhive_DAO.can_control(owner.address, addr5.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr6):`);
      result = await Travelhive_DAO.can_control(owner.address, addr6.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr7):`);
      result = await Travelhive_DAO.can_control(owner.address, addr7.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr8):`);
      result = await Travelhive_DAO.can_control(owner.address, addr8.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr9):`);
      result = await Travelhive_DAO.can_control(owner.address, addr9.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, owner):`);
      result = await Travelhive_DAO.can_control(owner.address, owner.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr10):`);
      result = await Travelhive_DAO.can_control(owner.address, addr10.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr11):`);
      result = await Travelhive_DAO.can_control(owner.address, addr11.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr12):`);
      result = await Travelhive_DAO.can_control(owner.address, addr12.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr13):`);
      result = await Travelhive_DAO.can_control(owner.address, addr13.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(owner, addr14):`);
      result = await Travelhive_DAO.can_control(owner.address, addr14.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 10 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr1):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr2):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr3):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr4):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr5):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr6):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr7):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr8):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr9):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, owner):`);
      result = await Travelhive_DAO.can_control(addr10.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr10):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr11):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr12):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr13):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr10, addr14):`);
      result = await Travelhive_DAO.can_control(addr10.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 11 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr1):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr2):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr3):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr4):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr5):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr6):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr7):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr8):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr9):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, owner):`);
      result = await Travelhive_DAO.can_control(addr11.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr10):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr10.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr11):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr11.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr12):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr12.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr13):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr13.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr11, addr14):`);
      result = await Travelhive_DAO.can_control(addr11.address, addr14.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 12 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr1):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr2):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr3):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr4):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr5):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr6):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr7):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr8):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr9):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, owner):`);
      result = await Travelhive_DAO.can_control(addr12.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr10):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr11):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr12):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr13):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr12, addr14):`);
      result = await Travelhive_DAO.can_control(addr12.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 13 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr1):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr2):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr3):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr4):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr5):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr6):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr7):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr8):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr9):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr9.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, owner):`);
      result = await Travelhive_DAO.can_control(addr13.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr10):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr11):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr12):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr13):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr13, addr14):`);
      result = await Travelhive_DAO.can_control(addr13.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 14 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr1):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr1.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 1:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr2):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr2.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 2:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr3):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr3.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 3:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr4):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr4.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 4:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr5):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr5.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 5:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr6):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr6.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 6:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr7):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr7.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 7:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr8):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr8.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 8:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr9):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr9.address);
      expect(result).to.equal( true );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 9:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, owner):`);
      result = await Travelhive_DAO.can_control(addr14.address, owner.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 10:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr10):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr10.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 11:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr11):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr11.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 12:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr12):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr12.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 13:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr13):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr13.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 14:`, error);
      throw error; // Stop execution if there's an error
      }
      
      try{
      console.log(`Result of can_control(addr14, addr14):`);
      result = await Travelhive_DAO.can_control(addr14.address, addr14.address);
      expect(result).to.equal( false );
      } catch (error){
      console.error(`Failed to validate control relation between 15 and 15:`, error);
      throw error; // Stop execution if there's an error
      }
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      await expect(addr1Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr1Connect.veto_proposal();
      console.log(`Execution result of permission (veto_proposal for 1)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.execute_Task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.propose_Task_Delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.supply_Service()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr1Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr2Connect.Post_Event();
      console.log(`Execution result of permission (Post_Event for 2)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr2Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr2Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 2)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 2)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 2)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 2)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr3Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr3Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 3)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 3)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 3)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 3)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr4Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr4Connect.veto_proposal();
      console.log(`Execution result of permission (veto_proposal for 4)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 4)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 4)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 4)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 4)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr5Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr5Connect.verify_Institutional_Profile();
      console.log(`Execution result of permission (verify_Institutional_Profile for 5)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr5Connect.appoint_Destination_Committee();
      console.log(`Execution result of permission (appoint_Destination_Committee for 5)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr5Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 5)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 5)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 5)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 5)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr6Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr6Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 6)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 6)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 6)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 6)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr7Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr7Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 7)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 7)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 7)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 7)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr8Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr8Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr8Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 8)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 8)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 8)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 8)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.create_new_DDMO()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.upgrade_platform_feature()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.activate_role_delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr9Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr9Connect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 9)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 9)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 9)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 9)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.transfer_tokens();
      console.log(`Execution result of permission (transfer_tokens for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.assign_task();
      console.log(`Execution result of permission (assign_task for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.cut_funding_to_project_budget();
      console.log(`Execution result of permission (cut_funding_to_project_budget for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_campaign_budget();
      console.log(`Execution result of permission (propose_campaign_budget for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.approve_project_budget();
      console.log(`Execution result of permission (approve_project_budget for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Post_Event();
      console.log(`Execution result of permission (Post_Event for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.verify_Institutional_Profile();
      console.log(`Execution result of permission (verify_Institutional_Profile for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.launchCampaign();
      console.log(`Execution result of permission (launchCampaign for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.appoint_Destination_Committee();
      console.log(`Execution result of permission (appoint_Destination_Committee for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.veto_proposal();
      console.log(`Execution result of permission (veto_proposal for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.execute_Task();
      console.log(`Execution result of permission (execute_Task for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_Task_Delegation();
      console.log(`Execution result of permission (propose_Task_Delegation for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.supply_Service();
      console.log(`Execution result of permission (supply_Service for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.apply_For_DAO_Governance_Role();
      console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 10)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.transfer_tokens();
      console.log(`Execution result of permission (transfer_tokens for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr10Connect.cut_funding_to_project_budget();
      console.log(`Execution result of permission (cut_funding_to_project_budget for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr10Connect.approve_project_budget();
      console.log(`Execution result of permission (approve_project_budget for 11)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.execute_Task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.propose_Task_Delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.supply_Service()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr10Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr11Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO for 12)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy for 12)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr11Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature for 12)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation for 12)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.execute_Task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.propose_Task_Delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.supply_Service()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr11Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr12Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO for 13)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy for 13)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr12Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature for 13)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation for 13)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.assign_task();
      console.log(`Execution result of permission (assign_task for 13)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.execute_Task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.propose_Task_Delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.supply_Service()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr12Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr13Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO for 14)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy for 14)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr13Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature for 14)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation for 14)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.propose_campaign_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.launchCampaign()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.execute_Task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.propose_Task_Delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.supply_Service()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr13Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr14Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO for 15)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy for 15)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.transfer_tokens()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr14Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature for 15)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation for 15)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.assign_task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr14Connect.propose_campaign_budget();
      console.log(`Execution result of permission (propose_campaign_budget for 15)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.approve_project_budget()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.Post_Event()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      result = await addr14Connect.launchCampaign();
      console.log(`Execution result of permission (launchCampaign for 15)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.veto_proposal()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.execute_Task()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.propose_Task_Delegation()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.supply_Service()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
      
      await expect(addr14Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "Only authorized roles can execute this function."
      );
      
      
});
});
