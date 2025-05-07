# DAO-ML-to-Solidity Translator

## Manual Run

### Run on Terminal a test file manually

With the Command Line (Terminal) pointing to the root of this project (i.e. "DAO-ML_to_Solidity" ),
run the following command to manually execute a test:

**`python -m src.tests.pipeline.manual.test_pi > AAAAA.txt`**

Breakdown of the command parts:
- -m : specifies that the current directory REMAINS TO BE the root directory, i.e. the top-level package is "src", as it should be
- src.test.pipeline.manual: "pipeline" and "manual" are a sub-package and a sub-sub-package inside the file system tree. You can chain how many sub-packages you like, separated by a dot.
- .test_pi: the file you actually want to run, BUT expressed as a module (i.e., the extension is missing, similarly to import statements)
- > AAAAA.txt: (Optional) output redirection into a text file named "AAAAA", optionally added to not clog the terminal output.
