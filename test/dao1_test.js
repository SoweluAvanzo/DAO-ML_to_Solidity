// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("dao1 Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployTokenFixture(){
    const [owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20] = await ethers.getSigners();
    const dao1 = await ethers.deployContract("dao1");
    await dao1.waitForDeployment();

    return{dao1, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20};
 }
    
    it("Should set the right owner", async function (){
      const{dao1, owner} = await loadFixture(deployTokenFixture);
      expect(await dao1.hasRole(owner.address)).to.equal(20);
      // Initialize committees
      const tx = await ownerConnect.initializeCommittees();
      await tx.wait();
      expect(tx).to.not.be.reverted;
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{dao1, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20} = await loadFixture(deployTokenFixture);

    ownerConnect = dao1.connect(owner);
    
    addr1Connect = dao1.connect(addr1);
    
    addr2Connect = dao1.connect(addr2);
    
    addr3Connect = dao1.connect(addr3);
    
    addr4Connect = dao1.connect(addr4);
    
    addr5Connect = dao1.connect(addr5);
    
    addr6Connect = dao1.connect(addr6);
    
    addr7Connect = dao1.connect(addr7);
    
    addr8Connect = dao1.connect(addr8);
    
    addr9Connect = dao1.connect(addr9);
    
    addr10Connect = dao1.connect(addr10);
    
    addr11Connect = dao1.connect(addr11);
    
    addr12Connect = dao1.connect(addr12);
    
    addr13Connect = dao1.connect(addr13);
    
    addr14Connect = dao1.connect(addr14);
    
    addr15Connect = dao1.connect(addr15);
    
    addr16Connect = dao1.connect(addr16);
    
    addr17Connect = dao1.connect(addr17);
    
    addr18Connect = dao1.connect(addr18);
    
    addr19Connect = dao1.connect(addr19);
    
    addr20Connect = dao1.connect(addr20);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(20, owner);
      
      addressesByEntityValue.set(62865152, addr1);
      
      addressesByEntityValue.set(38318401, addr2);
      
      addressesByEntityValue.set(46135426, addr3);
      
      addressesByEntityValue.set(59899331, addr4);
      
      addressesByEntityValue.set(907588, addr5);
      
      addressesByEntityValue.set(42981317, addr6);
      
      addressesByEntityValue.set(50064774, addr7);
      
      addressesByEntityValue.set(16195527, addr8);
      
      addressesByEntityValue.set(17545928, addr9);
      
      addressesByEntityValue.set(32399305, addr10);
      
      addressesByEntityValue.set(49980106, addr11);
      
      addressesByEntityValue.set(60415691, addr12);
      
      addressesByEntityValue.set(48889804, addr13);
      
      addressesByEntityValue.set(60223053, addr14);
      
      addressesByEntityValue.set(23575438, addr15);
      
      addressesByEntityValue.set(55137231, addr16);
      
      addressesByEntityValue.set(60096464, addr17);
      
      addressesByEntityValue.set(56535825, addr18);
      
      addressesByEntityValue.set(35586002, addr19);
      
      addressesByEntityValue.set(25026515, addr20);
      

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
      
      result = await dao1.canControl(62865152, 62865152);
      console.log(`Result of canControl(62865152, 62865152):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(62865152, 38318401);
      console.log(`Result of canControl(62865152, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 46135426);
      console.log(`Result of canControl(62865152, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(62865152, 59899331);
      console.log(`Result of canControl(62865152, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 907588);
      console.log(`Result of canControl(62865152, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 42981317);
      console.log(`Result of canControl(62865152, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 50064774);
      console.log(`Result of canControl(62865152, 50064774):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(62865152, 16195527);
      console.log(`Result of canControl(62865152, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 17545928);
      console.log(`Result of canControl(62865152, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 32399305);
      console.log(`Result of canControl(62865152, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 49980106);
      console.log(`Result of canControl(62865152, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 60415691);
      console.log(`Result of canControl(62865152, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 48889804);
      console.log(`Result of canControl(62865152, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 60223053);
      console.log(`Result of canControl(62865152, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 23575438);
      console.log(`Result of canControl(62865152, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(62865152, 55137231);
      console.log(`Result of canControl(62865152, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 60096464);
      console.log(`Result of canControl(62865152, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 56535825);
      console.log(`Result of canControl(62865152, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(62865152, 35586002);
      console.log(`Result of canControl(62865152, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 25026515);
      console.log(`Result of canControl(62865152, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(62865152, 20);
      console.log(`Result of canControl(62865152, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(38318401, 62865152);
      console.log(`Result of canControl(38318401, 62865152):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(38318401, 38318401);
      console.log(`Result of canControl(38318401, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(38318401, 46135426);
      console.log(`Result of canControl(38318401, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 59899331);
      console.log(`Result of canControl(38318401, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 907588);
      console.log(`Result of canControl(38318401, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(38318401, 42981317);
      console.log(`Result of canControl(38318401, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 50064774);
      console.log(`Result of canControl(38318401, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 16195527);
      console.log(`Result of canControl(38318401, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 17545928);
      console.log(`Result of canControl(38318401, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 32399305);
      console.log(`Result of canControl(38318401, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 49980106);
      console.log(`Result of canControl(38318401, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 60415691);
      console.log(`Result of canControl(38318401, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 48889804);
      console.log(`Result of canControl(38318401, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 60223053);
      console.log(`Result of canControl(38318401, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(38318401, 23575438);
      console.log(`Result of canControl(38318401, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 55137231);
      console.log(`Result of canControl(38318401, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 60096464);
      console.log(`Result of canControl(38318401, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 56535825);
      console.log(`Result of canControl(38318401, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(38318401, 35586002);
      console.log(`Result of canControl(38318401, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 25026515);
      console.log(`Result of canControl(38318401, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(38318401, 20);
      console.log(`Result of canControl(38318401, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(46135426, 62865152);
      console.log(`Result of canControl(46135426, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 38318401);
      console.log(`Result of canControl(46135426, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 46135426);
      console.log(`Result of canControl(46135426, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(46135426, 59899331);
      console.log(`Result of canControl(46135426, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 907588);
      console.log(`Result of canControl(46135426, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 42981317);
      console.log(`Result of canControl(46135426, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 50064774);
      console.log(`Result of canControl(46135426, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 16195527);
      console.log(`Result of canControl(46135426, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 17545928);
      console.log(`Result of canControl(46135426, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(46135426, 32399305);
      console.log(`Result of canControl(46135426, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 49980106);
      console.log(`Result of canControl(46135426, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(46135426, 60415691);
      console.log(`Result of canControl(46135426, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(46135426, 48889804);
      console.log(`Result of canControl(46135426, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 60223053);
      console.log(`Result of canControl(46135426, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(46135426, 23575438);
      console.log(`Result of canControl(46135426, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 55137231);
      console.log(`Result of canControl(46135426, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 60096464);
      console.log(`Result of canControl(46135426, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 56535825);
      console.log(`Result of canControl(46135426, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 35586002);
      console.log(`Result of canControl(46135426, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 25026515);
      console.log(`Result of canControl(46135426, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(46135426, 20);
      console.log(`Result of canControl(46135426, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(59899331, 62865152);
      console.log(`Result of canControl(59899331, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 38318401);
      console.log(`Result of canControl(59899331, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(59899331, 46135426);
      console.log(`Result of canControl(59899331, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(59899331, 59899331);
      console.log(`Result of canControl(59899331, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(59899331, 907588);
      console.log(`Result of canControl(59899331, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(59899331, 42981317);
      console.log(`Result of canControl(59899331, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 50064774);
      console.log(`Result of canControl(59899331, 50064774):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(59899331, 16195527);
      console.log(`Result of canControl(59899331, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 17545928);
      console.log(`Result of canControl(59899331, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 32399305);
      console.log(`Result of canControl(59899331, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 49980106);
      console.log(`Result of canControl(59899331, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 60415691);
      console.log(`Result of canControl(59899331, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 48889804);
      console.log(`Result of canControl(59899331, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 60223053);
      console.log(`Result of canControl(59899331, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 23575438);
      console.log(`Result of canControl(59899331, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 55137231);
      console.log(`Result of canControl(59899331, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 60096464);
      console.log(`Result of canControl(59899331, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 56535825);
      console.log(`Result of canControl(59899331, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 35586002);
      console.log(`Result of canControl(59899331, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 25026515);
      console.log(`Result of canControl(59899331, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(59899331, 20);
      console.log(`Result of canControl(59899331, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 62865152);
      console.log(`Result of canControl(907588, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 38318401);
      console.log(`Result of canControl(907588, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 46135426);
      console.log(`Result of canControl(907588, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 59899331);
      console.log(`Result of canControl(907588, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 907588);
      console.log(`Result of canControl(907588, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 42981317);
      console.log(`Result of canControl(907588, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 50064774);
      console.log(`Result of canControl(907588, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 16195527);
      console.log(`Result of canControl(907588, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 17545928);
      console.log(`Result of canControl(907588, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 32399305);
      console.log(`Result of canControl(907588, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 49980106);
      console.log(`Result of canControl(907588, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 60415691);
      console.log(`Result of canControl(907588, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 48889804);
      console.log(`Result of canControl(907588, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 60223053);
      console.log(`Result of canControl(907588, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 23575438);
      console.log(`Result of canControl(907588, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 55137231);
      console.log(`Result of canControl(907588, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 60096464);
      console.log(`Result of canControl(907588, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 56535825);
      console.log(`Result of canControl(907588, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(907588, 35586002);
      console.log(`Result of canControl(907588, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 25026515);
      console.log(`Result of canControl(907588, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(907588, 20);
      console.log(`Result of canControl(907588, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(42981317, 62865152);
      console.log(`Result of canControl(42981317, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 38318401);
      console.log(`Result of canControl(42981317, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(42981317, 46135426);
      console.log(`Result of canControl(42981317, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 59899331);
      console.log(`Result of canControl(42981317, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 907588);
      console.log(`Result of canControl(42981317, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 42981317);
      console.log(`Result of canControl(42981317, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(42981317, 50064774);
      console.log(`Result of canControl(42981317, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 16195527);
      console.log(`Result of canControl(42981317, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 17545928);
      console.log(`Result of canControl(42981317, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 32399305);
      console.log(`Result of canControl(42981317, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 49980106);
      console.log(`Result of canControl(42981317, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(42981317, 60415691);
      console.log(`Result of canControl(42981317, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 48889804);
      console.log(`Result of canControl(42981317, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 60223053);
      console.log(`Result of canControl(42981317, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 23575438);
      console.log(`Result of canControl(42981317, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 55137231);
      console.log(`Result of canControl(42981317, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(42981317, 60096464);
      console.log(`Result of canControl(42981317, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 56535825);
      console.log(`Result of canControl(42981317, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 35586002);
      console.log(`Result of canControl(42981317, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 25026515);
      console.log(`Result of canControl(42981317, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(42981317, 20);
      console.log(`Result of canControl(42981317, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(50064774, 62865152);
      console.log(`Result of canControl(50064774, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 38318401);
      console.log(`Result of canControl(50064774, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 46135426);
      console.log(`Result of canControl(50064774, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 59899331);
      console.log(`Result of canControl(50064774, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 907588);
      console.log(`Result of canControl(50064774, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 42981317);
      console.log(`Result of canControl(50064774, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 50064774);
      console.log(`Result of canControl(50064774, 50064774):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(50064774, 16195527);
      console.log(`Result of canControl(50064774, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 17545928);
      console.log(`Result of canControl(50064774, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 32399305);
      console.log(`Result of canControl(50064774, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 49980106);
      console.log(`Result of canControl(50064774, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(50064774, 60415691);
      console.log(`Result of canControl(50064774, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 48889804);
      console.log(`Result of canControl(50064774, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 60223053);
      console.log(`Result of canControl(50064774, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(50064774, 23575438);
      console.log(`Result of canControl(50064774, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 55137231);
      console.log(`Result of canControl(50064774, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 60096464);
      console.log(`Result of canControl(50064774, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 56535825);
      console.log(`Result of canControl(50064774, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(50064774, 35586002);
      console.log(`Result of canControl(50064774, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 25026515);
      console.log(`Result of canControl(50064774, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(50064774, 20);
      console.log(`Result of canControl(50064774, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 62865152);
      console.log(`Result of canControl(16195527, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 38318401);
      console.log(`Result of canControl(16195527, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 46135426);
      console.log(`Result of canControl(16195527, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 59899331);
      console.log(`Result of canControl(16195527, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 907588);
      console.log(`Result of canControl(16195527, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 42981317);
      console.log(`Result of canControl(16195527, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 50064774);
      console.log(`Result of canControl(16195527, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 16195527);
      console.log(`Result of canControl(16195527, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 17545928);
      console.log(`Result of canControl(16195527, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 32399305);
      console.log(`Result of canControl(16195527, 32399305):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 49980106);
      console.log(`Result of canControl(16195527, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 60415691);
      console.log(`Result of canControl(16195527, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 48889804);
      console.log(`Result of canControl(16195527, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 60223053);
      console.log(`Result of canControl(16195527, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 23575438);
      console.log(`Result of canControl(16195527, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 55137231);
      console.log(`Result of canControl(16195527, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 60096464);
      console.log(`Result of canControl(16195527, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 56535825);
      console.log(`Result of canControl(16195527, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 35586002);
      console.log(`Result of canControl(16195527, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(16195527, 25026515);
      console.log(`Result of canControl(16195527, 25026515):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(16195527, 20);
      console.log(`Result of canControl(16195527, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 62865152);
      console.log(`Result of canControl(17545928, 62865152):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 38318401);
      console.log(`Result of canControl(17545928, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 46135426);
      console.log(`Result of canControl(17545928, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 59899331);
      console.log(`Result of canControl(17545928, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 907588);
      console.log(`Result of canControl(17545928, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 42981317);
      console.log(`Result of canControl(17545928, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 50064774);
      console.log(`Result of canControl(17545928, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 16195527);
      console.log(`Result of canControl(17545928, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 17545928);
      console.log(`Result of canControl(17545928, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 32399305);
      console.log(`Result of canControl(17545928, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 49980106);
      console.log(`Result of canControl(17545928, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 60415691);
      console.log(`Result of canControl(17545928, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 48889804);
      console.log(`Result of canControl(17545928, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 60223053);
      console.log(`Result of canControl(17545928, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 23575438);
      console.log(`Result of canControl(17545928, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 55137231);
      console.log(`Result of canControl(17545928, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 60096464);
      console.log(`Result of canControl(17545928, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 56535825);
      console.log(`Result of canControl(17545928, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(17545928, 35586002);
      console.log(`Result of canControl(17545928, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 25026515);
      console.log(`Result of canControl(17545928, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(17545928, 20);
      console.log(`Result of canControl(17545928, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(32399305, 62865152);
      console.log(`Result of canControl(32399305, 62865152):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(32399305, 38318401);
      console.log(`Result of canControl(32399305, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 46135426);
      console.log(`Result of canControl(32399305, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 59899331);
      console.log(`Result of canControl(32399305, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 907588);
      console.log(`Result of canControl(32399305, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 42981317);
      console.log(`Result of canControl(32399305, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 50064774);
      console.log(`Result of canControl(32399305, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 16195527);
      console.log(`Result of canControl(32399305, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(32399305, 17545928);
      console.log(`Result of canControl(32399305, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 32399305);
      console.log(`Result of canControl(32399305, 32399305):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(32399305, 49980106);
      console.log(`Result of canControl(32399305, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 60415691);
      console.log(`Result of canControl(32399305, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 48889804);
      console.log(`Result of canControl(32399305, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 60223053);
      console.log(`Result of canControl(32399305, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 23575438);
      console.log(`Result of canControl(32399305, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 55137231);
      console.log(`Result of canControl(32399305, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(32399305, 60096464);
      console.log(`Result of canControl(32399305, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 56535825);
      console.log(`Result of canControl(32399305, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 35586002);
      console.log(`Result of canControl(32399305, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 25026515);
      console.log(`Result of canControl(32399305, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(32399305, 20);
      console.log(`Result of canControl(32399305, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 62865152);
      console.log(`Result of canControl(49980106, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 38318401);
      console.log(`Result of canControl(49980106, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 46135426);
      console.log(`Result of canControl(49980106, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 59899331);
      console.log(`Result of canControl(49980106, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 907588);
      console.log(`Result of canControl(49980106, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 42981317);
      console.log(`Result of canControl(49980106, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 50064774);
      console.log(`Result of canControl(49980106, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 16195527);
      console.log(`Result of canControl(49980106, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 17545928);
      console.log(`Result of canControl(49980106, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 32399305);
      console.log(`Result of canControl(49980106, 32399305):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 49980106);
      console.log(`Result of canControl(49980106, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 60415691);
      console.log(`Result of canControl(49980106, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 48889804);
      console.log(`Result of canControl(49980106, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 60223053);
      console.log(`Result of canControl(49980106, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 23575438);
      console.log(`Result of canControl(49980106, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 55137231);
      console.log(`Result of canControl(49980106, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 60096464);
      console.log(`Result of canControl(49980106, 60096464):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 56535825);
      console.log(`Result of canControl(49980106, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 35586002);
      console.log(`Result of canControl(49980106, 35586002):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(49980106, 25026515);
      console.log(`Result of canControl(49980106, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(49980106, 20);
      console.log(`Result of canControl(49980106, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 62865152);
      console.log(`Result of canControl(60415691, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 38318401);
      console.log(`Result of canControl(60415691, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 46135426);
      console.log(`Result of canControl(60415691, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 59899331);
      console.log(`Result of canControl(60415691, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 907588);
      console.log(`Result of canControl(60415691, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 42981317);
      console.log(`Result of canControl(60415691, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 50064774);
      console.log(`Result of canControl(60415691, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 16195527);
      console.log(`Result of canControl(60415691, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 17545928);
      console.log(`Result of canControl(60415691, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 32399305);
      console.log(`Result of canControl(60415691, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 49980106);
      console.log(`Result of canControl(60415691, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 60415691);
      console.log(`Result of canControl(60415691, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 48889804);
      console.log(`Result of canControl(60415691, 48889804):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 60223053);
      console.log(`Result of canControl(60415691, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 23575438);
      console.log(`Result of canControl(60415691, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 55137231);
      console.log(`Result of canControl(60415691, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 60096464);
      console.log(`Result of canControl(60415691, 60096464):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 56535825);
      console.log(`Result of canControl(60415691, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 35586002);
      console.log(`Result of canControl(60415691, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60415691, 25026515);
      console.log(`Result of canControl(60415691, 25026515):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60415691, 20);
      console.log(`Result of canControl(60415691, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 62865152);
      console.log(`Result of canControl(48889804, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 38318401);
      console.log(`Result of canControl(48889804, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 46135426);
      console.log(`Result of canControl(48889804, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 59899331);
      console.log(`Result of canControl(48889804, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 907588);
      console.log(`Result of canControl(48889804, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 42981317);
      console.log(`Result of canControl(48889804, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 50064774);
      console.log(`Result of canControl(48889804, 50064774):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 16195527);
      console.log(`Result of canControl(48889804, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 17545928);
      console.log(`Result of canControl(48889804, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 32399305);
      console.log(`Result of canControl(48889804, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 49980106);
      console.log(`Result of canControl(48889804, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 60415691);
      console.log(`Result of canControl(48889804, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 48889804);
      console.log(`Result of canControl(48889804, 48889804):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 60223053);
      console.log(`Result of canControl(48889804, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 23575438);
      console.log(`Result of canControl(48889804, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 55137231);
      console.log(`Result of canControl(48889804, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(48889804, 60096464);
      console.log(`Result of canControl(48889804, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 56535825);
      console.log(`Result of canControl(48889804, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 35586002);
      console.log(`Result of canControl(48889804, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 25026515);
      console.log(`Result of canControl(48889804, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(48889804, 20);
      console.log(`Result of canControl(48889804, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60223053, 62865152);
      console.log(`Result of canControl(60223053, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 38318401);
      console.log(`Result of canControl(60223053, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 46135426);
      console.log(`Result of canControl(60223053, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 59899331);
      console.log(`Result of canControl(60223053, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60223053, 907588);
      console.log(`Result of canControl(60223053, 907588):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 42981317);
      console.log(`Result of canControl(60223053, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 50064774);
      console.log(`Result of canControl(60223053, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 16195527);
      console.log(`Result of canControl(60223053, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60223053, 17545928);
      console.log(`Result of canControl(60223053, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 32399305);
      console.log(`Result of canControl(60223053, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 49980106);
      console.log(`Result of canControl(60223053, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 60415691);
      console.log(`Result of canControl(60223053, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 48889804);
      console.log(`Result of canControl(60223053, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 60223053);
      console.log(`Result of canControl(60223053, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60223053, 23575438);
      console.log(`Result of canControl(60223053, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60223053, 55137231);
      console.log(`Result of canControl(60223053, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 60096464);
      console.log(`Result of canControl(60223053, 60096464):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60223053, 56535825);
      console.log(`Result of canControl(60223053, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 35586002);
      console.log(`Result of canControl(60223053, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 25026515);
      console.log(`Result of canControl(60223053, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60223053, 20);
      console.log(`Result of canControl(60223053, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 62865152);
      console.log(`Result of canControl(23575438, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 38318401);
      console.log(`Result of canControl(23575438, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 46135426);
      console.log(`Result of canControl(23575438, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 59899331);
      console.log(`Result of canControl(23575438, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 907588);
      console.log(`Result of canControl(23575438, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 42981317);
      console.log(`Result of canControl(23575438, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 50064774);
      console.log(`Result of canControl(23575438, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 16195527);
      console.log(`Result of canControl(23575438, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 17545928);
      console.log(`Result of canControl(23575438, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 32399305);
      console.log(`Result of canControl(23575438, 32399305):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 49980106);
      console.log(`Result of canControl(23575438, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 60415691);
      console.log(`Result of canControl(23575438, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 48889804);
      console.log(`Result of canControl(23575438, 48889804):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 60223053);
      console.log(`Result of canControl(23575438, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 23575438);
      console.log(`Result of canControl(23575438, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 55137231);
      console.log(`Result of canControl(23575438, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(23575438, 60096464);
      console.log(`Result of canControl(23575438, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 56535825);
      console.log(`Result of canControl(23575438, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 35586002);
      console.log(`Result of canControl(23575438, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 25026515);
      console.log(`Result of canControl(23575438, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(23575438, 20);
      console.log(`Result of canControl(23575438, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 62865152);
      console.log(`Result of canControl(55137231, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 38318401);
      console.log(`Result of canControl(55137231, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 46135426);
      console.log(`Result of canControl(55137231, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 59899331);
      console.log(`Result of canControl(55137231, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 907588);
      console.log(`Result of canControl(55137231, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 42981317);
      console.log(`Result of canControl(55137231, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 50064774);
      console.log(`Result of canControl(55137231, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 16195527);
      console.log(`Result of canControl(55137231, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 17545928);
      console.log(`Result of canControl(55137231, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 32399305);
      console.log(`Result of canControl(55137231, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 49980106);
      console.log(`Result of canControl(55137231, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 60415691);
      console.log(`Result of canControl(55137231, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 48889804);
      console.log(`Result of canControl(55137231, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 60223053);
      console.log(`Result of canControl(55137231, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 23575438);
      console.log(`Result of canControl(55137231, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 55137231);
      console.log(`Result of canControl(55137231, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 60096464);
      console.log(`Result of canControl(55137231, 60096464):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 56535825);
      console.log(`Result of canControl(55137231, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 35586002);
      console.log(`Result of canControl(55137231, 35586002):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(55137231, 25026515);
      console.log(`Result of canControl(55137231, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(55137231, 20);
      console.log(`Result of canControl(55137231, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 62865152);
      console.log(`Result of canControl(60096464, 62865152):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 38318401);
      console.log(`Result of canControl(60096464, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 46135426);
      console.log(`Result of canControl(60096464, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 59899331);
      console.log(`Result of canControl(60096464, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 907588);
      console.log(`Result of canControl(60096464, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 42981317);
      console.log(`Result of canControl(60096464, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 50064774);
      console.log(`Result of canControl(60096464, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 16195527);
      console.log(`Result of canControl(60096464, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 17545928);
      console.log(`Result of canControl(60096464, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 32399305);
      console.log(`Result of canControl(60096464, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 49980106);
      console.log(`Result of canControl(60096464, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 60415691);
      console.log(`Result of canControl(60096464, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 48889804);
      console.log(`Result of canControl(60096464, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 60223053);
      console.log(`Result of canControl(60096464, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 23575438);
      console.log(`Result of canControl(60096464, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 55137231);
      console.log(`Result of canControl(60096464, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 60096464);
      console.log(`Result of canControl(60096464, 60096464):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 56535825);
      console.log(`Result of canControl(60096464, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 35586002);
      console.log(`Result of canControl(60096464, 35586002):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(60096464, 25026515);
      console.log(`Result of canControl(60096464, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(60096464, 20);
      console.log(`Result of canControl(60096464, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 62865152);
      console.log(`Result of canControl(56535825, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 38318401);
      console.log(`Result of canControl(56535825, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 46135426);
      console.log(`Result of canControl(56535825, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 59899331);
      console.log(`Result of canControl(56535825, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 907588);
      console.log(`Result of canControl(56535825, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 42981317);
      console.log(`Result of canControl(56535825, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 50064774);
      console.log(`Result of canControl(56535825, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 16195527);
      console.log(`Result of canControl(56535825, 16195527):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 17545928);
      console.log(`Result of canControl(56535825, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 32399305);
      console.log(`Result of canControl(56535825, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 49980106);
      console.log(`Result of canControl(56535825, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 60415691);
      console.log(`Result of canControl(56535825, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 48889804);
      console.log(`Result of canControl(56535825, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 60223053);
      console.log(`Result of canControl(56535825, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 23575438);
      console.log(`Result of canControl(56535825, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 55137231);
      console.log(`Result of canControl(56535825, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 60096464);
      console.log(`Result of canControl(56535825, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(56535825, 56535825);
      console.log(`Result of canControl(56535825, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 35586002);
      console.log(`Result of canControl(56535825, 35586002):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 25026515);
      console.log(`Result of canControl(56535825, 25026515):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(56535825, 20);
      console.log(`Result of canControl(56535825, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 62865152);
      console.log(`Result of canControl(35586002, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 38318401);
      console.log(`Result of canControl(35586002, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 46135426);
      console.log(`Result of canControl(35586002, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 59899331);
      console.log(`Result of canControl(35586002, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 907588);
      console.log(`Result of canControl(35586002, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 42981317);
      console.log(`Result of canControl(35586002, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 50064774);
      console.log(`Result of canControl(35586002, 50064774):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 16195527);
      console.log(`Result of canControl(35586002, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 17545928);
      console.log(`Result of canControl(35586002, 17545928):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 32399305);
      console.log(`Result of canControl(35586002, 32399305):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 49980106);
      console.log(`Result of canControl(35586002, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 60415691);
      console.log(`Result of canControl(35586002, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 48889804);
      console.log(`Result of canControl(35586002, 48889804):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 60223053);
      console.log(`Result of canControl(35586002, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 23575438);
      console.log(`Result of canControl(35586002, 23575438):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 55137231);
      console.log(`Result of canControl(35586002, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 60096464);
      console.log(`Result of canControl(35586002, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 56535825);
      console.log(`Result of canControl(35586002, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 35586002);
      console.log(`Result of canControl(35586002, 35586002):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(35586002, 25026515);
      console.log(`Result of canControl(35586002, 25026515):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(35586002, 20);
      console.log(`Result of canControl(35586002, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 62865152);
      console.log(`Result of canControl(25026515, 62865152):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 38318401);
      console.log(`Result of canControl(25026515, 38318401):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 46135426);
      console.log(`Result of canControl(25026515, 46135426):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 59899331);
      console.log(`Result of canControl(25026515, 59899331):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 907588);
      console.log(`Result of canControl(25026515, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 42981317);
      console.log(`Result of canControl(25026515, 42981317):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 50064774);
      console.log(`Result of canControl(25026515, 50064774):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 16195527);
      console.log(`Result of canControl(25026515, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 17545928);
      console.log(`Result of canControl(25026515, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 32399305);
      console.log(`Result of canControl(25026515, 32399305):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 49980106);
      console.log(`Result of canControl(25026515, 49980106):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 60415691);
      console.log(`Result of canControl(25026515, 60415691):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 48889804);
      console.log(`Result of canControl(25026515, 48889804):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 60223053);
      console.log(`Result of canControl(25026515, 60223053):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 23575438);
      console.log(`Result of canControl(25026515, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 55137231);
      console.log(`Result of canControl(25026515, 55137231):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 60096464);
      console.log(`Result of canControl(25026515, 60096464):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 56535825);
      console.log(`Result of canControl(25026515, 56535825):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 35586002);
      console.log(`Result of canControl(25026515, 35586002):`, result);
      expect(result).to.equal( true );
      
      result = await dao1.canControl(25026515, 25026515);
      console.log(`Result of canControl(25026515, 25026515):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(25026515, 20);
      console.log(`Result of canControl(25026515, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 62865152);
      console.log(`Result of canControl(20, 62865152):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 38318401);
      console.log(`Result of canControl(20, 38318401):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 46135426);
      console.log(`Result of canControl(20, 46135426):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 59899331);
      console.log(`Result of canControl(20, 59899331):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 907588);
      console.log(`Result of canControl(20, 907588):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 42981317);
      console.log(`Result of canControl(20, 42981317):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 50064774);
      console.log(`Result of canControl(20, 50064774):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 16195527);
      console.log(`Result of canControl(20, 16195527):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 17545928);
      console.log(`Result of canControl(20, 17545928):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 32399305);
      console.log(`Result of canControl(20, 32399305):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 49980106);
      console.log(`Result of canControl(20, 49980106):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 60415691);
      console.log(`Result of canControl(20, 60415691):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 48889804);
      console.log(`Result of canControl(20, 48889804):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 60223053);
      console.log(`Result of canControl(20, 60223053):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 23575438);
      console.log(`Result of canControl(20, 23575438):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 55137231);
      console.log(`Result of canControl(20, 55137231):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 60096464);
      console.log(`Result of canControl(20, 60096464):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 56535825);
      console.log(`Result of canControl(20, 56535825):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 35586002);
      console.log(`Result of canControl(20, 35586002):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 25026515);
      console.log(`Result of canControl(20, 25026515):`, result);
      expect(result).to.equal( false );
      
      result = await dao1.canControl(20, 20);
      console.log(`Result of canControl(20, 20):`, result);
      expect(result).to.equal( false );
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      result = await addr1Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 62865152):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 62865152):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 62865152):`, result);
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
      //console.log(`Execution result of permission (permission0 for 38318401):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 38318401):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 38318401):`, result);
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
      //console.log(`Execution result of permission (permission0 for 46135426):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 46135426):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 46135426):`, result);
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
      //console.log(`Execution result of permission (permission0 for 59899331):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 59899331):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 59899331):`, result);
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
      //console.log(`Execution result of permission (permission0 for 907588):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 907588):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 907588):`, result);
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
      //console.log(`Execution result of permission (permission0 for 42981317):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 42981317):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 42981317):`, result);
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
      //console.log(`Execution result of permission (permission0 for 50064774):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 50064774):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 50064774):`, result);
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
      //console.log(`Execution result of permission (permission0 for 16195527):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 16195527):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 16195527):`, result);
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
      //console.log(`Execution result of permission (permission0 for 17545928):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 17545928):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 17545928):`, result);
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
      //console.log(`Execution result of permission (permission0 for 32399305):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 32399305):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 32399305):`, result);
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
      //console.log(`Execution result of permission (permission0 for 49980106):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 49980106):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 49980106):`, result);
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
      //console.log(`Execution result of permission (permission0 for 60415691):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 60415691):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 60415691):`, result);
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
      //console.log(`Execution result of permission (permission0 for 48889804):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 48889804):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 48889804):`, result);
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
      //console.log(`Execution result of permission (permission0 for 60223053):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 60223053):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 60223053):`, result);
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
      //console.log(`Execution result of permission (permission0 for 23575438):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr15Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 23575438):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr15Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 23575438):`, result);
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
      //console.log(`Execution result of permission (permission0 for 55137231):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr16Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 55137231):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr16Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 55137231):`, result);
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
      //console.log(`Execution result of permission (permission0 for 60096464):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr17Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 60096464):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr17Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 60096464):`, result);
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
      //console.log(`Execution result of permission (permission0 for 56535825):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr18Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 56535825):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr18Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 56535825):`, result);
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
      //console.log(`Execution result of permission (permission0 for 35586002):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr19Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 35586002):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr19Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 35586002):`, result);
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
      //console.log(`Execution result of permission (permission0 for 25026515):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr20Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 25026515):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr20Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 25026515):`, result);
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
