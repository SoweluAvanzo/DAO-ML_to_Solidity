#  📄 **DAO-ML to Solidity Translator**

The **DAO-ML to Solidity Translator** converts XML files adhering to the DAO-ML schema into Solidity smart contracts or JSON files. This tool supports three translation schemes that define how the DAO's organizational structure is implemented in Solidity. The translation process described below can be executed by means of a command line interface (CLI) or using a proof-of-concept GUI, which also enables the user to visualize the control graph using the NetworkX library.

## Translation Process Workflow
1. **XML Schema Validation**: The input XML file is checked against the DAO-ML schema for compliance. If errors are found, the process stops, and an error is reported.
2. **Parsing**: ANTLR 4-generated parser reads and processes the XML file, structuring its content.
3. **Data Extraction**: A visitor class traverses the parsed document to extract raw data.
4. **Logical Model Generation**: The extracted data is postprocessed into a logical model that represents the DAO, independent of any target language.
5. **Translation**:
   - **Solidity Smart Contracts**: The logical model is transformed into Solidity code.
   - **JSON Output**: The model is exported as JSON files containing DAO properties.

# ⚙️ **Translation Schemes Overview**

The tool supports **three different translation schemes**:

1. **Optimized Scheme** (Command: `optimized`)
   - Designed for scalability and efficiency.
   - Encodes roles and permissions using bitmasks for better storage optimization.
   - Suitable for DAOs with a large number of roles and permissions, and granular access control requirements and complex control relations.

2. **Simple Scheme** (Command: `simple`)
   - Uses a straightforward mapping of DAO elements to Solidity contracts.
   - Efficient and scalable for basic access control without advanced role delegation.
   - Triggered automatically **only if** the following conditions are met.
   *Activation requirements:*
     - the user selects the `simple` command.
     - The **hierarchical inheritance** parameter **must** be set to `True`, ensuring roles and permissions are inherited along the hierarchy automatically.
     - The **control graph must be an acyclic path graph**, meaning:
       - Each node has at most **one outgoing** and **one incoming** edge.
       - The graph is **acyclic**, ensuring there are no loops in the control hierarchy.
   - Ideal for DAOs with simple organizational structures.

3. **Standard Scheme** (Command: `simple`)
   - This scheme is **automatically activated** if the **Simple** command is selected **and** the activation requirements for the **Simple** scheme are **not met**.
   - Uses explicit mappings for roles, permissions, and control relations.
   - Best for DAOs with more structured without specific granularity and optimization requirements.

---

## 🔧 **Command-Line Interface (CLI) Usage**

Run the translator using the following command:

```bash
python translator_cli.py -fn <function> -f <xml_file_path> [-tt <translation_logic>]
```

**Arguments:**
- `-fn` / `--function`: Choose the operation to execute (`simulate`, `translate`, or `to_json`).
- `-f` / `--file`: Path to the input XML file.
- `-tt` / `--translation_type`: Select the translation type (`simple` or `optimized`).
- `-n` / `--n_daos`: Number of DAOs to generate (default: `3`).
- `-sf`: Path to save simulation outputs (default: `sim`).
- `-test`: Execute Hardhat tests (default: `True`).
- `-gen_test`: Generate Hardhat test files (default: `False`).

---

## Directory Structure
- **`./translated/`**: Directory for storing translated Solidity files. Each DAO is contained in a separate folder, named after the DAO_ID attribute specified, which includes the following set of contracts:
   - a **Permission Manager** contract, handling the assignment of roles to agents, the respective permissions assigned to each role or committee of the DAO;
   - one contract per each **committee** defined, which implements the voting logic for that specific sub-community of DAO members;
   - additional **condition** smart contracts, when defined by the user, which check further conditions for role assignment, voting and making proposals;
   - **interface** files that facilitate the interaction between the Permission Manager of the DAO and other contracts.
- **`./out/json/daos/`**: Directory for storing JSON files with DAO properties.

---

## 🛠️ **Function Descriptions**

- **`simulate`**:
  - Generates Solidity code simulations for a given number of DAOs.
  - Example:
    ```bash
    python translator_cli.py -fn simulate -n 5 -tt optimized
    ```

- **`translate`**:
  - Converts an XML file into Solidity smart contracts using the selected translation logic.
  - Example:
    ```bash
    python translator_cli.py -fn translate -f path/to/file.xml -tt simple
    ```

- **`to_json`**:
  - Converts the DAO-ML model into a JSON representation.
  - Example:
    ```bash
    python translator_cli.py -fn to_json -f path/to/file.xml
    ```

---

## **Running Hardhat Tests**

To compile and run tests using Hardhat:

```bash
npx hardhat compile
npx hardhat test
```


## Manual Run


### Prerequisites

- A "command line", such as PowerShell (Windows) or Bash (Unix)
- Python 3.4
- pip, a Python packages manager

#### Installation

First of all, install all required packages by running the following command:
**`pip install requirements.txt`**
- lxml
- networkx

Then if you are using WINDOWS, installation warnings may arise, instructing you to add the path of Python scripts to your PATH environmnent variable. That folder the following one:
**`C:\Users\<<YOUR_USER>>\AppData\Roaming\Python\<<PYTHON_FOLDER_LIKE: Python312>>\Scripts`** .
The packages that might arise that waring are the following
- xmlschema-json2xml
- ipython
- ipython3
- pipreqs


#### compile the grammar

run:
**`python -m compile_DAOML_grammar > CCCCCC.txt`**


### Manually run a test file on Command Line 

With the Command Line (Terminal) pointing to the root of this project (i.e. "DAO-ML_to_Solidity" ),
run the following command to manually execute a test:

**`python -m src.tests.pipeline.manual.test_pi > AAAAA.txt`**
**`python -m src.tests.pipeline.manual.t_file_1 > AAAAA.txt`**

Breakdown of the command parts:
- -m : specifies that the current directory REMAINS TO BE the root directory, i.e. the top-level package is "src", as it should be
- src.test.pipeline.manual: "pipeline" and "manual" are a sub-package and a sub-sub-package inside the file system tree. You can chain how many sub-packages you like, separated by a dot.
- .test_pi: the file you actually want to run, BUT expressed as a module (i.e., the extension is missing, similarly to import statements)
- > AAAAA.txt: (Optional) output redirection into a text file named "AAAAA", optionally added to not clog the terminal output.




## **Translator Architecture**
We provide below a class diagram representing the architecture of the translator, including the main classes and modules and their relations. The OptimizedTranslator class handles translation using the **Optimized** scheme, whereas the **SimpleTranslator** class handles translation using the remaining two schemes automatically selecting either the **simple** or **standard** scheme.

![immagine](https://github.com/user-attachments/assets/3a60fc72-eb75-4fa3-a91f-b5041b7725a3)

---

## Data Model
We provide below a class diagram displaying the key classes of a language-independent model of a DAO specified using DAO-ML. This model expands the module in the diagram above, dsiplaying the translator architecture. Its implementation can be found in the DAOClasses.py file.

![immagine](https://github.com/user-attachments/assets/36f18139-71a0-44f7-8e69-d8fcd74912d9)
