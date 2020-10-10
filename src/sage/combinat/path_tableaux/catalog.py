r"""
Catalog of Path Tableaux

The ``path_tableaux`` object may be used to access examples of various path
tableau objects currently implemented in Sage. Using tab-completion on this
object is an easy way to discover and quickly create the path tableaux that
are available (as listed here).

Let ``<tab>`` indicate pressing the tab key.  So begin by typing
``path_tableaux.<tab>`` to the see the currently implemented path tableaux.

- :class:`~sage.combinat.path_tableaux.path_tableau.CylindricalDiagram`
- :class:`~sage.combinat.path_tableaux.dyck_path.DyckPath`
- :class:`~sage.combinat.path_tableaux.dyck_path.DyckPaths`
- :class:`~sage.combinat.path_tableaux.frieze.FriezePattern`
- :class:`~sage.combinat.path_tableaux.frieze.FriezePatterns`
- :class:`~sage.combinat.path_tableaux.semistandard.SemistandardPath`
- :class:`~sage.combinat.path_tableaux.semistandard.SemistandardPaths`
"""

from sage.misc.lazy_import import lazy_import

lazy_import('sage.combinat.path_tableaux.path_tableau', ['CylindricalDiagram'])
lazy_import('sage.combinat.path_tableaux.dyck_path', ['DyckPath', 'DyckPaths'])
lazy_import('sage.combinat.path_tableaux.frieze', ['FriezePattern','FriezePatterns'])
lazy_import('sage.combinat.path_tableaux.semistandard', ['SemistandardPath','SemistandardPaths'])

del lazy_import
