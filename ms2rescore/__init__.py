"""MS²ReScore: Sensitive PSM rescoring with predicted MS² peak intensities and RTs."""

__version__ = "v3.0.0-dev0"

from warnings import filterwarnings

# mzmlb is not used, so hdf5plugin is not needed
filterwarnings(
    "ignore",
    message="hdf5plugin is missing",
    category=UserWarning,
    module="psims.mzmlb",
)

from ms2rescore.ms2rescore_main import MS2Rescore
