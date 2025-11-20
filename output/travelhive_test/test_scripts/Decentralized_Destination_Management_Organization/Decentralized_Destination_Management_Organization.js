//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
}= require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("Decentralized_Destination_Management_Organization Permission Manager contract", function () {
  let addresses = null;
  let addressesByEntityValue = null;

  async function deployFixture(){
    const [owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr11] = await ethers.getSigners();
    const Decentralized_Destination_Management_Organization = await ethers.deployContract("Decentralized_Destination_Management_Organization");
    await Decentralized_Destination_Management_Organization.waitForDeployment();

    return{Decentralized_Destination_Management_Organization, owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr11};
 }
    it("Should set the right owner and initialize committees", async function (){
      const{Decentralized_Destination_Management_Organization, owner, addr11  } = await loadFixture(deployFixture);
      expect(await Decentralized_Destination_Management_Organization.hasRole(owner.address)).to.equal(32778);
      // Initialize committees
      ownerConnect = Decentralized_Destination_Management_Organization.connect(owner);

      const tx = await ownerConnect.initializeCommittees(addr11.address );
      await tx.wait();
      expect(tx).to.not.be.reverted;
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Decentralized_Destination_Management_Organization, owner, addr0, addr1, addr2, addr3, addr4, addr5, addr6, addr7, addr8, addr9, addr11} = await loadFixture(deployFixture);

    ownerConnect = Decentralized_Destination_Management_Organization.connect(owner);
    
    addr0Connect = Decentralized_Destination_Management_Organization.connect(addr0);
    
    addr1Connect = Decentralized_Destination_Management_Organization.connect(addr1);
    
    addr2Connect = Decentralized_Destination_Management_Organization.connect(addr2);
    
    addr3Connect = Decentralized_Destination_Management_Organization.connect(addr3);
    
    addr4Connect = Decentralized_Destination_Management_Organization.connect(addr4);
    
    addr5Connect = Decentralized_Destination_Management_Organization.connect(addr5);
    
    addr6Connect = Decentralized_Destination_Management_Organization.connect(addr6);
    
    addr7Connect = Decentralized_Destination_Management_Organization.connect(addr7);
    
    addr8Connect = Decentralized_Destination_Management_Organization.connect(addr8);
    
    addr9Connect = Decentralized_Destination_Management_Organization.connect(addr9);
    
    addr11Connect = Decentralized_Destination_Management_Organization.connect(addr11);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(32768, addr0);
      
      addressesByEntityValue.set(98305, addr1);
      
      addressesByEntityValue.set(32770, addr2);
      
      addressesByEntityValue.set(32771, addr3);
      
      addressesByEntityValue.set(32772, addr4);
      
      addressesByEntityValue.set(32773, addr5);
      
      addressesByEntityValue.set(98310, addr6);
      
      addressesByEntityValue.set(32775, addr7);
      
      addressesByEntityValue.set(98312, addr8);
      
      addressesByEntityValue.set(98313, addr9);
      
      addressesByEntityValue.set(32778, owner);
      
      addressesByEntityValue.set(32779, addr11);
      

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
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32768);
      console.log(`Result of canControl(DDMO_Member, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 98305);
      console.log(`Result of canControl(DDMO_Member, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32770);
      console.log(`Result of canControl(DDMO_Member, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32771);
      console.log(`Result of canControl(DDMO_Member, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32772);
      console.log(`Result of canControl(DDMO_Member, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32773);
      console.log(`Result of canControl(DDMO_Member, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 98310);
      console.log(`Result of canControl(DDMO_Member, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32775);
      console.log(`Result of canControl(DDMO_Member, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 98312);
      console.log(`Result of canControl(DDMO_Member, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 98313);
      console.log(`Result of canControl(DDMO_Member, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32778);
      console.log(`Result of canControl(DDMO_Member, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32768, 32779);
      console.log(`Result of canControl(DDMO_Member, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32768);
      console.log(`Result of canControl(Magister, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 98305);
      console.log(`Result of canControl(Magister, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32770);
      console.log(`Result of canControl(Magister, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32771);
      console.log(`Result of canControl(Magister, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32772);
      console.log(`Result of canControl(Magister, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32773);
      console.log(`Result of canControl(Magister, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 98310);
      console.log(`Result of canControl(Magister, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32775);
      console.log(`Result of canControl(Magister, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 98312);
      console.log(`Result of canControl(Magister, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 98313);
      console.log(`Result of canControl(Magister, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32778);
      console.log(`Result of canControl(Magister, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98305, 32779);
      console.log(`Result of canControl(Magister, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32768);
      console.log(`Result of canControl(Host, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 98305);
      console.log(`Result of canControl(Host, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32770);
      console.log(`Result of canControl(Host, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32771);
      console.log(`Result of canControl(Host, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32772);
      console.log(`Result of canControl(Host, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32773);
      console.log(`Result of canControl(Host, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 98310);
      console.log(`Result of canControl(Host, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32775);
      console.log(`Result of canControl(Host, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 98312);
      console.log(`Result of canControl(Host, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 98313);
      console.log(`Result of canControl(Host, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32778);
      console.log(`Result of canControl(Host, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32770, 32779);
      console.log(`Result of canControl(Host, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32768);
      console.log(`Result of canControl(Analyst, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 98305);
      console.log(`Result of canControl(Analyst, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32770);
      console.log(`Result of canControl(Analyst, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32771);
      console.log(`Result of canControl(Analyst, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32772);
      console.log(`Result of canControl(Analyst, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32773);
      console.log(`Result of canControl(Analyst, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 98310);
      console.log(`Result of canControl(Analyst, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32775);
      console.log(`Result of canControl(Analyst, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 98312);
      console.log(`Result of canControl(Analyst, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 98313);
      console.log(`Result of canControl(Analyst, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32778);
      console.log(`Result of canControl(Analyst, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32771, 32779);
      console.log(`Result of canControl(Analyst, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32768);
      console.log(`Result of canControl(Worker, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 98305);
      console.log(`Result of canControl(Worker, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32770);
      console.log(`Result of canControl(Worker, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32771);
      console.log(`Result of canControl(Worker, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32772);
      console.log(`Result of canControl(Worker, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32773);
      console.log(`Result of canControl(Worker, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 98310);
      console.log(`Result of canControl(Worker, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32775);
      console.log(`Result of canControl(Worker, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 98312);
      console.log(`Result of canControl(Worker, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 98313);
      console.log(`Result of canControl(Worker, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32778);
      console.log(`Result of canControl(Worker, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32772, 32779);
      console.log(`Result of canControl(Worker, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32768);
      console.log(`Result of canControl(Student, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 98305);
      console.log(`Result of canControl(Student, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32770);
      console.log(`Result of canControl(Student, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32771);
      console.log(`Result of canControl(Student, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32772);
      console.log(`Result of canControl(Student, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32773);
      console.log(`Result of canControl(Student, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 98310);
      console.log(`Result of canControl(Student, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32775);
      console.log(`Result of canControl(Student, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 98312);
      console.log(`Result of canControl(Student, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 98313);
      console.log(`Result of canControl(Student, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32778);
      console.log(`Result of canControl(Student, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32773, 32779);
      console.log(`Result of canControl(Student, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32768);
      console.log(`Result of canControl(DDMO_Board_Member, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 98305);
      console.log(`Result of canControl(DDMO_Board_Member, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32770);
      console.log(`Result of canControl(DDMO_Board_Member, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32771);
      console.log(`Result of canControl(DDMO_Board_Member, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32772);
      console.log(`Result of canControl(DDMO_Board_Member, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32773);
      console.log(`Result of canControl(DDMO_Board_Member, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 98310);
      console.log(`Result of canControl(DDMO_Board_Member, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32775);
      console.log(`Result of canControl(DDMO_Board_Member, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 98312);
      console.log(`Result of canControl(DDMO_Board_Member, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 98313);
      console.log(`Result of canControl(DDMO_Board_Member, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32778);
      console.log(`Result of canControl(DDMO_Board_Member, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98310, 32779);
      console.log(`Result of canControl(DDMO_Board_Member, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32768);
      console.log(`Result of canControl(Freelancer, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 98305);
      console.log(`Result of canControl(Freelancer, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32770);
      console.log(`Result of canControl(Freelancer, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32771);
      console.log(`Result of canControl(Freelancer, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32772);
      console.log(`Result of canControl(Freelancer, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32773);
      console.log(`Result of canControl(Freelancer, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 98310);
      console.log(`Result of canControl(Freelancer, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32775);
      console.log(`Result of canControl(Freelancer, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 98312);
      console.log(`Result of canControl(Freelancer, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 98313);
      console.log(`Result of canControl(Freelancer, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32778);
      console.log(`Result of canControl(Freelancer, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32775, 32779);
      console.log(`Result of canControl(Freelancer, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32768);
      console.log(`Result of canControl(Institutional_Representative, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 98305);
      console.log(`Result of canControl(Institutional_Representative, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32770);
      console.log(`Result of canControl(Institutional_Representative, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32771);
      console.log(`Result of canControl(Institutional_Representative, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32772);
      console.log(`Result of canControl(Institutional_Representative, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32773);
      console.log(`Result of canControl(Institutional_Representative, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 98310);
      console.log(`Result of canControl(Institutional_Representative, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32775);
      console.log(`Result of canControl(Institutional_Representative, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 98312);
      console.log(`Result of canControl(Institutional_Representative, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 98313);
      console.log(`Result of canControl(Institutional_Representative, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32778);
      console.log(`Result of canControl(Institutional_Representative, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98312, 32779);
      console.log(`Result of canControl(Institutional_Representative, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32768);
      console.log(`Result of canControl(Mentor, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 98305);
      console.log(`Result of canControl(Mentor, Magister):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32770);
      console.log(`Result of canControl(Mentor, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32771);
      console.log(`Result of canControl(Mentor, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32772);
      console.log(`Result of canControl(Mentor, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32773);
      console.log(`Result of canControl(Mentor, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 98310);
      console.log(`Result of canControl(Mentor, DDMO_Board_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32775);
      console.log(`Result of canControl(Mentor, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 98312);
      console.log(`Result of canControl(Mentor, Institutional_Representative):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 98313);
      console.log(`Result of canControl(Mentor, Mentor):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32778);
      console.log(`Result of canControl(Mentor, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(98313, 32779);
      console.log(`Result of canControl(Mentor, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32768);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, DDMO_Member):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 98305);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Magister):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32770);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Host):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32771);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Analyst):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32772);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Worker):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32773);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Student):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 98310);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, DDMO_Board_Member):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32775);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Freelancer):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 98312);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Institutional_Representative):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 98313);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Mentor):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32778);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32778, 32779);
      console.log(`Result of canControl(Decentralized_Destination_Management_OrganizationOwner, DDMO_Council):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32768);
      console.log(`Result of canControl(DDMO_Council, DDMO_Member):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 98305);
      console.log(`Result of canControl(DDMO_Council, Magister):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32770);
      console.log(`Result of canControl(DDMO_Council, Host):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32771);
      console.log(`Result of canControl(DDMO_Council, Analyst):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32772);
      console.log(`Result of canControl(DDMO_Council, Worker):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32773);
      console.log(`Result of canControl(DDMO_Council, Student):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 98310);
      console.log(`Result of canControl(DDMO_Council, DDMO_Board_Member):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32775);
      console.log(`Result of canControl(DDMO_Council, Freelancer):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 98312);
      console.log(`Result of canControl(DDMO_Council, Institutional_Representative):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 98313);
      console.log(`Result of canControl(DDMO_Council, Mentor):`, result);
      expect(result).to.equal( true );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32778);
      console.log(`Result of canControl(DDMO_Council, Decentralized_Destination_Management_OrganizationOwner):`, result);
      expect(result).to.equal( false );
      
      result = await Decentralized_Destination_Management_Organization.canControl(32779, 32779);
      console.log(`Result of canControl(DDMO_Council, DDMO_Council):`, result);
      expect(result).to.equal( false );
      
   });

it("Permissions should be properly configured.", async function (){
      
      
      result = await addr0Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by DDMO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr0Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by DDMO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr0Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by DDMO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr0Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by DDMO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr0Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by DDMO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr0Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr0Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr0Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by DDMO_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.block_user();
      console.log(`Execution result of permission (block_user by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.Trigger_dispute_resolution();
      console.log(`Execution result of permission (Trigger_dispute_resolution by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.Oversee_Dispute();
      console.log(`Execution result of permission (Oversee_Dispute by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.resolve_dispute();
      console.log(`Execution result of permission (resolve_dispute by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Magister)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Host)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Host)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Host)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Host)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr2Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Host)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Host)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr3Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.access_data();
      console.log(`Execution result of permission (access_data by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr3Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr3Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Analyst)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Worker)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Worker)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Worker)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Worker)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Worker)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr4Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Worker)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr5Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.access_data();
      console.log(`Execution result of permission (access_data by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Student)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by DDMO_Board_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by DDMO_Board_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by DDMO_Board_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by DDMO_Board_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by DDMO_Board_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by DDMO_Board_Member)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Freelancer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Freelancer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Freelancer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Freelancer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Freelancer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Freelancer)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr8Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr8Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr8Connect.access_data();
      console.log(`Execution result of permission (access_data by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr8Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr8Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr8Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Institutional_Representative)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr9Connect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.approve_KYB();
      console.log(`Execution result of permission (approve_KYB by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.suspend_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.liquidate_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.merge_DDMO()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.update_destination_portal()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.approve_AI_Recommendations();
      console.log(`Execution result of permission (approve_AI_Recommendations by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr9Connect.update_duration_of_user_block()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr9Connect.update_number_of_Council_participants()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr9Connect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Mentor)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Supply_Service();
      console.log(`Execution result of permission (Supply_Service by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Propose_Task_Delegation();
      console.log(`Execution result of permission (Propose_Task_Delegation by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Execute_Task();
      console.log(`Execution result of permission (Execute_Task by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Share_Task();
      console.log(`Execution result of permission (Share_Task by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.report_task_unaccomplishment();
      console.log(`Execution result of permission (report_task_unaccomplishment by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.block_user();
      console.log(`Execution result of permission (block_user by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Trigger_dispute_resolution();
      console.log(`Execution result of permission (Trigger_dispute_resolution by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Oversee_Dispute();
      console.log(`Execution result of permission (Oversee_Dispute by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.approve_KYB();
      console.log(`Execution result of permission (approve_KYB by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.resolve_dispute();
      console.log(`Execution result of permission (resolve_dispute by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.suspend_DDMO();
      console.log(`Execution result of permission (suspend_DDMO by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.liquidate_DDMO();
      console.log(`Execution result of permission (liquidate_DDMO by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.merge_DDMO();
      console.log(`Execution result of permission (merge_DDMO by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.access_data();
      console.log(`Execution result of permission (access_data by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.update_destination_portal();
      console.log(`Execution result of permission (update_destination_portal by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.approve_AI_Recommendations();
      console.log(`Execution result of permission (approve_AI_Recommendations by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.update_duration_of_user_block();
      console.log(`Execution result of permission (update_duration_of_user_block by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.update_number_of_Council_participants();
      console.log(`Execution result of permission (update_number_of_Council_participants by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.Request_DDMO_Change();
      console.log(`Execution result of permission (Request_DDMO_Change by Decentralized_Destination_Management_OrganizationOwner)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.Supply_Service()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Propose_Task_Delegation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Execute_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Share_Task()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.report_task_unaccomplishment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.block_user()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Trigger_dispute_resolution()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.Oversee_Dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.approve_KYB()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr11Connect.resolve_dispute()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.suspend_DDMO();
      console.log(`Execution result of permission (suspend_DDMO by DDMO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.liquidate_DDMO();
      console.log(`Execution result of permission (liquidate_DDMO by DDMO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.merge_DDMO();
      console.log(`Execution result of permission (merge_DDMO by DDMO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.access_data()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.update_destination_portal();
      console.log(`Execution result of permission (update_destination_portal by DDMO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.approve_AI_Recommendations()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr11Connect.update_duration_of_user_block();
      console.log(`Execution result of permission (update_duration_of_user_block by DDMO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr11Connect.update_number_of_Council_participants();
      console.log(`Execution result of permission (update_number_of_Council_participants by DDMO_Council)`);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr11Connect.Request_DDMO_Change()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
});
});
