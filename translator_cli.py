import sys
from FileHandler import *
              
def main(argv):

    if len(argv) < 3:
        if argv[1] == "simulate":
           sim= write_SCs(generate_simulations(), "sim")
        else:
            print("Error", "Please enter the function you wish to call (translate, to_json) followed by XML file name. You can also select the translation logic (simple or optimized)")
        return
    file_path = argv[2]
    if argv[1]=="translate":
        translation_logic= argv[3] if len(argv) > 3 else "simple"
        translate_SCs(file_path, translation_logic)
    elif argv[1]=="to_json":
        print_json(file_path)        
    else:
        print("Error", "Invalid function name. Please, enter translate followed by the xml file path, or to_json followed by the XML file path. to execute the desired action")
        
if __name__ == '__main__':
    main(sys.argv)