import src.pipeline.pipeline_item as pi

import src.postprocessing.consts_template as consts_t

import src.files.file_utils as files
import src.utilities.utils as u


class VotingProtocolListLoader(pi.PipelineItem):
    def __init__(self, pipeline_item_data,
                 printer_debug: u.PrinterDebug = None,
                 folder_voting_protocols: str = None,
                 key_folder_voting_protocols: str = None
                 ):
        super().__init__(pipeline_item_data, printer_debug=printer_debug)
        self.folder_voting_protocols = folder_voting_protocols
        self.key_folder_voting_protocols = key_folder_voting_protocols

    def load_list_from(self, from_input) -> set[str]:
        """
        Override-designed
        """
        files_vp = files.list_files_in(from_input)
        # just the filename
        files_vp = set([
            f[:f.find(".")]
            for f in files_vp
        ])
        return files_vp

    def run(self, inputs: dict):
        all_voting_protocols_folder = consts_t.DEFAULT_FOLDER_TEMPLATES_VOTING_PROTOCOL
        if self.folder_voting_protocols is not None:
            all_voting_protocols_folder = self.folder_voting_protocols
        elif (self.key_folder_voting_protocols is not None) and (self.key_folder_voting_protocols in input):
            x = inputs[self.key_folder_voting_protocols]
            if (x is not None) and isinstance(x, str):
                all_voting_protocols_folder = x
        return self.load_list_from(all_voting_protocols_folder)
