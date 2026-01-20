# 📄 **DAO-ML to Solidity Translator**

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
     _Activation requirements:_
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

## 🔧 **Command-Line Interface (CLI) Usage** (V 1.0 - legacy)

### Translator

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

#### Directory Structure

- **`./translated/`**: Directory for storing translated Solidity files. Each DAO is contained in a separate folder, named after the DAO_ID attribute specified, which includes the following set of contracts:
  - a **Permission Manager** contract, handling the assignment of roles to agents, the respective permissions assigned to each role or committee of the DAO;
  - one contract per each **committee** defined, which implements the voting logic for that specific sub-community of DAO members;
  - additional **condition** smart contracts, when defined by the user, which check further conditions for role assignment, voting and making proposals;
  - **interface** files that facilitate the interaction between the Permission Manager of the DAO and other contracts.
- **`./out/json/daos/`**: Directory for storing JSON files with DAO properties.

---

#### 🛠️ **Function Descriptions**

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

### **Running Hardhat Tests**

To compile and run tests using Hardhat:

```bash
npx hardhat compile
npx hardhat test
```

## 🔧 **Command-Line Interface (CLI) Usage** (V 2.0 - new)

### Prerequisites

- A "command line", such as PowerShell (Windows) or Bash (Unix)
- Python 3.4
- pip, a Python packages manager

#### Installation

First of all, install all required packages by running the following command:

```bash
pip install -r requirements.txt
```

Which will install, at the time of writings (2025-12-18)

- regex==2025.9.18
- networkx==3.5
- xmlschema==4.1.0
- lxml==6.0.2
- antlr4-python3-runtime==4.13.1
- typing==3.7.4
- jinja2==3.1.6
- snakes==0.9.33

Then if you are using WINDOWS, installation warnings may arise, instructing you to add the path of Python scripts to your PATH environmnent variable. That folder the following one:
**`C:\Users\<<YOUR_USER>>\AppData\Roaming\Python\<<PYTHON_FOLDER_LIKE: Python312>>\Scripts`** .
The packages that might arise that warning are the following:

- xmlschema-json2xml
- ipython
- ipython3
- pipreqs

#### compile the grammar

If the DAO-ML modules are somewhat missing, You can re-compile the grammar and the module by running the following command:

```bash
python -m compile_DAOML_grammar > CCCCCC.txt
```

By default, it produces the (also Python) files in **"./src/parser/xml/"**

### **Run the Translator** on Command Line

With the Command Line (Terminal) pointing to the root of this project (i.e. "DAO-ML_to_Solidity" ),
run the following command to manually execute the whole translation process comprised of:

- input: retrieved from a file, either an XML or a JSON one (furhter developments will include a DataBase). If the input is an XML file, then the XML schema data needs to be defined as well
- output (one or more of the following; a folder path might be required, see the flags descriptions):
  - Solidity code, under the folder "**solidity**"; each DAO has its own folder with all the related Solidity code; the Solidity code for the Diagram might be added
  - Tests in _JavaScript_ of the Solidity code based on the _Hardhat_ software, under the folder "**test_scripts**"
  - _ASM_ representation of each DAO, individually, under the folder "**asm**"
  - a JSON file with the whole Diagram representation

#### Note:

Currently, You can either run the default Translation process (which produces all the results mentioned above) or a customized one.
If You want the default one, just type .

**BEWARE TO REDIRECT YOUR OUTPUT!** By default, currently (2025-12-18), the translator process produces a considerable amount of debug output to the console. _Despite already existing a logger-based system, it's not already tested nor made available through configuration, so the output !._

Here follows the same example of CLI-based usage, both in Windows's Command Line and Bash codes.
It assumes that the input (containing the DAO definition [well, the *Diagram with the DAOs inside*, actually])

#### Command Line (Windows):

```
python run_cmd.py --file "Travelhive_final_model" --input_base_folder ".\data" --input_format "xml" --file_input_extension "xml" --persistance_type "file" --xml_schema_folder ".\data" --xml_schema_filename "XSD_DAO_ML" --xml_schema_extension "xsd" --post_processing_transformation "sol" --output_persistance "file" --output_type "jinja" --output_uri ".\out_put" --base_template_folder ".\Templates" --folder_voting_protocols_solidity ".\Templates\voting_protocols" --version_translator "1.0.0" --version_translation_target "1.0.0" --post_processing_transformation "sol_tests" --output_persistance "file" --output_type "jinja" --output_uri ".\out_put" --folder_voting_protocols_solidity ".\Templates\voting_protocols" --post_processing_transformation "asm" --output_persistance "file" --output_type "jinja" --output_uri ".\out_put" --folder_voting_protocols_solidity ".\Templates\voting_protocols" --post_processing_transformation "json" --output_persistance "file" --output_type "str" --indent_json 2 > RUN_cmd.txt
```

#### Bash:

```bash
#!/bin/bash
python run_cmd.py --file "Travelhive_final_model" --input_base_folder "./data" --input_format "xml" --file_input_extension "xml" --persistance_type "file" --xml_schema_folder "./data" --xml_schema_filename "XSD_DAO_ML" --xml_schema_extension "xsd" \
 --post_processing_transformation "sol" --output_persistance "file" --output_type "jinja" --output_uri "./out" --base_template_folder "./Templates" --folder_voting_protocols_solidity "./Templates/voting_protocols" --version_translator "1.0.0" --version_translation_target "1.0.0" \
 --post_processing_transformation "sol_tests" --output_persistance "file" --output_type "jinja" --output_uri "./out" --folder_voting_protocols_solidity "./Templates/voting_protocols" \
 --post_processing_transformation "asm" --output_persistance "file" --output_type "jinja" --output_uri "./out"  --folder_voting_protocols_solidity "./Templates/voting_protocols" \
 --post_processing_transformation "json" --output_persistance "file" --output_type "str" --indent_json 2 \
 > RUN_cmd.txt

```

<!--
- **`python -m src.tests.pipeline.manual.test_pi > AAAAA.txt`**
- **`python -m src.tests.pipeline.manual.t_file_1 > AAAAA.txt`**
- **`python -m src.tests.pipeline.manual.t_jinja > COMPILE_TEST.txt`**

Breakdown of the command parts:
- -m : specifies that the current directory REMAINS TO BE the root directory, i.e. the top-level package is "src", as it should be
- src.test.pipeline.manual: "pipeline" and "manual" are a sub-package and a sub-sub-package inside the file system tree. You can chain how many sub-packages you like, separated by a dot.
- .test_pi: the file you actually want to run, BUT expressed as a module (i.e., the extension is missing, similarly to import statements)
- > AAAAA.txt: (Optional) output redirection into a text file named "AAAAA", optionally added to not clog the terminal output.
-->

### Flags and arguments

All flags that are not required have a default value, so can be safely ignored.

The fields related with both the "post-processing transformation" and the output can be inserted multiple times, forming an array.
This is needed to define multiple elaborations of a loaded DAO (_diagram_).

- filename / filepath

  - alternatives: -f, --file, --file-name, --file_name, --file-path, --file_path, -i, --input, --input_uri, --input-uri
  - type: string
  - required: No
  - example: "Travelhive_final_model"
  - description: file name/path of the (XML?) DAO (Diagram, actually) You need to process

- input base folder

  - alternatives: -if, --input_base_folder, --input-base-folder, --input-folder, --input_folder,
  - type: string
  - required: No
  - example: "./data"
  - description: folder path acting as the starting point for all inputs,

- Input format

  - alternatives: -i_f, --input_format, --input-format
  - type: string
  - required: No
  - example: "xml"
  - description: Format of the input in which the model has been encoded; currently the accepted values are the following ones: "xml", "json"

- File input extension

  - alternatives: -fie, --file_input_extension, --file-input-extension
  - type: string
  - required: No
  - example: "xml"
  - description: Extension of the input file

- Persistance type

  - alternatives: -pt, --persistance_type, --persistance-type
  - type: string
  - required: No
  - example: "file"
  - description: Types of persistance units to read the model from or to save the produced output; currently it accepts: "FILE", "file", "DATABASE", "db" ( **BEWARE! Currently 2025-12-18 Database is not implemented!** )

- XML version

  - alternatives: -xml_v, --xml_version, --xml-version
  - type: string
  - required: No
  - example: "1.0.0"
  - description: Version of the XML standard (as input), usually it's 1.0.0

- Folder of the XML schema

  - alternatives: xml_schema_folder, --xml-schema-folder
  - type: string
  - required: No
  - example: "./data"
  - description: Folder path holding the XML schema file

- Filename of the XML schema

  - alternatives: xml_schema_filename, --xml-schema-filename
  - type: string
  - required: No
  - example: "XSD_DAO_ML"
  - description: Folder path holding the XML schema file

- Extension of the XML schema

  - alternatives: xml_schema_extension, --xml-schema-extension
  - type: string
  - required: No
  - example: "xsd"
  - description: Extension of the XML schema file

- Post-processing transformation(s)

  - alternatives: -pp, -ppt, --post_processing_transformation, --post-processing-transformation, --post_processing, --post-processing
  - type: (array of) string
  - required: Yes
  - example: "sol"
  - description: Post-processing phase(s) to digest a Diagram, one(+) of the following: "SOLIDITY" (or "sol"), "SOLIDITY_HARDHAT_TESTS" (or "sol_tests"), "ASM" (or "asm"), "JSON" (or "json")

- Version(s) of the translator(s)

  - alternatives: -vt, -vtr, --version_translator, --version-translator
  - type: (array of) string
  - required: No
  - example: "1.0.0"
  - description: Version of the translator; Defaults to '1.0.0'. Currently, only one version is implemented, but it's designed for retrocompatibility.

- Base folder path(s) of all templates

  - alternatives: --base_template_folder, --folder-template-base, --folder_templates, --folder_template, --folder-base-template, --folder-template, --template-folder, --base-template-folder, -ft, -ftb, --base_template_folder, -tf, -btf, --template-folder-base, --templates_folder_base, -tfb, --folder_base_template, --templates-folder-base, --folder-templates, --base-folder-template, --templates_folder, --template_base_folder, --folder_template_base, --template_folder_base, --templates-base-folder, --templates-folder, --templates_base_folder, --template-base-folder, --base_folder_template, --template_folder
  - type: (array of) string
  - required: No
  - example: "./Templates"
  - description: folder (base) path for all template files; could be an absolute path or a relative path. If it is defined in the FIRST Post Processing Subphase and it's a "file", then this path could be shared for all other "file"-based entries without the need to repeat them

- Base folder path(s) of all Solidity Voting Protocols templates

  - alternatives: -fvps, --folder_voting_protocols_solidity, --folder-voting-protocols-solidity, -sfvp, --solidity_folder_voting_protocols, --solidity-folder-voting-protocols, -fps, --folder_voting_solidity, --folder-voting-solidity, -sfp, --solidity_folder_voting, --solidity-folder-voting
  - type: (array of) string
  - required: No
  - example: "./Templates/voting_protocols"
  - description: folder (base) path for all voting protocol template files; could be an absolute path or a relative path.

- JSON dumping indentation

  - alternatives: -ij, --indent_json, --indent-json
  - type: (array of) either string or number
  - required: No
  - example: 2
  - description: Indentation for JSON dumping; could be a number, which indicates the amount of "tab"s added at each nesting level, or a string for custom indentation

- Output type(s)

  - alternatives: -ot, --output_type, --output-type
  - type: (array of) string
  - required: No
  - example: "jinja"
  - description: Output type, which depends upon the related Post Processing Translation: either a plain text (used for JSON) or a Jinja-based template (currently used for Solidity, Solidity Hardhat Test or ASM); current available options: "jinja", "str".

- Output persistance type(S)

  - alternatives: -op, -opt, --output_persistance, --output-persistance, --output_persistance_type, --output-persistance-type
  - type: (array of) string
  - required: Yes
  - example: "file"
  - description: Types of persistance ends to output the result of the related Post Processing Translation; currently it accepts: "FILE", "file", "DATABASE", "db" ( **BEWARE! Currently 2025-12-18 Database is not implemented!** )

- Output URI(s) / base folder path(s)

  - alternatives: -ouri, --output, --output-uri, --output_uri
  - type: (array of) string
  - required: No
  - example: "./out_put"
  - description: URI for the output (a folder path for the File-based ones, a onnection string for); if it's specified once, then it's applied to all outpts. If multiple postprocessing are defined and some (but not all) of them requires a file-based output, then You can shortcut the outputs entries: at first, define the first postprocessing with the file output and the folder path as this flag value, then define all non-file-outputting postprocessing, then define the last postprocessing omitting the output-uri, so that they will inherit the value.

## **Translator Architecture**

We provide below a class diagram representing the architecture of the translator, including the main classes and modules and their relations. The OptimizedTranslator class handles translation using the **Optimized** scheme, whereas the **SimpleTranslator** class handles translation using the remaining two schemes automatically selecting either the **simple** or **standard** scheme.

![immagine](https://github.com/user-attachments/assets/3a60fc72-eb75-4fa3-a91f-b5041b7725a3)

---

-

## Data Model

We provide below a class diagram displaying the key classes of a language-independent model of a DAO specified using DAO-ML. This model expands the module in the diagram above, dsiplaying the translator architecture. Its implementation can be found in the DAOClasses.py file.

![immagine](https://github.com/user-attachments/assets/36f18139-71a0-44f7-8e69-d8fcd74912d9)
