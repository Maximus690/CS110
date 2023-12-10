import os
import runpy
import sys

import pytest


def run_script(script, *args, module='__main__'):
    """
    Run the python script with arguments

    If the script expects STDIN, use the dialog framework instead

    :param script: Python script to run
    :param args: Arguments to the python script
    :param module: Defaults to '__main__'
    :return: Namespace as a result of running the script
    """
    if not os.path.exists(script):
        pytest.fail(f'The file {script} does not exist. Did you submit it?')

    def _input(*args):
        raise Exception("input function not supported for this test")

    output = []

    def _print(*args, sep=' ', end='\n'):
        output.append(sep.join(args) + end)
        print(*args, sep=sep, end=end)

    sys.argv = [script, *(str(a) for a in args)]
    _globals = {
        'sys': sys,
        'input': _input,
        'print': _print
    }

    return output, runpy.run_path(script, _globals, module)
