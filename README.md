⚠️ This repo is deprecated and no longer maintained. Since [napari 0.6.2](https://github.com/napari/napari/releases/tag/v0.6.2), there is nicer, built-in feature table widget!

# napari-properties-viewer

[![License](https://img.shields.io/pypi/l/napari-properties-viewer.svg?color=green)](https://github.com/napari/napari-properties-viewer/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-properties-viewer.svg?color=green)](https://pypi.org/project/napari-properties-viewer)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-properties-viewer.svg?color=green)](https://python.org)
[![tests](https://github.com/kevinyamauchi/napari-properties-viewer/workflows/tests/badge.svg)](https://github.com/kevinyamauchi/napari-properties-viewer/actions)
[![codecov](https://codecov.io/gh/kevinyamauchi/napari-properties-viewer/branch/master/graph/badge.svg)](https://codecov.io/gh/kevinyamauchi/napari-properties-viewer)

A viewer for napari layer properties

![image](resources/properties_viewer.gif)
----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-properties-viewer` via [pip]:

    pip install napari-properties-viewer
    
## Using the properties viewer table

1. Open a a napari viewer with a layer with properties (e.g., Points)
2. View the properties by opening the properties viewer plugin from Plugins menu -> Add dock widget -> napari-propertiews-viewer: properties table
3. The layer property values are now displayed in the table widget. You can edit the values by double clicking the cell of interest and entering a new value.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-properties-viewer" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/kevinyamauchi/napari-properties-viewer/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
