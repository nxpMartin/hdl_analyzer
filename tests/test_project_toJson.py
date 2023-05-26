
import os
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project
import hdl_analyzer.scripts.hdl_analyzer_toJson as hdl_analyzer_toJson
import hdl_analyzer.scripts.hdl_analyzer_hiearchy as hdl_analyzer_hiearchy

def test_project_toJson_parse():
  testdir = os.path.dirname(os.path.abspath(__file__))
  cmd = ["tests/project_toJson.json", "--clear", "--dir", testdir, "--add-directory", os.path.join(testdir,"vhdl_top_verilog")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/project_toJson.json", "--analyze"]
  hdl_analyzer_project.main(cmd)
  #raise(Exception("Fail here"))

def test_project_toJson_convert():
  cmd = ["tests/project_toJson.json", "tests/project_toJson_out.json", "--debug"]
  hdl_analyzer_toJson.main(cmd)
  #raise(Exception("Fail here"))

def test_project_toJson_quick_load():
  cmd = ["tests/project_toJson.json", "--module", "top"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/project_toJson_out.json", "--module", "top"]
  hdl_analyzer_hiearchy.main(cmd)
  #raise(Exception("Fail here"))

