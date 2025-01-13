#!/usr/bin/python3

# Manages file paths
import pathlib
import sys

sys.dont_write_bytecode = True # Prevent the bytecodes for the resources directory from being cached
# Add to the system path the "resources" directory relative to the script that was run
resources_path = pathlib.Path(__file__).resolve().parent.parent  / 'resources'
sys.path.append( str(resources_path) )

import test_suite_320
import repo_test

def main():
    # Check on vivado
    tester = test_suite_320.build_test_suite_320("lab04", start_date="02/03/2025")
    tester.add_required_tracked_files(["sim_logic.tcl", "sim_logic.png", "hierarchy.png", "post-schematic.png", "implementation.png"])
    tester.add_Makefile_rule("synth_logic", ["synth_logic.tcl"], ["synth_logic.log", "logic_functions_synth.dcp"])
    tester.add_Makefile_rule("implement_logic", ["implement_logic.tcl"], ["implement_logic.log", "logic_functions.bit", 
                                                                          "logic_functions.dcp", "utilization.rpt"])
    tester.run_tests()

if __name__ == "__main__":
    main()