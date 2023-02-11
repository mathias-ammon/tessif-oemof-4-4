# tests/test_optimization.py
"""Module aggregating the optimzation tests."""
import pytest
import tessif_examples.basic as tsf_exmp_bsc

from tessif_oemof_4_4 import optimize, transform

# tessif-examples sytem model creation functionalities
# reside in an identically named module minus the "create" prefix
# E.g., "create_mwe()" resides in tessif_examples.basic.mwe.py
creates = [
    attr
    for attr in dir(tsf_exmp_bsc)
    if "create" in attr
    if not any(
        [
            buggy in attr
            for buggy in [
                "mssesu",
                "variable_chp",
                "self_similar",
            ]
        ]
    )
]


@pytest.mark.parametrize("system_model_name", creates)
def test_basic_sysmod_optimization(system_model_name):
    """Test succesful mwe transformation."""
    tsf_system_model = getattr(tsf_exmp_bsc, system_model_name)()
    omf_system_model = transform(tsf_system_model)
    optimized_omf_sm = optimize(omf_system_model)

    assert "costs" in optimized_omf_sm.results["global"]
