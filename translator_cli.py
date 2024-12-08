import sys
from FileHandler import *
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="CLI Parser for DAO-ML to Solidity Translator"
    )
    parser.add_argument(
        "-n", "--n_daos",
        type=int,
        help="Number of DAOs to generate",
        required=False,
        default=3
    )
    parser.add_argument(
        "-fn", "--function",
        type=str,
        help="Select the function needed of the translator",
        required=True,
        choices=["simulate", "translate", "to_json"]
    )
    parser.add_argument(
        "-tt", "--translation_type",
        type=str,
        help="Select whether you want to use the simple or optimized translation logic",
        required=False,
        choices=["optimized", "simple"],
        default="simple"
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="XML file path",
        required=False
    )
    parser.add_argument(
        "-sf",
        type=str,
        help="path of the folder where the simulations will be saved",
        required=False,
        default="sim"
    )
    parser.add_argument(
        "-test",
        type=bool,
        help="execute hardhat test simulations",
        required=False,
        default=True
        )
    
    args = parser.parse_args()

    if args.function == "simulate":
        write_SCs(generate_simulations(n_daos=args.n_daos), args.sf)
    elif args.test:
        write_SCs(generate_simulations(n_daos=args.n_daos), args.sf)
        
    else:
        if not args.file:
            print("Error", "Please enter the XML file name.")
            return None
        if args.function=="translate":
            translate_SCs(args.file, args.translation_type)
        elif args.function=="to_json":
            print_json(args.file)
        else:
            print("Error", "Invalid function name. Please, enter translate followed by the xml file path, or to_json followed by the XML file path. to execute the desired action")
      
if __name__ == '__main__':
    main()