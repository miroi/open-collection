# io_utils_fixed.py
# Replacement for the uploaded io_utils.py.
# The only required correction is calculator-dependent output directory selection.

import os
import numpy as np
import pandas as pd

def get_output_directory(config):
    output_config = config.get('output', {})
    calculator_mode = config.get('calculator', 'qe').lower()

    if calculator_mode == 'mace':
        return output_config.get('mace_output_dir', 'results_mace')
    elif calculator_mode == 'qe':
        return output_config.get('output_dir', 'results_qe')
    elif calculator_mode == 'mace+qe':
        return output_config.get('mace_qe_output_dir', 'results_mace_qe')
    else:
        raise ValueError(
            f"Unknown calculator mode '{calculator_mode}'. "
            "Allowed values: qe, mace, mace+qe"
        )

# In the uploaded io_utils.py replace:
# output_dir = output_config.get('output_dir', 'results_qe')
#
# with:
#
# output_dir = get_output_directory(config)
#
# All remaining CSV/TXT writing code stays unchanged.
