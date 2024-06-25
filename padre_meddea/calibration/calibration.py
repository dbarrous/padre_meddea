"""
A module for all things calibration.
"""
from pathlib import Path
import random

from astropy.time import Time

from swxsoc.util import util
from padre_meddea import log

__all__ = [
    "process_file",
    "calibrate_file",
    "get_calibration_file",
    "read_calibration_file",
]


def process_file(data_filename: Path) -> list:
    """
    This is the entry point for the pipeline processing.
    It runs all of the various processing steps required.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of an input file

    Returns
    -------
    output_filenames: list
        Fully specificied filenames for the output files.
    """
    log.info(f"Processing file {data_filename}.")
    output_files = []

    calibrated_file = calibrate_file(data_filename)
    
    log.info(f"Calibrated file saved as {calibrated_file}.")
    output_files.append(calibrated_file)
    log.info(f"Output files: {output_files}")
    #  data_plot_files = plot_file(data_filename)
    #  calib_plot_files = plot_file(calibrated_file)

    # add other tasks below
    return output_files


def calibrate_file(data_filename: Path, output_level=2) -> Path:
    """
    Given an input file, calibrate it and return a new file.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)
    output_level: int
        The requested data level of the output file.

    Returns
    -------
    output_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)

    Examples
    --------
    """

    log.info(
        "Despiking removing {num_spikes} spikes".format(
            num_spikes=random.randint(0, 10)
        )
    )
    log.warning(
        "Despiking could not remove {num_spikes}".format(
            num_spikes=random.randint(1, 5)
        )
    )
    
    log.info(f"Calibrating file {data_filename.name}.")

    file_metadata = util.parse_science_filename(data_filename)
    
    log.info(f"File metadata: {file_metadata}")
    
    if file_metadata is None:
        log.error(f"Could not parse filename {data_filename}.")
        return None

    if file_metadata["level"] == "l0":
        new_filename = util.create_science_filename(
            instrument=file_metadata["instrument"],
            time=file_metadata["time"],
            version=f"0.0.{file_metadata['version']}",
            level="l1"
        )
        with open(new_filename, "w"):
            pass

    elif file_metadata["level"] == "l1":
        new_filename = util.create_science_filename(
            instrument=file_metadata["instrument"],
            time=file_metadata["time"],
            version=file_metadata["version"],
            level="ql"
        )
        
        with open(new_filename, "w"):
            pass
    else:
        log.error(f"Could not calibrate file {data_filename}.")
        raise ValueError(f"Cannot find calibration for file {data_filename}.")
    
    log.info(f"Calibrated file saved as {new_filename}.")
    return new_filename


def get_calibration_file(time: Time) -> Path:
    """
    Given a time, return the appropriate calibration file.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)
    time: ~astropy.time.Time

    Returns
    -------
    calib_filename: str
        Fully specificied filename for the appropriate calibration file.

    Examples
    --------
    """
    return None


def read_calibration_file(calib_filename: Path):
    """
    Given a calibration, return the calibration structure.

    Parameters
    ----------
    calib_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)

    Returns
    -------
    output_filename: str
        Fully specificied filename of the appropriate calibration file.

    Examples
    --------
    """

    # if can't read the file

    return None
