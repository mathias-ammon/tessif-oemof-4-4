"""Wrapping the oemof optimization process."""
import numbers

from oemof import solph


def optimize(energy_system, solver="cbc", **kwargs):
    """Optimize oemof system model

    Parameters
    ----------
    energy_system: ~oemof.energy_system.EnergySystem
        Oemof energy system to be simulated.

    solver: str, default='cbc'
        String specifying the solver to be used. For `FOSS
        <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_
        application, this is usually either ``cbc`` or ``glpk``.

        But since :mod:`pyomo` is used for interfacing the solver. Any of it's
        `supported solvers
        <https://pyomo.readthedocs.io/en/stable/solving_pyomo_models.html#supported-solvers>`_
        can be used.

        Note
        ----
        In case the link above is servered, use the pyomo cli command::

            pyomo help --solvers

    kwargs:
        Keywords parameterizing the solver used as well as the energy system
        transformation process.

        Use one of :meth:`solve's <oemof.solph.models.BaseModel.solve>`
        parameters for tweaking the solver.

    Return
    ------
    optimized_es : :class:`~oemof.energy_system.EnergySystem`
        Energy system carrying the optimization results.
    """
    # Default solver kwargs
    skwargs = {
        "solver_io": "lp",
        "solve_kwargs": {},
        "cmdline_options": {},
    }

    # Seperate the kwargs:
    for key in skwargs.keys():
        if key in kwargs.keys():
            skwargs.update({key: kwargs.pop(key)})

    # enforce solver from argument:
    skwargs["solver"] = solver

    # Prepare the optimization problem
    om = solph.Model(energy_system)

    # Parse global constraints (potentially added by a tessif transformation)
    if hasattr(energy_system, "global_constraints"):
        for constraint, value in energy_system.global_constraints.items():

            if isinstance(value, numbers.Number):
                om = solph.constraints.generic_integral_limit(
                    om=om, keyword=constraint, limit=value
                )

    om.solve(**skwargs)

    # Pump results into the model:
    energy_system.results["main"] = solph.processing.results(om)
    energy_system.results["meta"] = solph.processing.meta_results(om)

    # parse global results
    energy_system.results["global"] = dict()

    # Parse global constraint results (potentially added by a tessif
    # transformation)
    if hasattr(energy_system, "global_constraints"):
        for constraint, value in energy_system.global_constraints.items():

            if isinstance(value, numbers.Number):
                energy_system.results["global"][constraint] = getattr(
                    om, "integral_limit_{}".format(constraint)
                )()

    energy_system.results["global"]["costs"] = energy_system.results["meta"][
        "objective"
    ]

    # Return the optimized oemof energy system
    return energy_system
