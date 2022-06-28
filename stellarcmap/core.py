from matplotlib import cm, colors
from astropy.table import Table
from astropy.utils.data import download_file

import numpy as np

__all__ = [
    'gaia_bp_rp'
]
mamajek_url = "http://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt"
mamajek_colnames = (
    "SpT   Teff  logT   BCv    logL   Mbol R_Rsun   Mv    B-V    Bt-Vt  "
    "G-V    Bp-Rp  G-Rp   M_G    b-y    U-B    V-Rc   V-Ic   V-Ks   J-H"
    "    H-Ks   M_J    M_Ks   Ks-W1   W1-W2  W1-W3  W1-W4   g-r   i-z"
    "  z-Y  Msun SpT2"
).split()


def get_spt_to_rgb():
    """
    Return Table 5 from Harre & Heller (2021) as an astropy table.

    Returns
    -------
    harre_heller_table5 : `~astropy.table.Table`
        Harre & Heller (2021) Table 5.
    """
    harre_heller_table5 = Table.read(
        """SpT	Teff	logg	rgb	hex	image
M9.5V	2,300	5.0	1.0,0.491,0.144	#ff7d24	image
M9V	2,400	5.0	1.0,0.518,0.179	#ff842d	image
M8V	2,500	5.0	1.0,0.542,0.202	#ff8a33	image
M7.5V	2,600	5.0	1.0,0.607,0.255	#ff9a41	image
M6.5V	2,700	5.0	1.0,0.648,0.286	#ffa548	image
M6V	2,800	5.0	1.0,0.649,0.285	#ffa548	image
M6V	2,900	5.0	1.0,0.644,0.285	#ffa448	image
M5.5V	3,000	5.0	1.0,0.641,0.289	#ffa349	image
M4.5V	3,100	5.0	1.0,0.638,0.293	#ffa24a	image
M4V	3,200	5.0	1.0,0.638,0.3	#ffa24c	image
M3.5V	3,300	5.0	1.0,0.638,0.308	#ffa24e	image
M3V	3,400	5.0	1.0,0.638,0.315	#ffa250	imaget
M2.5V	3,500	5.0	1.0,0.637,0.322	#ffa251	image
M2V	3,600	5.0	1.0,0.635,0.327	#ffa153	image
M1V	3,700	4.5	1.0,0.637,0.34	#ffa256	image
M0.5V	3,800	4.5	1.0,0.635,0.346	#ffa158	image
M0V	3,900	4.5	1.0,0.636,0.354	#ffa25a	image
K8V	4,000	4.5	1.0,0.641,0.369	#ffa35e	image
K7V	4,100	4.5	1.0,0.65,0.389	#ffa563	image
K6.5V	4,200	4.5	1.0,0.662,0.411	#ffa868	image
K5.5V	4,300	4.5	1.0,0.677,0.439	#ffac6f	image
K5V	4,400	4.5	1.0,0.696,0.47	#ffb177	image
K4.5V	4,500	4.5	1.0,0.717,0.501	#ffb67f	image
K4V	4,600	4.5	1.0,0.739,0.533	#ffbc87	image
K3.5V	4,700	4.5	1.0,0.761,0.565	#ffc18f	image
K3V	4,800	4.5	1.0,0.781,0.595	#ffc797	image
K3V	4,900	4.5	1.0,0.802,0.626	#ffcc9f	image
K2.5V	5,000	4.5	1.0,0.821,0.657	#ffd1a7	image
K1.5V	5,100	4.5	1.0,0.84,0.691	#ffd6b0	image
K1V	5,200	4.5	1.0,0.857,0.722	#ffdab8	image
K0V	5,300	4.5	1.0,0.872,0.753	#ffdec0	image
G9V	5,400	4.5	1.0,0.886,0.783	#ffe1c7	image
G8V	5,500	4.5	1.0,0.898,0.813	#ffe5cf	image
G6V	5,600	4.5	1.0,0.91,0.845	#ffe8d7	image
G4V	5,700	4.5	1.0,0.922,0.878	#ffebdf	image
G2V	5,800	4.5	1.0,0.931,0.905	#ffede6	image
G1V	5,900	4.5	1.0,0.94,0.931	#ffefed	image
F9.5V	6,000	4.5	1.0,0.951,0.967	#fff2f6	image
F9V	6,100	4.5	1.0,0.96,0.998	#fff4fe	image
F8V	6,200	4.0	0.955,0.931,1.0	#f3edff	image
F6V	6,300	4.0	0.922,0.908,1.0	#ebe7ff	image
F6V	6,400	4.0	0.896,0.891,1.0	#e4e3ff	image
F5V	6,500	4.0	0.869,0.871,1.0	#dddeff	image
F4V	6,600	4.0	0.844,0.855,1.0	#d7d9ff	image
F3V	6,700	4.0	0.823,0.84,1.0	#d1d6ff	image
F2V	6,800	4.0	0.802,0.826,1.0	#ccd2ff	image
F2V	6,900	4.0	0.782,0.812,1.0	#c7cfff	image
F1V	7,000	4.0	0.763,0.799,1.0	#c2cbff	image
F0V	7,200	4.0	0.725,0.773,1.0	#b8c5ff	image
A9V	7,400	4.0	0.692,0.75,1.0	#b0bfff	image
A8V	7,600	4.0	0.674,0.738,1.0	#abbcff	image
A7V	7,800	4.0	0.636,0.712,1.0	#a2b5ff	image
A6V	8,000	4.0	0.606,0.69,1.0	#9ab0ff	image
A4V	8,200	4.0	0.579,0.67,1.0	#93aaff	image
A4V	8,400	4.0	0.556,0.652,1.0	#8da6ff	image
A3V	8,600	4.0	0.546,0.645,1.0	#8ba4ff	image
A2V	8,800	4.0	0.531,0.634,1.0	#87a1ff	image
A2V	9,000	4.0	0.519,0.624,1.0	#849fff	image
A1V	9,200	4.0	0.508,0.616,1.0	#819dff	image
A1V	9,400	4.0	0.498,0.608,1.0	#7f9bff	image
A0V	9,600	4.0	0.49,0.601,1.0	#7d99ff	image
A0V	9,800	4.0	0.483,0.595,1.0	#7b97ff	image
A0V	10,000	4.0	0.477,0.59,1.0	#7996ff	image
B9.5V	10,200	4.0	0.472,0.586,1.0	#7895ff	image
B9.5V	10,400	4.0	0.467,0.582,1.0	#7794ff	image
B9V	10,600	4.0	0.463,0.578,1.0	#7693ff	image
B9V	10,800	4.0	0.459,0.575,1.0	#7592ff	image
B9V	11,000	4.0	0.456,0.572,1.0	#7491ff	image
B9V	11,200	4.0	0.453,0.57,1.0	#7391ff	image
B9V	11,400	4.0	0.451,0.567,1.0	#7290ff	image
B9V	11,600	4.0	0.45,0.566,1.0	#7290ff	image
B8V	11,800	4.0	0.448,0.564,1.0	#728fff	image
B8V	12,000	4.0	0.446,0.562,1.0	#718fff	image
B8V	12,500	4.0	0.44,0.557,1.0	#708eff	image
B8V	13,000	4.0	0.436,0.554,1.0	#6f8dff	image
B7V	13,500	4.0	0.432,0.55,1.0	#6e8cff	image
B7V	14,000	4.0	0.429,0.547,1.0	#6d8bff	image
B6V	14,500	4.0	0.425,0.544,1.0	#6c8aff	image
B6V	15,000	4.0	0.421,0.541,1.0	#6b89ff	image
B5V	16,000	4.0	0.414,0.536,1.0	#6988ff	image
B3V	17,000	4.0	0.408,0.532,1.0	#6887ff	image
B2.5V	18,000	4.0	0.403,0.527,1.0	#6686ff	image
B2.5V	19,000	4.0	0.398,0.524,1.0	#6585ff	image
B2V	20,000	4.0	0.394,0.52,1.0	#6484ff	image
B2V	21,000	4.0	0.39,0.517,1.0	#6383ff	image
B2V	22,000	4.0	0.387,0.514,1.0	#6283ff	image
B1.5V	23,000	4.0	0.384,0.512,1.0	#6182ff	image
B1.5V	24,000	4.0	0.381,0.509,1.0	#6181ff	image
B1.5V	25,000	4.0	0.379,0.507,1.0	#6081ff	image
B1V	26,000	4.0	0.376,0.505,1.0	#5f80ff	image
B1V	27,000	4.0	0.373,0.503,1.0	#5f80ff	image
B1V	27,500	4.0	0.371,0.501,1.0	#5e7fff	image
B0.5V	28,000	4.0	0.371,0.5,1.0	#5e7fff	image
B0.5V	29,000	4.0	0.368,0.498,1.0	#5d7fff	image
B0.5V	30,000	4.0	0.366,0.496,1.0	#5d7eff	image
O9.5V	32,500	4.0	0.361,0.491,1.0	#5c7dff	image
O8V	35,000	4.0	0.357,0.487,1.0	#5b7cff	image
O6V	37,500	4.0	0.359,0.487,1.0	#5b7cff	image
O5V	40,000	4.0	0.358,0.486,1.0	#5b7bff	image
O4V	42,500	4.0	0.357,0.485,1.0	#5a7bff	image
O4V	45,000	4.0	0.357,0.485,1.0	#5a7bff	image
O3V	47,500	4.0	0.357,0.485,1.0	#5b7bff	image
O2V	50,000	4.0	0.358,0.486,1.0	#5b7bff	image
O2V	52,500	4.0	0.359,0.487,1.0	#5b7cff	image
O1V	55,000	4.0	0.361,0.489,1.0	#5c7cff	image""",
        format='ascii.csv', delimiter='\t',
        names=['SpT', 'Teff', 'logg', 'rgb', 'hex', 'image']
    )

    harre_heller_table5.remove_column('image')
    harre_heller_table5.add_index('SpT')

    return harre_heller_table5


def get_mamajek_table():
    """
    Get the Pecaut & Mamajek (2013) Table 5 of spectral types, Teffs, colors.

    Returns
    -------
    mamajek : `~astropy.table.Table`
        Latest Pecaut & Mamajek (2013) table.
    """
    ncols = 32
    dtypes = ncols * [float,]
    dtypes[0] = "U16"
    dtypes[-1] = "U16"

    mamajek = Table(
        np.genfromtxt(
            download_file(mamajek_url, cache=True), dtype=dtypes, max_rows=118
        ), names=mamajek_colnames
    )
    mamajek.add_index("SpT")

    return mamajek


def gaia_bp_rp():
    """
    Return the kwargs to pass to ``plt.scatter()`` to produce a colored scatter
    plot. See example below.

    Example
    -------
    >>> from stellarcmap import gaia_bp_rp
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> np.random.seed(42)
    >>> kwargs = gaia_bp_rp()
    >>> bp_rp_color = np.random.uniform(-0.5, 5, size=10)
    >>> plt.scatter(x, y, c=bp_rp_color, **kwargs)

    Returns
    -------
    kwargs : dict
        Dictionary containing keys for ``cmap`` and ``norm``.
    """
    mamajek = get_mamajek_table()
    harre_heller_table5 = get_spt_to_rgb()

    # Grab the nearest spectral type from the Mamajek table for each entry
    # in the Harre & Heller table
    nearest_spt = {spt: spt for spt in mamajek['SpT'] if
                   spt in harre_heller_table5['SpT']}
    for spt in harre_heller_table5['SpT']:
        if spt not in mamajek['SpT'] and '.' in spt:
            nearest_spt[spt] = spt[0] + str(1 + int(spt[1])) + spt[-1]

    # Assemble the sorted list of RGB stellar colors from Harre & Heller and the
    # corresponding BP-RP values into a linear segmented colormap
    available_mamajek_hex = []
    available_mamajek_colors = []
    available_mamajek_sptypes = []
    for spt, hex_code in zip(harre_heller_table5['SpT'],
                             harre_heller_table5['rgb']):
        if spt in mamajek['SpT']:
            c = mamajek.loc[spt]['Bp-Rp']
            if not np.isnan(c) and c not in available_mamajek_colors:
                available_mamajek_hex.append(hex_code)
                available_mamajek_colors.append(c)
                available_mamajek_sptypes.append(spt)
        elif spt in nearest_spt:
            c = mamajek.loc[nearest_spt[spt]]['Bp-Rp']
            if not np.isnan(c) and c not in available_mamajek_colors:
                available_mamajek_hex.append(hex_code)
                available_mamajek_colors.append(c)
                available_mamajek_sptypes.append(spt)

    sort = np.argsort(available_mamajek_colors)

    sorted_rgbs = [
        list(map(float, i.split(',')))
        for i in np.array(available_mamajek_hex)[sort]
    ]
    sorted_values = (
        np.array(available_mamajek_colors)[sort] -
        np.min(available_mamajek_colors)
    ) / np.ptp(available_mamajek_colors)
    colors_to_rgb = list(zip(sorted_values, sorted_rgbs))

    stellar_cmap = colors.LinearSegmentedColormap.from_list(
        "stellar", colors_to_rgb, N=256
    )
    norm = colors.Normalize(
        vmin=min(available_mamajek_colors),
        vmax=max(available_mamajek_colors),
        clip=True
    )

    return dict(cmap=stellar_cmap, norm=norm)
