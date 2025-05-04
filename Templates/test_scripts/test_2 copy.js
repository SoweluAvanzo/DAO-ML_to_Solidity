

// We import Chai to use its asserting functions here.
//parameters: DAO_name, addresses_list, addresses, owner_role_value, role_value, role_address, role_name
const { expect } = require("chai");

const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("{{DAO_name}} Permission Manager contract", function () {
  let addresses = null;
  /* let entityByValue = null; */
  let addressesByEntityValue = null;

  async function deployTokenFixture() {
    const [owner, {{ addresses_list }}] = await ethers.getSigners();
    const {{DAO_name}} = await ethers.deployContract("{{DAO_name}}");
    await {{DAO_name}}.waitForDeployment();
    
    return { {{DAO_name}}, owner, {{addresses_list}}};
  }

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      const { {{DAO_name}}, owner } = await loadFixture(deployTokenFixture);
      expect(await {{DAO_name}}.hasRole(owner.address)).to.equal({{owner_role_value}});
    });

  });

    
    
  describe("Control relations", function () {
    
    
    
    before(async function () { 
      
      // NOI ABBIAMO (in python da fornire a Jinja):
      // 1) addresses_list : lista degli addresses
      // 2) addressesByEntityValue : mappa Entity value -> address name
      // 3) owner: valore numerico dell'ìowner
      
      let tx = null;
       

      let { {{DAO_name}}, owner, {{addresses_list}}} = await loadFixture(deployTokenFixture);
      addresses = [owner, {{addresses_list}}}];

      //entityByValue = new Map();
      addressesByEntityValue = new Map();

      addressesByEntityValue.set({{owner}}, owner);
      {% for entity_value, address in addressesByEntityValue.items() %}
      addressesByEntityValue.set({{entity_value}}, {{address}});
      {% endfor %}


      let ownerAddr = {{DAO_name}}.connect(owner);
      {% for role_address in addresses %}
        let {{ role_address }}Connect = {{DAO_name}}.connect(role_address);
       
      // addresses_by_entity.set({{role_value}}, {{role_address}}); //{{role_value}} is the role {{role_name}}
      {% endfor %}
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

    });
      
    it("Each role should be the controller of all and only the controlled roles", async function () {
    
    {%for role_control_test in role_control_tests%}
    role_control_test
    {% endfor %}

    {%for role_control_tests in controlled_addresses%}
    control_tests
    {% endfor %}

    it ("Control relations should be properly configured", async function () {
    {%for role_control_tests in controlled_addresses%}
    control_tests
    {% endfor %}
      expect(await {{DAO_name}}.canControl(259), (259)).to.equal(true);
      expect(await {{DAO_name}}.canControl(259), (1281)).to.equal(true);
      expect(await {{DAO_name}}.canControl(259), (1348)).to.equal(true);

  }); //end of Roles canControl

/* 
  describe("Transactions", function () {
    it("Should transfer tokens between accounts", async function () {
      const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
        deployTokenFixture
      );
      // Transfer 50 tokens from owner to addr1
      await expect(
        hardhatToken.transfer(addr1.address, 50)
      ).to.changeTokenBalances(hardhatToken, [owner, addr1], [-50, 50]);

      // Transfer 50 tokens from addr1 to addr2
      // We use .connect(signer) to send a transaction from another account
      await expect(
        hardhatToken.connect(addr1).transfer(addr2.address, 50)
      ).to.changeTokenBalances(hardhatToken, [addr1, addr2], [-50, 50]);
    });

    it("Should emit Transfer events", async function () {
      const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
        deployTokenFixture
      );

      // Transfer 50 tokens from owner to addr1
      await expect(hardhatToken.transfer(addr1.address, 50))
        .to.emit(hardhatToken, "Transfer")
        .withArgs(owner.address, addr1.address, 50);

      // Transfer 50 tokens from addr1 to addr2
      // We use .connect(signer) to send a transaction from another account
      await expect(hardhatToken.connect(addr1).transfer(addr2.address, 50))
        .to.emit(hardhatToken, "Transfer")
        .withArgs(addr1.address, addr2.address, 50);
    });

    it("Should fail if sender doesn't have enough tokens", async function () {
      const { hardhatToken, owner, addr1 } = await loadFixture(
        deployTokenFixture
      );
      const initialOwnerBalance = await hardhatToken.balanceOf(owner.address);

      // Try to send 1 token from addr1 (0 tokens) to owner.
      // `require` will evaluate false and revert the transaction.
      await expect(
        hardhatToken.connect(addr1).transfer(owner.address, 1)
      ).to.be.revertedWith("Not enough tokens");

      // Owner balance shouldn't have changed.
      expect(await hardhatToken.balanceOf(owner.address)).to.equal(
        initialOwnerBalance
      );
    });
  }); 
    */
});