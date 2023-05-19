
import hdl_analyzer.ProjectLanguage.Language as Language

from hdlConvertor import HdlConvertor
from hdlConvertorAst.language import Language as AstLanguage

import os

class Verilog(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language, debug):
    super().__init__(json_data, directory, language, debug)
    self.file_extensions = [".v"]
  
  def analyze(self, analyzer):
    convertor = HdlConvertor()
    for file_name in self.files:
      if self.debug:
        print("Parsing Verilog file {}".format(file_name))
      parsed = convertor.parse(file_name, AstLanguage.VERILOG, self.includes, debug=self.debug)
      analyzer.apply_parsed(parsed, file_name)
  
  def preprocess(self, out_dir):
    convertor = HdlConvertor()
    for file_name in self.files:
      out_file = file_name.replace(self.directory,out_dir)
      if self.debug:
        print("Preprocess Verilog file {}".format(file_name))
      preprocessed = convertor.verilog_pp(file_name, AstLanguage.VERILOG, self.includes)
      os.makedirs(os.path.dirname(out_file), exist_ok = True)
      file = open(out_file, "w")
      file.write(preprocessed)
      file.close()
      if self.debug:
        print("Save preprocessed Verilog file as {}".format(out_name))

