import os, sys, pytest
# import run_scenario

def test_input_generation():
    import filecmp
    filecmp.clear_cache()
    workspace = '/usr/local/apps/workspace'
    BASIN_INPUT_FILE = os.path.join(workspace, 'testing/test_basin/INPUT.wenatchee.testing')
    OUTPUT_FILE = os.path.join(workspace, 'templates/basin/scenarios/scenario/run/INPUT.basin.scenario')
    python_script = os.path.join(workspace, 'run_scenario.py')
    # Run default template creation
    os.system('%s %s -p %s/templates/ -b basin -s scenario' % (sys.executable, python_script, workspace))
    # Compare output to existing default basin input file
    # filecmp.cmp does not seem to have an 'ignore whitespace' option
    #       Using *nix diff instead (-b for 'ignore whitespace')
    # assert filecmp.cmp(BASIN_INPUT_FILE, OUTPUT_FILE, shallow=False)
    diff = os.system("diff -b %s %s" % (BASIN_INPUT_FILE, OUTPUT_FILE))
    assert(diff == 0)
