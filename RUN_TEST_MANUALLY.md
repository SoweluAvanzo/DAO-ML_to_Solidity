# DAO-ML-to-Solidity Translator

## Manual Run

A "command line" is required, as well as Python 3.4 or greater.

### Prerequisites

#### Installation

First of all, install all required packages by running the following command:
**`pip install requirements.txt`**

- lxml
- networkx

Then if you are using WINDOWS, installation warnings may arise, instructing you to add the path of Python scripts to your PATH environmnent variable. That folder the following one:
**`C:\Users\<<YOUR_USER>>\AppData\Roaming\Python\<<PYTHON_FOLDER_LIKE: Python312>>\Scripts`** .

The packages that might arise that waring are the following
- xmlschema-json2xml
- xmlschema-json2xml
- xmlschema-json2xml
- ipython
- ipython3
- pipreqs


#### compile the grammar

run:
**`python -m compile_DAOML_grammar > CCCCCC.txt`**


### Run on Terminal a test file manually

With the Command Line (Terminal) pointing to the root of this project (i.e. "DAO-ML_to_Solidity" ),
run the following command to manually execute a test:

**`python -m src.tests.pipeline.manual.test_pi > AAAAA.txt`**
**`python -m src.tests.pipeline.manual.t_file_1 > AAAAA.txt`**

Breakdown of the command parts:
- -m : specifies that the current directory REMAINS TO BE the root directory, i.e. the top-level package is "src", as it should be
- src.test.pipeline.manual: "pipeline" and "manual" are a sub-package and a sub-sub-package inside the file system tree. You can chain how many sub-packages you like, separated by a dot.
- .test_pi: the file you actually want to run, BUT expressed as a module (i.e., the extension is missing, similarly to import statements)
- > AAAAA.txt: (Optional) output redirection into a text file named "AAAAA", optionally added to not clog the terminal output.
