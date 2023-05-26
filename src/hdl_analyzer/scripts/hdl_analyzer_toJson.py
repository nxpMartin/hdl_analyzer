
import hdl_analyzer.Project as Project

import hdl_analyzer.Analyzer.ToJson as Analyzer

import argparse
import json
import os

def main(argv):
  parser = argparse.ArgumentParser(
      prog = "hdl_analyzer_hiearchy.py",
      description = "Open hdl_analyzer json project file and analyze hiearchy for wanted instance/module."
    )
  
  parser.add_argument("project_file", help="hdl_analyzer JSON project file.")
  parser.add_argument("out_file", help="Output JSON file.")
  parser.add_argument("--dir", dest = "dir", default = None, help = "Redefinition of base directory.")
  
  parser.add_argument("--debug", dest = "debug", default = False, action = "store_true")
  
  args = parser.parse_args(args=argv)
  
  hdl_project = Project.Project(args.project_file, args.dir, args.debug)
  
  print("Project loaded")
  
  analyzer = Analyzer.ToJson(args.debug)
  hdl_project.analyze(analyzer)
  
  print("Project analyzed")
  
  #json_dict = analyzer.get_JSON()
  #print("Project json dict")
  #if args.debug:
  #  json_data = json.dumps(json_dict, indent=2)
  #else:
  #  json_data = json.dumps(json_dict)
  
  with open(args.out_file, "w") as file:
    analyzer.write_JSON(file)

