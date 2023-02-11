# tests/test_transformation.py
"""Module aggregating basic transformation tests."""
import pytest
import tessif_examples.basic as tsf_exmp_bsc

from tessif_oemof_4_4 import transform

# tessif-examples sytem model creation functionalities
# reside in an identically named module minus the "create" prefix
# E.g., "create_mwe()" resides in tessif_examples.basic.mwe.py
creates = [
    attr for attr in dir(tsf_exmp_bsc) if "create" in attr if "mssesu" not in attr
]


@pytest.mark.parametrize("system_model_name", creates)
def test_node_name_transformation(system_model_name):
    """Test succesful mwe transformation."""
    tsf_system_model = getattr(tsf_exmp_bsc, system_model_name)()
    tessif_node_names = [node.uid.name for node in tsf_system_model.nodes]

    omf_system_model = transform(tsf_system_model)
    omf_node_names = [str(node) for node in omf_system_model.nodes]

    assert sorted(tessif_node_names) == sorted(omf_node_names)
