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
    const Group_Currency_DAO = await ethers.deployContract("Group_Currency_DAO", ["Group_Currency_DAO", owner.address, addr1.address  , addr2.address  , addr3.address  , addr4.address ]);
    await Group_Currency_DAO.waitForDeployment();

    return{Group_Currency_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7};
 }
    
    it("Should set the right owner", async function (){
      const{Group_Currency_DAO, owner} = await loadFixture(deployTokenFixture);
      expect(await Group_Currency_DAO.hasRole(owner.address)).to.equal(4);
   });

    it("Control relations should reflect the organizational structure of the DAO.", async function (){
      let{Group_Currency_DAO, owner, addr1, addr2, addr3, addr4, addr5, addr6, addr7} = await loadFixture(deployTokenFixture);

    ownerConnect = Group_Currency_DAO.connect(owner);
    
    addr1Connect = Group_Currency_DAO.connect(addr1);
    
    addr2Connect = Group_Currency_DAO.connect(addr2);
    
    addr3Connect = Group_Currency_DAO.connect(addr3);
    
    addr4Connect = Group_Currency_DAO.connect(addr4);
    
    addr5Connect = Group_Currency_DAO.connect(addr5);
    
    addr6Connect = Group_Currency_DAO.connect(addr6);
    
    addr7Connect = Group_Currency_DAO.connect(addr7);
    

      // Map to link roles with addresses
      addressesByEntityValue = new Map();
      
      addressesByEntityValue.set(4, owner);
      
      addressesByEntityValue.set(1, addr1);
      
      addressesByEntityValue.set(2, addr2);
      
      addressesByEntityValue.set(3, addr3);
      
      addressesByEntityValue.set(5, addr4);
      
      addressesByEntityValue.set(6, addr5);
      
      addressesByEntityValue.set(7, addr6);
      
      addressesByEntityValue.set(8, addr7);
      

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
      
      result = await Group_Currency_DAO.can_control(1, 1);
      console.log(`Result of canControl(1, 1):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 2);
      console.log(`Result of canControl(1, 2):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 3);
      console.log(`Result of canControl(1, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 4);
      console.log(`Result of canControl(1, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 5);
      console.log(`Result of canControl(1, 5):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 6);
      console.log(`Result of canControl(1, 6):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 7);
      console.log(`Result of canControl(1, 7):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(1, 8);
      console.log(`Result of canControl(1, 8):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(2, 1);
      console.log(`Result of canControl(2, 1):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(2, 2);
      console.log(`Result of canControl(2, 2):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(2, 3);
      console.log(`Result of canControl(2, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(2, 4);
      console.log(`Result of canControl(2, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(2, 5);
      console.log(`Result of canControl(2, 5):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(2, 6);
      console.log(`Result of canControl(2, 6):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(2, 7);
      console.log(`Result of canControl(2, 7):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(2, 8);
      console.log(`Result of canControl(2, 8):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 1);
      console.log(`Result of canControl(3, 1):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 2);
      console.log(`Result of canControl(3, 2):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 3);
      console.log(`Result of canControl(3, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 4);
      console.log(`Result of canControl(3, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 5);
      console.log(`Result of canControl(3, 5):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 6);
      console.log(`Result of canControl(3, 6):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 7);
      console.log(`Result of canControl(3, 7):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(3, 8);
      console.log(`Result of canControl(3, 8):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(4, 1);
      console.log(`Result of canControl(4, 1):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 2);
      console.log(`Result of canControl(4, 2):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 3);
      console.log(`Result of canControl(4, 3):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 4);
      console.log(`Result of canControl(4, 4):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 5);
      console.log(`Result of canControl(4, 5):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 6);
      console.log(`Result of canControl(4, 6):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 7);
      console.log(`Result of canControl(4, 7):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(4, 8);
      console.log(`Result of canControl(4, 8):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(5, 1);
      console.log(`Result of canControl(5, 1):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 2);
      console.log(`Result of canControl(5, 2):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 3);
      console.log(`Result of canControl(5, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 4);
      console.log(`Result of canControl(5, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 5);
      console.log(`Result of canControl(5, 5):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 6);
      console.log(`Result of canControl(5, 6):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 7);
      console.log(`Result of canControl(5, 7):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(5, 8);
      console.log(`Result of canControl(5, 8):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(6, 1);
      console.log(`Result of canControl(6, 1):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(6, 2);
      console.log(`Result of canControl(6, 2):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(6, 3);
      console.log(`Result of canControl(6, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(6, 4);
      console.log(`Result of canControl(6, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(6, 5);
      console.log(`Result of canControl(6, 5):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(6, 6);
      console.log(`Result of canControl(6, 6):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(6, 7);
      console.log(`Result of canControl(6, 7):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(6, 8);
      console.log(`Result of canControl(6, 8):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 1);
      console.log(`Result of canControl(7, 1):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 2);
      console.log(`Result of canControl(7, 2):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 3);
      console.log(`Result of canControl(7, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 4);
      console.log(`Result of canControl(7, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 5);
      console.log(`Result of canControl(7, 5):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 6);
      console.log(`Result of canControl(7, 6):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(7, 7);
      console.log(`Result of canControl(7, 7):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(7, 8);
      console.log(`Result of canControl(7, 8):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 1);
      console.log(`Result of canControl(8, 1):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 2);
      console.log(`Result of canControl(8, 2):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 3);
      console.log(`Result of canControl(8, 3):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 4);
      console.log(`Result of canControl(8, 4):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 5);
      console.log(`Result of canControl(8, 5):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 6);
      console.log(`Result of canControl(8, 6):`, result);
      expect(result).to.equal( false );
      
      result = await Group_Currency_DAO.can_control(8, 7);
      console.log(`Result of canControl(8, 7):`, result);
      expect(result).to.equal( true );
      
      result = await Group_Currency_DAO.can_control(8, 8);
      console.log(`Result of canControl(8, 8):`, result);
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
      console.log(`Execution result of permission (propose_service_provision for 1):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.update_user_profile();
      console.log(`Execution result of permission (update_user_profile for 1):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr1Connect.funding_request_submission();
      console.log(`Execution result of permission (funding_request_submission for 1):`, result);
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
      console.log(`Execution result of permission (set_limits_to_group_currency_minting for 2):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr2Connect.add_remove_allowed_collateral_type()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr2Connect.funding_request_assessment();
      console.log(`Execution result of permission (funding_request_assessment for 2):`, result);
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
      console.log(`Execution result of permission (suspend_service_provision for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.evaluate_service_provision();
      console.log(`Execution result of permission (evaluate_service_provision for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.propose_service_provision();
      console.log(`Execution result of permission (propose_service_provision for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.update_user_profile();
      console.log(`Execution result of permission (update_user_profile for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.funding_request_submission();
      console.log(`Execution result of permission (funding_request_submission for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.set_limits_to_group_currency_minting();
      console.log(`Execution result of permission (set_limits_to_group_currency_minting for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.add_remove_allowed_collateral_type();
      console.log(`Execution result of permission (add_remove_allowed_collateral_type for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.funding_request_assessment();
      console.log(`Execution result of permission (funding_request_assessment for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.set_membership_requirements();
      console.log(`Execution result of permission (set_membership_requirements for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.suspension_of_the_Group_Currency();
      console.log(`Execution result of permission (suspension_of_the_Group_Currency for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_Group_Currency_smart_contracts();
      console.log(`Execution result of permission (upgrade_Group_Currency_smart_contracts for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.upgrade_DAO_smart_contracts();
      console.log(`Execution result of permission (upgrade_DAO_smart_contracts for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.include_exclude_members();
      console.log(`Execution result of permission (include_exclude_members for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.set_contribution_attestation();
      console.log(`Execution result of permission (set_contribution_attestation for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await ownerConnect.member_data_management();
      console.log(`Execution result of permission (member_data_management for 4):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.suspend_service_provision();
      console.log(`Execution result of permission (suspend_service_provision for 5):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr4Connect.evaluate_service_provision();
      console.log(`Execution result of permission (evaluate_service_provision for 5):`, result);
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
      console.log(`Execution result of permission (add_remove_allowed_collateral_type for 6):`, result);
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
      console.log(`Execution result of permission (set_membership_requirements for 7):`, result);
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
      console.log(`Execution result of permission (include_exclude_members for 7):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr6Connect.set_contribution_attestation();
      console.log(`Execution result of permission (set_contribution_attestation for 7):`, result);
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
      console.log(`Execution result of permission (suspension_of_the_Group_Currency for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.upgrade_Group_Currency_smart_contracts();
      console.log(`Execution result of permission (upgrade_Group_Currency_smart_contracts for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      result = await addr7Connect.upgrade_DAO_smart_contracts();
      console.log(`Execution result of permission (upgrade_DAO_smart_contracts for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
      
      await expect(addr7Connect.include_exclude_members()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      await expect(addr7Connect.set_contribution_attestation()).to.be.revertedWith(
        "User does not have this permission"
      );
      
      
      
      result = await addr7Connect.member_data_management();
      console.log(`Execution result of permission (member_data_management for 8):`, result);
      await expect(result).not.to.be.reverted;
      
      
});
});
