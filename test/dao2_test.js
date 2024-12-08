// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("dao2 Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployTokenFixture(){
    const [owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20] = await ethers.getSigners();
    const dao2 = await ethers.deployContract("dao2");
    await dao2.waitForDeployment();

    return{dao2, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20};
 }
    
    it("Should set the right owner", async function (){
      const{dao2, owner} = await loadFixture(deployTokenFixture);
      expect(await dao2.hasRole(owner.address)).to.equal(20);
      // Initialize committees
      const tx = await ownerConnect.initializeCommittees();
      await tx.wait();
      expect(tx).to.not.be.reverted;
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{dao2, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr10, addr11, addr12, addr13, addr14, addr15, addr16, addr17, addr18, addr19, addr20} = await loadFixture(deployTokenFixture);

    ownerConnect = dao2.connect(owner);
    
    addr1Connect = dao2.connect(addr1);
    
    addr2Connect = dao2.connect(addr2);
    
    addr3Connect = dao2.connect(addr3);
    
    addr4Connect = dao2.connect(addr4);
    
    addr5Connect = dao2.connect(addr5);
    
    addr6Connect = dao2.connect(addr6);
    
    addr7Connect = dao2.connect(addr7);
    
    addr8Connect = dao2.connect(addr8);
    
    addr9Connect = dao2.connect(addr9);
    
    addr10Connect = dao2.connect(addr10);
    
    addr11Connect = dao2.connect(addr11);
    
    addr12Connect = dao2.connect(addr12);
    
    addr13Connect = dao2.connect(addr13);
    
    addr14Connect = dao2.connect(addr14);
    
    addr15Connect = dao2.connect(addr15);
    
    addr16Connect = dao2.connect(addr16);
    
    addr17Connect = dao2.connect(addr17);
    
    addr18Connect = dao2.connect(addr18);
    
    addr19Connect = dao2.connect(addr19);
    
    addr20Connect = dao2.connect(addr20);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(20, owner);
      
      addressesByEntityValue.set(33554304, addr1);
      
      addressesByEntityValue.set(67108417, addr2);
      
      addressesByEntityValue.set(67108482, addr3);
      
      addressesByEntityValue.set(67034563, addr4);
      
      addressesByEntityValue.set(66845636, addr5);
      
      addressesByEntityValue.set(62911941, addr6);
      
      addressesByEntityValue.set(50196422, addr7);
      
      addressesByEntityValue.set(67100615, addr8);
      
      addressesByEntityValue.set(64995272, addr9);
      
      addressesByEntityValue.set(67076041, addr10);
      
      addressesByEntityValue.set(66518986, addr11);
      
      addressesByEntityValue.set(66977739, addr12);
      
      addressesByEntityValue.set(65789900, addr13);
      
      addressesByEntityValue.set(66568141, addr14);
      
      addressesByEntityValue.set(66059854, addr15);
      
      addressesByEntityValue.set(55573455, addr16);
      
      addressesByEntityValue.set(62914512, addr17);
      
      addressesByEntityValue.set(58719185, addr18);
      
      addressesByEntityValue.set(50323410, addr19);
      
      addressesByEntityValue.set(33152979, addr20);
      

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
      
      result = await dao2.canControl(33554304, 33554304);
      console.log(`Result of canControl(33554304, 33554304):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(33554304, 67108417);
      console.log(`Result of canControl(33554304, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 67108482);
      console.log(`Result of canControl(33554304, 67108482):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(33554304, 67034563);
      console.log(`Result of canControl(33554304, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 66845636);
      console.log(`Result of canControl(33554304, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 62911941);
      console.log(`Result of canControl(33554304, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 50196422);
      console.log(`Result of canControl(33554304, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 67100615);
      console.log(`Result of canControl(33554304, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 64995272);
      console.log(`Result of canControl(33554304, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 67076041);
      console.log(`Result of canControl(33554304, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 66518986);
      console.log(`Result of canControl(33554304, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 66977739);
      console.log(`Result of canControl(33554304, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 65789900);
      console.log(`Result of canControl(33554304, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 66568141);
      console.log(`Result of canControl(33554304, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 66059854);
      console.log(`Result of canControl(33554304, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 55573455);
      console.log(`Result of canControl(33554304, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 62914512);
      console.log(`Result of canControl(33554304, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 58719185);
      console.log(`Result of canControl(33554304, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 50323410);
      console.log(`Result of canControl(33554304, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 33152979);
      console.log(`Result of canControl(33554304, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33554304, 20);
      console.log(`Result of canControl(33554304, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108417, 33554304);
      console.log(`Result of canControl(67108417, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 67108417);
      console.log(`Result of canControl(67108417, 67108417):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108417, 67108482);
      console.log(`Result of canControl(67108417, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 67034563);
      console.log(`Result of canControl(67108417, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 66845636);
      console.log(`Result of canControl(67108417, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 62911941);
      console.log(`Result of canControl(67108417, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 50196422);
      console.log(`Result of canControl(67108417, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 67100615);
      console.log(`Result of canControl(67108417, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 64995272);
      console.log(`Result of canControl(67108417, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 67076041);
      console.log(`Result of canControl(67108417, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 66518986);
      console.log(`Result of canControl(67108417, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 66977739);
      console.log(`Result of canControl(67108417, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 65789900);
      console.log(`Result of canControl(67108417, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 66568141);
      console.log(`Result of canControl(67108417, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 66059854);
      console.log(`Result of canControl(67108417, 66059854):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108417, 55573455);
      console.log(`Result of canControl(67108417, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 62914512);
      console.log(`Result of canControl(67108417, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 58719185);
      console.log(`Result of canControl(67108417, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 50323410);
      console.log(`Result of canControl(67108417, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 33152979);
      console.log(`Result of canControl(67108417, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108417, 20);
      console.log(`Result of canControl(67108417, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108482, 33554304);
      console.log(`Result of canControl(67108482, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 67108417);
      console.log(`Result of canControl(67108482, 67108417):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108482, 67108482);
      console.log(`Result of canControl(67108482, 67108482):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108482, 67034563);
      console.log(`Result of canControl(67108482, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 66845636);
      console.log(`Result of canControl(67108482, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 62911941);
      console.log(`Result of canControl(67108482, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 50196422);
      console.log(`Result of canControl(67108482, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 67100615);
      console.log(`Result of canControl(67108482, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 64995272);
      console.log(`Result of canControl(67108482, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 67076041);
      console.log(`Result of canControl(67108482, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 66518986);
      console.log(`Result of canControl(67108482, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 66977739);
      console.log(`Result of canControl(67108482, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 65789900);
      console.log(`Result of canControl(67108482, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 66568141);
      console.log(`Result of canControl(67108482, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 66059854);
      console.log(`Result of canControl(67108482, 66059854):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67108482, 55573455);
      console.log(`Result of canControl(67108482, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 62914512);
      console.log(`Result of canControl(67108482, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 58719185);
      console.log(`Result of canControl(67108482, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 50323410);
      console.log(`Result of canControl(67108482, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 33152979);
      console.log(`Result of canControl(67108482, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67108482, 20);
      console.log(`Result of canControl(67108482, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67034563, 33554304);
      console.log(`Result of canControl(67034563, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 67108417);
      console.log(`Result of canControl(67034563, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 67108482);
      console.log(`Result of canControl(67034563, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 67034563);
      console.log(`Result of canControl(67034563, 67034563):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67034563, 66845636);
      console.log(`Result of canControl(67034563, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 62911941);
      console.log(`Result of canControl(67034563, 62911941):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67034563, 50196422);
      console.log(`Result of canControl(67034563, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 67100615);
      console.log(`Result of canControl(67034563, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 64995272);
      console.log(`Result of canControl(67034563, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 67076041);
      console.log(`Result of canControl(67034563, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 66518986);
      console.log(`Result of canControl(67034563, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 66977739);
      console.log(`Result of canControl(67034563, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 65789900);
      console.log(`Result of canControl(67034563, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 66568141);
      console.log(`Result of canControl(67034563, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 66059854);
      console.log(`Result of canControl(67034563, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 55573455);
      console.log(`Result of canControl(67034563, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 62914512);
      console.log(`Result of canControl(67034563, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 58719185);
      console.log(`Result of canControl(67034563, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 50323410);
      console.log(`Result of canControl(67034563, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 33152979);
      console.log(`Result of canControl(67034563, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67034563, 20);
      console.log(`Result of canControl(67034563, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66845636, 33554304);
      console.log(`Result of canControl(66845636, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 67108417);
      console.log(`Result of canControl(66845636, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 67108482);
      console.log(`Result of canControl(66845636, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 67034563);
      console.log(`Result of canControl(66845636, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 66845636);
      console.log(`Result of canControl(66845636, 66845636):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66845636, 62911941);
      console.log(`Result of canControl(66845636, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 50196422);
      console.log(`Result of canControl(66845636, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 67100615);
      console.log(`Result of canControl(66845636, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 64995272);
      console.log(`Result of canControl(66845636, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 67076041);
      console.log(`Result of canControl(66845636, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 66518986);
      console.log(`Result of canControl(66845636, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 66977739);
      console.log(`Result of canControl(66845636, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 65789900);
      console.log(`Result of canControl(66845636, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 66568141);
      console.log(`Result of canControl(66845636, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 66059854);
      console.log(`Result of canControl(66845636, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 55573455);
      console.log(`Result of canControl(66845636, 55573455):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66845636, 62914512);
      console.log(`Result of canControl(66845636, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 58719185);
      console.log(`Result of canControl(66845636, 58719185):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66845636, 50323410);
      console.log(`Result of canControl(66845636, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 33152979);
      console.log(`Result of canControl(66845636, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66845636, 20);
      console.log(`Result of canControl(66845636, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(62911941, 33554304);
      console.log(`Result of canControl(62911941, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 67108417);
      console.log(`Result of canControl(62911941, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 67108482);
      console.log(`Result of canControl(62911941, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 67034563);
      console.log(`Result of canControl(62911941, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 66845636);
      console.log(`Result of canControl(62911941, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 62911941);
      console.log(`Result of canControl(62911941, 62911941):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(62911941, 50196422);
      console.log(`Result of canControl(62911941, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 67100615);
      console.log(`Result of canControl(62911941, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 64995272);
      console.log(`Result of canControl(62911941, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 67076041);
      console.log(`Result of canControl(62911941, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 66518986);
      console.log(`Result of canControl(62911941, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 66977739);
      console.log(`Result of canControl(62911941, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 65789900);
      console.log(`Result of canControl(62911941, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 66568141);
      console.log(`Result of canControl(62911941, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 66059854);
      console.log(`Result of canControl(62911941, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 55573455);
      console.log(`Result of canControl(62911941, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 62914512);
      console.log(`Result of canControl(62911941, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 58719185);
      console.log(`Result of canControl(62911941, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 50323410);
      console.log(`Result of canControl(62911941, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 33152979);
      console.log(`Result of canControl(62911941, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62911941, 20);
      console.log(`Result of canControl(62911941, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(50196422, 33554304);
      console.log(`Result of canControl(50196422, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 67108417);
      console.log(`Result of canControl(50196422, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 67108482);
      console.log(`Result of canControl(50196422, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 67034563);
      console.log(`Result of canControl(50196422, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 66845636);
      console.log(`Result of canControl(50196422, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 62911941);
      console.log(`Result of canControl(50196422, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 50196422);
      console.log(`Result of canControl(50196422, 50196422):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(50196422, 67100615);
      console.log(`Result of canControl(50196422, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 64995272);
      console.log(`Result of canControl(50196422, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 67076041);
      console.log(`Result of canControl(50196422, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 66518986);
      console.log(`Result of canControl(50196422, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 66977739);
      console.log(`Result of canControl(50196422, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 65789900);
      console.log(`Result of canControl(50196422, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 66568141);
      console.log(`Result of canControl(50196422, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 66059854);
      console.log(`Result of canControl(50196422, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 55573455);
      console.log(`Result of canControl(50196422, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 62914512);
      console.log(`Result of canControl(50196422, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 58719185);
      console.log(`Result of canControl(50196422, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 50323410);
      console.log(`Result of canControl(50196422, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 33152979);
      console.log(`Result of canControl(50196422, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50196422, 20);
      console.log(`Result of canControl(50196422, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67100615, 33554304);
      console.log(`Result of canControl(67100615, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 67108417);
      console.log(`Result of canControl(67100615, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 67108482);
      console.log(`Result of canControl(67100615, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 67034563);
      console.log(`Result of canControl(67100615, 67034563):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67100615, 66845636);
      console.log(`Result of canControl(67100615, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 62911941);
      console.log(`Result of canControl(67100615, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 50196422);
      console.log(`Result of canControl(67100615, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 67100615);
      console.log(`Result of canControl(67100615, 67100615):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67100615, 64995272);
      console.log(`Result of canControl(67100615, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 67076041);
      console.log(`Result of canControl(67100615, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 66518986);
      console.log(`Result of canControl(67100615, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 66977739);
      console.log(`Result of canControl(67100615, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 65789900);
      console.log(`Result of canControl(67100615, 65789900):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67100615, 66568141);
      console.log(`Result of canControl(67100615, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 66059854);
      console.log(`Result of canControl(67100615, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 55573455);
      console.log(`Result of canControl(67100615, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 62914512);
      console.log(`Result of canControl(67100615, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 58719185);
      console.log(`Result of canControl(67100615, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67100615, 50323410);
      console.log(`Result of canControl(67100615, 50323410):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67100615, 33152979);
      console.log(`Result of canControl(67100615, 33152979):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67100615, 20);
      console.log(`Result of canControl(67100615, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(64995272, 33554304);
      console.log(`Result of canControl(64995272, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 67108417);
      console.log(`Result of canControl(64995272, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 67108482);
      console.log(`Result of canControl(64995272, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 67034563);
      console.log(`Result of canControl(64995272, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 66845636);
      console.log(`Result of canControl(64995272, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 62911941);
      console.log(`Result of canControl(64995272, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 50196422);
      console.log(`Result of canControl(64995272, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 67100615);
      console.log(`Result of canControl(64995272, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 64995272);
      console.log(`Result of canControl(64995272, 64995272):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(64995272, 67076041);
      console.log(`Result of canControl(64995272, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 66518986);
      console.log(`Result of canControl(64995272, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 66977739);
      console.log(`Result of canControl(64995272, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 65789900);
      console.log(`Result of canControl(64995272, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 66568141);
      console.log(`Result of canControl(64995272, 66568141):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(64995272, 66059854);
      console.log(`Result of canControl(64995272, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 55573455);
      console.log(`Result of canControl(64995272, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 62914512);
      console.log(`Result of canControl(64995272, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 58719185);
      console.log(`Result of canControl(64995272, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 50323410);
      console.log(`Result of canControl(64995272, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 33152979);
      console.log(`Result of canControl(64995272, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(64995272, 20);
      console.log(`Result of canControl(64995272, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67076041, 33554304);
      console.log(`Result of canControl(67076041, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 67108417);
      console.log(`Result of canControl(67076041, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 67108482);
      console.log(`Result of canControl(67076041, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 67034563);
      console.log(`Result of canControl(67076041, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 66845636);
      console.log(`Result of canControl(67076041, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 62911941);
      console.log(`Result of canControl(67076041, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 50196422);
      console.log(`Result of canControl(67076041, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 67100615);
      console.log(`Result of canControl(67076041, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 64995272);
      console.log(`Result of canControl(67076041, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 67076041);
      console.log(`Result of canControl(67076041, 67076041):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(67076041, 66518986);
      console.log(`Result of canControl(67076041, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 66977739);
      console.log(`Result of canControl(67076041, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 65789900);
      console.log(`Result of canControl(67076041, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 66568141);
      console.log(`Result of canControl(67076041, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 66059854);
      console.log(`Result of canControl(67076041, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 55573455);
      console.log(`Result of canControl(67076041, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 62914512);
      console.log(`Result of canControl(67076041, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 58719185);
      console.log(`Result of canControl(67076041, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 50323410);
      console.log(`Result of canControl(67076041, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 33152979);
      console.log(`Result of canControl(67076041, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(67076041, 20);
      console.log(`Result of canControl(67076041, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66518986, 33554304);
      console.log(`Result of canControl(66518986, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 67108417);
      console.log(`Result of canControl(66518986, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 67108482);
      console.log(`Result of canControl(66518986, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 67034563);
      console.log(`Result of canControl(66518986, 67034563):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66518986, 66845636);
      console.log(`Result of canControl(66518986, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 62911941);
      console.log(`Result of canControl(66518986, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 50196422);
      console.log(`Result of canControl(66518986, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 67100615);
      console.log(`Result of canControl(66518986, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 64995272);
      console.log(`Result of canControl(66518986, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 67076041);
      console.log(`Result of canControl(66518986, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 66518986);
      console.log(`Result of canControl(66518986, 66518986):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66518986, 66977739);
      console.log(`Result of canControl(66518986, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 65789900);
      console.log(`Result of canControl(66518986, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 66568141);
      console.log(`Result of canControl(66518986, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 66059854);
      console.log(`Result of canControl(66518986, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 55573455);
      console.log(`Result of canControl(66518986, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 62914512);
      console.log(`Result of canControl(66518986, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 58719185);
      console.log(`Result of canControl(66518986, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 50323410);
      console.log(`Result of canControl(66518986, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 33152979);
      console.log(`Result of canControl(66518986, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66518986, 20);
      console.log(`Result of canControl(66518986, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66977739, 33554304);
      console.log(`Result of canControl(66977739, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 67108417);
      console.log(`Result of canControl(66977739, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 67108482);
      console.log(`Result of canControl(66977739, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 67034563);
      console.log(`Result of canControl(66977739, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 66845636);
      console.log(`Result of canControl(66977739, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 62911941);
      console.log(`Result of canControl(66977739, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 50196422);
      console.log(`Result of canControl(66977739, 50196422):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66977739, 67100615);
      console.log(`Result of canControl(66977739, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 64995272);
      console.log(`Result of canControl(66977739, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 67076041);
      console.log(`Result of canControl(66977739, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 66518986);
      console.log(`Result of canControl(66977739, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 66977739);
      console.log(`Result of canControl(66977739, 66977739):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66977739, 65789900);
      console.log(`Result of canControl(66977739, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 66568141);
      console.log(`Result of canControl(66977739, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 66059854);
      console.log(`Result of canControl(66977739, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 55573455);
      console.log(`Result of canControl(66977739, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 62914512);
      console.log(`Result of canControl(66977739, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 58719185);
      console.log(`Result of canControl(66977739, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 50323410);
      console.log(`Result of canControl(66977739, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66977739, 33152979);
      console.log(`Result of canControl(66977739, 33152979):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66977739, 20);
      console.log(`Result of canControl(66977739, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(65789900, 33554304);
      console.log(`Result of canControl(65789900, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 67108417);
      console.log(`Result of canControl(65789900, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 67108482);
      console.log(`Result of canControl(65789900, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 67034563);
      console.log(`Result of canControl(65789900, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 66845636);
      console.log(`Result of canControl(65789900, 66845636):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(65789900, 62911941);
      console.log(`Result of canControl(65789900, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 50196422);
      console.log(`Result of canControl(65789900, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 67100615);
      console.log(`Result of canControl(65789900, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 64995272);
      console.log(`Result of canControl(65789900, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 67076041);
      console.log(`Result of canControl(65789900, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 66518986);
      console.log(`Result of canControl(65789900, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 66977739);
      console.log(`Result of canControl(65789900, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 65789900);
      console.log(`Result of canControl(65789900, 65789900):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(65789900, 66568141);
      console.log(`Result of canControl(65789900, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 66059854);
      console.log(`Result of canControl(65789900, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 55573455);
      console.log(`Result of canControl(65789900, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 62914512);
      console.log(`Result of canControl(65789900, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 58719185);
      console.log(`Result of canControl(65789900, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 50323410);
      console.log(`Result of canControl(65789900, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(65789900, 33152979);
      console.log(`Result of canControl(65789900, 33152979):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(65789900, 20);
      console.log(`Result of canControl(65789900, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66568141, 33554304);
      console.log(`Result of canControl(66568141, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 67108417);
      console.log(`Result of canControl(66568141, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 67108482);
      console.log(`Result of canControl(66568141, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 67034563);
      console.log(`Result of canControl(66568141, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 66845636);
      console.log(`Result of canControl(66568141, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 62911941);
      console.log(`Result of canControl(66568141, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 50196422);
      console.log(`Result of canControl(66568141, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 67100615);
      console.log(`Result of canControl(66568141, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 64995272);
      console.log(`Result of canControl(66568141, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 67076041);
      console.log(`Result of canControl(66568141, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 66518986);
      console.log(`Result of canControl(66568141, 66518986):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66568141, 66977739);
      console.log(`Result of canControl(66568141, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 65789900);
      console.log(`Result of canControl(66568141, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 66568141);
      console.log(`Result of canControl(66568141, 66568141):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66568141, 66059854);
      console.log(`Result of canControl(66568141, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 55573455);
      console.log(`Result of canControl(66568141, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 62914512);
      console.log(`Result of canControl(66568141, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 58719185);
      console.log(`Result of canControl(66568141, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 50323410);
      console.log(`Result of canControl(66568141, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 33152979);
      console.log(`Result of canControl(66568141, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66568141, 20);
      console.log(`Result of canControl(66568141, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66059854, 33554304);
      console.log(`Result of canControl(66059854, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 67108417);
      console.log(`Result of canControl(66059854, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 67108482);
      console.log(`Result of canControl(66059854, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 67034563);
      console.log(`Result of canControl(66059854, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 66845636);
      console.log(`Result of canControl(66059854, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 62911941);
      console.log(`Result of canControl(66059854, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 50196422);
      console.log(`Result of canControl(66059854, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 67100615);
      console.log(`Result of canControl(66059854, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 64995272);
      console.log(`Result of canControl(66059854, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 67076041);
      console.log(`Result of canControl(66059854, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 66518986);
      console.log(`Result of canControl(66059854, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 66977739);
      console.log(`Result of canControl(66059854, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 65789900);
      console.log(`Result of canControl(66059854, 65789900):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66059854, 66568141);
      console.log(`Result of canControl(66059854, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 66059854);
      console.log(`Result of canControl(66059854, 66059854):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66059854, 55573455);
      console.log(`Result of canControl(66059854, 55573455):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(66059854, 62914512);
      console.log(`Result of canControl(66059854, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 58719185);
      console.log(`Result of canControl(66059854, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 50323410);
      console.log(`Result of canControl(66059854, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 33152979);
      console.log(`Result of canControl(66059854, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(66059854, 20);
      console.log(`Result of canControl(66059854, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(55573455, 33554304);
      console.log(`Result of canControl(55573455, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 67108417);
      console.log(`Result of canControl(55573455, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 67108482);
      console.log(`Result of canControl(55573455, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 67034563);
      console.log(`Result of canControl(55573455, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 66845636);
      console.log(`Result of canControl(55573455, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 62911941);
      console.log(`Result of canControl(55573455, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 50196422);
      console.log(`Result of canControl(55573455, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 67100615);
      console.log(`Result of canControl(55573455, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 64995272);
      console.log(`Result of canControl(55573455, 64995272):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(55573455, 67076041);
      console.log(`Result of canControl(55573455, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 66518986);
      console.log(`Result of canControl(55573455, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 66977739);
      console.log(`Result of canControl(55573455, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 65789900);
      console.log(`Result of canControl(55573455, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 66568141);
      console.log(`Result of canControl(55573455, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 66059854);
      console.log(`Result of canControl(55573455, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 55573455);
      console.log(`Result of canControl(55573455, 55573455):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(55573455, 62914512);
      console.log(`Result of canControl(55573455, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 58719185);
      console.log(`Result of canControl(55573455, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 50323410);
      console.log(`Result of canControl(55573455, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 33152979);
      console.log(`Result of canControl(55573455, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(55573455, 20);
      console.log(`Result of canControl(55573455, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(62914512, 33554304);
      console.log(`Result of canControl(62914512, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 67108417);
      console.log(`Result of canControl(62914512, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 67108482);
      console.log(`Result of canControl(62914512, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 67034563);
      console.log(`Result of canControl(62914512, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 66845636);
      console.log(`Result of canControl(62914512, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 62911941);
      console.log(`Result of canControl(62914512, 62911941):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(62914512, 50196422);
      console.log(`Result of canControl(62914512, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 67100615);
      console.log(`Result of canControl(62914512, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 64995272);
      console.log(`Result of canControl(62914512, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 67076041);
      console.log(`Result of canControl(62914512, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 66518986);
      console.log(`Result of canControl(62914512, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 66977739);
      console.log(`Result of canControl(62914512, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 65789900);
      console.log(`Result of canControl(62914512, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 66568141);
      console.log(`Result of canControl(62914512, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 66059854);
      console.log(`Result of canControl(62914512, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 55573455);
      console.log(`Result of canControl(62914512, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 62914512);
      console.log(`Result of canControl(62914512, 62914512):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(62914512, 58719185);
      console.log(`Result of canControl(62914512, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 50323410);
      console.log(`Result of canControl(62914512, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 33152979);
      console.log(`Result of canControl(62914512, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(62914512, 20);
      console.log(`Result of canControl(62914512, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(58719185, 33554304);
      console.log(`Result of canControl(58719185, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 67108417);
      console.log(`Result of canControl(58719185, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 67108482);
      console.log(`Result of canControl(58719185, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 67034563);
      console.log(`Result of canControl(58719185, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 66845636);
      console.log(`Result of canControl(58719185, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 62911941);
      console.log(`Result of canControl(58719185, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 50196422);
      console.log(`Result of canControl(58719185, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 67100615);
      console.log(`Result of canControl(58719185, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 64995272);
      console.log(`Result of canControl(58719185, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 67076041);
      console.log(`Result of canControl(58719185, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 66518986);
      console.log(`Result of canControl(58719185, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 66977739);
      console.log(`Result of canControl(58719185, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 65789900);
      console.log(`Result of canControl(58719185, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 66568141);
      console.log(`Result of canControl(58719185, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 66059854);
      console.log(`Result of canControl(58719185, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 55573455);
      console.log(`Result of canControl(58719185, 55573455):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(58719185, 62914512);
      console.log(`Result of canControl(58719185, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 58719185);
      console.log(`Result of canControl(58719185, 58719185):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(58719185, 50323410);
      console.log(`Result of canControl(58719185, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 33152979);
      console.log(`Result of canControl(58719185, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(58719185, 20);
      console.log(`Result of canControl(58719185, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(50323410, 33554304);
      console.log(`Result of canControl(50323410, 33554304):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 67108417);
      console.log(`Result of canControl(50323410, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 67108482);
      console.log(`Result of canControl(50323410, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 67034563);
      console.log(`Result of canControl(50323410, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 66845636);
      console.log(`Result of canControl(50323410, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 62911941);
      console.log(`Result of canControl(50323410, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 50196422);
      console.log(`Result of canControl(50323410, 50196422):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(50323410, 67100615);
      console.log(`Result of canControl(50323410, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 64995272);
      console.log(`Result of canControl(50323410, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 67076041);
      console.log(`Result of canControl(50323410, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 66518986);
      console.log(`Result of canControl(50323410, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 66977739);
      console.log(`Result of canControl(50323410, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 65789900);
      console.log(`Result of canControl(50323410, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 66568141);
      console.log(`Result of canControl(50323410, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 66059854);
      console.log(`Result of canControl(50323410, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 55573455);
      console.log(`Result of canControl(50323410, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 62914512);
      console.log(`Result of canControl(50323410, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 58719185);
      console.log(`Result of canControl(50323410, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 50323410);
      console.log(`Result of canControl(50323410, 50323410):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(50323410, 33152979);
      console.log(`Result of canControl(50323410, 33152979):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(50323410, 20);
      console.log(`Result of canControl(50323410, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(33152979, 33554304);
      console.log(`Result of canControl(33152979, 33554304):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(33152979, 67108417);
      console.log(`Result of canControl(33152979, 67108417):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 67108482);
      console.log(`Result of canControl(33152979, 67108482):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 67034563);
      console.log(`Result of canControl(33152979, 67034563):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 66845636);
      console.log(`Result of canControl(33152979, 66845636):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 62911941);
      console.log(`Result of canControl(33152979, 62911941):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 50196422);
      console.log(`Result of canControl(33152979, 50196422):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 67100615);
      console.log(`Result of canControl(33152979, 67100615):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 64995272);
      console.log(`Result of canControl(33152979, 64995272):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 67076041);
      console.log(`Result of canControl(33152979, 67076041):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 66518986);
      console.log(`Result of canControl(33152979, 66518986):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 66977739);
      console.log(`Result of canControl(33152979, 66977739):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 65789900);
      console.log(`Result of canControl(33152979, 65789900):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 66568141);
      console.log(`Result of canControl(33152979, 66568141):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 66059854);
      console.log(`Result of canControl(33152979, 66059854):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 55573455);
      console.log(`Result of canControl(33152979, 55573455):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 62914512);
      console.log(`Result of canControl(33152979, 62914512):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 58719185);
      console.log(`Result of canControl(33152979, 58719185):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 50323410);
      console.log(`Result of canControl(33152979, 50323410):`, result);
      expect(result).to.equal( true );
      
      result = await dao2.canControl(33152979, 33152979);
      console.log(`Result of canControl(33152979, 33152979):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(33152979, 20);
      console.log(`Result of canControl(33152979, 20):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 33554304);
      console.log(`Result of canControl(20, 33554304):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 67108417);
      console.log(`Result of canControl(20, 67108417):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 67108482);
      console.log(`Result of canControl(20, 67108482):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 67034563);
      console.log(`Result of canControl(20, 67034563):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 66845636);
      console.log(`Result of canControl(20, 66845636):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 62911941);
      console.log(`Result of canControl(20, 62911941):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 50196422);
      console.log(`Result of canControl(20, 50196422):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 67100615);
      console.log(`Result of canControl(20, 67100615):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 64995272);
      console.log(`Result of canControl(20, 64995272):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 67076041);
      console.log(`Result of canControl(20, 67076041):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 66518986);
      console.log(`Result of canControl(20, 66518986):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 66977739);
      console.log(`Result of canControl(20, 66977739):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 65789900);
      console.log(`Result of canControl(20, 65789900):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 66568141);
      console.log(`Result of canControl(20, 66568141):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 66059854);
      console.log(`Result of canControl(20, 66059854):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 55573455);
      console.log(`Result of canControl(20, 55573455):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 62914512);
      console.log(`Result of canControl(20, 62914512):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 58719185);
      console.log(`Result of canControl(20, 58719185):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 50323410);
      console.log(`Result of canControl(20, 50323410):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 33152979);
      console.log(`Result of canControl(20, 33152979):`, result);
      expect(result).to.equal( false );
      
      result = await dao2.canControl(20, 20);
      console.log(`Result of canControl(20, 20):`, result);
      expect(result).to.equal( false );
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      result = await addr1Connect.permission0();
      //console.log(`Execution result of permission (permission0 for 33554304):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 33554304):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 33554304):`, result);
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
      //console.log(`Execution result of permission (permission0 for 67108417):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 67108417):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 67108417):`, result);
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
      //console.log(`Execution result of permission (permission0 for 67108482):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 67108482):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 67108482):`, result);
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
      //console.log(`Execution result of permission (permission0 for 67034563):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 67034563):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 67034563):`, result);
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
      //console.log(`Execution result of permission (permission0 for 66845636):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 66845636):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 66845636):`, result);
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
      //console.log(`Execution result of permission (permission0 for 62911941):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 62911941):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 62911941):`, result);
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
      //console.log(`Execution result of permission (permission0 for 50196422):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 50196422):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 50196422):`, result);
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
      //console.log(`Execution result of permission (permission0 for 67100615):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 67100615):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 67100615):`, result);
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
      //console.log(`Execution result of permission (permission0 for 64995272):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 64995272):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 64995272):`, result);
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
      //console.log(`Execution result of permission (permission0 for 67076041):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 67076041):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr10Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 67076041):`, result);
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
      //console.log(`Execution result of permission (permission0 for 66518986):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 66518986):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 66518986):`, result);
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
      //console.log(`Execution result of permission (permission0 for 66977739):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 66977739):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr12Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 66977739):`, result);
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
      //console.log(`Execution result of permission (permission0 for 65789900):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 65789900):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr13Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 65789900):`, result);
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
      //console.log(`Execution result of permission (permission0 for 66568141):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 66568141):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr14Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 66568141):`, result);
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
      //console.log(`Execution result of permission (permission0 for 66059854):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr15Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 66059854):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr15Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 66059854):`, result);
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
      //console.log(`Execution result of permission (permission0 for 55573455):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr16Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 55573455):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr16Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 55573455):`, result);
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
      //console.log(`Execution result of permission (permission0 for 62914512):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr17Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 62914512):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr17Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 62914512):`, result);
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
      //console.log(`Execution result of permission (permission0 for 58719185):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr18Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 58719185):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr18Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 58719185):`, result);
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
      //console.log(`Execution result of permission (permission0 for 50323410):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr19Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 50323410):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr19Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 50323410):`, result);
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
      //console.log(`Execution result of permission (permission0 for 33152979):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr20Connect.permission1();
      //console.log(`Execution result of permission (permission1 for 33152979):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr20Connect.permission2();
      //console.log(`Execution result of permission (permission2 for 33152979):`, result);
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
