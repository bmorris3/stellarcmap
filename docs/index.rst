stellarcmap Documentation
-------------------------

stellarcmap provides a quick and easy way to make colormaps that correspond to
true stellar colors. Below is an example for producing a plot showing some
entries in the TESS Input Catalog, where the color for each point is determined
from the Gaia BP-RP color.

.. plot::
    :include-source:

    # First we'll use astroquery to get a small catalog of stellar properties:
    from astroquery.vizier import Vizier

    v = Vizier(
        columns="BPmag RPmag Dist Teff".split(),
        column_filters=dict(BPmag="<10")
    )
    tic = v.query_constraints("IV/38/tic")[0]

    color = tic['BPmag'] - tic['RPmag']

    # This is the bit specific to stellarcmap, which generates the kwargs
    # that you supply to the `plt.scatter` function:
    from stellarcmap import gaia_bp_rp
    kwargs = gaia_bp_rp()

    # Now let's make the plot:
    fig, ax = plt.subplots(figsize=(5, 4))
    c = ax.scatter(tic['Teff'], tic['RPmag'], c=color, edgecolor='k', **kwargs)
    plt.colorbar(c, label='BP-RP', extend='both')
    ax.invert_xaxis()
    ax.set(
        xlabel='$T_{\\rm eff}$',
        ylabel='RP'
    )


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   stellarcmap/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
