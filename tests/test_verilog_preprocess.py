import os
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project
import hdl_analyzer.scripts.hdl_analyzer_preprocess as hdl_analyzer_preprocess

def test_verilog_preprocess_project():
  testdir = os.path.dirname(os.path.abspath(__file__))
  cmd = ["tests/verilog_preprocess.json", "--clear", "--dir", testdir, "--add-directory", os.path.join(testdir, "verilog_preprocess")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_preprocess.json", "--remove-file", os.path.join(testdir, "verilog_preprocess/params.v")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_preprocess.json", "--lang", "verilog", "--add-include", os.path.join(testdir, "verilog_preprocess")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_preprocess.json", "--analyze"]
  hdl_analyzer_project.main(cmd)
  #raise(Exception("Fail here"))

def test_verilog_preprocess_preprocess():
  cmd = ["tests/verilog_preprocess.json", "tests/verilog_preprocessed"]
  hdl_analyzer_preprocess.main(cmd)
  #raise(Exception("Fail here"))
