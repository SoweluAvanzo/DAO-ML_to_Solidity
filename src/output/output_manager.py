import src.output.base_output as b_o
import src.pipeline.pipeline_item as pi

# TODO : WHAT TO ADD?
# from notes
# 2) OutputManager: in questo caso, "FileManager" che accetta produce un file a partire da una lista di stringhe / un template
# 2.1) TextFileOutput: prende una lista di stringhe (le varie righe) e salva su file (utile per ...".sol"-generator -> crea file .sol)
# 2.2) TemplateRenderer -> accetta dei dati in un dizionario, popola un template (in Jinja) e restituisce le righe (po: crea il file (usa un TextFileOutput))

class OutputManager(pi.PipelineItem):
    def __init__(self, key:str, preferential_output: b_o.BaseOutput):
        super().__init__(key)
        self.preferential_output = preferential_output

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        return self.preferential_output.to_output(what, destination=destination, additional_data=additional_data)
