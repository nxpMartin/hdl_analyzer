
from hdl_analyzer.Analyzer import Analyzer

#from hdlConvertorAst.hdlAst import HdlModuleDef, HdlCompInst, HdlStmFor
from hdlConvertorAst.hdlAst import *

import hdlConvertorAst.to.json

import json

class OneObj:
  def __init__(self, obj):
    self.objs = [obj]

class ToJson(Analyzer.Analyzer):
  def __init__(self, debug):
    super().__init__(debug)
    
    self.objs = []
  
  def apply_parsed(self, parsed, file_name):
    if self.debug:
      print("{}:\n{}".format(file_name,parsed))
    for obj in parsed.objs:
      self.objs.append(obj)
  
  def write_JSON(self, fp):
    conv = hdlConvertorAst.to.json.ToJson()
    if self.debug:
      fp.write("[\n")
    else:
      fp.write("[")
    separator = False
    for subobj in self.objs:
      json_dict = conv.visit_HdlContext(OneObj(subobj))
      
      if self.debug:
        if separator:
          fp.write(",\n")
        json.dump(json_dict[0], fp, indent=2)
      else:
        if separator:
          fp.write(",")
        json.dump(json_dict[0], fp)
      separator = True
    if self.debug:
      fp.write("\n]")
    else:
      fp.write("]")

