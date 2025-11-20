#!/usr/bin/env python3
"""
Test script to translate Travelhive XML to Solidity using the translator service.
"""
import sys
import os
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.api.services.translator_service import TranslatorService


def main():
    # Paths
    templates_dir = PROJECT_ROOT / 'Templates'
    output_dir = PROJECT_ROOT / 'output' / 'travelhive_test'
    xml_file = PROJECT_ROOT / 'data' / 'Travelhive_final_model.xml'

    # Read XML content
    print(f"Reading XML file: {xml_file}")
    with open(xml_file, 'r') as f:
        xml_content = f.read()

    # Initialize translator service
    print(f"Initializing translator service...")
    translator_service = TranslatorService(templates_dir, output_dir)

    # Step 1: Validate XML
    print("\n--- Step 1: Validating XML ---")
    is_valid, errors, _ = translator_service.validate_xml(xml_content)
    if not is_valid:
        print(f"Validation failed with errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("XML validation: PASSED")

    # Step 2: Generate model
    print("\n--- Step 2: Generating model ---")
    success, errors, diagram_manager = translator_service.generate_model(xml_content)
    if not success:
        print(f"Model generation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    # Print model info
    if diagram_manager:
        print(f"Model generated successfully!")
        print(f"  DAOs found: {len(diagram_manager.daos) if hasattr(diagram_manager, 'daos') else 'N/A'}")

    # Step 3: Translate to Solidity
    print("\n--- Step 3: Translating to Solidity ---")
    success, errors, contract_files, test_files = translator_service.translate_to_solidity(
        xml_content,
        output_dir,
        generate_tests=True
    )

    if not success:
        print(f"Translation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"\nTranslation completed successfully!")
    print(f"\nGenerated contracts ({len(contract_files)}):")
    for contract_file in contract_files:
        print(f"  - {contract_file}")

    print(f"\nGenerated tests ({len(test_files)}):")
    for test_file in test_files:
        print(f"  - {test_file}")

    print(f"\nOutput directory: {output_dir}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
