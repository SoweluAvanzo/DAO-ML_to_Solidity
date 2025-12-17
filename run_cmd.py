import src.launchers.launcher_cmd as launcher


# python -m src.launchers.launcher_cmd --file "asd.xml" --.... > lss.txt

"""
python run_cmd.py --file "Travelhive_final_model" --input_base_folder "./data" --input_format "xml" --file_input_extension "xml" --persistance_type "file" --xml_schema_folder "./data" --xml_schema_filename "XSD_DAO_ML" --xml_schema_extension "xsd" \
 --post_processing "sol" --version_translator "1.0.0" --version_translation_target "1.0.0" --output_persistance "file" --output_type "jinja" --output_uri "./out_put" --base_template_folder "./Templates" --folder_voting_protocols_solidity "./Templates/voting_protocols" \
 --post_processing "sol_tests" --output_persistance "file" --output_type "jinja" --output_uri "./out_put" --base_template_folder "./Templates" --folder_voting_protocols_solidity "./Templates/voting_protocols" \
 --post_processing "asm" --output_persistance "file" --output_type "jinja" --output_uri "./out_put" --base_template_folder "./Templates" --folder_voting_protocols_solidity "./Templates/voting_protocols" \
 --post_processing "json" --output_persistance "file" --output_type "jinja" --indent_json 2 \
 > RUN_cmd.txt
"""

print("START running translator ...\n\n")
launcher.main()
print("\n\n END")
