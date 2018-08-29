from sage.structure.element cimport Element
from .morphism cimport Morphism
from .map cimport Map
from .functor cimport Functor

cdef class Action(Functor):
    cdef readonly G
    cdef readonly op
    cdef readonly bint _is_left
    cdef US
    cdef underlying_set(self)
    cpdef _call_(self, a, b)


cdef class InverseAction(Action):
    cdef Action _action
    cdef Map S_precomposition

cdef class PrecomposedAction(Action):
    cdef Action _action
    cdef Map left_precomposition
    cdef Map right_precomposition

cdef class ActionEndomorphism(Morphism):
    cdef Action _action
    cdef Element _g

cdef class BaseActionOnRing(Action):
    cdef _base
    cdef _algebra
    cdef _defining_morphism
