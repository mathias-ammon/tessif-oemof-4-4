# tests/test_post_processing.py
"""Module aggregating the post-processing tests."""
import pytest
import tessif_examples.basic as tsf_exmp_bsc
from tessif.post_process import IntegratedGlobalResultier

from tessif_oemof_4_4 import optimize, transform, post_process

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
def test_basic_sysmod_postprocessing(system_model_name):
    """Test succesful mwe transformation."""
    tsf_system_model = getattr(tsf_exmp_bsc, system_model_name)()
    omf_system_model = transform(tsf_system_model)
    opt_omf_sysmod = optimize(omf_system_model)
    glbl = post_process.IntegratedGlobalResultier(opt_omf_sysmod)
    all_res = post_process.AllResultier(opt_omf_sysmod)

    assert isinstance(glbl, IntegratedGlobalResultier)
    assert isinstance(all_res.node_installed_capacity, dict)
