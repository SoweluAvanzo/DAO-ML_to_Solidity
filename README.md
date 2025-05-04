# DAO-ML-to-Solidity Translator

## Overview
The DAO-ML to Solidity translator transforms XML files conforming to the DAO-ML schema into Solidity smart contracts or JSON files. The Solidity code generation supports two distinct schemas, named **Simple** and **Optimized**. The **Simple** schema provides a basic implementation of the access-control logic within the DAO, while the **Optimized** schema enhances storage efficiency and scalability by encoding information concerning roles and permission assignments into bitmasks. The translation process described below can be executed by means of a command line interface (CLI) or using a proof-of-concept GUI, which also enables the user to visualize the control graph using the NetworkX library.
## Process Workflow
1. **XML Schema Validation**: The input XML file is checked against the DAO-ML schema for compliance. If errors are found, the process stops, and an error is reported.
2. **Parsing**: ANTLR 4-generated parser reads and processes the XML file, structuring its content.
3. **Data Extraction**: A visitor class traverses the parsed document to extract raw data.
4. **Logical Model Generation**: The extracted data is postprocessed into a logical model that represents the DAO, independent of any target language.
5. **Translation**:
   - **Solidity Smart Contracts**: The logical model is transformed into Solidity code.
   - **JSON Output**: The model is exported as JSON files containing DAO properties.

## CLI Commands Overview
### Command Structure

**`python translator_cli.py <function> <xml_file_path> [translation_logic]`**

- **`<function>`**: The action to execute (`translate` or `to_json`).
- **`<xml_file_path>`**: Path to the input XML file.
- **`[translation_logic]`**: (Optional) Specifies the Solidity schema (`simple` or `optimized`). Defaults to `simple` if not provided.
  
### Directory Structure
- **`./translated/`**: Directory for storing translated Solidity files. Each DAO is contained in a separate folder, named after the DAO_ID attribute specified, which includes the following set of contracts:
   - a **Permission Manager** contract, handling the assignment of roles to agents, the respective permissions assigned to each role or committee of the DAO;
   - one contract per each **committee** defined, which implements the voting logic for that specific sub-community of DAO members;
   - additional **condition** smart contracts, when defined by the user, which check further conditions for role assignment, voting and making proposals;
   - **interface** files that facilitate the interaction between the Permission Manager of the DAO and other contracts.
- **`./out/json/daos/`**: Directory for storing JSON files with DAO properties.
## Translator Architecture
We provide below a class diagram representing the architecture of the translator, including the main classes and modules and their relations.

![immagine](https://github.com/user-attachments/assets/3a60fc72-eb75-4fa3-a91f-b5041b7725a3)

## Data Model
We provide below a class diagram displaying the key classes of a language-independent model of a DAO specified using DAO-ML. This model expands the module in the diagram above, dsiplaying the translator architecture. Its implementation can be found in the DAOClasses.py file.

![immagine](https://github.com/user-attachments/assets/36f18139-71a0-44f7-8e69-d8fcd74912d9)


## Run Simulation tests

npx hardhat compile
npx hardhat test
