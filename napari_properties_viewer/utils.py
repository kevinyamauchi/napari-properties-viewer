from typing import Any
import warnings

import numpy as np


def str2prop(property_string: str, dtype: np.dtype)-> Any:
    """Convert a string from a table cell to a property value.

    For bool conversion, true (any case) and numbers > 0 are treated
    as True and all other values are false.

    Parameters
    ----------
    property_string : str
        The value from the cell to be converted
    dtype :
        The dtype of the numpy array the property_string should
        be converted to.

    Returns
    -------
    converted_value : Any
        The property_string converted to the type specifed by dtype.
        Returns None if the conversion is not successful.
    """
    if dtype == bool:
        # we have to handle the conversion to bool specially
        standardize_property_string = property_string.lower()

        if standardize_property_string.isnumeric():
            converted_value = int(standardize_property_string) > 0
        else:
            converted_value = standardize_property_string == 'true'

    else:
        # otherwise, just let numpy do the conversion
        type_class = dtype.type

        try:
            converted_value = type_class(property_string)
        except ValueError:
            warnings.warn(f'{property_string} could not be converted to {dtype}', RuntimeWarning)
            converted_value = None

    return converted_value

