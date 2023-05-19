
import hdl_analyzer.Project as Project

import argparse
import json
import os

def main(argv):
  parser = argparse.ArgumentParser(
      prog = "hdl_analyzer_preprocess.py",
      description = "Open hdl_analyzer json project file and preprocess project files."
    )
  
  parser.add_argument("project_file", help="hdl_analyzer JSON project file.")
  parser.add_argument("dest_dir", help="Destination directory for preprocessed files.")
  parser.add_argument("--dir", dest = "dir", default = None, help = "Redefinition of base directory.")
  
  parser.add_argument("--debug", dest = "debug", default = False, action = "store_true")
  
  args = parser.parse_args(args=argv)
  
  hdl_project = Project.Project(args.project_file, args.dir, args.debug)
  
  hdl_project.preprocess(args.dest_dir)
  
   
