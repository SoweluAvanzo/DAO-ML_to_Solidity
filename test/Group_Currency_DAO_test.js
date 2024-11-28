

// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("Group_Currency_DAO Permission Manager contract", function () {
  let addresses = null;
  /* let entityByValue = null; */
  let addressesByEntityValue = null;

  async function deployTokenFixture() {
    const [owner  , dict0  , dict1  , dict2  , dict3  , dict4  , dict5  , dict6  ] = await ethers.getSigners();
    const Group_Currency_DAO = await ethers.deployContract("Group_Currency_DAO");
    await Group_Currency_DAO.waitForDeployment();
    
    return { Group_Currency_DAO, owner  , dict0  , dict1  , dict2  , dict3  , dict4  , dict5  , dict6  };
  }

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      const { Group_Currency_DAO, owner } = await loadFixture(deployTokenFixture);
      expect(await Group_Currency_DAO.hasRole(owner.address)).to.equal(259);
    });

  });

    
    
  describe("Control relations", function () {
    
    
    
    before(async function () { 
       
      
      let tx = null;
       

      let { Group_Currency_DAO, owner  , dict0  , dict1  , dict2  , dict3  , dict4  , dict5  , dict6  } = await loadFixture(deployTokenFixture);
      addresses = [owner  , dict0  , dict1  , dict2  , dict3  , dict4  , dict5  , dict6  ];

      //entityByValue = new Map();
      addressesByEntityValue = new Map();

      addressesByEntityValue.set(259, owner);
      
      addressesByEntityValue.set(259, owner);
      
      addressesByEntityValue.set(320, addr1);
      
      addressesByEntityValue.set(1281, addr2);
      
      addressesByEntityValue.set(258, addr3);
      
      addressesByEntityValue.set(1348, addr4);
      
      addressesByEntityValue.set(2309, addr5);
      
      addressesByEntityValue.set(4358, addr6);
      
      addressesByEntityValue.set(263, addr7);
      


      let ownerAddr = Group_Currency_DAO.connect(owner);
      
        let dict0Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
        let dict1Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
        let dict2Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
        let dict3Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
        let dict4Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
        let dict5Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
        let dict6Connect = Group_Currency_DAO.connect(role_address);
       
      // addresses_by_entity.set( role_value, role_address); // role_value is the role role_name
      
      // TODO: Add members, one per each role and committee (therefore, assigning a role/committee to each member)

      const assignRolesPromises = addresses.map(
        (addr, index) => {
          return new Promise( (resolve, reject)  => {
            
            let txPromise = ownerAddr.assignRole(addr.address, addressesByEntityValue.get(addr.address));
            
            return txPromise.then( (txAR) => {
            
              txAR.wait().then(
                (txWaitResult) => {
                  resolve( { "address": addr.address, "tx": txWaitResult, "indexAddress": index} ); // FINALMENTE QUESTO assignRole E' FINITO!
                }
              ).catch( errTX => reject(errTX) );
            
            }).catch( (errAssignRole) =>{
              reject(errAssignRole);
            });
            
          });
        }
      );

      const txAll = await Promise.allSettled(
        assignRolesPromises
      );

      const failedAssignmentTx = txAll.filter((txAssignmentPromiseState, index) => txAssignmentPromiseState.status == 'rejected');
      const emptyArrayOfFailures = [];
      expect(failedAssignmentTx).deep.equal(emptyArrayOfFailures);

    } ); // end of BEFORE
    
  }); // end of describe "Control relations"

}); // end of describe "__DAO__ Permission Manager contract"
