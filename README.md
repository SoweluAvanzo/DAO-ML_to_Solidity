# DAO-ML-to-Solidity Translator

## Overview
This tool translates XML files conforming to the DAO-ML schema into Solidity smart contracts or JSON files. The Solidity code generation supports two distinct schemas, named **Simple** and **Optimized**. The **Simple** schema provides a basic implementation of the access-control logic within the DAO, while the **Optimized** schema enhances storage efficiency and scalability by encoding information concerning roles and permission assignments into bitmasks.

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
```bash
python translator_cli.py <function> <xml_file_path> [translation_logic]
```
    -**<function>**: The action to execute (translate or to_json).
    -**<xml_file_path>**: Path to the input XML file.
    -**[translation_logic]**: (Optional) Specifies the Solidity schema (simple or optimized). Defaults to simple if not provided.
