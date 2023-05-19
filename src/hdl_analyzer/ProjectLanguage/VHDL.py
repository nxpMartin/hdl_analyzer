
import hdl_analyzer.ProjectLanguage.Language as Language

from hdlConvertor import HdlConvertor
from hdlConvertorAst.language import Language as AstLanguage

class VHDL(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language, debug):
    super().__init__(json_data, directory, language, debug)
    self.file_extensions = [".vhd",".vhdl"]
  
  def analyze(self, analyzer):
    convertor = HdlConvertor()
    for file_name in self.files:
      if self.debug:
        print("Parsing VHDL file {}".format(file_name))
      parsed = convertor.parse(file_name, AstLanguage.VHDL, self.includes)
      analyzer.apply_parsed(parsed, file_name)
