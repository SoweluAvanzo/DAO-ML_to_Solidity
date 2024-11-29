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
    
    it("Should set the right owner", async function (){
      const{Group_Currency_DAO, owner} = await loadFixture(deployTokenFixture);
      expect(await Group_Currency_DAO.hasRole(owner.address)).to.equal(259);
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Group_Currency_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7} = await loadFixture(deployTokenFixture);

    ownerAddr = Group_Currency_DAO.connect(owner);
    
    addr1Connect = Group_Currency_DAO.connect(addr1);
    
    addr2Connect = Group_Currency_DAO.connect(addr2);
    
    addr3Connect = Group_Currency_DAO.connect(addr3);
    
    addr4Connect = Group_Currency_DAO.connect(addr4);
    
    addr5Connect = Group_Currency_DAO.connect(addr5);
    
    addr6Connect = Group_Currency_DAO.connect(addr6);
    
    addr7Connect = Group_Currency_DAO.connect(addr7);
    

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



it("Permissions should be properly configured.", async function (){
      
      
      await expect(addr1Connect.suspend_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.evaluate_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr1Connect.propose_service_provision();
      console.log(`Execution result of permission (propose_service_provision for 320):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.update_user_profile();
      console.log(`Execution result of permission (update_user_profile for 320):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.funding_request_submission();
      console.log(`Execution result of permission (funding_request_submission for 320):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr1Connect.set_limits_to_group_currency_minting()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.funding_request_assessment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.set_membership_requirements()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.suspension_of_the_Group_Currency()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.upgrade_Group_Currency_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.upgrade_DAO_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr1Connect.member_data_management()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.suspend_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.evaluate_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.propose_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.update_user_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.funding_request_submission()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.set_limits_to_group_currency_minting();
      console.log(`Execution result of permission (set_limits_to_group_currency_minting for 1281):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.funding_request_assessment();
      console.log(`Execution result of permission (funding_request_assessment for 1281):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.set_membership_requirements()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.suspension_of_the_Group_Currency()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.upgrade_Group_Currency_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.upgrade_DAO_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr2Connect.member_data_management()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.suspend_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.evaluate_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.propose_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.update_user_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.funding_request_submission()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.set_limits_to_group_currency_minting()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.funding_request_assessment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.set_membership_requirements()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.suspension_of_the_Group_Currency()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.upgrade_Group_Currency_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.upgrade_DAO_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr3Connect.member_data_management()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await ownerConnect.suspend_service_provision();
      console.log(`Execution result of permission (suspend_service_provision for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.evaluate_service_provision();
      console.log(`Execution result of permission (evaluate_service_provision for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_service_provision();
      console.log(`Execution result of permission (propose_service_provision for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.update_user_profile();
      console.log(`Execution result of permission (update_user_profile for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.funding_request_submission();
      console.log(`Execution result of permission (funding_request_submission for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.set_limits_to_group_currency_minting();
      console.log(`Execution result of permission (set_limits_to_group_currency_minting for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.add_remove_allowed_collateral_type();
      console.log(`Execution result of permission (add_remove_allowed_collateral_type for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.funding_request_assessment();
      console.log(`Execution result of permission (funding_request_assessment for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.set_membership_requirements();
      console.log(`Execution result of permission (set_membership_requirements for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.suspension_of_the_Group_Currency();
      console.log(`Execution result of permission (suspension_of_the_Group_Currency for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_Group_Currency_smart_contracts();
      console.log(`Execution result of permission (upgrade_Group_Currency_smart_contracts for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_DAO_smart_contracts();
      console.log(`Execution result of permission (upgrade_DAO_smart_contracts for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.include_exclude_members();
      console.log(`Execution result of permission (include_exclude_members for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.set_contribution_attestation();
      console.log(`Execution result of permission (set_contribution_attestation for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.member_data_management();
      console.log(`Execution result of permission (member_data_management for 259):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.suspend_service_provision();
      console.log(`Execution result of permission (suspend_service_provision for 1348):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.evaluate_service_provision();
      console.log(`Execution result of permission (evaluate_service_provision for 1348):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr4Connect.propose_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.update_user_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.funding_request_submission()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.set_limits_to_group_currency_minting()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.funding_request_assessment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.set_membership_requirements()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.suspension_of_the_Group_Currency()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.upgrade_Group_Currency_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.upgrade_DAO_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr4Connect.member_data_management()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.suspend_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.evaluate_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.propose_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.update_user_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.funding_request_submission()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.set_limits_to_group_currency_minting()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr5Connect.add_remove_allowed_collateral_type();
      console.log(`Execution result of permission (add_remove_allowed_collateral_type for 2309):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr5Connect.funding_request_assessment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.set_membership_requirements()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.suspension_of_the_Group_Currency()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.upgrade_Group_Currency_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.upgrade_DAO_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr5Connect.member_data_management()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.suspend_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.evaluate_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.propose_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.update_user_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.funding_request_submission()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.set_limits_to_group_currency_minting()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.funding_request_assessment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.set_membership_requirements();
      console.log(`Execution result of permission (set_membership_requirements for 4358):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.suspension_of_the_Group_Currency()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.upgrade_Group_Currency_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr6Connect.upgrade_DAO_smart_contracts()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr6Connect.include_exclude_members();
      console.log(`Execution result of permission (include_exclude_members for 4358):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.set_contribution_attestation();
      console.log(`Execution result of permission (set_contribution_attestation for 4358):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr6Connect.member_data_management()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.suspend_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.evaluate_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.propose_service_provision()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.update_user_profile()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.funding_request_submission()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.set_limits_to_group_currency_minting()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.funding_request_assessment()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.set_membership_requirements()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.suspension_of_the_Group_Currency();
      console.log(`Execution result of permission (suspension_of_the_Group_Currency for 263):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.upgrade_Group_Currency_smart_contracts();
      console.log(`Execution result of permission (upgrade_Group_Currency_smart_contracts for 263):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.upgrade_DAO_smart_contracts();
      console.log(`Execution result of permission (upgrade_DAO_smart_contracts for 263):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.member_data_management();
      console.log(`Execution result of permission (member_data_management for 263):`, result);
      await expect(result).not.to.be.reverted;
      
      
});
});
