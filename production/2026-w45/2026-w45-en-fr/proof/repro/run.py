# -*- coding: utf-8 -*-
"""Single-process driver: imports the content modules in registry order.
Never import a content module standalone — the shared exercise registry
accumulates numbering across modules in this one process."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content12, content34, content56, content7, content8
print("driver done")
