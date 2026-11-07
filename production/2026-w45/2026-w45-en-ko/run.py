# -*- coding: utf-8 -*-
"""One-process driver for the W45 EN x KO edition (shared registry: never run
content modules standalone). Imports content12/34/56/7/8 in order."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content12  # noqa: F401
import content34  # noqa: F401
import content56  # noqa: F401
import content7  # noqa: F401
import content8  # noqa: F401
