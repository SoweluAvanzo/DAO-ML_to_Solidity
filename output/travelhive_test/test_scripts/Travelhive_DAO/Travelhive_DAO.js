//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("Travelhive_DAO Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployFixture(){
    const [owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr9, addr10, addr11, addr12, addr13] = await ethers.getSigners();
    const Travelhive_DAO = await ethers.deployContract("Travelhive_DAO");
    await Travelhive_DAO.waitForDeployment();

    return{Travelhive_DAO, owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr9, addr10, addr11, addr12, addr13};
 }
    it("Should set the right owner and initialize committees", async function (){
      const{Travelhive_DAO, owner, addr9  , addr10  , addr11  , addr12  , addr13  } = await loadFixture(deployFixture);
      expect(await Travelhive_DAO.hasRole(owner.address)).to.equal(8200);
      // Initialize committees
      ownerConnect = Travelhive_DAO.connect(owner);

      const tx = await ownerConnect.initializeCommittees(addr9.address  , addr10.address  , addr11.address  , addr12.address  , addr13.address );
      await tx.wait();
      expect(tx).to.not.be.reverted;
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Travelhive_DAO, owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr9, addr10, addr11, addr12, addr13} = await loadFixture(deployFixture);

    ownerConnect = Travelhive_DAO.connect(owner);
    
    addr0Connect = Travelhive_DAO.connect(addr0);
    
    addr1Connect = Travelhive_DAO.connect(addr1);
    
    addr2Connect = Travelhive_DAO.connect(addr2);
    
    addr3Connect = Travelhive_DAO.connect(addr3);
    
    addr4Connect = Travelhive_DAO.connect(addr4);
    
    addr5Connect = Travelhive_DAO.connect(addr5);
    
    addr6Connect = Travelhive_DAO.connect(addr6);
    
    addr7Connect = Travelhive_DAO.connect(addr7);
    
    addr9Connect = Travelhive_DAO.connect(addr9);
    
    addr10Connect = Travelhive_DAO.connect(addr10);
    
    addr11Connect = Travelhive_DAO.connect(addr11);
    
    addr12Connect = Travelhive_DAO.connect(addr12);
    
    addr13Connect = Travelhive_DAO.connect(addr13);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(24576, addr0);
      
      addressesByEntityValue.set(24577, addr1);
      
      addressesByEntityValue.set(24578, addr2);
      
      addressesByEntityValue.set(24579, addr3);
      
      addressesByEntityValue.set(24580, addr4);
      
      addressesByEntityValue.set(24581, addr5);
      
      addressesByEntityValue.set(24582, addr6);
      
      addressesByEntityValue.set(24583, addr7);
      
      addressesByEntityValue.set(8200, owner);
      
      addressesByEntityValue.set(24585, addr9);
      
      addressesByEntityValue.set(24586, addr10);
      
      addressesByEntityValue.set(24587, addr11);
      
      addressesByEntityValue.set(24588, addr12);
      
      addressesByEntityValue.set(24589, addr13);
      

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
      
      result = await Travelhive_DAO.canControl(24576, 24576);
      console.log(`Result of canControl(Advisor, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24577);
      console.log(`Result of canControl(Advisor, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24578);
      console.log(`Result of canControl(Advisor, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24579);
      console.log(`Result of canControl(Advisor, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24580);
      console.log(`Result of canControl(Advisor, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24581);
      console.log(`Result of canControl(Advisor, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24582);
      console.log(`Result of canControl(Advisor, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24583);
      console.log(`Result of canControl(Advisor, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 8200);
      console.log(`Result of canControl(Advisor, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24585);
      console.log(`Result of canControl(Advisor, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24586);
      console.log(`Result of canControl(Advisor, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24587);
      console.log(`Result of canControl(Advisor, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24588);
      console.log(`Result of canControl(Advisor, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24576, 24589);
      console.log(`Result of canControl(Advisor, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24576);
      console.log(`Result of canControl(Founder, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24577);
      console.log(`Result of canControl(Founder, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24578);
      console.log(`Result of canControl(Founder, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24579);
      console.log(`Result of canControl(Founder, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24580);
      console.log(`Result of canControl(Founder, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24581);
      console.log(`Result of canControl(Founder, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24582);
      console.log(`Result of canControl(Founder, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24583);
      console.log(`Result of canControl(Founder, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 8200);
      console.log(`Result of canControl(Founder, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24585);
      console.log(`Result of canControl(Founder, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24586);
      console.log(`Result of canControl(Founder, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24587);
      console.log(`Result of canControl(Founder, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24588);
      console.log(`Result of canControl(Founder, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24577, 24589);
      console.log(`Result of canControl(Founder, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24576);
      console.log(`Result of canControl(Master_Node, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24577);
      console.log(`Result of canControl(Master_Node, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24578);
      console.log(`Result of canControl(Master_Node, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24579);
      console.log(`Result of canControl(Master_Node, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24580);
      console.log(`Result of canControl(Master_Node, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24581);
      console.log(`Result of canControl(Master_Node, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24582);
      console.log(`Result of canControl(Master_Node, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24583);
      console.log(`Result of canControl(Master_Node, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 8200);
      console.log(`Result of canControl(Master_Node, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24585);
      console.log(`Result of canControl(Master_Node, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24586);
      console.log(`Result of canControl(Master_Node, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24587);
      console.log(`Result of canControl(Master_Node, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24588);
      console.log(`Result of canControl(Master_Node, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24578, 24589);
      console.log(`Result of canControl(Master_Node, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24576);
      console.log(`Result of canControl(Marketing_Delegate, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24577);
      console.log(`Result of canControl(Marketing_Delegate, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24578);
      console.log(`Result of canControl(Marketing_Delegate, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24579);
      console.log(`Result of canControl(Marketing_Delegate, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24580);
      console.log(`Result of canControl(Marketing_Delegate, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24581);
      console.log(`Result of canControl(Marketing_Delegate, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24582);
      console.log(`Result of canControl(Marketing_Delegate, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24583);
      console.log(`Result of canControl(Marketing_Delegate, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 8200);
      console.log(`Result of canControl(Marketing_Delegate, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24585);
      console.log(`Result of canControl(Marketing_Delegate, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24586);
      console.log(`Result of canControl(Marketing_Delegate, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24587);
      console.log(`Result of canControl(Marketing_Delegate, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24588);
      console.log(`Result of canControl(Marketing_Delegate, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24579, 24589);
      console.log(`Result of canControl(Marketing_Delegate, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24576);
      console.log(`Result of canControl(Investor, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24577);
      console.log(`Result of canControl(Investor, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24578);
      console.log(`Result of canControl(Investor, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24579);
      console.log(`Result of canControl(Investor, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24580);
      console.log(`Result of canControl(Investor, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24581);
      console.log(`Result of canControl(Investor, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24582);
      console.log(`Result of canControl(Investor, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24583);
      console.log(`Result of canControl(Investor, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 8200);
      console.log(`Result of canControl(Investor, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24585);
      console.log(`Result of canControl(Investor, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24586);
      console.log(`Result of canControl(Investor, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24587);
      console.log(`Result of canControl(Investor, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24588);
      console.log(`Result of canControl(Investor, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24580, 24589);
      console.log(`Result of canControl(Investor, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24576);
      console.log(`Result of canControl(Developer, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24577);
      console.log(`Result of canControl(Developer, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24578);
      console.log(`Result of canControl(Developer, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24579);
      console.log(`Result of canControl(Developer, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24580);
      console.log(`Result of canControl(Developer, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24581);
      console.log(`Result of canControl(Developer, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24582);
      console.log(`Result of canControl(Developer, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24583);
      console.log(`Result of canControl(Developer, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 8200);
      console.log(`Result of canControl(Developer, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24585);
      console.log(`Result of canControl(Developer, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24586);
      console.log(`Result of canControl(Developer, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24587);
      console.log(`Result of canControl(Developer, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24588);
      console.log(`Result of canControl(Developer, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24581, 24589);
      console.log(`Result of canControl(Developer, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24576);
      console.log(`Result of canControl(Ambassador, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24577);
      console.log(`Result of canControl(Ambassador, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24578);
      console.log(`Result of canControl(Ambassador, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24579);
      console.log(`Result of canControl(Ambassador, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24580);
      console.log(`Result of canControl(Ambassador, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24581);
      console.log(`Result of canControl(Ambassador, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24582);
      console.log(`Result of canControl(Ambassador, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24583);
      console.log(`Result of canControl(Ambassador, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 8200);
      console.log(`Result of canControl(Ambassador, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24585);
      console.log(`Result of canControl(Ambassador, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24586);
      console.log(`Result of canControl(Ambassador, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24587);
      console.log(`Result of canControl(Ambassador, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24588);
      console.log(`Result of canControl(Ambassador, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24582, 24589);
      console.log(`Result of canControl(Ambassador, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24576);
      console.log(`Result of canControl(DAO_Member, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24577);
      console.log(`Result of canControl(DAO_Member, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24578);
      console.log(`Result of canControl(DAO_Member, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24579);
      console.log(`Result of canControl(DAO_Member, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24580);
      console.log(`Result of canControl(DAO_Member, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24581);
      console.log(`Result of canControl(DAO_Member, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24582);
      console.log(`Result of canControl(DAO_Member, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24583);
      console.log(`Result of canControl(DAO_Member, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 8200);
      console.log(`Result of canControl(DAO_Member, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24585);
      console.log(`Result of canControl(DAO_Member, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24586);
      console.log(`Result of canControl(DAO_Member, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24587);
      console.log(`Result of canControl(DAO_Member, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24588);
      console.log(`Result of canControl(DAO_Member, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24583, 24589);
      console.log(`Result of canControl(DAO_Member, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(8200, 24576);
      console.log(`Result of canControl(Travelhive_DAOOwner, Advisor):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24577);
      console.log(`Result of canControl(Travelhive_DAOOwner, Founder):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24578);
      console.log(`Result of canControl(Travelhive_DAOOwner, Master_Node):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24579);
      console.log(`Result of canControl(Travelhive_DAOOwner, Marketing_Delegate):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24580);
      console.log(`Result of canControl(Travelhive_DAOOwner, Investor):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24581);
      console.log(`Result of canControl(Travelhive_DAOOwner, Developer):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24582);
      console.log(`Result of canControl(Travelhive_DAOOwner, Ambassador):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24583);
      console.log(`Result of canControl(Travelhive_DAOOwner, DAO_Member):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 8200);
      console.log(`Result of canControl(Travelhive_DAOOwner, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24585);
      console.log(`Result of canControl(Travelhive_DAOOwner, DAO_Council):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24586);
      console.log(`Result of canControl(Travelhive_DAOOwner, Marketing_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24587);
      console.log(`Result of canControl(Travelhive_DAOOwner, Financial_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24588);
      console.log(`Result of canControl(Travelhive_DAOOwner, Travelware_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(8200, 24589);
      console.log(`Result of canControl(Travelhive_DAOOwner, Development_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24576);
      console.log(`Result of canControl(DAO_Council, Advisor):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24577);
      console.log(`Result of canControl(DAO_Council, Founder):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24578);
      console.log(`Result of canControl(DAO_Council, Master_Node):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24579);
      console.log(`Result of canControl(DAO_Council, Marketing_Delegate):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24580);
      console.log(`Result of canControl(DAO_Council, Investor):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24581);
      console.log(`Result of canControl(DAO_Council, Developer):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24582);
      console.log(`Result of canControl(DAO_Council, Ambassador):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24583);
      console.log(`Result of canControl(DAO_Council, DAO_Member):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 8200);
      console.log(`Result of canControl(DAO_Council, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24585, 24585);
      console.log(`Result of canControl(DAO_Council, DAO_Council):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24586);
      console.log(`Result of canControl(DAO_Council, Marketing_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24587);
      console.log(`Result of canControl(DAO_Council, Financial_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24588);
      console.log(`Result of canControl(DAO_Council, Travelware_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24585, 24589);
      console.log(`Result of canControl(DAO_Council, Development_Board):`, result);
      expect(result).to.equal( true );
      
      result = await Travelhive_DAO.canControl(24586, 24576);
      console.log(`Result of canControl(Marketing_Board, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24577);
      console.log(`Result of canControl(Marketing_Board, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24578);
      console.log(`Result of canControl(Marketing_Board, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24579);
      console.log(`Result of canControl(Marketing_Board, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24580);
      console.log(`Result of canControl(Marketing_Board, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24581);
      console.log(`Result of canControl(Marketing_Board, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24582);
      console.log(`Result of canControl(Marketing_Board, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24583);
      console.log(`Result of canControl(Marketing_Board, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 8200);
      console.log(`Result of canControl(Marketing_Board, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24585);
      console.log(`Result of canControl(Marketing_Board, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24586);
      console.log(`Result of canControl(Marketing_Board, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24587);
      console.log(`Result of canControl(Marketing_Board, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24588);
      console.log(`Result of canControl(Marketing_Board, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24586, 24589);
      console.log(`Result of canControl(Marketing_Board, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24576);
      console.log(`Result of canControl(Financial_Board, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24577);
      console.log(`Result of canControl(Financial_Board, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24578);
      console.log(`Result of canControl(Financial_Board, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24579);
      console.log(`Result of canControl(Financial_Board, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24580);
      console.log(`Result of canControl(Financial_Board, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24581);
      console.log(`Result of canControl(Financial_Board, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24582);
      console.log(`Result of canControl(Financial_Board, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24583);
      console.log(`Result of canControl(Financial_Board, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 8200);
      console.log(`Result of canControl(Financial_Board, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24585);
      console.log(`Result of canControl(Financial_Board, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24586);
      console.log(`Result of canControl(Financial_Board, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24587);
      console.log(`Result of canControl(Financial_Board, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24588);
      console.log(`Result of canControl(Financial_Board, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24587, 24589);
      console.log(`Result of canControl(Financial_Board, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24576);
      console.log(`Result of canControl(Travelware_Board, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24577);
      console.log(`Result of canControl(Travelware_Board, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24578);
      console.log(`Result of canControl(Travelware_Board, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24579);
      console.log(`Result of canControl(Travelware_Board, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24580);
      console.log(`Result of canControl(Travelware_Board, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24581);
      console.log(`Result of canControl(Travelware_Board, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24582);
      console.log(`Result of canControl(Travelware_Board, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24583);
      console.log(`Result of canControl(Travelware_Board, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 8200);
      console.log(`Result of canControl(Travelware_Board, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24585);
      console.log(`Result of canControl(Travelware_Board, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24586);
      console.log(`Result of canControl(Travelware_Board, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24587);
      console.log(`Result of canControl(Travelware_Board, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24588);
      console.log(`Result of canControl(Travelware_Board, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24588, 24589);
      console.log(`Result of canControl(Travelware_Board, Development_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24576);
      console.log(`Result of canControl(Development_Board, Advisor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24577);
      console.log(`Result of canControl(Development_Board, Founder):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24578);
      console.log(`Result of canControl(Development_Board, Master_Node):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24579);
      console.log(`Result of canControl(Development_Board, Marketing_Delegate):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24580);
      console.log(`Result of canControl(Development_Board, Investor):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24581);
      console.log(`Result of canControl(Development_Board, Developer):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24582);
      console.log(`Result of canControl(Development_Board, Ambassador):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24583);
      console.log(`Result of canControl(Development_Board, DAO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 8200);
      console.log(`Result of canControl(Development_Board, Travelhive_DAOOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24585);
      console.log(`Result of canControl(Development_Board, DAO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24586);
      console.log(`Result of canControl(Development_Board, Marketing_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24587);
      console.log(`Result of canControl(Development_Board, Financial_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24588);
      console.log(`Result of canControl(Development_Board, Travelware_Board):`, result);
      expect(result).to.equal( false );
      
      result = await Travelhive_DAO.canControl(24589, 24589);
      console.log(`Result of canControl(Development_Board, Development_Board):`, result);
      expect(result).to.equal( false );
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      await expect(addr0Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr0Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Advisor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr0Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Advisor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr0Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr0Connect.Veto_Proposal();
      console.log(`Execution result of permission (Veto_Proposal by Advisor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr0Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Advisor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr0Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr0Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Advisor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Founder)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Founder)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.Veto_Proposal();
      console.log(`Execution result of permission (Veto_Proposal by Founder)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Founder)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Founder)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Master_Node)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Master_Node)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Master_Node)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Master_Node)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Marketing_Delegate)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Marketing_Delegate)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.post_event();
      console.log(`Execution result of permission (post_event by Marketing_Delegate)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Marketing_Delegate)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Marketing_Delegate)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Investor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Investor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Investor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Investor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Developer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Developer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Developer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Developer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.supply_service();
      console.log(`Execution result of permission (supply_service by Ambassador)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.execute_task();
      console.log(`Execution result of permission (execute_task by Ambassador)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.verify_institutional_profile();
      console.log(`Execution result of permission (verify_institutional_profile by Ambassador)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.appoint_destination_committee();
      console.log(`Execution result of permission (appoint_destination_committee by Ambassador)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Ambassador)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Ambassador)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.upgrade_platform_feature()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.Modify_salary_distribution_policy()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.supply_service();
      console.log(`Execution result of permission (supply_service by DAO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.execute_task();
      console.log(`Execution result of permission (execute_task by DAO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.create_new_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by DAO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.activate_role_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by DAO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.transfer_tokens();
      console.log(`Execution result of permission (transfer_tokens by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.approve_project_budget();
      console.log(`Execution result of permission (approve_project_budget by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.cut_project_funding();
      console.log(`Execution result of permission (cut_project_funding by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Modify_salary_distribution_policy();
      console.log(`Execution result of permission (Modify_salary_distribution_policy by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.supply_service();
      console.log(`Execution result of permission (supply_service by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.execute_task();
      console.log(`Execution result of permission (execute_task by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.assign_task();
      console.log(`Execution result of permission (assign_task by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.post_event();
      console.log(`Execution result of permission (post_event by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.verify_institutional_profile();
      console.log(`Execution result of permission (verify_institutional_profile by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.appoint_destination_committee();
      console.log(`Execution result of permission (appoint_destination_committee by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_campaign_budget();
      console.log(`Execution result of permission (propose_campaign_budget by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Veto_Proposal();
      console.log(`Execution result of permission (Veto_Proposal by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.apply_for_governance_role();
      console.log(`Execution result of permission (apply_for_governance_role by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.request_task_delegation();
      console.log(`Execution result of permission (request_task_delegation by Travelhive_DAOOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy by DAO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature by DAO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.Modify_salary_distribution_policy();
      console.log(`Execution result of permission (Modify_salary_distribution_policy by DAO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.supply_service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.execute_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO by DAO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.apply_for_governance_role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation by DAO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.request_task_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy by Marketing_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature by Marketing_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.Modify_salary_distribution_policy();
      console.log(`Execution result of permission (Modify_salary_distribution_policy by Marketing_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.supply_service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.execute_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO by Marketing_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.propose_campaign_budget();
      console.log(`Execution result of permission (propose_campaign_budget by Marketing_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr10Connect.apply_for_governance_role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr10Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation by Marketing_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr10Connect.request_task_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.transfer_tokens();
      console.log(`Execution result of permission (transfer_tokens by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.approve_project_budget();
      console.log(`Execution result of permission (approve_project_budget by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.cut_project_funding();
      console.log(`Execution result of permission (cut_project_funding by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.Modify_salary_distribution_policy();
      console.log(`Execution result of permission (Modify_salary_distribution_policy by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.supply_service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.execute_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.apply_for_governance_role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation by Financial_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.request_task_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy by Travelware_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature by Travelware_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.Modify_salary_distribution_policy();
      console.log(`Execution result of permission (Modify_salary_distribution_policy by Travelware_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.supply_service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.execute_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.assign_task();
      console.log(`Execution result of permission (assign_task by Travelware_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO by Travelware_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr12Connect.apply_for_governance_role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr12Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation by Travelware_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr12Connect.request_task_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.modify_salary_distribution_policy();
      console.log(`Execution result of permission (modify_salary_distribution_policy by Development_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.upgrade_platform_feature();
      console.log(`Execution result of permission (upgrade_platform_feature by Development_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.transfer_tokens()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.approve_project_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.cut_project_funding()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.Modify_salary_distribution_policy();
      console.log(`Execution result of permission (Modify_salary_distribution_policy by Development_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.supply_service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.execute_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.assign_task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.post_event()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.verify_institutional_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.appoint_destination_committee()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.create_new_DDMO();
      console.log(`Execution result of permission (create_new_DDMO by Development_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.propose_campaign_budget()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.Veto_Proposal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr13Connect.apply_for_governance_role()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr13Connect.activate_role_delegation();
      console.log(`Execution result of permission (activate_role_delegation by Development_Board)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr13Connect.request_task_delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
});
});
