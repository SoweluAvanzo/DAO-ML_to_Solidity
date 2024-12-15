import sys
from FileHandler import *
import argparse
import json
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
        optimized= True if args.translation_type== "optimized" else False
        write_SCs(generate_simulations(n_daos=args.n_daos, optimized=optimized), args.sf)
        return        
    
    if not args.file:
        print("Error", "Please enter the XML file name.")
        return None
    
    if args.function=="translate":
        translate_SCs(args.file, args.translation_type)
        # TODO: refactoring
        # 1) DiagramInput: mix (da refattorizzare!) di lettura XML e istanziazione di "DiagramManager"
        # 2) OutputManager: in questo caso, "FileManager" che accetta produce un file a partire da una lista di stringhe / un template
        # 2.1) TextFileOutput: prende una lista di stringhe (le varie righe) e salva su file (utile per ...".sol"-generator -> crea file .sol)
        # 2.2) TemplateRenderer -> accetta dei dati in un dizionario, popola un template (in Jinja) e restituisce le righe (po: crea il file (usa un TextFileOutput))
        # 3) SolidityTranslator: mega classe / sub-framework che si occupa di:
        # 3.1) SoliditySmartContractGenerators: "simple" o "optimized", trasformano un "DiagramManager" in una lista di Smart Contract
        # 3.1.N) abbiamo: "SolidityTranslatorSimple", "SolidityTranslatorOptimize", "SolidityTranslatorDiamond", "SolidityTranslator" (sopraclasse), "Translator" (sopra-sopraclasse)
        # 3.2) SoliditySCOutput: prende una lista di Smart Contract e un "TextFileOutput" e genera i file ".sol"
        # 3.3) SolidityTestOutput: riceve dei dati gia' preparati, invoca "TemplateRenderer" e fornisce il suo risultato ad un "TextFileOutput"
        # 3.3) SolidityTestManager: algoritmo:
        # 3.3.1) prende una DAO (o meglio: un "DiagramManager" ed itera per ogni DAO)
        # 3.3.2) istanzia un "TestGeneratorOptimized", lo invoca e ottiene i dati
        # 3.3.3) istanzia e invoca una "SolidityTestOutput" con i dati di cui sopra

        # Note FUTURE per refactoring:
        # 1) "SoliditySCOutput" e "SolidityTestOutput" dovranno estendere la classe "WXYZ_Output_ABCD", cosi' che
        #    la sopraclasse di "SolidityTranslator" possa definire una lista di "Output" e iterarla per proddure cose
        # 2) "TextFileOutput" sara' solo una classe tra le varie sottoclassi di "OutputEndpoint": "to-JSON" sara' un'altra sottoclasse, "to-SQL-DB" una terza, etc
        # 2.1) in futuro dovremo capire come generalizzare la "lista di righe" e "oggetto intero" (Smart Contract / dati di test / etc) in un modo coerente

    elif args.function=="to_json":
        print_json(args.file)
    elif args.test:
        pass
    else:
        print("Error", "Invalid function name. Please, enter translate followed by the xml file path, or to_json followed by the XML file path. to execute the desired action")
      
if __name__ == '__main__':
    main()
    