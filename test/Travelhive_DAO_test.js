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
    const [owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr10, addr11, addr12, addr13, addr14] = await ethers.getSigners();
    const Travelhive_DAO = await ethers.deployContract("Travelhive_DAO");
    await Travelhive_DAO.waitForDeployment();

    return{Travelhive_DAO, owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr10, addr11, addr12, addr13, addr14};
 }
    
    it("Should set the right owner and initialize committees", async function (){
      const{Travelhive_DAO, owner, addr10  , addr11  , addr12  , addr13  , addr14  } = await loadFixture(deployTokenFixture);
      expect(await Travelhive_DAO.hasRole(owner.address)).to.equal(16393);
      // Initialize committees
      ownerConnect = Travelhive_DAO.connect(owner);
      const tx = await ownerConnect.initializeCommittees(addr10.address  , addr11.address  , addr12.address  , addr13.address  , addr14.address );
      await tx.wait();
      expect(tx).to.not.be.reverted;
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Travelhive_DAO, owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr10, addr11, addr12, addr13, addr14} = await loadFixture(deployTokenFixture);

    ownerConnect = Travelhive_DAO.connect(owner);
    
    addr0Connect = Travelhive_DAO.connect(addr0);
    
    addr1Connect = Travelhive_DAO.connect(addr1);
    
    addr2Connect = Travelhive_DAO.connect(addr2);
    
    addr3Connect = Travelhive_DAO.connect(addr3);
    
    addr4Connect = Travelhive_DAO.connect(addr4);
    
    addr5Connect = Travelhive_DAO.connect(addr5);
    
    addr6Connect = Travelhive_DAO.connect(addr6);
    
    addr7Connect = Travelhive_DAO.connect(addr7);
    
    addr8Connect = Travelhive_DAO.connect(addr8);
    
    addr10Connect = Travelhive_DAO.connect(addr10);
    
    addr11Connect = Travelhive_DAO.connect(addr11);
    
    addr12Connect = Travelhive_DAO.connect(addr12);
    
    addr13Connect = Travelhive_DAO.connect(addr13);
    
    addr14Connect = Travelhive_DAO.connect(addr14);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(16384, addr0);
      
      addressesByEntityValue.set(16641, addr1);
      
      addressesByEntityValue.set(16642, addr2);
      
      addressesByEntityValue.set(16643, addr3);
      
      addressesByEntityValue.set(16644, addr4);
      
      addressesByEntityValue.set(16645, addr5);
      
      addressesByEntityValue.set(16646, addr6);
      
      addressesByEntityValue.set(16647, addr7);
      
      addressesByEntityValue.set(540936, addr8);
      
      addressesByEntityValue.set(16393, owner);
      
      addressesByEntityValue.set(81930, addr10);
      
      addressesByEntityValue.set(81931, addr11);
      
      addressesByEntityValue.set(81932, addr12);
      
      addressesByEntityValue.set(81933, addr13);
      
      addressesByEntityValue.set(81934, addr14);
      

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
      
      result = await Travelhive_DAO.canControl(16384, 16384);
      console.log(`Result of canControl(16384, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16641);
      console.log(`Result of canControl(16384, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16642);
      console.log(`Result of canControl(16384, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16643);
      console.log(`Result of canControl(16384, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16644);
      console.log(`Result of canControl(16384, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16645);
      console.log(`Result of canControl(16384, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16646);
      console.log(`Result of canControl(16384, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16647);
      console.log(`Result of canControl(16384, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 540936);
      console.log(`Result of canControl(16384, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 16393);
      console.log(`Result of canControl(16384, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 81930);
      console.log(`Result of canControl(16384, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 81931);
      console.log(`Result of canControl(16384, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 81932);
      console.log(`Result of canControl(16384, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 81933);
      console.log(`Result of canControl(16384, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16384, 81934);
      console.log(`Result of canControl(16384, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16384);
      console.log(`Result of canControl(16641, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16641);
      console.log(`Result of canControl(16641, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16642);
      console.log(`Result of canControl(16641, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16643);
      console.log(`Result of canControl(16641, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16644);
      console.log(`Result of canControl(16641, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16645);
      console.log(`Result of canControl(16641, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16646);
      console.log(`Result of canControl(16641, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16647);
      console.log(`Result of canControl(16641, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 540936);
      console.log(`Result of canControl(16641, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 16393);
      console.log(`Result of canControl(16641, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 81930);
      console.log(`Result of canControl(16641, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 81931);
      console.log(`Result of canControl(16641, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 81932);
      console.log(`Result of canControl(16641, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 81933);
      console.log(`Result of canControl(16641, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16641, 81934);
      console.log(`Result of canControl(16641, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16384);
      console.log(`Result of canControl(16642, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16641);
      console.log(`Result of canControl(16642, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16642);
      console.log(`Result of canControl(16642, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16643);
      console.log(`Result of canControl(16642, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16644);
      console.log(`Result of canControl(16642, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16645);
      console.log(`Result of canControl(16642, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16646);
      console.log(`Result of canControl(16642, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16647);
      console.log(`Result of canControl(16642, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 540936);
      console.log(`Result of canControl(16642, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 16393);
      console.log(`Result of canControl(16642, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 81930);
      console.log(`Result of canControl(16642, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 81931);
      console.log(`Result of canControl(16642, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 81932);
      console.log(`Result of canControl(16642, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 81933);
      console.log(`Result of canControl(16642, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16642, 81934);
      console.log(`Result of canControl(16642, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 16384);
      console.log(`Result of canControl(16643, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 16641);
      console.log(`Result of canControl(16643, 16641):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16642);
      console.log(`Result of canControl(16643, 16642):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16643);
      console.log(`Result of canControl(16643, 16643):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16644);
      console.log(`Result of canControl(16643, 16644):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16645);
      console.log(`Result of canControl(16643, 16645):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16646);
      console.log(`Result of canControl(16643, 16646):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16647);
      console.log(`Result of canControl(16643, 16647):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 540936);
      console.log(`Result of canControl(16643, 540936):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16643, 16393);
      console.log(`Result of canControl(16643, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 81930);
      console.log(`Result of canControl(16643, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 81931);
      console.log(`Result of canControl(16643, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 81932);
      console.log(`Result of canControl(16643, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 81933);
      console.log(`Result of canControl(16643, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16643, 81934);
      console.log(`Result of canControl(16643, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16384);
      console.log(`Result of canControl(16644, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16641);
      console.log(`Result of canControl(16644, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16642);
      console.log(`Result of canControl(16644, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16643);
      console.log(`Result of canControl(16644, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16644);
      console.log(`Result of canControl(16644, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16645);
      console.log(`Result of canControl(16644, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16646);
      console.log(`Result of canControl(16644, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16647);
      console.log(`Result of canControl(16644, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 540936);
      console.log(`Result of canControl(16644, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 16393);
      console.log(`Result of canControl(16644, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 81930);
      console.log(`Result of canControl(16644, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 81931);
      console.log(`Result of canControl(16644, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 81932);
      console.log(`Result of canControl(16644, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 81933);
      console.log(`Result of canControl(16644, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16644, 81934);
      console.log(`Result of canControl(16644, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16384);
      console.log(`Result of canControl(16645, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16641);
      console.log(`Result of canControl(16645, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16642);
      console.log(`Result of canControl(16645, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16643);
      console.log(`Result of canControl(16645, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16644);
      console.log(`Result of canControl(16645, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16645);
      console.log(`Result of canControl(16645, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16646);
      console.log(`Result of canControl(16645, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16647);
      console.log(`Result of canControl(16645, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 540936);
      console.log(`Result of canControl(16645, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 16393);
      console.log(`Result of canControl(16645, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 81930);
      console.log(`Result of canControl(16645, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 81931);
      console.log(`Result of canControl(16645, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 81932);
      console.log(`Result of canControl(16645, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 81933);
      console.log(`Result of canControl(16645, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16645, 81934);
      console.log(`Result of canControl(16645, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16384);
      console.log(`Result of canControl(16646, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16641);
      console.log(`Result of canControl(16646, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16642);
      console.log(`Result of canControl(16646, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16643);
      console.log(`Result of canControl(16646, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16644);
      console.log(`Result of canControl(16646, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16645);
      console.log(`Result of canControl(16646, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16646);
      console.log(`Result of canControl(16646, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16647);
      console.log(`Result of canControl(16646, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 540936);
      console.log(`Result of canControl(16646, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 16393);
      console.log(`Result of canControl(16646, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 81930);
      console.log(`Result of canControl(16646, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 81931);
      console.log(`Result of canControl(16646, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 81932);
      console.log(`Result of canControl(16646, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 81933);
      console.log(`Result of canControl(16646, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16646, 81934);
      console.log(`Result of canControl(16646, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16384);
      console.log(`Result of canControl(16647, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16641);
      console.log(`Result of canControl(16647, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16642);
      console.log(`Result of canControl(16647, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16643);
      console.log(`Result of canControl(16647, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16644);
      console.log(`Result of canControl(16647, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16645);
      console.log(`Result of canControl(16647, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16646);
      console.log(`Result of canControl(16647, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16647);
      console.log(`Result of canControl(16647, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 540936);
      console.log(`Result of canControl(16647, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 16393);
      console.log(`Result of canControl(16647, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 81930);
      console.log(`Result of canControl(16647, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 81931);
      console.log(`Result of canControl(16647, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 81932);
      console.log(`Result of canControl(16647, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 81933);
      console.log(`Result of canControl(16647, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16647, 81934);
      console.log(`Result of canControl(16647, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16384);
      console.log(`Result of canControl(540936, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16641);
      console.log(`Result of canControl(540936, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16642);
      console.log(`Result of canControl(540936, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16643);
      console.log(`Result of canControl(540936, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16644);
      console.log(`Result of canControl(540936, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16645);
      console.log(`Result of canControl(540936, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16646);
      console.log(`Result of canControl(540936, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16647);
      console.log(`Result of canControl(540936, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 540936);
      console.log(`Result of canControl(540936, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 16393);
      console.log(`Result of canControl(540936, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 81930);
      console.log(`Result of canControl(540936, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 81931);
      console.log(`Result of canControl(540936, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 81932);
      console.log(`Result of canControl(540936, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 81933);
      console.log(`Result of canControl(540936, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(540936, 81934);
      console.log(`Result of canControl(540936, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(16393, 16384);
      console.log(`Result of canControl(16393, 16384):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16641);
      console.log(`Result of canControl(16393, 16641):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16642);
      console.log(`Result of canControl(16393, 16642):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16643);
      console.log(`Result of canControl(16393, 16643):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16644);
      console.log(`Result of canControl(16393, 16644):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16645);
      console.log(`Result of canControl(16393, 16645):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16646);
      console.log(`Result of canControl(16393, 16646):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16647);
      console.log(`Result of canControl(16393, 16647):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 540936);
      console.log(`Result of canControl(16393, 540936):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 16393);
      console.log(`Result of canControl(16393, 16393):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 81930);
      console.log(`Result of canControl(16393, 81930):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 81931);
      console.log(`Result of canControl(16393, 81931):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 81932);
      console.log(`Result of canControl(16393, 81932):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 81933);
      console.log(`Result of canControl(16393, 81933):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(16393, 81934);
      console.log(`Result of canControl(16393, 81934):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81930, 16384);
      console.log(`Result of canControl(81930, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16641);
      console.log(`Result of canControl(81930, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16642);
      console.log(`Result of canControl(81930, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16643);
      console.log(`Result of canControl(81930, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16644);
      console.log(`Result of canControl(81930, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16645);
      console.log(`Result of canControl(81930, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16646);
      console.log(`Result of canControl(81930, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16647);
      console.log(`Result of canControl(81930, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 540936);
      console.log(`Result of canControl(81930, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 16393);
      console.log(`Result of canControl(81930, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 81930);
      console.log(`Result of canControl(81930, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 81931);
      console.log(`Result of canControl(81930, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 81932);
      console.log(`Result of canControl(81930, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 81933);
      console.log(`Result of canControl(81930, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81930, 81934);
      console.log(`Result of canControl(81930, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16384);
      console.log(`Result of canControl(81931, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16641);
      console.log(`Result of canControl(81931, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16642);
      console.log(`Result of canControl(81931, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16643);
      console.log(`Result of canControl(81931, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16644);
      console.log(`Result of canControl(81931, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16645);
      console.log(`Result of canControl(81931, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16646);
      console.log(`Result of canControl(81931, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16647);
      console.log(`Result of canControl(81931, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 540936);
      console.log(`Result of canControl(81931, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 16393);
      console.log(`Result of canControl(81931, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81931, 81930);
      console.log(`Result of canControl(81931, 81930):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81931, 81931);
      console.log(`Result of canControl(81931, 81931):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81931, 81932);
      console.log(`Result of canControl(81931, 81932):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81931, 81933);
      console.log(`Result of canControl(81931, 81933):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81931, 81934);
      console.log(`Result of canControl(81931, 81934):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81932, 16384);
      console.log(`Result of canControl(81932, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16641);
      console.log(`Result of canControl(81932, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16642);
      console.log(`Result of canControl(81932, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16643);
      console.log(`Result of canControl(81932, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16644);
      console.log(`Result of canControl(81932, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16645);
      console.log(`Result of canControl(81932, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16646);
      console.log(`Result of canControl(81932, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16647);
      console.log(`Result of canControl(81932, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 540936);
      console.log(`Result of canControl(81932, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 16393);
      console.log(`Result of canControl(81932, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 81930);
      console.log(`Result of canControl(81932, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 81931);
      console.log(`Result of canControl(81932, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 81932);
      console.log(`Result of canControl(81932, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 81933);
      console.log(`Result of canControl(81932, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81932, 81934);
      console.log(`Result of canControl(81932, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16384);
      console.log(`Result of canControl(81933, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16641);
      console.log(`Result of canControl(81933, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16642);
      console.log(`Result of canControl(81933, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16643);
      console.log(`Result of canControl(81933, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16644);
      console.log(`Result of canControl(81933, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16645);
      console.log(`Result of canControl(81933, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16646);
      console.log(`Result of canControl(81933, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16647);
      console.log(`Result of canControl(81933, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 540936);
      console.log(`Result of canControl(81933, 540936):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 16393);
      console.log(`Result of canControl(81933, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 81930);
      console.log(`Result of canControl(81933, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 81931);
      console.log(`Result of canControl(81933, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 81932);
      console.log(`Result of canControl(81933, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 81933);
      console.log(`Result of canControl(81933, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81933, 81934);
      console.log(`Result of canControl(81933, 81934):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16384);
      console.log(`Result of canControl(81934, 16384):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16641);
      console.log(`Result of canControl(81934, 16641):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16642);
      console.log(`Result of canControl(81934, 16642):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16643);
      console.log(`Result of canControl(81934, 16643):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16644);
      console.log(`Result of canControl(81934, 16644):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16645);
      console.log(`Result of canControl(81934, 16645):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16646);
      console.log(`Result of canControl(81934, 16646):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 16647);
      console.log(`Result of canControl(81934, 16647):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 540936);
      console.log(`Result of canControl(81934, 540936):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(81934, 16393);
      console.log(`Result of canControl(81934, 16393):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 81930);
      console.log(`Result of canControl(81934, 81930):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 81931);
      console.log(`Result of canControl(81934, 81931):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 81932);
      console.log(`Result of canControl(81934, 81932):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 81933);
      console.log(`Result of canControl(81934, 81933):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(81934, 81934);
      console.log(`Result of canControl(81934, 81934):`, result);
      expect(result).to.equal( false );
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      await expect(addr0Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr0Connect.veto_proposal();
      //console.log(`Execution result of permission (veto_proposal for 16384):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr0Connect.execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.Post_Event();
      //console.log(`Execution result of permission (Post_Event for 16641):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16641):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16641):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16641):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16641):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16642):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16642):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16642):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16642):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.veto_proposal();
      //console.log(`Execution result of permission (veto_proposal for 16643):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16643):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16643):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16643):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16643):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.verify_Institutional_Profile();
      //console.log(`Execution result of permission (verify_Institutional_Profile for 16644):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.appoint_Destination_Committee();
      //console.log(`Execution result of permission (appoint_Destination_Committee for 16644):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16644):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16644):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16644):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16644):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16645):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16645):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16645):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16645):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16646):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16646):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16646):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16646):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16647):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16647):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16647):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16647):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr8Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr8Connect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 540936):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 540936):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 540936):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 540936):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.create_new_DDMO();
      //console.log(`Execution result of permission (create_new_DDMO for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.modify_salary_distribution_policy();
      //console.log(`Execution result of permission (modify_salary_distribution_policy for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.transfer_tokens();
      //console.log(`Execution result of permission (transfer_tokens for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_platform_feature();
      //console.log(`Execution result of permission (upgrade_platform_feature for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.activate_role_delegation();
      //console.log(`Execution result of permission (activate_role_delegation for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.assign_task();
      //console.log(`Execution result of permission (assign_task for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.cut_funding_to_project_budget();
      //console.log(`Execution result of permission (cut_funding_to_project_budget for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_campaign_budget();
      //console.log(`Execution result of permission (propose_campaign_budget for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.approve_project_budget();
      //console.log(`Execution result of permission (approve_project_budget for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Post_Event();
      //console.log(`Execution result of permission (Post_Event for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.verify_Institutional_Profile();
      //console.log(`Execution result of permission (verify_Institutional_Profile for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.launchCampaign();
      //console.log(`Execution result of permission (launchCampaign for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.appoint_Destination_Committee();
      //console.log(`Execution result of permission (appoint_Destination_Committee for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.veto_proposal();
      //console.log(`Execution result of permission (veto_proposal for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.execute_Task();
      //console.log(`Execution result of permission (execute_Task for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_Task_Delegation();
      //console.log(`Execution result of permission (propose_Task_Delegation for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.supply_Service();
      //console.log(`Execution result of permission (supply_Service for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.apply_For_DAO_Governance_Role();
      //console.log(`Execution result of permission (apply_For_DAO_Governance_Role for 16393):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.create_new_DDMO();
      //console.log(`Execution result of permission (create_new_DDMO for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.modify_salary_distribution_policy();
      //console.log(`Execution result of permission (modify_salary_distribution_policy for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.transfer_tokens();
      //console.log(`Execution result of permission (transfer_tokens for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.upgrade_platform_feature();
      //console.log(`Execution result of permission (upgrade_platform_feature for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.activate_role_delegation();
      //console.log(`Execution result of permission (activate_role_delegation for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.cut_funding_to_project_budget();
      //console.log(`Execution result of permission (cut_funding_to_project_budget for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.approve_project_budget();
      //console.log(`Execution result of permission (approve_project_budget for 81930):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.create_new_DDMO();
      //console.log(`Execution result of permission (create_new_DDMO for 81931):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.modify_salary_distribution_policy();
      //console.log(`Execution result of permission (modify_salary_distribution_policy for 81931):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.upgrade_platform_feature();
      //console.log(`Execution result of permission (upgrade_platform_feature for 81931):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.activate_role_delegation();
      //console.log(`Execution result of permission (activate_role_delegation for 81931):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.create_new_DDMO();
      //console.log(`Execution result of permission (create_new_DDMO for 81932):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.modify_salary_distribution_policy();
      //console.log(`Execution result of permission (modify_salary_distribution_policy for 81932):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.upgrade_platform_feature();
      //console.log(`Execution result of permission (upgrade_platform_feature for 81932):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.activate_role_delegation();
      //console.log(`Execution result of permission (activate_role_delegation for 81932):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.assign_task();
      //console.log(`Execution result of permission (assign_task for 81932):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.create_new_DDMO();
      //console.log(`Execution result of permission (create_new_DDMO for 81933):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.modify_salary_distribution_policy();
      //console.log(`Execution result of permission (modify_salary_distribution_policy for 81933):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.upgrade_platform_feature();
      //console.log(`Execution result of permission (upgrade_platform_feature for 81933):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.activate_role_delegation();
      //console.log(`Execution result of permission (activate_role_delegation for 81933):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.launchCampaign()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr14Connect.create_new_DDMO();
      //console.log(`Execution result of permission (create_new_DDMO for 81934):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.modify_salary_distribution_policy();
      //console.log(`Execution result of permission (modify_salary_distribution_policy for 81934):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr14Connect.upgrade_platform_feature();
      //console.log(`Execution result of permission (upgrade_platform_feature for 81934):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.activate_role_delegation();
      //console.log(`Execution result of permission (activate_role_delegation for 81934):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.cut_funding_to_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr14Connect.propose_campaign_budget();
      //console.log(`Execution result of permission (propose_campaign_budget for 81934):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.Post_Event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.verify_Institutional_Profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr14Connect.launchCampaign();
      //console.log(`Execution result of permission (launchCampaign for 81934):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr14Connect.appoint_Destination_Committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.veto_proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr14Connect.apply_For_DAO_Governance_Role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
});
});
