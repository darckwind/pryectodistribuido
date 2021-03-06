# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `Comunication.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Comunication
_M_Comunication = Ice.openModule('Comunication')
__name__ = 'Comunication'

_M_Comunication._t_Birateral = IcePy.defineValue('::Comunication::Birateral', Ice.Value, -1, (), False, True, None, ())

if 'BirateralPrx' not in _M_Comunication.__dict__:
    _M_Comunication.BirateralPrx = Ice.createTempClass()
    class BirateralPrx(Ice.ObjectPrx):

        def comunicationBilateral(self, s, context=None):
            return _M_Comunication.Birateral._op_comunicationBilateral.invoke(self, ((s, ), context))

        def comunicationBilateralAsync(self, s, context=None):
            return _M_Comunication.Birateral._op_comunicationBilateral.invokeAsync(self, ((s, ), context))

        def begin_comunicationBilateral(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Comunication.Birateral._op_comunicationBilateral.begin(self, ((s, ), _response, _ex, _sent, context))

        def end_comunicationBilateral(self, _r):
            return _M_Comunication.Birateral._op_comunicationBilateral.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Comunication.BirateralPrx.ice_checkedCast(proxy, '::Comunication::Birateral', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Comunication.BirateralPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Comunication::Birateral'
    _M_Comunication._t_BirateralPrx = IcePy.defineProxy('::Comunication::Birateral', BirateralPrx)

    _M_Comunication.BirateralPrx = BirateralPrx
    del BirateralPrx

    _M_Comunication.Birateral = Ice.createTempClass()
    class Birateral(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Comunication::Birateral', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Comunication::Birateral'

        @staticmethod
        def ice_staticId():
            return '::Comunication::Birateral'

        def comunicationBilateral(self, s, current=None):
            raise NotImplementedError("servant method 'comunicationBilateral' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Comunication._t_BirateralDisp)

        __repr__ = __str__

    _M_Comunication._t_BirateralDisp = IcePy.defineClass('::Comunication::Birateral', Birateral, (), None, ())
    Birateral._ice_type = _M_Comunication._t_BirateralDisp

    Birateral._op_comunicationBilateral = IcePy.Operation('comunicationBilateral', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), IcePy._t_string, False, 0),), None, ())

    _M_Comunication.Birateral = Birateral
    del Birateral

# End of module Comunication
