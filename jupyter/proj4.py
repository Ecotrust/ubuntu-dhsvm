__all__ = ['proj4']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['D', 'St', 'lt', 'ot', 'Mi', 'I', 'Fs', 's', 'p', 'r', 'k', 'ct', 'is', 'Ps', 'Vs', 'Z', 'Ns', 'E', 'j', 'Ts', 'h', 'Qt', 'y', 'x', 'cs', '$s', 'O', 'pt', 'fi', 'm', 'Ds', 'ti', 'at', 'Es', 'Tt', 'S', 'gs', 'bt', 'R', 'l', 'o', 'bs', 'ds', 'ut', 'Zt', 'Ks', 'si', 'vs', 'F', 'tt', 'zs', 'Bs', 'Xs', '_s', 'yt', 'n', 'Ls', 'As', 'Y', 'it', 'g', 't', 'J', 'Gt', 'Pt', 'ps', 'K', 'vt', 'ht', 'qs', 'i', 'H', 'L', 'Ct', 'Rt', 'hs', 'js', 'ei', '$', 'ss', '_i', 'ai', 'Projection', 'C', 'It', 'Xt', 'hi', 'Ys', 'V', 'li', 'xt', 'Kt', 'ws', 'yi', 'U', 'Nt', 'f', 'At', 'a', 'wt', 'zt', 'gt', 'P', 'di', 'qt', 'Hs', 'ui', 'et', 'Zs', 'c', 'ni', 'A', 'Dt', 'Us', 'Ms', 'rt', 'Q', 'ii', 'Ss', 'mt', 'Mt', 'us', '_t', 'es', 'Js', 'Ht', 'z', 'ts', 'd', 'ms', 'Cs', 'Gs', 'mi', 'Point', 'kt', 'Wt', '_', 'X', 'T', 'Ut', 'Et', 'Jt', 'Ws', 'u', 'xs', 'Bt', 'e', '$t', 'Lt', 'ls', 'M', 'q', 'ri', 'st', 'b', 'Yt', 'ns', 'fs', 'Ot', 'Os', 'ci', 'Is', 'oi', 'dt', 'W', 'Vt', 'G', 'rs', 'xi', 'v', 'os', 'ft', 'nt', 'ys', 'w', 'N', 'Rs', 'jt', 'Qs', 'pi', 'as', 'Ft', 'ks', 'B'])
    @Js
    def PyJsHoisted_t_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'e', 'i', 's', 't', 'a'])
        if var.get('t').get(var.get('s')):
            return var.get('t').get(var.get('s'))
        #for JS loop
        var.put('a', var.get('Object').callprop('keys', var.get('t')))
        var.put('h', var.get('s').callprop('toLowerCase').callprop('replace', var.get('dt'), Js('')))
        var.put('e', (-Js(1.0)))
        while (var.put('e',Js(var.get('e').to_number())+Js(1))<var.get('a').get('length')):
            if PyJsComma(var.put('i', var.get('a').get(var.get('e'))),PyJsStrictEq(var.get('i').callprop('toLowerCase').callprop('replace', var.get('dt'), Js('')),var.get('h'))):
                return var.get('t').get(var.get('i'))
        
    PyJsHoisted_t_.func_name = 't'
    var.put('t', PyJsHoisted_t_)
    @Js
    def PyJsHoisted_s_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        if (Js('string')!=var.get('t',throw=False).typeof()):
            PyJsTempException = JsToPyException(var.get('Error').create(Js('not a string')))
            raise PyJsTempException
        PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('text', var.get('t').callprop('trim')),var.get(u"this").put('level', Js(0.0))),var.get(u"this").put('place', Js(0.0))),var.get(u"this").put('root', var.get(u"null"))),var.get(u"this").put('stack', Js([]))),var.get(u"this").put('currentObject', var.get(u"null"))),var.get(u"this").put('state', var.get('_t')))
    PyJsHoisted_s_.func_name = 's'
    var.put('s', PyJsHoisted_s_)
    @Js
    def PyJsHoisted_i_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('s').create(var.get('t')).callprop('output')
    PyJsHoisted_i_.func_name = 'i'
    var.put('i', PyJsHoisted_i_)
    @Js
    def PyJsHoisted_a_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'i', 's', 't', 'a'])
        (var.get('Array').callprop('isArray', var.get('s')) and PyJsComma(var.get('i').callprop('unshift', var.get('s')),var.put('s', var.get(u"null"))))
        var.put('a', (Js({}) if var.get('s') else var.get('t')))
        @Js
        def PyJs_anonymous_1_(t, s, this, arguments, var=var):
            var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 's'])
            return PyJsComma(var.get('h')(var.get('s'), var.get('t')),var.get('t'))
        PyJs_anonymous_1_._set_name('anonymous')
        var.put('e', var.get('i').callprop('reduce', PyJs_anonymous_1_, var.get('a')))
        (var.get('s') and var.get('t').put(var.get('s'), var.get('e')))
    PyJsHoisted_a_.func_name = 'a'
    var.put('a', PyJsHoisted_a_)
    @Js
    def PyJsHoisted_h_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 't', 'i', 's'])
        if var.get('Array').callprop('isArray', var.get('t')):
            var.put('i', var.get('t').callprop('shift'))
            if PyJsComma((PyJsStrictEq(Js('PARAMETER'),var.get('i')) and var.put('i', var.get('t').callprop('shift'))),PyJsStrictEq(Js(1.0),var.get('t').get('length'))):
                return (PyJsComma(var.get('s').put(var.get('i'), Js({})),PyJsComma(var.get('h')(var.get('t').get('0'), var.get('s').get(var.get('i'))), Js(None))) if var.get('Array').callprop('isArray', var.get('t').get('0')) else PyJsComma(var.get('s').put(var.get('i'), var.get('t').get('0')), Js(None)))
            if var.get('t').get('length'):
                if PyJsStrictNeq(Js('TOWGS84'),var.get('i')):
                    if PyJsStrictEq(Js('AXIS'),var.get('i')):
                        return PyJsComma((var.get('s').contains(var.get('i')) or var.get('s').put(var.get('i'), Js([]))),PyJsComma(var.get('s').get(var.get('i')).callprop('push', var.get('t')), Js(None)))
                    (var.get('Array').callprop('isArray', var.get('i')) or var.get('s').put(var.get('i'), Js({})))
                    pass
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('i'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('UNIT')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('PRIMEM')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('VERT_DATUM')):
                            SWITCHED = True
                            return PyJsComma(var.get('s').put(var.get('i'), Js({'name':var.get('t').get('0').callprop('toLowerCase'),'convert':var.get('t').get('1')})),PyJsComma((PyJsStrictEq(Js(3.0),var.get('t').get('length')) and var.get('h')(var.get('t').get('2'), var.get('s').get(var.get('i')))), Js(None)))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('SPHEROID')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('ELLIPSOID')):
                            SWITCHED = True
                            return PyJsComma(var.get('s').put(var.get('i'), Js({'name':var.get('t').get('0'),'a':var.get('t').get('1'),'rf':var.get('t').get('2')})),PyJsComma((PyJsStrictEq(Js(4.0),var.get('t').get('length')) and var.get('h')(var.get('t').get('3'), var.get('s').get(var.get('i')))), Js(None)))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('PROJECTEDCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('PROJCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('GEOGCS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('GEOCCS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('PROJCS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('LOCAL_CS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('GEODCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('GEODETICCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('GEODETICDATUM')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('EDATUM')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('ENGINEERINGDATUM')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('VERT_CS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('VERTCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('VERTICALCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('COMPD_CS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('COMPOUNDCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('ENGINEERINGCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('ENGCRS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('FITTED_CS')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('LOCAL_DATUM')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('DATUM')):
                            SWITCHED = True
                            return PyJsComma(var.get('t').put('0', Js([Js('name'), var.get('t').get('0')])),PyJsComma(var.get('a')(var.get('s'), var.get('i'), var.get('t')), Js(None)))
                        if True:
                            SWITCHED = True
                            #for JS loop
                            var.put('e', (-Js(1.0)))
                            while (var.put('e',Js(var.get('e').to_number())+Js(1))<var.get('t').get('length')):
                                if var.get('Array').callprop('isArray', var.get('t').get(var.get('e'))).neg():
                                    return var.get('h')(var.get('t'), var.get('s').get(var.get('i')))
                            
                            return var.get('a')(var.get('s'), var.get('i'), var.get('t'))
                        SWITCHED = True
                        break
                else:
                    var.get('s').put(var.get('i'), var.get('t'))
            else:
                var.get('s').put(var.get('i'), Js(0.0).neg())
        else:
            var.get('s').put(var.get('t'), Js(0.0).neg())
    PyJsHoisted_h_.func_name = 'h'
    var.put('h', PyJsHoisted_h_)
    @Js
    def PyJsHoisted_e_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        var.put('i', var.get('s').get('0'))
        var.put('a', var.get('s').get('1'))
        ((var.get('t').contains(var.get('i')).neg() and var.get('t').contains(var.get('a'))) and PyJsComma(var.get('t').put(var.get('i'), var.get('t').get(var.get('a'))),(PyJsStrictEq(Js(3.0),var.get('s').get('length')) and var.get('t').put(var.get('i'), var.get('s').callprop('2', var.get('t').get(var.get('i')))))))
    PyJsHoisted_e_.func_name = 'e'
    var.put('e', PyJsHoisted_e_)
    @Js
    def PyJsHoisted_n_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (var.get('t')*var.get('At'))
    PyJsHoisted_n_.func_name = 'n'
    var.put('n', PyJsHoisted_n_)
    @Js
    def PyJsHoisted_r_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'h', 'i', 's', 'r', 't', 'a'])
        @Js
        def PyJsHoisted_s_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return (var.get('s')*(var.get('t').get('to_meter') or Js(1.0)))
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        pass
        def PyJs_LONG_2_(var=var):
            return (var.get('t').put('projName', Js('longlat')) if PyJsStrictEq(Js('GEOGCS'),var.get('t').get('type')) else (PyJsComma(var.get('t').put('projName', Js('identity')),var.get('t').put('local', Js(0.0).neg())) if PyJsStrictEq(Js('LOCAL_CS'),var.get('t').get('type')) else (var.get('t').put('projName', var.get('Object').callprop('keys', var.get('t').get('PROJECTION')).get('0')) if (Js('object')==var.get('t').get('PROJECTION').typeof()) else var.get('t').put('projName', var.get('t').get('PROJECTION')))))
        if PyJsComma(PyJs_LONG_2_(),var.get('t').get('AXIS')):
            #for JS loop
            var.put('i', Js(''))
            var.put('a', Js(0.0))
            var.put('h', var.get('t').get('AXIS').get('length'))
            while (var.get('a')<var.get('h')):
                try:
                    var.put('r', var.get('t').get('AXIS').get(var.get('a')).get('0').callprop('toLowerCase'))
                    def PyJs_LONG_3_(var=var):
                        return (var.put('i', Js('n'), '+') if PyJsStrictNeq((-Js(1.0)),var.get('r').callprop('indexOf', Js('north'))) else (var.put('i', Js('s'), '+') if PyJsStrictNeq((-Js(1.0)),var.get('r').callprop('indexOf', Js('south'))) else (var.put('i', Js('e'), '+') if PyJsStrictNeq((-Js(1.0)),var.get('r').callprop('indexOf', Js('east'))) else (PyJsStrictNeq((-Js(1.0)),var.get('r').callprop('indexOf', Js('west'))) and var.put('i', Js('w'), '+')))))
                    PyJs_LONG_3_()
                finally:
                        var.put('a',Js(var.get('a').to_number())+Js(1))
            PyJsComma((PyJsStrictEq(Js(2.0),var.get('i').get('length')) and var.put('i', Js('u'), '+')),(PyJsStrictEq(Js(3.0),var.get('i').get('length')) and var.get('t').put('axis', var.get('i'))))
        def PyJs_LONG_4_(var=var):
            return PyJsComma(PyJsComma(var.get('t').put('units', var.get('t').get('UNIT').get('name').callprop('toLowerCase')),(PyJsStrictEq(Js('metre'),var.get('t').get('units')) and var.get('t').put('units', Js('meter')))),(var.get('t').get('UNIT').get('convert') and (((var.get('t').get('DATUM') and var.get('t').get('DATUM').get('SPHEROID')) and var.get('t').put('to_meter', (var.get('t').get('UNIT').get('convert')*var.get('t').get('DATUM').get('SPHEROID').get('a')))) if PyJsStrictEq(Js('GEOGCS'),var.get('t').get('type')) else var.get('t').put('to_meter', var.get('t').get('UNIT').get('convert')))))
        (var.get('t').get('UNIT') and PyJs_LONG_4_())
        var.put('o', var.get('t').get('GEOGCS'))
        def PyJs_LONG_6_(var=var):
            def PyJs_LONG_5_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(var.get('t').put('ellps', var.get('o').get('DATUM').get('SPHEROID').get('name').callprop('replace', Js('_19'), Js('')).callprop('replace', JsRegExp('/[Cc]larke\\_18/'), Js('clrk'))),(PyJsStrictEq(Js('international'),var.get('t').get('ellps').callprop('toLowerCase').callprop('slice', Js(0.0), Js(13.0))) and var.get('t').put('ellps', Js('intl')))),var.get('t').put('a', var.get('o').get('DATUM').get('SPHEROID').get('a'))),var.get('t').put('rf', var.get('parseFloat')(var.get('o').get('DATUM').get('SPHEROID').get('rf'), Js(10.0))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get('t').put('datumCode', var.get('o').get('DATUM').get('name').callprop('toLowerCase')) if var.get('o').get('DATUM') else var.get('t').put('datumCode', var.get('o').get('name').callprop('toLowerCase'))),(PyJsStrictEq(Js('d_'),var.get('t').get('datumCode').callprop('slice', Js(0.0), Js(2.0))) and var.get('t').put('datumCode', var.get('t').get('datumCode').callprop('slice', Js(2.0))))),((PyJsStrictNeq(Js('new_zealand_geodetic_datum_1949'),var.get('t').get('datumCode')) and PyJsStrictNeq(Js('new_zealand_1949'),var.get('t').get('datumCode'))) or var.get('t').put('datumCode', Js('nzgd49')))),((PyJsStrictNeq(Js('wgs_1984'),var.get('t').get('datumCode')) and PyJsStrictNeq(Js('world_geodetic_system_1984'),var.get('t').get('datumCode'))) or PyJsComma((PyJsStrictEq(Js('Mercator_Auxiliary_Sphere'),var.get('t').get('PROJECTION')) and var.get('t').put('sphere', Js(0.0).neg())),var.get('t').put('datumCode', Js('wgs84'))))),(PyJsStrictEq(Js('_ferro'),var.get('t').get('datumCode').callprop('slice', (-Js(6.0)))) and var.get('t').put('datumCode', var.get('t').get('datumCode').callprop('slice', Js(0.0), (-Js(6.0)))))),(PyJsStrictEq(Js('_jakarta'),var.get('t').get('datumCode').callprop('slice', (-Js(8.0)))) and var.get('t').put('datumCode', var.get('t').get('datumCode').callprop('slice', Js(0.0), (-Js(8.0)))))),((~var.get('t').get('datumCode').callprop('indexOf', Js('belge'))) and var.get('t').put('datumCode', Js('rnb72')))),((var.get('o').get('DATUM') and var.get('o').get('DATUM').get('SPHEROID')) and PyJs_LONG_5_())),((var.get('o').get('DATUM') and var.get('o').get('DATUM').get('TOWGS84')) and var.get('t').put('datum_params', var.get('o').get('DATUM').get('TOWGS84')))),((~var.get('t').get('datumCode').callprop('indexOf', Js('osgb_1936'))) and var.get('t').put('datumCode', Js('osgb36')))),((~var.get('t').get('datumCode').callprop('indexOf', Js('osni_1952'))) and var.get('t').put('datumCode', Js('osni52')))),(((~var.get('t').get('datumCode').callprop('indexOf', Js('tm65'))) or (~var.get('t').get('datumCode').callprop('indexOf', Js('geodetic_datum_of_1965')))) and var.get('t').put('datumCode', Js('ire65')))),(PyJsStrictEq(Js('ch1903+'),var.get('t').get('datumCode')) and var.get('t').put('datumCode', Js('ch1903')))),((~var.get('t').get('datumCode').callprop('indexOf', Js('israel'))) and var.get('t').put('datumCode', Js('isr93'))))
        PyJsComma(PyJsComma((PyJsStrictEq(Js('GEOGCS'),var.get('t').get('type')) and var.put('o', var.get('t'))),(var.get('o') and PyJs_LONG_6_())),((var.get('t').get('b') and var.get('isFinite')(var.get('t').get('b')).neg()) and var.get('t').put('b', var.get('t').get('a'))))
        def PyJs_LONG_8_(var=var):
            @Js
            def PyJs_anonymous_7_(s, this, arguments, var=var):
                var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
                var.registers(['s'])
                return var.get('e')(var.get('t'), var.get('s'))
            PyJs_anonymous_7_._set_name('anonymous')
            return Js([Js([Js('standard_parallel_1'), Js('Standard_Parallel_1')]), Js([Js('standard_parallel_2'), Js('Standard_Parallel_2')]), Js([Js('false_easting'), Js('False_Easting')]), Js([Js('false_northing'), Js('False_Northing')]), Js([Js('central_meridian'), Js('Central_Meridian')]), Js([Js('latitude_of_origin'), Js('Latitude_Of_Origin')]), Js([Js('latitude_of_origin'), Js('Central_Parallel')]), Js([Js('scale_factor'), Js('Scale_Factor')]), Js([Js('k0'), Js('scale_factor')]), Js([Js('latitude_of_center'), Js('Latitude_Of_Center')]), Js([Js('latitude_of_center'), Js('Latitude_of_center')]), Js([Js('lat0'), Js('latitude_of_center'), var.get('n')]), Js([Js('longitude_of_center'), Js('Longitude_Of_Center')]), Js([Js('longitude_of_center'), Js('Longitude_of_center')]), Js([Js('longc'), Js('longitude_of_center'), var.get('n')]), Js([Js('x0'), Js('false_easting'), var.get('s')]), Js([Js('y0'), Js('false_northing'), var.get('s')]), Js([Js('long0'), Js('central_meridian'), var.get('n')]), Js([Js('lat0'), Js('latitude_of_origin'), var.get('n')]), Js([Js('lat0'), Js('standard_parallel_1'), var.get('n')]), Js([Js('lat1'), Js('standard_parallel_1'), var.get('n')]), Js([Js('lat2'), Js('standard_parallel_2'), var.get('n')]), Js([Js('azimuth'), Js('Azimuth')]), Js([Js('alpha'), Js('azimuth'), var.get('n')]), Js([Js('srsCode'), Js('name')])]).callprop('forEach', PyJs_anonymous_7_)
        def PyJs_LONG_9_(var=var):
            return (((var.get('t').get('lat_ts') or var.get('t').get('lat1').neg()) or (PyJsStrictNeq(Js('Stereographic_South_Pole'),var.get('t').get('projName')) and PyJsStrictNeq(Js('Polar Stereographic (variant B)'),var.get('t').get('projName')))) or PyJsComma(var.get('t').put('lat0', var.get('n')((Js(90.0) if (var.get('t').get('lat1')>Js(0.0)) else (-Js(90.0))))),var.get('t').put('lat_ts', var.get('t').get('lat1'))))
        PyJsComma(PyJsComma(PyJs_LONG_8_(),(((var.get('t').get('long0') or var.get('t').get('longc').neg()) or (PyJsStrictNeq(Js('Albers_Conic_Equal_Area'),var.get('t').get('projName')) and PyJsStrictNeq(Js('Lambert_Azimuthal_Equal_Area'),var.get('t').get('projName')))) or var.get('t').put('long0', var.get('t').get('longc')))),PyJs_LONG_9_())
    PyJsHoisted_r_.func_name = 'r'
    var.put('r', PyJsHoisted_r_)
    @Js
    def PyJsHoisted_o_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('s', var.get(u"this"))
        if PyJsStrictEq(Js(2.0),var.get('arguments').get('length')):
            var.put('i', var.get('arguments').get('1'))
            ((var.get('o').put(var.get('t'), var.get('yt')(var.get('arguments').get('1'))) if PyJsStrictEq(Js('+'),var.get('i').callprop('charAt', Js(0.0))) else var.get('o').put(var.get('t'), var.get('Ct')(var.get('arguments').get('1')))) if (Js('string')==var.get('i',throw=False).typeof()) else var.get('o').put(var.get('t'), var.get('i')))
        else:
            if PyJsStrictEq(Js(1.0),var.get('arguments').get('length')):
                if var.get('Array').callprop('isArray', var.get('t')):
                    @Js
                    def PyJs_anonymous_10_(t, this, arguments, var=var):
                        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                        var.registers(['t'])
                        (var.get('o').callprop('apply', var.get('s'), var.get('t')) if var.get('Array').callprop('isArray', var.get('t')) else var.get('o')(var.get('t')))
                    PyJs_anonymous_10_._set_name('anonymous')
                    return var.get('t').callprop('map', PyJs_anonymous_10_)
                if (Js('string')==var.get('t',throw=False).typeof()):
                    if var.get('o').contains(var.get('t')):
                        return var.get('o').get(var.get('t'))
                else:
                    def PyJs_LONG_11_(var=var):
                        return (var.get('o').put((Js('EPSG:')+var.get('t').get('EPSG')), var.get('t')) if var.get('t').contains(Js('EPSG')) else (var.get('o').put((Js('ESRI:')+var.get('t').get('ESRI')), var.get('t')) if var.get('t').contains(Js('ESRI')) else (var.get('o').put((Js('IAU2000:')+var.get('t').get('IAU2000')), var.get('t')) if var.get('t').contains(Js('IAU2000')) else var.get('console').callprop('log', var.get('t')))))
                    PyJs_LONG_11_()
                return var.get('undefined')
    PyJsHoisted_o_.func_name = 'o'
    var.put('o', PyJsHoisted_o_)
    @Js
    def PyJsHoisted_l_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (Js('string')==var.get('t',throw=False).typeof())
    PyJsHoisted_l_.func_name = 'l'
    var.put('l', PyJsHoisted_l_)
    @Js
    def PyJsHoisted_M_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('o').contains(var.get('t'))
    PyJsHoisted_M_.func_name = 'M'
    var.put('M', PyJsHoisted_M_)
    @Js
    def PyJsHoisted_c_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        @Js
        def PyJs_anonymous_12_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return (var.get('t').callprop('indexOf', var.get('s'))>(-Js(1.0)))
        PyJs_anonymous_12_._set_name('anonymous')
        return var.get('Et').callprop('some', PyJs_anonymous_12_)
    PyJsHoisted_c_.func_name = 'c'
    var.put('c', PyJsHoisted_c_)
    @Js
    def PyJsHoisted_u_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'a', 's'])
        var.put('i', var.get('t')(var.get('s'), Js('authority')))
        if var.get('i'):
            var.put('a', var.get('t')(var.get('i'), Js('epsg')))
            return (var.get('a') and (var.get('Pt').callprop('indexOf', var.get('a'))>(-Js(1.0))))
    PyJsHoisted_u_.func_name = 'u'
    var.put('u', PyJsHoisted_u_)
    @Js
    def PyJsHoisted_f_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 's'])
        var.put('i', var.get('t')(var.get('s'), Js('extension')))
        if var.get('i'):
            return var.get('t')(var.get('i'), Js('proj4'))
    PyJsHoisted_f_.func_name = 'f'
    var.put('f', PyJsHoisted_f_)
    @Js
    def PyJsHoisted_m_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return PyJsStrictEq(Js('+'),var.get('t').get('0'))
    PyJsHoisted_m_.func_name = 'm'
    var.put('m', PyJsHoisted_m_)
    @Js
    def PyJsHoisted_p_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        if var.get('l')(var.get('t')).neg():
            return var.get('t')
        if var.get('M')(var.get('t')):
            return var.get('o').get(var.get('t'))
        if var.get('c')(var.get('t')):
            var.put('s', var.get('Ct')(var.get('t')))
            if var.get('u')(var.get('s')):
                return var.get('o').get('EPSG:3857')
            var.put('i', var.get('f')(var.get('s')))
            return (var.get('yt')(var.get('i')) if var.get('i') else var.get('s'))
        return (var.get('yt')(var.get('t')) if var.get('m')(var.get('t')) else PyJsComma(Js(0.0), Js(None)))
    PyJsHoisted_p_.func_name = 'p'
    var.put('p', PyJsHoisted_p_)
    @Js
    def PyJsHoisted_d_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('t')
    PyJsHoisted_d_.func_name = 'd'
    var.put('d', PyJsHoisted_d_)
    @Js
    def PyJsHoisted_y_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('i', var.get('Tt').get('length'))
        @Js
        def PyJs_anonymous_13_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('Gt').put(var.get('t').callprop('toLowerCase'), var.get('i'))
        PyJs_anonymous_13_._set_name('anonymous')
        return (PyJsComma(PyJsComma(var.get('Tt').put(var.get('i'), var.get('t')),var.get('t').get('names').callprop('forEach', PyJs_anonymous_13_)),var.get(u"this")) if var.get('t').get('names') else PyJsComma(var.get('console').callprop('log', var.get('s')),Js(0.0).neg()))
    PyJsHoisted_y_.func_name = 'y'
    var.put('y', PyJsHoisted_y_)
    @Js
    def PyJsHoisted___(t, s, i, a, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('h', (var.get('t')*var.get('t')))
        var.put('e', (var.get('s')*var.get('s')))
        var.put('n', ((var.get('h')-var.get('e'))/var.get('h')))
        var.put('r', Js(0.0))
        return PyJsComma((PyJsComma(var.put('h', (var.put('t', (Js(1.0)-(var.get('n')*(var.get('et')+(var.get('n')*(var.get('nt')+(var.get('n')*var.get('rt'))))))), '*')*var.get('t'))),var.put('n', Js(0.0))) if var.get('a') else var.put('r', var.get('Math').callprop('sqrt', var.get('n')))),Js({'es':var.get('n'),'e':var.get('r'),'ep2':((var.get('h')-var.get('e'))/var.get('e'))}))
    PyJsHoisted___.func_name = '_'
    var.put('_', PyJsHoisted___)
    @Js
    def PyJsHoisted_x_(s, i, a, h, e, this, arguments, var=var):
        var = Scope({'s':s, 'i':i, 'a':a, 'h':h, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'a'])
        if var.get('s').neg():
            var.put('n', var.get('t')(var.get('zt'), var.get('h')))
            PyJsComma(PyJsComma(PyJsComma((var.get('n') or var.put('n', var.get('Lt'))),var.put('s', var.get('n').get('a'))),var.put('i', var.get('n').get('b'))),var.put('a', var.get('n').get('rf')))
        return PyJsComma(PyJsComma(((var.get('a') and var.get('i').neg()) and var.put('i', ((Js(1.0)-(Js(1.0)/var.get('a')))*var.get('s')))),((PyJsStrictEq(Js(0.0),var.get('a')) or (var.get('Math').callprop('abs', (var.get('s')-var.get('i')))<var.get('ot'))) and PyJsComma(var.put('e', Js(0.0).neg()),var.put('i', var.get('s'))))),Js({'a':var.get('s'),'b':var.get('i'),'rf':var.get('a'),'sphere':var.get('e')}))
    PyJsHoisted_x_.func_name = 'x'
    var.put('x', PyJsHoisted_x_)
    @Js
    def PyJsHoisted_v_(t, s, i, a, h, e, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'h':h, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        var.put('n', Js({}))
        def PyJs_LONG_16_(var=var):
            def PyJs_LONG_15_(var=var):
                def PyJs_LONG_14_(var=var):
                    return ((((PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('3')) and PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('4'))) and PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('5'))) and PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('6'))) or PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('n').put('datum_type', var.get('tt')),var.get('n').get('datum_params').put('3', var.get('at'), '*')),var.get('n').get('datum_params').put('4', var.get('at'), '*')),var.get('n').get('datum_params').put('5', var.get('at'), '*')),var.get('n').get('datum_params').put('6', ((var.get('n').get('datum_params').get('6')/Js(1000000.0))+Js(1.0)))))
                return PyJsComma(PyJsComma(var.get('n').put('datum_params', var.get('s').callprop('map', var.get('parseFloat'))),(((PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('0')) and PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('1'))) and PyJsStrictEq(Js(0.0),var.get('n').get('datum_params').get('2'))) or var.get('n').put('datum_type', var.get('$')))),((var.get('n').get('datum_params').get('length')>Js(3.0)) and PyJs_LONG_14_()))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('n').put('datum_type', (var.get('it') if (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('t')) or PyJsStrictEq(Js('none'),var.get('t'))) else var.get('st'))),(var.get('s') and PyJs_LONG_15_())),var.get('n').put('a', var.get('i'))),var.get('n').put('b', var.get('a'))),var.get('n').put('es', var.get('h'))),var.get('n').put('ep2', var.get('e'))),var.get('n'))
        return PyJs_LONG_16_()
    PyJsHoisted_v_.func_name = 'v'
    var.put('v', PyJsHoisted_v_)
    @Js
    def PyJsHoisted_Projection_(s, i, this, arguments, var=var):
        var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 'a'])
        if var.get(u"this").instanceof(var.get('Projection')).neg():
            return var.get('Projection').create(var.get('s'))
        @Js
        def PyJs_anonymous_17_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            if var.get('t'):
                PyJsTempException = JsToPyException(var.get('t'))
                raise PyJsTempException
        PyJs_anonymous_17_._set_name('anonymous')
        var.put('i', (var.get('i') or PyJs_anonymous_17_))
        var.put('a', var.get('p')(var.get('s')))
        if (Js('object')==var.get('a',throw=False).typeof()):
            var.put('h', var.get('Projection').get('projections').callprop('get', var.get('a').get('projName')))
            if var.get('h'):
                if (var.get('a').get('datumCode') and PyJsStrictNeq(Js('none'),var.get('a').get('datumCode'))):
                    var.put('e', var.get('t')(var.get('Dt'), var.get('a').get('datumCode')))
                    (var.get('e') and PyJsComma(PyJsComma(var.get('a').put('datum_params', (var.get('e').get('towgs84').callprop('split', Js(',')) if var.get('e').get('towgs84') else var.get(u"null"))),var.get('a').put('ellps', var.get('e').get('ellipse'))),var.get('a').put('datumName', (var.get('e').get('datumName') if var.get('e').get('datumName') else var.get('a').get('datumCode')))))
                PyJsComma(PyJsComma(var.get('a').put('k0', (var.get('a').get('k0') or Js(1.0))),var.get('a').put('axis', (var.get('a').get('axis') or Js('enu')))),var.get('a').put('ellps', (var.get('a').get('ellps') or Js('wgs84'))))
                var.put('n', var.get('x')(var.get('a').get('a'), var.get('a').get('b'), var.get('a').get('rf'), var.get('a').get('ellps'), var.get('a').get('sphere')))
                var.put('r', var.get('_')(var.get('n').get('a'), var.get('n').get('b'), var.get('n').get('rf'), var.get('a').get('R_A')))
                var.put('o', (var.get('a').get('datum') or var.get('v')(var.get('a').get('datumCode'), var.get('a').get('datum_params'), var.get('n').get('a'), var.get('n').get('b'), var.get('r').get('es'), var.get('r').get('ep2'))))
                def PyJs_LONG_18_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('Nt')(var.get(u"this"), var.get('a')),var.get('Nt')(var.get(u"this"), var.get('h'))),var.get(u"this").put('a', var.get('n').get('a'))),var.get(u"this").put('b', var.get('n').get('b'))),var.get(u"this").put('rf', var.get('n').get('rf'))),var.get(u"this").put('sphere', var.get('n').get('sphere'))),var.get(u"this").put('es', var.get('r').get('es'))),var.get(u"this").put('e', var.get('r').get('e'))),var.get(u"this").put('ep2', var.get('r').get('ep2'))),var.get(u"this").put('datum', var.get('o'))),var.get(u"this").callprop('init')),var.get('i')(var.get(u"null"), var.get(u"this")))
                PyJs_LONG_18_()
            else:
                var.get('i')(var.get('s'))
        else:
            var.get('i')(var.get('s'))
    PyJsHoisted_Projection_.func_name = 'Projection'
    var.put('Projection', PyJsHoisted_Projection_)
    @Js
    def PyJsHoisted_g_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        def PyJs_LONG_20_(var=var):
            def PyJs_LONG_19_(var=var):
                return (((PyJsStrictEq(var.get('t').get('datum_params').get('0'),var.get('s').get('datum_params').get('0')) and PyJsStrictEq(var.get('t').get('datum_params').get('1'),var.get('s').get('datum_params').get('1'))) and PyJsStrictEq(var.get('t').get('datum_params').get('2'),var.get('s').get('datum_params').get('2'))) and PyJsStrictEq(var.get('t').get('datum_params').get('3'),var.get('s').get('datum_params').get('3')))
            return (((PyJsStrictEq(var.get('t').get('datum_params').get('0'),var.get('s').get('datum_params').get('0')) and PyJsStrictEq(var.get('t').get('datum_params').get('1'),var.get('s').get('datum_params').get('1'))) and PyJsStrictEq(var.get('t').get('datum_params').get('2'),var.get('s').get('datum_params').get('2'))) if PyJsStrictEq(var.get('t').get('datum_type'),var.get('$')) else (PyJsStrictNeq(var.get('t').get('datum_type'),var.get('tt')) or (((PyJs_LONG_19_() and PyJsStrictEq(var.get('t').get('datum_params').get('4'),var.get('s').get('datum_params').get('4'))) and PyJsStrictEq(var.get('t').get('datum_params').get('5'),var.get('s').get('datum_params').get('5'))) and PyJsStrictEq(var.get('t').get('datum_params').get('6'),var.get('s').get('datum_params').get('6')))))
        return (PyJsStrictEq(var.get('t').get('datum_type'),var.get('s').get('datum_type')) and ((PyJsStrictNeq(var.get('t').get('a'),var.get('s').get('a')) or (var.get('Math').callprop('abs', (var.get('t').get('es')-var.get('s').get('es')))>Js(5e-11))).neg() and PyJs_LONG_20_()))
    PyJsHoisted_g_.func_name = 'g'
    var.put('g', PyJsHoisted_g_)
    @Js
    def PyJsHoisted_b_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('r', var.get('t').get('x'))
        var.put('o', var.get('t').get('y'))
        var.put('l', (var.get('t').get('z') if var.get('t').get('z') else Js(0.0)))
        if ((var.get('o')<(-var.get('ht'))) and (var.get('o')>((-Js(1.001))*var.get('ht')))):
            var.put('o', (-var.get('ht')))
        else:
            if ((var.get('o')>var.get('ht')) and (var.get('o')<(Js(1.001)*var.get('ht')))):
                var.put('o', var.get('ht'))
            else:
                if (var.get('o')<(-var.get('ht'))):
                    return Js({'x':((-Js(1.0))/Js(0.0)),'y':((-Js(1.0))/Js(0.0)),'z':var.get('t').get('z')})
                if (var.get('o')>var.get('ht')):
                    return Js({'x':(Js(1.0)/Js(0.0)),'y':(Js(1.0)/Js(0.0)),'z':var.get('t').get('z')})
        def PyJs_LONG_21_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get('r')>var.get('Math').get('PI')) and var.put('r', (Js(2.0)*var.get('Math').get('PI')), '-')),var.put('h', var.get('Math').callprop('sin', var.get('o')))),var.put('n', var.get('Math').callprop('cos', var.get('o')))),var.put('e', (var.get('h')*var.get('h')))),var.put('a', (var.get('i')/var.get('Math').callprop('sqrt', (Js(1.0)-(var.get('s')*var.get('e'))))))),Js({'x':(((var.get('a')+var.get('l'))*var.get('n'))*var.get('Math').callprop('cos', var.get('r'))),'y':(((var.get('a')+var.get('l'))*var.get('n'))*var.get('Math').callprop('sin', var.get('r'))),'z':(((var.get('a')*(Js(1.0)-var.get('s')))+var.get('l'))*var.get('h'))}))
        return PyJs_LONG_21_()
    PyJsHoisted_b_.func_name = 'b'
    var.put('b', PyJsHoisted_b_)
    @Js
    def PyJsHoisted_w_(t, s, i, a, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 'n', 'e', 's', 'p', 'r', 't', 'g', 'M', 'c', 'b', 'h', 'i', 'y', 'x', 'm', 'v', 'd', 'l', 'o', 'f', '_', 'a'])
        var.put('v', var.get('t').get('x'))
        var.put('g', var.get('t').get('y'))
        var.put('b', (var.get('t').get('z') if var.get('t').get('z') else Js(0.0)))
        if PyJsComma(PyJsComma(var.put('h', var.get('Math').callprop('sqrt', ((var.get('v')*var.get('v'))+(var.get('g')*var.get('g'))))),var.put('e', var.get('Math').callprop('sqrt', (((var.get('v')*var.get('v'))+(var.get('g')*var.get('g')))+(var.get('b')*var.get('b')))))),((var.get('h')/var.get('i'))<Js(1e-12))):
            if PyJsComma(var.put('y', Js(0.0)),((var.get('e')/var.get('i'))<Js(1e-12))):
                return PyJsComma(PyJsComma(var.put('_', var.get('ht')),var.put('x', (-var.get('a')))),Js({'x':var.get('t').get('x'),'y':var.get('t').get('y'),'z':var.get('t').get('z')}))
        else:
            var.put('y', var.get('Math').callprop('atan2', var.get('g'), var.get('v')))
        PyJsComma(PyJsComma(PyJsComma(var.put('n', (var.get('b')/var.get('e'))),var.put('c', ((var.put('r', (var.get('h')/var.get('e')))*(Js(1.0)-var.get('s')))*var.put('o', (Js(1.0)/var.get('Math').callprop('sqrt', (Js(1.0)-(((var.get('s')*(Js(2.0)-var.get('s')))*var.get('r'))*var.get('r'))))))))),var.put('u', (var.get('n')*var.get('o')))),var.put('d', Js(0.0)))
        while 1:
            def PyJs_LONG_22_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)),var.put('l', ((var.get('s')*var.put('M', (var.get('i')/var.get('Math').callprop('sqrt', (Js(1.0)-((var.get('s')*var.get('u'))*var.get('u')))))))/(var.get('M')+var.put('x', (((var.get('h')*var.get('c'))+(var.get('b')*var.get('u')))-(var.get('M')*(Js(1.0)-((var.get('s')*var.get('u'))*var.get('u')))))))))),var.put('p', ((var.put('m', (var.get('n')*var.put('o', (Js(1.0)/var.get('Math').callprop('sqrt', (Js(1.0)-(((var.get('l')*(Js(2.0)-var.get('l')))*var.get('r'))*var.get('r'))))))))*var.get('c'))-(var.put('f', ((var.get('r')*(Js(1.0)-var.get('l')))*var.get('o')))*var.get('u'))))),var.put('c', var.get('f'))),var.put('u', var.get('m')))
            PyJs_LONG_22_()
            if not (((var.get('p')*var.get('p'))>Js(1e-24)) and (var.get('d')<Js(30.0))):
                break
        return PyJsComma(var.put('_', var.get('Math').callprop('atan', (var.get('m')/var.get('Math').callprop('abs', var.get('f'))))),Js({'x':var.get('y'),'y':var.get('_'),'z':var.get('x')}))
    PyJsHoisted_w_.func_name = 'w'
    var.put('w', PyJsHoisted_w_)
    @Js
    def PyJsHoisted_A_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        if PyJsStrictEq(var.get('s'),var.get('$')):
            return Js({'x':(var.get('t').get('x')+var.get('i').get('0')),'y':(var.get('t').get('y')+var.get('i').get('1')),'z':(var.get('t').get('z')+var.get('i').get('2'))})
        if PyJsStrictEq(var.get('s'),var.get('tt')):
            var.put('a', var.get('i').get('0'))
            var.put('h', var.get('i').get('1'))
            var.put('e', var.get('i').get('2'))
            var.put('n', var.get('i').get('3'))
            var.put('r', var.get('i').get('4'))
            var.put('o', var.get('i').get('5'))
            var.put('l', var.get('i').get('6'))
            return Js({'x':((var.get('l')*((var.get('t').get('x')-(var.get('o')*var.get('t').get('y')))+(var.get('r')*var.get('t').get('z'))))+var.get('a')),'y':((var.get('l')*(((var.get('o')*var.get('t').get('x'))+var.get('t').get('y'))-(var.get('n')*var.get('t').get('z'))))+var.get('h')),'z':((var.get('l')*((((-var.get('r'))*var.get('t').get('x'))+(var.get('n')*var.get('t').get('y')))+var.get('t').get('z')))+var.get('e'))})
    PyJsHoisted_A_.func_name = 'A'
    var.put('A', PyJsHoisted_A_)
    @Js
    def PyJsHoisted_C_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        if PyJsStrictEq(var.get('s'),var.get('$')):
            return Js({'x':(var.get('t').get('x')-var.get('i').get('0')),'y':(var.get('t').get('y')-var.get('i').get('1')),'z':(var.get('t').get('z')-var.get('i').get('2'))})
        if PyJsStrictEq(var.get('s'),var.get('tt')):
            var.put('a', var.get('i').get('0'))
            var.put('h', var.get('i').get('1'))
            var.put('e', var.get('i').get('2'))
            var.put('n', var.get('i').get('3'))
            var.put('r', var.get('i').get('4'))
            var.put('o', var.get('i').get('5'))
            var.put('l', var.get('i').get('6'))
            var.put('M', ((var.get('t').get('x')-var.get('a'))/var.get('l')))
            var.put('c', ((var.get('t').get('y')-var.get('h'))/var.get('l')))
            var.put('u', ((var.get('t').get('z')-var.get('e'))/var.get('l')))
            return Js({'x':((var.get('M')+(var.get('o')*var.get('c')))-(var.get('r')*var.get('u'))),'y':((((-var.get('o'))*var.get('M'))+var.get('c'))+(var.get('n')*var.get('u'))),'z':(((var.get('r')*var.get('M'))-(var.get('n')*var.get('c')))+var.get('u'))})
    PyJsHoisted_C_.func_name = 'C'
    var.put('C', PyJsHoisted_C_)
    @Js
    def PyJsHoisted_E_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (PyJsStrictEq(var.get('t'),var.get('$')) or PyJsStrictEq(var.get('t'),var.get('tt')))
    PyJsHoisted_E_.func_name = 'E'
    var.put('E', PyJsHoisted_E_)
    @Js
    def PyJsHoisted_P_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        if (Js('function')==var.get('Number').get('isFinite').typeof()):
            if var.get('Number').callprop('isFinite', var.get('t')):
                return var.get('undefined')
            PyJsTempException = JsToPyException(var.get('TypeError').create(Js('coordinates must be finite numbers')))
            raise PyJsTempException
        if (((Js('number')!=var.get('t',throw=False).typeof()) or PyJsStrictNeq(var.get('t'),var.get('t'))) or var.get('isFinite')(var.get('t')).neg()):
            PyJsTempException = JsToPyException(var.get('TypeError').create(Js('coordinates must be finite numbers')))
            raise PyJsTempException
    PyJsHoisted_P_.func_name = 'P'
    var.put('P', PyJsHoisted_P_)
    @Js
    def PyJsHoisted_N_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        def PyJs_LONG_23_(var=var):
            return (((PyJsStrictEq(var.get('t').get('datum').get('datum_type'),var.get('$')) or PyJsStrictEq(var.get('t').get('datum').get('datum_type'),var.get('tt'))) and PyJsStrictNeq(Js('WGS84'),var.get('s').get('datumCode'))) or ((PyJsStrictEq(var.get('s').get('datum').get('datum_type'),var.get('$')) or PyJsStrictEq(var.get('s').get('datum').get('datum_type'),var.get('tt'))) and PyJsStrictNeq(Js('WGS84'),var.get('t').get('datumCode'))))
        return PyJs_LONG_23_()
    PyJsHoisted_N_.func_name = 'N'
    var.put('N', PyJsHoisted_N_)
    @Js
    def PyJsHoisted_S_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        pass
        def PyJs_LONG_24_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get('Array').callprop('isArray', var.get('i')) and var.put('i', var.get('Ft')(var.get('i')))),var.get('Qt')(var.get('i'))),(((var.get('t').get('datum') and var.get('s').get('datum')) and var.get('N')(var.get('t'), var.get('s'))) and PyJsComma(var.put('i', var.get('S')(var.get('t'), var.put('a', var.get('Projection').create(Js('WGS84'))), var.get('i'))),var.put('t', var.get('a'))))),(PyJsStrictNeq(Js('enu'),var.get('t').get('axis')) and var.put('i', var.get('Ut')(var.get('t'), Js(1.0).neg(), var.get('i'))))),PyJsStrictEq(Js('longlat'),var.get('t').get('projName')))
        if PyJs_LONG_24_():
            var.put('i', Js({'x':(var.get('i').get('x')*var.get('lt')),'y':(var.get('i').get('y')*var.get('lt')),'z':(var.get('i').get('z') or Js(0.0))}))
        else:
            if PyJsComma((var.get('t').get('to_meter') and var.put('i', Js({'x':(var.get('i').get('x')*var.get('t').get('to_meter')),'y':(var.get('i').get('y')*var.get('t').get('to_meter')),'z':(var.get('i').get('z') or Js(0.0))}))),var.put('i', var.get('t').callprop('inverse', var.get('i'))).neg()):
                return var.get('undefined')
        def PyJs_LONG_26_(var=var):
            def PyJs_LONG_25_(var=var):
                return (var.put('i', Js({'x':(var.get('i').get('x')*var.get('Mt')),'y':(var.get('i').get('y')*var.get('Mt')),'z':(var.get('i').get('z') or Js(0.0))})) if PyJsStrictEq(Js('longlat'),var.get('s').get('projName')) else PyJsComma(var.put('i', var.get('s').callprop('forward', var.get('i'))),(var.get('s').get('to_meter') and var.put('i', Js({'x':(var.get('i').get('x')/var.get('s').get('to_meter')),'y':(var.get('i').get('y')/var.get('s').get('to_meter')),'z':(var.get('i').get('z') or Js(0.0))})))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get('t').get('from_greenwich') and var.get('i').put('x', var.get('t').get('from_greenwich'), '+')),var.put('i', var.get('Bt')(var.get('t').get('datum'), var.get('s').get('datum'), var.get('i')))),(var.get('s').get('from_greenwich') and var.put('i', Js({'x':(var.get('i').get('x')-var.get('s').get('from_greenwich')),'y':var.get('i').get('y'),'z':(var.get('i').get('z') or Js(0.0))})))),PyJs_LONG_25_()),(var.get('Ut')(var.get('s'), Js(0.0).neg(), var.get('i')) if PyJsStrictNeq(Js('enu'),var.get('s').get('axis')) else var.get('i')))
        return PyJs_LONG_26_()
    PyJsHoisted_S_.func_name = 'S'
    var.put('S', PyJsHoisted_S_)
    @Js
    def PyJsHoisted_k_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'e', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_29_(var=var):
            def PyJs_LONG_27_(var=var):
                return ((Js([var.get('a').get('x'), var.get('a').get('y'), var.get('a').get('z')]).callprop('concat', var.get('i').callprop('splice', Js(3.0))) if (Js('number')==var.get('a').get('z').typeof()) else Js([var.get('a').get('x'), var.get('a').get('y'), var.get('i').get('2')]).callprop('concat', var.get('i').callprop('splice', Js(3.0)))) if ((PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('t').get('name')) and PyJsStrictEq(Js('geocent'),var.get('t').get('name'))) or (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('s').get('name')) and PyJsStrictEq(Js('geocent'),var.get('s').get('name')))) else Js([var.get('a').get('x'), var.get('a').get('y')]).callprop('concat', var.get('i').callprop('splice', Js(2.0))))
            @Js
            def PyJs_anonymous_28_(a, this, arguments, var=var):
                var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
                var.registers(['a'])
                if ((PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('t').get('name')) and PyJsStrictEq(Js('geocent'),var.get('t').get('name'))) or (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('s').get('name')) and PyJsStrictEq(Js('geocent'),var.get('s').get('name')))):
                    if ((PyJsStrictEq(Js('x'),var.get('a')) or PyJsStrictEq(Js('y'),var.get('a'))) or PyJsStrictEq(Js('z'),var.get('a'))):
                        return var.get('undefined')
                else:
                    if (PyJsStrictEq(Js('x'),var.get('a')) or PyJsStrictEq(Js('y'),var.get('a'))):
                        return var.get('undefined')
                var.get('h').put(var.get('a'), var.get('i').get(var.get('a')))
            PyJs_anonymous_28_._set_name('anonymous')
            return (PyJsComma(var.put('a', (var.get('S')(var.get('t'), var.get('s'), var.get('i')) or Js({'x':var.get('NaN'),'y':var.get('NaN')}))),(PyJs_LONG_27_() if (var.get('i').get('length')>Js(2.0)) else Js([var.get('a').get('x'), var.get('a').get('y')]))) if var.get('Array').callprop('isArray', var.get('i')) else PyJsComma(var.put('h', var.get('S')(var.get('t'), var.get('s'), var.get('i'))),(var.get('h') if PyJsStrictEq(Js(2.0),var.put('e', var.get('Object').callprop('keys', var.get('i'))).get('length')) else PyJsComma(var.get('e').callprop('forEach', PyJs_anonymous_28_),var.get('h')))))
        return PyJs_LONG_29_()
    PyJsHoisted_k_.func_name = 'k'
    var.put('k', PyJsHoisted_k_)
    @Js
    def PyJsHoisted_q_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (var.get('t') if var.get('t').instanceof(var.get('Projection')) else (var.get('t').get('oProj') if var.get('t').get('oProj') else var.get('Projection')(var.get('t'))))
    PyJsHoisted_q_.func_name = 'q'
    var.put('q', PyJsHoisted_q_)
    @Js
    def PyJsHoisted_I_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        var.put('t', var.get('q')(var.get('t')))
        var.put('h', Js(1.0).neg())
        def PyJs_LONG_30_(var=var):
            return (PyJsComma(PyJsComma(var.put('s', var.get('t')),var.put('t', var.get('Wt'))),var.put('h', Js(0.0).neg())) if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('s')) else ((PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('s').get('x')) or var.get('Array').callprop('isArray', var.get('s'))) and PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('s')),var.put('s', var.get('t'))),var.put('t', var.get('Wt'))),var.put('h', Js(0.0).neg()))))
        @Js
        def PyJs_anonymous_31_(i, this, arguments, var=var):
            var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i'])
            return var.get('k')(var.get('t'), var.get('s'), var.get('i'))
        PyJs_anonymous_31_._set_name('anonymous')
        @Js
        def PyJs_anonymous_32_(i, this, arguments, var=var):
            var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i'])
            return var.get('k')(var.get('s'), var.get('t'), var.get('i'))
        PyJs_anonymous_32_._set_name('anonymous')
        return PyJsComma(PyJsComma(PyJs_LONG_30_(),var.put('s', var.get('q')(var.get('s')))),(var.get('k')(var.get('t'), var.get('s'), var.get('i')) if var.get('i') else PyJsComma(PyJsComma(var.put('a', Js({'forward':PyJs_anonymous_31_,'inverse':PyJs_anonymous_32_})),(var.get('h') and var.get('a').put('oProj', var.get('s')))),var.get('a'))))
    PyJsHoisted_I_.func_name = 'I'
    var.put('I', PyJsHoisted_I_)
    @Js
    def PyJsHoisted_O_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        return PyJsComma(var.put('s', (var.get('s') or Js(5.0))),var.get('D')(var.get('j')(Js({'lat':var.get('t').get('1'),'lon':var.get('t').get('0')})), var.get('s')))
    PyJsHoisted_O_.func_name = 'O'
    var.put('O', PyJsHoisted_O_)
    @Js
    def PyJsHoisted_R_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', var.get('z')(var.get('Q')(var.get('t').callprop('toUpperCase'))))
        return (Js([var.get('s').get('lon'), var.get('s').get('lat')]) if (var.get('s').get('lat') and var.get('s').get('lon')) else Js([((var.get('s').get('left')+var.get('s').get('right'))/Js(2.0)), ((var.get('s').get('top')+var.get('s').get('bottom'))/Js(2.0))]))
    PyJsHoisted_R_.func_name = 'R'
    var.put('R', PyJsHoisted_R_)
    @Js
    def PyJsHoisted_G_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (var.get('t')*(var.get('Math').get('PI')/Js(180.0)))
    PyJsHoisted_G_.func_name = 'G'
    var.put('G', PyJsHoisted_G_)
    @Js
    def PyJsHoisted_T_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return ((var.get('t')/var.get('Math').get('PI'))*Js(180.0))
    PyJsHoisted_T_.func_name = 'T'
    var.put('T', PyJsHoisted_T_)
    @Js
    def PyJsHoisted_j_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 's', 'r', 'f', 'a'])
        var.put('o', var.get('t').get('lat'))
        var.put('l', var.get('t').get('lon'))
        var.put('M', Js(6378137.0))
        var.put('c', var.get('G')(var.get('o')))
        var.put('u', var.get('G')(var.get('l')))
        def PyJs_LONG_34_(var=var):
            def PyJs_LONG_33_(var=var):
                return (((var.get('o')>=Js(72.0)) and (var.get('o')<Js(84.0))) and (var.put('r', Js(31.0)) if ((var.get('l')>=Js(0.0)) and (var.get('l')<Js(9.0))) else (var.put('r', Js(33.0)) if ((var.get('l')>=Js(9.0)) and (var.get('l')<Js(21.0))) else (var.put('r', Js(35.0)) if ((var.get('l')>=Js(21.0)) and (var.get('l')<Js(33.0))) else (((var.get('l')>=Js(33.0)) and (var.get('l')<Js(42.0))) and var.put('r', Js(37.0)))))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('r', (var.get('Math').callprop('floor', ((var.get('l')+Js(180.0))/Js(6.0)))+Js(1.0))),(PyJsStrictEq(Js(180.0),var.get('l')) and var.put('r', Js(60.0)))),(((((var.get('o')>=Js(56.0)) and (var.get('o')<Js(64.0))) and (var.get('l')>=Js(3.0))) and (var.get('l')<Js(12.0))) and var.put('r', Js(32.0)))),PyJs_LONG_33_()),var.put('n', var.get('G')((((Js(6.0)*(var.get('r')-Js(1.0)))-Js(180.0))+Js(3.0))))),var.put('s', (var.get('M')/var.get('Math').callprop('sqrt', (Js(1.0)-((Js(0.00669438)*var.get('Math').callprop('sin', var.get('c')))*var.get('Math').callprop('sin', var.get('c')))))))),var.put('i', (var.get('Math').callprop('tan', var.get('c'))*var.get('Math').callprop('tan', var.get('c'))))),var.put('a', ((Js(0.006739496752268451)*var.get('Math').callprop('cos', var.get('c')))*var.get('Math').callprop('cos', var.get('c')))))
        PyJs_LONG_34_()
        def PyJs_LONG_35_(var=var):
            return ((Js(0.9996)*var.get('s'))*((var.put('h', (var.get('Math').callprop('cos', var.get('c'))*(var.get('u')-var.get('n'))))+((((((Js(1.0)-var.get('i'))+var.get('a'))*var.get('h'))*var.get('h'))*var.get('h'))/Js(6.0)))+((((((((((Js(5.0)-(Js(18.0)*var.get('i')))+(var.get('i')*var.get('i')))+(Js(72.0)*var.get('a')))-Js(0.39089081163157013))*var.get('h'))*var.get('h'))*var.get('h'))*var.get('h'))*var.get('h'))/Js(120.0))))
        var.put('f', (PyJs_LONG_35_()+Js(500000.0)))
        def PyJs_LONG_37_(var=var):
            def PyJs_LONG_36_(var=var):
                return ((((var.get('h')*var.get('h'))/Js(2.0))+((((((((Js(5.0)-var.get('i'))+(Js(9.0)*var.get('a')))+((Js(4.0)*var.get('a'))*var.get('a')))*var.get('h'))*var.get('h'))*var.get('h'))*var.get('h'))/Js(24.0)))+(((((((((((Js(61.0)-(Js(58.0)*var.get('i')))+(var.get('i')*var.get('i')))+(Js(600.0)*var.get('a')))-Js(2.2240339282485886))*var.get('h'))*var.get('h'))*var.get('h'))*var.get('h'))*var.get('h'))*var.get('h'))/Js(720.0)))
            return (var.put('e', (var.get('M')*((((Js(0.9983242984503243)*var.get('c'))-(Js(0.002514607064228144)*var.get('Math').callprop('sin', (Js(2.0)*var.get('c')))))+(Js(2.639046602129982e-06)*var.get('Math').callprop('sin', (Js(4.0)*var.get('c')))))-(Js(3.418046101696858e-09)*var.get('Math').callprop('sin', (Js(6.0)*var.get('c')))))))+((var.get('s')*var.get('Math').callprop('tan', var.get('c')))*PyJs_LONG_36_()))
        var.put('m', (Js(0.9996)*PyJs_LONG_37_()))
        return PyJsComma(((var.get('o')<Js(0.0)) and var.put('m', Js(10000000.0), '+')),Js({'northing':var.get('Math').callprop('round', var.get('m')),'easting':var.get('Math').callprop('round', var.get('f')),'zoneNumber':var.get('r'),'zoneLetter':var.get('L')(var.get('o'))}))
    PyJsHoisted_j_.func_name = 'j'
    var.put('j', PyJsHoisted_j_)
    @Js
    def PyJsHoisted_z_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 'n', 'e', 's', 'p', 'r', 't', 'M', 'c', 'h', 'i', 'y', 'x', 'm', 'v', 'd', 'l', 'o', 'f', '_', 'a'])
        var.put('s', var.get('t').get('northing'))
        var.put('i', var.get('t').get('easting'))
        var.put('a', var.get('t').get('zoneLetter'))
        var.put('h', var.get('t').get('zoneNumber'))
        if ((var.get('h')<Js(0.0)) or (var.get('h')>Js(60.0))):
            return var.get(u"null")
        var.put('f', Js(6378137.0))
        var.put('m', ((Js(1.0)-var.get('Math').callprop('sqrt', Js(0.99330562)))/(Js(1.0)+var.get('Math').callprop('sqrt', Js(0.99330562)))))
        var.put('p', (var.get('i')-Js(500000.0)))
        var.put('d', var.get('s'))
        def PyJs_LONG_39_(var=var):
            def PyJs_LONG_38_(var=var):
                return ((var.put('c', ((var.get('d')/Js(0.9996))/Js(6367449.145945056)))+((((Js(3.0)*var.get('m'))/Js(2.0))-((((Js(27.0)*var.get('m'))*var.get('m'))*var.get('m'))/Js(32.0)))*var.get('Math').callprop('sin', (Js(2.0)*var.get('c')))))+(((((Js(21.0)*var.get('m'))*var.get('m'))/Js(16.0))-(((((Js(55.0)*var.get('m'))*var.get('m'))*var.get('m'))*var.get('m'))/Js(32.0)))*var.get('Math').callprop('sin', (Js(4.0)*var.get('c')))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get('a')<Js('N')) and var.put('d', Js(10000000.0), '-')),var.put('M', (((Js(6.0)*(var.get('h')-Js(1.0)))-Js(180.0))+Js(3.0)))),var.put('u', (PyJs_LONG_38_()+(((((Js(151.0)*var.get('m'))*var.get('m'))*var.get('m'))/Js(96.0))*var.get('Math').callprop('sin', (Js(6.0)*var.get('c'))))))),var.put('e', (var.get('f')/var.get('Math').callprop('sqrt', (Js(1.0)-((Js(0.00669438)*var.get('Math').callprop('sin', var.get('u')))*var.get('Math').callprop('sin', var.get('u')))))))),var.put('n', (var.get('Math').callprop('tan', var.get('u'))*var.get('Math').callprop('tan', var.get('u'))))),var.put('r', ((Js(0.006739496752268451)*var.get('Math').callprop('cos', var.get('u')))*var.get('Math').callprop('cos', var.get('u'))))),var.put('o', ((Js(0.99330562)*var.get('f'))/var.get('Math').callprop('pow', (Js(1.0)-((Js(0.00669438)*var.get('Math').callprop('sin', var.get('u')))*var.get('Math').callprop('sin', var.get('u')))), Js(1.5))))),var.put('l', (var.get('p')/(Js(0.9996)*var.get('e')))))
        PyJs_LONG_39_()
        def PyJs_LONG_40_(var=var):
            return ((((var.get('l')*var.get('l'))/Js(2.0))-(((((((((Js(5.0)+(Js(3.0)*var.get('n')))+(Js(10.0)*var.get('r')))-((Js(4.0)*var.get('r'))*var.get('r')))-Js(0.06065547077041606))*var.get('l'))*var.get('l'))*var.get('l'))*var.get('l'))/Js(24.0)))+((((((((((((Js(61.0)+(Js(90.0)*var.get('n')))+(Js(298.0)*var.get('r')))+((Js(45.0)*var.get('n'))*var.get('n')))-Js(1.6983531815716497))-((Js(3.0)*var.get('r'))*var.get('r')))*var.get('l'))*var.get('l'))*var.get('l'))*var.get('l'))*var.get('l'))*var.get('l'))/Js(720.0)))
        var.put('y', (var.get('u')-(((var.get('e')*var.get('Math').callprop('tan', var.get('u')))/var.get('o'))*PyJs_LONG_40_())))
        var.put('y', var.get('T')(var.get('y')))
        def PyJs_LONG_41_(var=var):
            return (((var.get('l')-((((((Js(1.0)+(Js(2.0)*var.get('n')))+var.get('r'))*var.get('l'))*var.get('l'))*var.get('l'))/Js(6.0)))+(((((((((((Js(5.0)-(Js(2.0)*var.get('r')))+(Js(28.0)*var.get('n')))-((Js(3.0)*var.get('r'))*var.get('r')))+Js(0.05391597401814761))+((Js(24.0)*var.get('n'))*var.get('n')))*var.get('l'))*var.get('l'))*var.get('l'))*var.get('l'))*var.get('l'))/Js(120.0)))/var.get('Math').callprop('cos', var.get('u')))
        var.put('_', PyJs_LONG_41_())
        var.put('_', (var.get('M')+var.get('T')(var.get('_'))))
        pass
        if var.get('t').get('accuracy'):
            var.put('v', var.get('z')(Js({'northing':(var.get('t').get('northing')+var.get('t').get('accuracy')),'easting':(var.get('t').get('easting')+var.get('t').get('accuracy')),'zoneLetter':var.get('t').get('zoneLetter'),'zoneNumber':var.get('t').get('zoneNumber')})))
            var.put('x', Js({'top':var.get('v').get('lat'),'right':var.get('v').get('lon'),'bottom':var.get('y'),'left':var.get('_')}))
        else:
            var.put('x', Js({'lat':var.get('y'),'lon':var.get('_')}))
        return var.get('x')
    PyJsHoisted_z_.func_name = 'z'
    var.put('z', PyJsHoisted_z_)
    @Js
    def PyJsHoisted_L_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', Js('Z'))
        def PyJs_LONG_45_(var=var):
            def PyJs_LONG_44_(var=var):
                def PyJs_LONG_43_(var=var):
                    def PyJs_LONG_42_(var=var):
                        return (var.put('s', Js('G')) if (((-Js(40.0))>var.get('t')) and (var.get('t')>=(-Js(48.0)))) else (var.put('s', Js('F')) if (((-Js(48.0))>var.get('t')) and (var.get('t')>=(-Js(56.0)))) else (var.put('s', Js('E')) if (((-Js(56.0))>var.get('t')) and (var.get('t')>=(-Js(64.0)))) else (var.put('s', Js('D')) if (((-Js(64.0))>var.get('t')) and (var.get('t')>=(-Js(72.0)))) else ((((-Js(72.0))>var.get('t')) and (var.get('t')>=(-Js(80.0)))) and var.put('s', Js('C')))))))
                    return (var.put('s', Js('M')) if ((Js(0.0)>var.get('t')) and (var.get('t')>=(-Js(8.0)))) else (var.put('s', Js('L')) if (((-Js(8.0))>var.get('t')) and (var.get('t')>=(-Js(16.0)))) else (var.put('s', Js('K')) if (((-Js(16.0))>var.get('t')) and (var.get('t')>=(-Js(24.0)))) else (var.put('s', Js('J')) if (((-Js(24.0))>var.get('t')) and (var.get('t')>=(-Js(32.0)))) else (var.put('s', Js('H')) if (((-Js(32.0))>var.get('t')) and (var.get('t')>=(-Js(40.0)))) else PyJs_LONG_42_())))))
                return (var.put('s', Js('S')) if ((Js(40.0)>var.get('t')) and (var.get('t')>=Js(32.0))) else (var.put('s', Js('R')) if ((Js(32.0)>var.get('t')) and (var.get('t')>=Js(24.0))) else (var.put('s', Js('Q')) if ((Js(24.0)>var.get('t')) and (var.get('t')>=Js(16.0))) else (var.put('s', Js('P')) if ((Js(16.0)>var.get('t')) and (var.get('t')>=Js(8.0))) else (var.put('s', Js('N')) if ((Js(8.0)>var.get('t')) and (var.get('t')>=Js(0.0))) else PyJs_LONG_43_())))))
            return (var.put('s', Js('X')) if ((Js(84.0)>=var.get('t')) and (var.get('t')>=Js(72.0))) else (var.put('s', Js('W')) if ((Js(72.0)>var.get('t')) and (var.get('t')>=Js(64.0))) else (var.put('s', Js('V')) if ((Js(64.0)>var.get('t')) and (var.get('t')>=Js(56.0))) else (var.put('s', Js('U')) if ((Js(56.0)>var.get('t')) and (var.get('t')>=Js(48.0))) else (var.put('s', Js('T')) if ((Js(48.0)>var.get('t')) and (var.get('t')>=Js(40.0))) else PyJs_LONG_44_())))))
        return PyJsComma(PyJs_LONG_45_(),var.get('s'))
    PyJsHoisted_L_.func_name = 'L'
    var.put('L', PyJsHoisted_L_)
    @Js
    def PyJsHoisted_D_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        var.put('i', (Js('00000')+var.get('t').get('easting')))
        var.put('a', (Js('00000')+var.get('t').get('northing')))
        return ((((var.get('t').get('zoneNumber')+var.get('t').get('zoneLetter'))+var.get('B')(var.get('t').get('easting'), var.get('t').get('northing'), var.get('t').get('zoneNumber')))+var.get('i').callprop('substr', (var.get('i').get('length')-Js(5.0)), var.get('s')))+var.get('a').callprop('substr', (var.get('a').get('length')-Js(5.0)), var.get('s')))
    PyJsHoisted_D_.func_name = 'D'
    var.put('D', PyJsHoisted_D_)
    @Js
    def PyJsHoisted_B_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        var.put('a', var.get('U')(var.get('i')))
        return var.get('F')(var.get('Math').callprop('floor', (var.get('t')/Js(100000.0))), (var.get('Math').callprop('floor', (var.get('s')/Js(100000.0)))%Js(20.0)), var.get('a'))
    PyJsHoisted_B_.func_name = 'B'
    var.put('B', PyJsHoisted_B_)
    @Js
    def PyJsHoisted_U_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', (var.get('t')%var.get('Ht')))
        return PyJsComma((PyJsStrictEq(Js(0.0),var.get('s')) and var.put('s', var.get('Ht'))),var.get('s'))
    PyJsHoisted_U_.func_name = 'U'
    var.put('U', PyJsHoisted_U_)
    @Js
    def PyJsHoisted_F_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('a', (var.get('i')-Js(1.0)))
        var.put('h', var.get('Xt').callprop('charCodeAt', var.get('a')))
        var.put('e', var.get('Kt').callprop('charCodeAt', var.get('a')))
        var.put('n', ((var.get('h')+var.get('t'))-Js(1.0)))
        var.put('r', (var.get('e')+var.get('s')))
        var.put('o', Js(1.0).neg())
        def PyJs_LONG_46_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get('n')>var.get('$t')) and PyJsComma(var.put('n', (((var.get('n')-var.get('$t'))+var.get('Jt'))-Js(1.0))),var.put('o', Js(0.0).neg()))),(((PyJsStrictEq(var.get('n'),var.get('Vt')) or ((var.get('h')<var.get('Vt')) and (var.get('n')>var.get('Vt')))) or (((var.get('n')>var.get('Vt')) or (var.get('h')<var.get('Vt'))) and var.get('o'))) and (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)))),((((PyJsStrictEq(var.get('n'),var.get('Zt')) or ((var.get('h')<var.get('Zt')) and (var.get('n')>var.get('Zt')))) or (((var.get('n')>var.get('Zt')) or (var.get('h')<var.get('Zt'))) and var.get('o'))) and PyJsStrictEq(var.put('n',Js(var.get('n').to_number())+Js(1)),var.get('Vt'))) and (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)))),((var.get('n')>var.get('$t')) and var.put('n', (((var.get('n')-var.get('$t'))+var.get('Jt'))-Js(1.0))))),(PyJsComma(var.put('r', (((var.get('r')-var.get('Yt'))+var.get('Jt'))-Js(1.0))),var.put('o', Js(0.0).neg())) if (var.get('r')>var.get('Yt')) else var.put('o', Js(1.0).neg()))),(((PyJsStrictEq(var.get('r'),var.get('Vt')) or ((var.get('e')<var.get('Vt')) and (var.get('r')>var.get('Vt')))) or (((var.get('r')>var.get('Vt')) or (var.get('e')<var.get('Vt'))) and var.get('o'))) and (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1)))),((((PyJsStrictEq(var.get('r'),var.get('Zt')) or ((var.get('e')<var.get('Zt')) and (var.get('r')>var.get('Zt')))) or (((var.get('r')>var.get('Zt')) or (var.get('e')<var.get('Zt'))) and var.get('o'))) and PyJsStrictEq(var.put('r',Js(var.get('r').to_number())+Js(1)),var.get('Vt'))) and (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1)))),((var.get('r')>var.get('Yt')) and var.put('r', (((var.get('r')-var.get('Yt'))+var.get('Jt'))-Js(1.0))))),(var.get('String').callprop('fromCharCode', var.get('n'))+var.get('String').callprop('fromCharCode', var.get('r'))))
        return PyJs_LONG_46_()
    PyJsHoisted_F_.func_name = 'F'
    var.put('F', PyJsHoisted_F_)
    @Js
    def PyJsHoisted_Q_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'd', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 'y', 'x', 's', 'r', 'f', '_', 'a'])
        if (var.get('t') and PyJsStrictEq(Js(0.0),var.get('t').get('length'))):
            PyJsTempException = JsToPyException(Js('MGRSPoint coverting from nothing'))
            raise PyJsTempException
        #for JS loop
        var.put('i', var.get('t').get('length'))
        var.put('a', var.get(u"null"))
        var.put('h', Js(''))
        var.put('e', Js(0.0))
        while JsRegExp('/[A-Z]/').callprop('test', var.put('s', var.get('t').callprop('charAt', var.get('e')))).neg():
            if (var.get('e')>=Js(2.0)):
                PyJsTempException = JsToPyException((Js('MGRSPoint bad conversion from: ')+var.get('t')))
                raise PyJsTempException
            PyJsComma(var.put('h', var.get('s'), '+'),(var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1)))
        
        var.put('n', var.get('parseInt')(var.get('h'), Js(10.0)))
        if (PyJsStrictEq(Js(0.0),var.get('e')) or ((var.get('e')+Js(3.0))>var.get('i'))):
            PyJsTempException = JsToPyException((Js('MGRSPoint bad conversion from: ')+var.get('t')))
            raise PyJsTempException
        var.put('r', var.get('t').callprop('charAt', (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))))
        if ((((((var.get('r')<=Js('A')) or PyJsStrictEq(Js('B'),var.get('r'))) or PyJsStrictEq(Js('Y'),var.get('r'))) or (var.get('r')>=Js('Z'))) or PyJsStrictEq(Js('I'),var.get('r'))) or PyJsStrictEq(Js('O'),var.get('r'))):
            PyJsTempException = JsToPyException((((Js('MGRSPoint zone letter ')+var.get('r'))+Js(' not handled: '))+var.get('t')))
            raise PyJsTempException
        var.put('a', var.get('t').callprop('substring', var.get('e'), var.put('e', Js(2.0), '+')))
        #for JS loop
        var.put('o', var.get('U')(var.get('n')))
        var.put('l', var.get('W')(var.get('a').callprop('charAt', Js(0.0)), var.get('o')))
        var.put('M', var.get('H')(var.get('a').callprop('charAt', Js(1.0)), var.get('o')))
        while (var.get('M')<var.get('X')(var.get('r'))):
            var.put('M', Js(2000000.0), '+')
        
        var.put('c', (var.get('i')-var.get('e')))
        if ((var.get('c')%Js(2.0))!=Js(0.0)):
            PyJsTempException = JsToPyException((Js('MGRSPoint has to have an even number \nof digits after the zone letter and two 100km letters - front \nhalf for easting meters, second half for \nnorthing meters')+var.get('t')))
            raise PyJsTempException
        var.put('y', (var.get('c')/Js(2.0)))
        var.put('_', Js(0.0))
        var.put('x', Js(0.0))
        def PyJs_LONG_47_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('u', (Js(100000.0)/var.get('Math').callprop('pow', Js(10.0), var.get('y')))),var.put('f', var.get('t').callprop('substring', var.get('e'), (var.get('e')+var.get('y'))))),var.put('_', (var.get('parseFloat')(var.get('f'))*var.get('u')))),var.put('m', var.get('t').callprop('substring', (var.get('e')+var.get('y'))))),var.put('x', (var.get('parseFloat')(var.get('m'))*var.get('u'))))
        return PyJsComma(PyJsComma(PyJsComma(((var.get('y')>Js(0.0)) and PyJs_LONG_47_()),var.put('p', (var.get('_')+var.get('l')))),var.put('d', (var.get('x')+var.get('M')))),Js({'easting':var.get('p'),'northing':var.get('d'),'zoneLetter':var.get('r'),'zoneNumber':var.get('n'),'accuracy':var.get('u')}))
    PyJsHoisted_Q_.func_name = 'Q'
    var.put('Q', PyJsHoisted_Q_)
    @Js
    def PyJsHoisted_W_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        #for JS loop
        var.put('i', var.get('Xt').callprop('charCodeAt', (var.get('s')-Js(1.0))))
        var.put('a', Js(100000.0))
        var.put('h', Js(1.0).neg())
        while PyJsStrictNeq(var.get('i'),var.get('t').callprop('charCodeAt', Js(0.0))):
            if PyJsComma(PyJsComma((PyJsStrictEq(var.put('i',Js(var.get('i').to_number())+Js(1)),var.get('Vt')) and (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))),(PyJsStrictEq(var.get('i'),var.get('Zt')) and (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))),(var.get('i')>var.get('$t'))):
                if var.get('h'):
                    PyJsTempException = JsToPyException((Js('Bad character: ')+var.get('t')))
                    raise PyJsTempException
                PyJsComma(var.put('i', var.get('Jt')),var.put('h', Js(0.0).neg()))
            var.put('a', Js(100000.0), '+')
        
        return var.get('a')
    PyJsHoisted_W_.func_name = 'W'
    var.put('W', PyJsHoisted_W_)
    @Js
    def PyJsHoisted_H_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        if (var.get('t')>Js('V')):
            PyJsTempException = JsToPyException((Js('MGRSPoint given invalid Northing ')+var.get('t')))
            raise PyJsTempException
        #for JS loop
        var.put('i', var.get('Kt').callprop('charCodeAt', (var.get('s')-Js(1.0))))
        var.put('a', Js(0.0))
        var.put('h', Js(1.0).neg())
        while PyJsStrictNeq(var.get('i'),var.get('t').callprop('charCodeAt', Js(0.0))):
            if PyJsComma(PyJsComma((PyJsStrictEq(var.put('i',Js(var.get('i').to_number())+Js(1)),var.get('Vt')) and (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))),(PyJsStrictEq(var.get('i'),var.get('Zt')) and (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))),(var.get('i')>var.get('Yt'))):
                if var.get('h'):
                    PyJsTempException = JsToPyException((Js('Bad character: ')+var.get('t')))
                    raise PyJsTempException
                PyJsComma(var.put('i', var.get('Jt')),var.put('h', Js(0.0).neg()))
            var.put('a', Js(100000.0), '+')
        
        return var.get('a')
    PyJsHoisted_H_.func_name = 'H'
    var.put('H', PyJsHoisted_H_)
    @Js
    def PyJsHoisted_X_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        pass
        while 1:
            SWITCHED = False
            CONDITION = (var.get('t'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js('C')):
                SWITCHED = True
                var.put('s', Js(1100000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('D')):
                SWITCHED = True
                var.put('s', Js(2000000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('E')):
                SWITCHED = True
                var.put('s', Js(2800000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('F')):
                SWITCHED = True
                var.put('s', Js(3700000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('G')):
                SWITCHED = True
                var.put('s', Js(4600000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('H')):
                SWITCHED = True
                var.put('s', Js(5500000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('J')):
                SWITCHED = True
                var.put('s', Js(6400000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('K')):
                SWITCHED = True
                var.put('s', Js(7300000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('L')):
                SWITCHED = True
                var.put('s', Js(8200000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('M')):
                SWITCHED = True
                var.put('s', Js(9100000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('N')):
                SWITCHED = True
                var.put('s', Js(0.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('P')):
                SWITCHED = True
                var.put('s', Js(800000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('Q')):
                SWITCHED = True
                var.put('s', Js(1700000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('R')):
                SWITCHED = True
                var.put('s', Js(2600000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('S')):
                SWITCHED = True
                var.put('s', Js(3500000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('T')):
                SWITCHED = True
                var.put('s', Js(4400000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('U')):
                SWITCHED = True
                var.put('s', Js(5300000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('V')):
                SWITCHED = True
                var.put('s', Js(6200000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('W')):
                SWITCHED = True
                var.put('s', Js(7000000.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('X')):
                SWITCHED = True
                var.put('s', Js(7900000.0))
                break
            if True:
                SWITCHED = True
                var.put('s', (-Js(1.0)))
            SWITCHED = True
            break
        if (var.get('s')>=Js(0.0)):
            return var.get('s')
        PyJsTempException = JsToPyException((Js('Invalid zone letter: ')+var.get('t')))
        raise PyJsTempException
    PyJsHoisted_X_.func_name = 'X'
    var.put('X', PyJsHoisted_X_)
    @Js
    def PyJsHoisted_Point_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        if var.get(u"this").instanceof(var.get('Point')).neg():
            return var.get('Point').create(var.get('t'), var.get('s'), var.get('i'))
        if var.get('Array').callprop('isArray', var.get('t')):
            PyJsComma(PyJsComma(var.get(u"this").put('x', var.get('t').get('0')),var.get(u"this").put('y', var.get('t').get('1'))),var.get(u"this").put('z', (var.get('t').get('2') or Js(0.0))))
        else:
            if (Js('object')==var.get('t',throw=False).typeof()):
                PyJsComma(PyJsComma(var.get(u"this").put('x', var.get('t').get('x')),var.get(u"this").put('y', var.get('t').get('y'))),var.get(u"this").put('z', (var.get('t').get('z') or Js(0.0))))
            else:
                if ((Js('string')==var.get('t',throw=False).typeof()) and PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('s'))):
                    var.put('a', var.get('t').callprop('split', Js(',')))
                    PyJsComma(PyJsComma(var.get(u"this").put('x', var.get('parseFloat')(var.get('a').get('0'), Js(10.0))),var.get(u"this").put('y', var.get('parseFloat')(var.get('a').get('1'), Js(10.0)))),var.get(u"this").put('z', (var.get('parseFloat')(var.get('a').get('2'), Js(10.0)) or Js(0.0))))
                else:
                    PyJsComma(PyJsComma(var.get(u"this").put('x', var.get('t')),var.get(u"this").put('y', var.get('s'))),var.get(u"this").put('z', (var.get('i') or Js(0.0))))
        var.get('console').callprop('warn', Js('proj4.Point will be removed in version 3, use proj4.toPoint'))
    PyJsHoisted_Point_.func_name = 'Point'
    var.put('Point', PyJsHoisted_Point_)
    @Js
    def PyJsHoisted_K_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('i', Js([]))
        def PyJs_LONG_48_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('i').put('0', (var.get('t')*var.get('Ts'))),var.put('s', (var.get('t')*var.get('t')))),var.get('i').put('0', (var.get('s')*var.get('js')), '+')),var.get('i').put('1', (var.get('s')*var.get('Ls')))),var.put('s', var.get('t'), '*')),var.get('i').put('0', (var.get('s')*var.get('zs')), '+')),var.get('i').put('1', (var.get('s')*var.get('Ds')), '+')),var.get('i').put('2', (var.get('s')*var.get('Bs')))),var.get('i'))
        return PyJs_LONG_48_()
    PyJsHoisted_K_.func_name = 'K'
    var.put('K', PyJsHoisted_K_)
    @Js
    def PyJsHoisted_J_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('i', (var.get('t')+var.get('t')))
        return (((var.get('t')+(var.get('s').get('0')*var.get('Math').callprop('sin', var.get('i'))))+(var.get('s').get('1')*var.get('Math').callprop('sin', (var.get('i')+var.get('i')))))+(var.get('s').get('2')*var.get('Math').callprop('sin', ((var.get('i')+var.get('i'))+var.get('i')))))
    PyJsHoisted_J_.func_name = 'J'
    var.put('J', PyJsHoisted_J_)
    @Js
    def PyJsHoisted_V_(t, s, i, a, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_49_(var=var):
            return (PyJsComma(var.get('a').put('value', var.get('ri').get('AREA_1')),var.put('h', var.get('ht'), '-')) if ((var.get('h')>var.get('ct')) and (var.get('h')<=(var.get('ht')+var.get('ct')))) else (PyJsComma(var.get('a').put('value', var.get('ri').get('AREA_2')),var.put('h', ((var.get('h')-var.get('ft')) if (var.get('h')>=Js(0.0)) else (var.get('h')+var.get('ft'))))) if ((var.get('h')>(var.get('ht')+var.get('ct'))) or (var.get('h')<=(-(var.get('ht')+var.get('ct'))))) else PyJsComma(var.get('a').put('value', var.get('ri').get('AREA_3')),var.put('h', var.get('ht'), '+'))))
        return PyJsComma((PyJsComma(var.get('a').put('value', var.get('ri').get('AREA_0')),var.put('h', Js(0.0))) if (var.get('t')<var.get('ot')) else PyJsComma(var.put('h', var.get('Math').callprop('atan2', var.get('s'), var.get('i'))),(var.get('a').put('value', var.get('ri').get('AREA_0')) if (var.get('Math').callprop('abs', var.get('h'))<=var.get('ct')) else PyJs_LONG_49_()))),var.get('h'))
    PyJsHoisted_V_.func_name = 'V'
    var.put('V', PyJsHoisted_V_)
    @Js
    def PyJsHoisted_Z_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('i', (var.get('t')+var.get('s')))
        return PyJsComma((var.put('i', var.get('ut'), '+') if (var.get('i')<(-var.get('ft'))) else ((var.get('i')>(+var.get('ft'))) and var.put('i', var.get('ut'), '-'))),var.get('i'))
    PyJsHoisted_Z_.func_name = 'Z'
    var.put('Z', PyJsHoisted_Z_)
    @Js
    def PyJsHoisted_Y_(t, s, i, a, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'e', 'i', 's', 't', 'a'])
        #for JS loop
        var.put('h', var.get('s'))
        while var.get('a'):
            try:
                var.put('e', var.get('t')(var.get('h')))
                if PyJsComma(var.put('h', var.get('e'), '-'),(var.get('Math').callprop('abs', var.get('e'))<var.get('i'))):
                    break
            finally:
                    var.put('a',Js(var.get('a').to_number())-Js(1))
        return var.get('h')
    PyJsHoisted_Y_.func_name = 'Y'
    var.put('Y', PyJsHoisted_Y_)
    Js('use strict')
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put('$', Js(1.0))
    var.put('tt', Js(2.0))
    var.put('st', Js(4.0))
    var.put('it', Js(5.0))
    var.put('at', Js(4.84813681109536e-06))
    var.put('ht', (var.get('Math').get('PI')/Js(2.0)))
    var.put('et', Js(0.16666666666666666))
    var.put('nt', Js(0.04722222222222222))
    var.put('rt', Js(0.022156084656084655))
    var.put('ot', Js(1e-10))
    var.put('lt', Js(0.017453292519943295))
    var.put('Mt', Js(57.29577951308232))
    var.put('ct', (var.get('Math').get('PI')/Js(4.0)))
    var.put('ut', (Js(2.0)*var.get('Math').get('PI')))
    var.put('ft', Js(3.14159265359))
    var.put('mt', Js({}))
    def PyJs_LONG_50_(var=var):
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('mt').put('greenwich', Js(0.0)),var.get('mt').put('lisbon', (-Js(9.131906111111)))),var.get('mt').put('paris', Js(2.337229166667))),var.get('mt').put('bogota', (-Js(74.080916666667)))),var.get('mt').put('madrid', (-Js(3.687938888889)))),var.get('mt').put('rome', Js(12.452333333333))),var.get('mt').put('bern', Js(7.439583333333))),var.get('mt').put('jakarta', Js(106.807719444444))),var.get('mt').put('ferro', (-Js(17.666666666667)))),var.get('mt').put('brussels', Js(4.367975))),var.get('mt').put('stockholm', Js(18.058277777778))),var.get('mt').put('athens', Js(23.7163375))),var.get('mt').put('oslo', Js(10.722916666667)))
    PyJs_LONG_50_()
    var.put('pt', Js({'ft':Js({'to_meter':Js(0.3048)}),'us-ft':Js({'to_meter':(Js(1200.0)/Js(3937.0))})}))
    var.put('dt', JsRegExp('/[\\s_\\-\\/\\(\\)]/g'))
    @Js
    def PyJs_anonymous_51_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 'a'])
        var.put('e', Js({}))
        @Js
        def PyJs_anonymous_52_(t, s, this, arguments, var=var):
            var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'i', 's'])
            var.put('i', var.get('s').callprop('split', Js('=')))
            return PyJsComma(PyJsComma(var.get('i').callprop('push', Js(0.0).neg()),var.get('t').put(var.get('i').get('0').callprop('toLowerCase'), var.get('i').get('1'))),var.get('t'))
        PyJs_anonymous_52_._set_name('anonymous')
        @Js
        def PyJs_anonymous_53_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            return var.get('t')
        PyJs_anonymous_53_._set_name('anonymous')
        @Js
        def PyJs_anonymous_54_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            return var.get('t').callprop('trim')
        PyJs_anonymous_54_._set_name('anonymous')
        var.put('n', var.get('s').callprop('split', Js('+')).callprop('map', PyJs_anonymous_54_).callprop('filter', PyJs_anonymous_53_).callprop('reduce', PyJs_anonymous_52_, Js({})))
        @Js
        def PyJs_anonymous_55_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('rf', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_55_._set_name('anonymous')
        @Js
        def PyJs_anonymous_56_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('lat0', (var.get('t')*var.get('lt')))
        PyJs_anonymous_56_._set_name('anonymous')
        @Js
        def PyJs_anonymous_57_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('lat1', (var.get('t')*var.get('lt')))
        PyJs_anonymous_57_._set_name('anonymous')
        @Js
        def PyJs_anonymous_58_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('lat2', (var.get('t')*var.get('lt')))
        PyJs_anonymous_58_._set_name('anonymous')
        @Js
        def PyJs_anonymous_59_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('lat_ts', (var.get('t')*var.get('lt')))
        PyJs_anonymous_59_._set_name('anonymous')
        @Js
        def PyJs_anonymous_60_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('long0', (var.get('t')*var.get('lt')))
        PyJs_anonymous_60_._set_name('anonymous')
        @Js
        def PyJs_anonymous_61_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('long1', (var.get('t')*var.get('lt')))
        PyJs_anonymous_61_._set_name('anonymous')
        @Js
        def PyJs_anonymous_62_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('long2', (var.get('t')*var.get('lt')))
        PyJs_anonymous_62_._set_name('anonymous')
        @Js
        def PyJs_anonymous_63_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('alpha', (var.get('parseFloat')(var.get('t'))*var.get('lt')))
        PyJs_anonymous_63_._set_name('anonymous')
        @Js
        def PyJs_anonymous_64_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('longc', (var.get('t')*var.get('lt')))
        PyJs_anonymous_64_._set_name('anonymous')
        @Js
        def PyJs_anonymous_65_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('x0', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_65_._set_name('anonymous')
        @Js
        def PyJs_anonymous_66_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('y0', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_66_._set_name('anonymous')
        @Js
        def PyJs_anonymous_67_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('k0', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_67_._set_name('anonymous')
        @Js
        def PyJs_anonymous_68_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('k0', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_68_._set_name('anonymous')
        @Js
        def PyJs_anonymous_69_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('a', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_69_._set_name('anonymous')
        @Js
        def PyJs_anonymous_70_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('b', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_70_._set_name('anonymous')
        @Js
        def PyJs_anonymous_71_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get('e').put('R_A', Js(0.0).neg())
        PyJs_anonymous_71_._set_name('anonymous')
        @Js
        def PyJs_anonymous_72_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('zone', var.get('parseInt')(var.get('t'), Js(10.0)))
        PyJs_anonymous_72_._set_name('anonymous')
        @Js
        def PyJs_anonymous_73_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get('e').put('utmSouth', Js(0.0).neg())
        PyJs_anonymous_73_._set_name('anonymous')
        @Js
        def PyJs_anonymous_74_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            @Js
            def PyJs_anonymous_75_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['t'])
                return var.get('parseFloat')(var.get('t'))
            PyJs_anonymous_75_._set_name('anonymous')
            var.get('e').put('datum_params', var.get('t').callprop('split', Js(',')).callprop('map', PyJs_anonymous_75_))
        PyJs_anonymous_74_._set_name('anonymous')
        @Js
        def PyJs_anonymous_76_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('to_meter', var.get('parseFloat')(var.get('t')))
        PyJs_anonymous_76_._set_name('anonymous')
        @Js
        def PyJs_anonymous_77_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 's'])
            var.get('e').put('units', var.get('s'))
            var.put('i', var.get('t')(var.get('pt'), var.get('s')))
            (var.get('i') and var.get('e').put('to_meter', var.get('i').get('to_meter')))
        PyJs_anonymous_77_._set_name('anonymous')
        @Js
        def PyJs_anonymous_78_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.get('e').put('from_greenwich', (var.get('t')*var.get('lt')))
        PyJs_anonymous_78_._set_name('anonymous')
        @Js
        def PyJs_anonymous_79_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 's'])
            var.put('i', var.get('t')(var.get('mt'), var.get('s')))
            var.get('e').put('from_greenwich', ((var.get('i') or var.get('parseFloat')(var.get('s')))*var.get('lt')))
        PyJs_anonymous_79_._set_name('anonymous')
        @Js
        def PyJs_anonymous_80_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            (var.get('e').put('datumCode', Js('none')) if PyJsStrictEq(Js('@null'),var.get('t')) else var.get('e').put('nadgrids', var.get('t')))
        PyJs_anonymous_80_._set_name('anonymous')
        @Js
        def PyJs_anonymous_81_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            def PyJs_LONG_82_(var=var):
                return ((((PyJsStrictEq(Js(3.0),var.get('t').get('length')) and PyJsStrictNeq((-Js(1.0)),Js('ewnsud').callprop('indexOf', var.get('t').callprop('substr', Js(0.0), Js(1.0))))) and PyJsStrictNeq((-Js(1.0)),Js('ewnsud').callprop('indexOf', var.get('t').callprop('substr', Js(1.0), Js(1.0))))) and PyJsStrictNeq((-Js(1.0)),Js('ewnsud').callprop('indexOf', var.get('t').callprop('substr', Js(2.0), Js(1.0))))) and var.get('e').put('axis', var.get('t')))
            PyJs_LONG_82_()
        PyJs_anonymous_81_._set_name('anonymous')
        var.put('r', Js({'proj':Js('projName'),'datum':Js('datumCode'),'rf':PyJs_anonymous_55_,'lat_0':PyJs_anonymous_56_,'lat_1':PyJs_anonymous_57_,'lat_2':PyJs_anonymous_58_,'lat_ts':PyJs_anonymous_59_,'lon_0':PyJs_anonymous_60_,'lon_1':PyJs_anonymous_61_,'lon_2':PyJs_anonymous_62_,'alpha':PyJs_anonymous_63_,'lonc':PyJs_anonymous_64_,'x_0':PyJs_anonymous_65_,'y_0':PyJs_anonymous_66_,'k_0':PyJs_anonymous_67_,'k':PyJs_anonymous_68_,'a':PyJs_anonymous_69_,'b':PyJs_anonymous_70_,'r_a':PyJs_anonymous_71_,'zone':PyJs_anonymous_72_,'south':PyJs_anonymous_73_,'towgs84':PyJs_anonymous_74_,'to_meter':PyJs_anonymous_76_,'units':PyJs_anonymous_77_,'from_greenwich':PyJs_anonymous_78_,'pm':PyJs_anonymous_79_,'nadgrids':PyJs_anonymous_80_,'axis':PyJs_anonymous_81_}))
        for PyJsTemp in var.get('n'):
            var.put('i', PyJsTemp)
            PyJsComma(var.put('a', var.get('n').get(var.get('i'))),((var.get('h')(var.get('a')) if (Js('function')==var.put('h', var.get('r').get(var.get('i'))).typeof()) else var.get('e').put(var.get('h'), var.get('a'))) if var.get('r').contains(var.get('i')) else var.get('e').put(var.get('i'), var.get('a'))))
        return PyJsComma((((Js('string')==var.get('e').get('datumCode').typeof()) and PyJsStrictNeq(Js('WGS84'),var.get('e').get('datumCode'))) and var.get('e').put('datumCode', var.get('e').get('datumCode').callprop('toLowerCase'))),var.get('e'))
    PyJs_anonymous_51_._set_name('anonymous')
    var.put('yt', PyJs_anonymous_51_)
    var.put('_t', Js(1.0))
    var.put('xt', JsRegExp('/\\s/'))
    var.put('vt', JsRegExp('/[A-Za-z]/'))
    var.put('gt', JsRegExp('/[A-Za-z84]/'))
    var.put('bt', JsRegExp('/[,\\]]/'))
    var.put('wt', JsRegExp('/[\\d\\.E\\-\\+]/'))
    def PyJs_LONG_94_(var=var):
        @Js
        def PyJs_anonymous_83_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            var.put('t', var.get(u"this").get('text').get((var.get(u"this").put('place',Js(var.get(u"this").get('place').to_number())+Js(1))-Js(1))))
            if PyJsStrictNeq(Js(4.0),var.get(u"this").get('state')):
                #for JS loop
                
                while var.get('xt').callprop('test', var.get('t')):
                    if (var.get(u"this").get('place')>=var.get(u"this").get('text').get('length')):
                        return var.get('undefined')
                    var.put('t', var.get(u"this").get('text').get((var.get(u"this").put('place',Js(var.get(u"this").get('place').to_number())+Js(1))-Js(1))))
                
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u"this").get('state'))
                if SWITCHED or PyJsStrictEq(CONDITION, var.get('_t')):
                    SWITCHED = True
                    return var.get(u"this").callprop('neutral', var.get('t'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get(u"this").callprop('keyword', var.get('t'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    return var.get(u"this").callprop('quoted', var.get('t'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    return var.get(u"this").callprop('afterquote', var.get('t'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get(u"this").callprop('number', var.get('t'))
                if SWITCHED or PyJsStrictEq(CONDITION, (-Js(1.0))):
                    SWITCHED = True
                    return var.get('undefined')
                SWITCHED = True
                break
        PyJs_anonymous_83_._set_name('anonymous')
        @Js
        def PyJs_anonymous_84_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            if PyJsStrictEq(Js('"'),var.get('t')):
                return PyJsComma(var.get(u"this").put('word', Js('"'), '+'),PyJsComma(var.get(u"this").put('state', Js(4.0)), Js(None)))
            if var.get('bt').callprop('test', var.get('t')):
                return PyJsComma(var.get(u"this").put('word', var.get(u"this").get('word').callprop('trim')),PyJsComma(var.get(u"this").callprop('afterItem', var.get('t')), Js(None)))
            PyJsTempException = JsToPyException(var.get('Error').create((((Js('havn\'t handled "')+var.get('t'))+Js('" in afterquote yet, index '))+var.get(u"this").get('place'))))
            raise PyJsTempException
        PyJs_anonymous_84_._set_name('anonymous')
        @Js
        def PyJs_anonymous_85_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            def PyJs_LONG_87_(var=var):
                def PyJs_LONG_86_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get(u"this").put('level',Js(var.get(u"this").get('level').to_number())-Js(1))+Js(1)),(PyJsStrictNeq(var.get(u"null"),var.get(u"this").get('word')) and PyJsComma(var.get(u"this").get('currentObject').callprop('push', var.get(u"this").get('word')),var.get(u"this").put('word', var.get(u"null"))))),var.get(u"this").put('state', var.get('_t'))),var.get(u"this").put('currentObject', var.get(u"this").get('stack').callprop('pop'))),PyJsComma((var.get(u"this").get('currentObject') or var.get(u"this").put('state', (-Js(1.0)))), Js(None)))
                return (PyJsComma(PyJsComma((PyJsStrictNeq(var.get(u"null"),var.get(u"this").get('word')) and var.get(u"this").get('currentObject').callprop('push', var.get(u"this").get('word'))),var.get(u"this").put('word', var.get(u"null"))),PyJsComma(var.get(u"this").put('state', var.get('_t')), Js(None))) if PyJsStrictEq(Js(','),var.get('t')) else (PyJs_LONG_86_() if PyJsStrictEq(Js(']'),var.get('t')) else PyJsComma(Js(0.0), Js(None))))
            return PyJs_LONG_87_()
        PyJs_anonymous_85_._set_name('anonymous')
        @Js
        def PyJs_anonymous_88_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            if var.get('wt').callprop('test', var.get('t')).neg():
                if var.get('bt').callprop('test', var.get('t')):
                    return PyJsComma(var.get(u"this").put('word', var.get('parseFloat')(var.get(u"this").get('word'))),PyJsComma(var.get(u"this").callprop('afterItem', var.get('t')), Js(None)))
                PyJsTempException = JsToPyException(var.get('Error').create((((Js('havn\'t handled "')+var.get('t'))+Js('" in number yet, index '))+var.get(u"this").get('place'))))
                raise PyJsTempException
            var.get(u"this").put('word', var.get('t'), '+')
        PyJs_anonymous_88_._set_name('anonymous')
        @Js
        def PyJs_anonymous_89_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            (var.get(u"this").put('word', var.get('t'), '+') if PyJsStrictNeq(Js('"'),var.get('t')) else var.get(u"this").put('state', Js(5.0)))
        PyJs_anonymous_89_._set_name('anonymous')
        @Js
        def PyJs_anonymous_90_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 's'])
            if var.get('gt').callprop('test', var.get('t')):
                var.get(u"this").put('word', var.get('t'), '+')
            else:
                if PyJsStrictEq(Js('['),var.get('t')):
                    var.put('s', Js([]))
                    def PyJs_LONG_91_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('s').callprop('push', var.get(u"this").get('word')),(var.get(u"this").put('level',Js(var.get(u"this").get('level').to_number())+Js(1))-Js(1))),(var.get(u"this").put('root', var.get('s')) if PyJsStrictEq(var.get(u"null"),var.get(u"this").get('root')) else var.get(u"this").get('currentObject').callprop('push', var.get('s')))),var.get(u"this").get('stack').callprop('push', var.get(u"this").get('currentObject'))),var.get(u"this").put('currentObject', var.get('s'))),PyJsComma(var.get(u"this").put('state', var.get('_t')), Js(None)))
                    return PyJs_LONG_91_()
                if var.get('bt').callprop('test', var.get('t')).neg():
                    PyJsTempException = JsToPyException(var.get('Error').create((((Js('havn\'t handled "')+var.get('t'))+Js('" in keyword yet, index '))+var.get(u"this").get('place'))))
                    raise PyJsTempException
                var.get(u"this").callprop('afterItem', var.get('t'))
        PyJs_anonymous_90_._set_name('anonymous')
        @Js
        def PyJs_anonymous_92_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            if var.get('vt').callprop('test', var.get('t')):
                return PyJsComma(var.get(u"this").put('word', var.get('t')),PyJsComma(var.get(u"this").put('state', Js(2.0)), Js(None)))
            if PyJsStrictEq(Js('"'),var.get('t')):
                return PyJsComma(var.get(u"this").put('word', Js('')),PyJsComma(var.get(u"this").put('state', Js(4.0)), Js(None)))
            if var.get('wt').callprop('test', var.get('t')):
                return PyJsComma(var.get(u"this").put('word', var.get('t')),PyJsComma(var.get(u"this").put('state', Js(3.0)), Js(None)))
            if var.get('bt').callprop('test', var.get('t')).neg():
                PyJsTempException = JsToPyException(var.get('Error').create((((Js('havn\'t handled "')+var.get('t'))+Js('" in neutral yet, index '))+var.get(u"this").get('place'))))
                raise PyJsTempException
            var.get(u"this").callprop('afterItem', var.get('t'))
        PyJs_anonymous_92_._set_name('anonymous')
        @Js
        def PyJs_anonymous_93_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            #for JS loop
            
            while (var.get(u"this").get('place')<var.get(u"this").get('text').get('length')):
                var.get(u"this").callprop('readCharicter')
            
            if PyJsStrictEq((-Js(1.0)),var.get(u"this").get('state')):
                return var.get(u"this").get('root')
            PyJsTempException = JsToPyException(var.get('Error').create((((Js('unable to parse string "')+var.get(u"this").get('text'))+Js('". State is '))+var.get(u"this").get('state'))))
            raise PyJsTempException
        PyJs_anonymous_93_._set_name('anonymous')
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('s').get('prototype').put('readCharicter', PyJs_anonymous_83_),var.get('s').get('prototype').put('afterquote', PyJs_anonymous_84_)),var.get('s').get('prototype').put('afterItem', PyJs_anonymous_85_)),var.get('s').get('prototype').put('number', PyJs_anonymous_88_)),var.get('s').get('prototype').put('quoted', PyJs_anonymous_89_)),var.get('s').get('prototype').put('keyword', PyJs_anonymous_90_)),var.get('s').get('prototype').put('neutral', PyJs_anonymous_92_)),var.get('s').get('prototype').put('output', PyJs_anonymous_93_))
    PyJs_LONG_94_()
    var.put('At', Js(0.017453292519943295))
    @Js
    def PyJs_anonymous_95_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 's', 't', 'a'])
        var.put('s', var.get('i')(var.get('t')))
        var.put('a', var.get('s').callprop('shift'))
        var.put('e', var.get('s').callprop('shift'))
        PyJsComma(var.get('s').callprop('unshift', Js([Js('name'), var.get('e')])),var.get('s').callprop('unshift', Js([Js('type'), var.get('a')])))
        var.put('n', Js({}))
        return PyJsComma(PyJsComma(var.get('h')(var.get('s'), var.get('n')),var.get('r')(var.get('n'))),var.get('n'))
    PyJs_anonymous_95_._set_name('anonymous')
    var.put('Ct', PyJs_anonymous_95_)
    @Js
    def PyJs_anonymous_96_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        def PyJs_LONG_97_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t')(Js('EPSG:4326'), Js('+title=WGS 84 (long/lat) +proj=longlat +ellps=WGS84 +datum=WGS84 +units=degrees')),var.get('t')(Js('EPSG:4269'), Js('+title=NAD83 (long/lat) +proj=longlat +a=6378137.0 +b=6356752.31414036 +ellps=GRS80 +datum=NAD83 +units=degrees'))),var.get('t')(Js('EPSG:3857'), Js('+title=WGS 84 / Pseudo-Mercator +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs'))),var.get('t').put('WGS84', var.get('t').get('EPSG:4326'))),var.get('t').put('EPSG:3785', var.get('t').get('EPSG:3857'))),var.get('t').put('GOOGLE', var.get('t').get('EPSG:3857'))),var.get('t').put('EPSG:900913', var.get('t').get('EPSG:3857'))),var.get('t').put('EPSG:102113', var.get('t').get('EPSG:3857')))
        PyJs_LONG_97_()
    PyJs_anonymous_96_._set_name('anonymous')
    PyJs_anonymous_96_(var.get('o')).neg()
    var.put('Et', Js([Js('PROJECTEDCRS'), Js('PROJCRS'), Js('GEOGCS'), Js('GEOCCS'), Js('PROJCS'), Js('LOCAL_CS'), Js('GEODCRS'), Js('GEODETICCRS'), Js('GEODETICDATUM'), Js('ENGCRS'), Js('ENGINEERINGCRS')]))
    var.put('Pt', Js([Js('3857'), Js('900913'), Js('3785'), Js('102113')]))
    @Js
    def PyJs_anonymous_98_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        var.put('t', (var.get('t') or Js({})))
        pass
        if var.get('s').neg():
            return var.get('t')
        for PyJsTemp in var.get('s'):
            var.put('a', PyJsTemp)
            (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.put('i', var.get('s').get(var.get('a')))) and var.get('t').put(var.get('a'), var.get('i')))
        return var.get('t')
    PyJs_anonymous_98_._set_name('anonymous')
    var.put('Nt', PyJs_anonymous_98_)
    @Js
    def PyJs_anonymous_99_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        var.put('a', (var.get('t')*var.get('s')))
        return (var.get('i')/var.get('Math').callprop('sqrt', (Js(1.0)-(var.get('a')*var.get('a')))))
    PyJs_anonymous_99_._set_name('anonymous')
    var.put('St', PyJs_anonymous_99_)
    @Js
    def PyJs_anonymous_100_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return ((-Js(1.0)) if (var.get('t')<Js(0.0)) else Js(1.0))
    PyJs_anonymous_100_._set_name('anonymous')
    var.put('kt', PyJs_anonymous_100_)
    @Js
    def PyJs_anonymous_101_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (var.get('t') if (var.get('Math').callprop('abs', var.get('t'))<=var.get('ft')) else (var.get('t')-(var.get('kt')(var.get('t'))*var.get('ut'))))
    PyJs_anonymous_101_._set_name('anonymous')
    var.put('qt', PyJs_anonymous_101_)
    @Js
    def PyJs_anonymous_102_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        var.put('a', (var.get('t')*var.get('i')))
        var.put('h', (Js(0.5)*var.get('t')))
        return PyJsComma(var.put('a', var.get('Math').callprop('pow', ((Js(1.0)-var.get('a'))/(Js(1.0)+var.get('a'))), var.get('h'))),(var.get('Math').callprop('tan', (Js(0.5)*(var.get('ht')-var.get('s'))))/var.get('a')))
    PyJs_anonymous_102_._set_name('anonymous')
    var.put('It', PyJs_anonymous_102_)
    @Js
    def PyJs_anonymous_103_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        #for JS loop
        var.put('h', (Js(0.5)*var.get('t')))
        var.put('e', (var.get('ht')-(Js(2.0)*var.get('Math').callprop('atan', var.get('s')))))
        var.put('n', Js(0.0))
        while (var.get('n')<=Js(15.0)):
            try:
                if PyJsComma(PyJsComma(PyJsComma(var.put('i', (var.get('t')*var.get('Math').callprop('sin', var.get('e')))),var.put('a', ((var.get('ht')-(Js(2.0)*var.get('Math').callprop('atan', (var.get('s')*var.get('Math').callprop('pow', ((Js(1.0)-var.get('i'))/(Js(1.0)+var.get('i'))), var.get('h'))))))-var.get('e')))),var.put('e', var.get('a'), '+')),(var.get('Math').callprop('abs', var.get('a'))<=Js(1e-10))):
                    return var.get('e')
            finally:
                    (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
        return (-Js(9999.0))
    PyJs_anonymous_103_._set_name('anonymous')
    var.put('Ot', PyJs_anonymous_103_)
    @Js
    def PyJs_anonymous_104_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        var.put('t', (var.get(u"this").get('b')/var.get(u"this").get('a')))
        def PyJs_LONG_105_(var=var):
            return ((var.get(u"this").put('k0', var.get('Math').callprop('cos', var.get(u"this").get('lat_ts'))) if var.get(u"this").get('sphere') else var.get(u"this").put('k0', var.get('St')(var.get(u"this").get('e'), var.get('Math').callprop('sin', var.get(u"this").get('lat_ts')), var.get('Math').callprop('cos', var.get(u"this").get('lat_ts'))))) if var.get(u"this").get('lat_ts') else (var.get(u"this").get('k0') or (var.get(u"this").put('k0', var.get(u"this").get('k')) if var.get(u"this").get('k') else var.get(u"this").put('k0', Js(1.0)))))
        PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('es', (Js(1.0)-(var.get('t')*var.get('t')))),(var.get(u"this").contains(Js('x0')) or var.get(u"this").put('x0', Js(0.0)))),(var.get(u"this").contains(Js('y0')) or var.get(u"this").put('y0', Js(0.0)))),var.get(u"this").put('e', var.get('Math').callprop('sqrt', var.get(u"this").get('es')))),PyJs_LONG_105_())
    PyJs_anonymous_104_._set_name('anonymous')
    @Js
    def PyJs_anonymous_106_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        if (((((var.get('i')*var.get('Mt'))>Js(90.0)) and ((var.get('i')*var.get('Mt'))<(-Js(90.0)))) and ((var.get('s')*var.get('Mt'))>Js(180.0))) and ((var.get('s')*var.get('Mt'))<(-Js(180.0)))):
            return var.get(u"null")
        pass
        if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('i'))-var.get('ht')))<=var.get('ot')):
            return var.get(u"null")
        if var.get(u"this").get('sphere'):
            PyJsComma(var.put('a', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*var.get(u"this").get('k0'))*var.get('qt')((var.get('s')-var.get(u"this").get('long0')))))),var.put('h', (var.get(u"this").get('y0')+((var.get(u"this").get('a')*var.get(u"this").get('k0'))*var.get('Math').callprop('log', var.get('Math').callprop('tan', (var.get('ct')+(Js(0.5)*var.get('i')))))))))
        else:
            var.put('e', var.get('Math').callprop('sin', var.get('i')))
            var.put('n', var.get('It')(var.get(u"this").get('e'), var.get('i'), var.get('e')))
            PyJsComma(var.put('a', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*var.get(u"this").get('k0'))*var.get('qt')((var.get('s')-var.get(u"this").get('long0')))))),var.put('h', (var.get(u"this").get('y0')-((var.get(u"this").get('a')*var.get(u"this").get('k0'))*var.get('Math').callprop('log', var.get('n'))))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('a')),var.get('t').put('y', var.get('h'))),var.get('t'))
    PyJs_anonymous_106_._set_name('anonymous')
    @Js
    def PyJs_anonymous_107_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'e', 'i', 's', 't', 'a'])
        var.put('a', (var.get('t').get('x')-var.get(u"this").get('x0')))
        var.put('h', (var.get('t').get('y')-var.get(u"this").get('y0')))
        if var.get(u"this").get('sphere'):
            var.put('i', (var.get('ht')-(Js(2.0)*var.get('Math').callprop('atan', var.get('Math').callprop('exp', ((-var.get('h'))/(var.get(u"this").get('a')*var.get(u"this").get('k0'))))))))
        else:
            var.put('e', var.get('Math').callprop('exp', ((-var.get('h'))/(var.get(u"this").get('a')*var.get(u"this").get('k0')))))
            if PyJsStrictEq((-Js(9999.0)),var.put('i', var.get('Ot')(var.get(u"this").get('e'), var.get('e')))):
                return var.get(u"null")
        return PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('qt')((var.get(u"this").get('long0')+(var.get('a')/(var.get(u"this").get('a')*var.get(u"this").get('k0')))))),var.get('t').put('x', var.get('s'))),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_107_._set_name('anonymous')
    @Js
    def PyJs_anonymous_108_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        pass
    PyJs_anonymous_108_._set_name('anonymous')
    var.put('Rt', Js([Js({'init':PyJs_anonymous_104_,'forward':PyJs_anonymous_106_,'inverse':PyJs_anonymous_107_,'names':Js([Js('Mercator'), Js('Popular Visualisation Pseudo Mercator'), Js('Mercator_1SP'), Js('Mercator_Auxiliary_Sphere'), Js('merc')])}), Js({'init':PyJs_anonymous_108_,'forward':var.get('d'),'inverse':var.get('d'),'names':Js([Js('longlat'), Js('identity')])})]))
    var.put('Gt', Js({}))
    var.put('Tt', Js([]))
    @Js
    def PyJs_anonymous_109_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('Rt').callprop('forEach', var.get('y'))
    PyJs_anonymous_109_._set_name('anonymous')
    @Js
    def PyJs_anonymous_110_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        if var.get('t').neg():
            return Js(1.0).neg()
        var.put('s', var.get('t').callprop('toLowerCase'))
        return (var.get('Tt').get(var.get('Gt').get(var.get('s'))) if (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('Gt').get(var.get('s'))) and var.get('Tt').get(var.get('Gt').get(var.get('s')))) else PyJsComma(Js(0.0), Js(None)))
    PyJs_anonymous_110_._set_name('anonymous')
    var.put('jt', Js({'start':PyJs_anonymous_109_,'add':var.get('y'),'get':PyJs_anonymous_110_}))
    var.put('zt', Js({}))
    def PyJs_LONG_111_(var=var):
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('zt').put('MERIT', Js({'a':Js(6378137.0),'rf':Js(298.257),'ellipseName':Js('MERIT 1983')})),var.get('zt').put('SGS85', Js({'a':Js(6378136.0),'rf':Js(298.257),'ellipseName':Js('Soviet Geodetic System 85')}))),var.get('zt').put('GRS80', Js({'a':Js(6378137.0),'rf':Js(298.257222101),'ellipseName':Js('GRS 1980(IUGG, 1980)')}))),var.get('zt').put('IAU76', Js({'a':Js(6378140.0),'rf':Js(298.257),'ellipseName':Js('IAU 1976')}))),var.get('zt').put('airy', Js({'a':Js(6377563.396),'b':Js(6356256.91),'ellipseName':Js('Airy 1830')}))),var.get('zt').put('APL4', Js({'a':Js(6378137.0),'rf':Js(298.25),'ellipseName':Js('Appl. Physics. 1965')}))),var.get('zt').put('NWL9D', Js({'a':Js(6378145.0),'rf':Js(298.25),'ellipseName':Js('Naval Weapons Lab., 1965')}))),var.get('zt').put('mod_airy', Js({'a':Js(6377340.189),'b':Js(6356034.446),'ellipseName':Js('Modified Airy')}))),var.get('zt').put('andrae', Js({'a':Js(6377104.43),'rf':Js(300.0),'ellipseName':Js('Andrae 1876 (Den., Iclnd.)')}))),var.get('zt').put('aust_SA', Js({'a':Js(6378160.0),'rf':Js(298.25),'ellipseName':Js('Australian Natl & S. Amer. 1969')}))),var.get('zt').put('GRS67', Js({'a':Js(6378160.0),'rf':Js(298.247167427),'ellipseName':Js('GRS 67(IUGG 1967)')}))),var.get('zt').put('bessel', Js({'a':Js(6377397.155),'rf':Js(299.1528128),'ellipseName':Js('Bessel 1841')}))),var.get('zt').put('bess_nam', Js({'a':Js(6377483.865),'rf':Js(299.1528128),'ellipseName':Js('Bessel 1841 (Namibia)')}))),var.get('zt').put('clrk66', Js({'a':Js(6378206.4),'b':Js(6356583.8),'ellipseName':Js('Clarke 1866')}))),var.get('zt').put('clrk80', Js({'a':Js(6378249.145),'rf':Js(293.4663),'ellipseName':Js('Clarke 1880 mod.')}))),var.get('zt').put('clrk58', Js({'a':Js(6378293.645208759),'rf':Js(294.2606763692654),'ellipseName':Js('Clarke 1858')}))),var.get('zt').put('CPM', Js({'a':Js(6375738.7),'rf':Js(334.29),'ellipseName':Js('Comm. des Poids et Mesures 1799')}))),var.get('zt').put('delmbr', Js({'a':Js(6376428.0),'rf':Js(311.5),'ellipseName':Js('Delambre 1810 (Belgium)')}))),var.get('zt').put('engelis', Js({'a':Js(6378136.05),'rf':Js(298.2566),'ellipseName':Js('Engelis 1985')}))),var.get('zt').put('evrst30', Js({'a':Js(6377276.345),'rf':Js(300.8017),'ellipseName':Js('Everest 1830')}))),var.get('zt').put('evrst48', Js({'a':Js(6377304.063),'rf':Js(300.8017),'ellipseName':Js('Everest 1948')}))),var.get('zt').put('evrst56', Js({'a':Js(6377301.243),'rf':Js(300.8017),'ellipseName':Js('Everest 1956')}))),var.get('zt').put('evrst69', Js({'a':Js(6377295.664),'rf':Js(300.8017),'ellipseName':Js('Everest 1969')}))),var.get('zt').put('evrstSS', Js({'a':Js(6377298.556),'rf':Js(300.8017),'ellipseName':Js('Everest (Sabah & Sarawak)')}))),var.get('zt').put('fschr60', Js({'a':Js(6378166.0),'rf':Js(298.3),'ellipseName':Js('Fischer (Mercury Datum) 1960')}))),var.get('zt').put('fschr60m', Js({'a':Js(6378155.0),'rf':Js(298.3),'ellipseName':Js('Fischer 1960')}))),var.get('zt').put('fschr68', Js({'a':Js(6378150.0),'rf':Js(298.3),'ellipseName':Js('Fischer 1968')}))),var.get('zt').put('helmert', Js({'a':Js(6378200.0),'rf':Js(298.3),'ellipseName':Js('Helmert 1906')}))),var.get('zt').put('hough', Js({'a':Js(6378270.0),'rf':Js(297.0),'ellipseName':Js('Hough')}))),var.get('zt').put('intl', Js({'a':Js(6378388.0),'rf':Js(297.0),'ellipseName':Js('International 1909 (Hayford)')}))),var.get('zt').put('kaula', Js({'a':Js(6378163.0),'rf':Js(298.24),'ellipseName':Js('Kaula 1961')}))),var.get('zt').put('lerch', Js({'a':Js(6378139.0),'rf':Js(298.257),'ellipseName':Js('Lerch 1979')}))),var.get('zt').put('mprts', Js({'a':Js(6397300.0),'rf':Js(191.0),'ellipseName':Js('Maupertius 1738')}))),var.get('zt').put('new_intl', Js({'a':Js(6378157.5),'b':Js(6356772.2),'ellipseName':Js('New International 1967')}))),var.get('zt').put('plessis', Js({'a':Js(6376523.0),'rf':Js(6355863.0),'ellipseName':Js('Plessis 1817 (France)')}))),var.get('zt').put('krass', Js({'a':Js(6378245.0),'rf':Js(298.3),'ellipseName':Js('Krassovsky, 1942')}))),var.get('zt').put('SEasia', Js({'a':Js(6378155.0),'b':Js(6356773.3205),'ellipseName':Js('Southeast Asia')}))),var.get('zt').put('walbeck', Js({'a':Js(6376896.0),'b':Js(6355834.8467),'ellipseName':Js('Walbeck')}))),var.get('zt').put('WGS60', Js({'a':Js(6378165.0),'rf':Js(298.3),'ellipseName':Js('WGS 60')}))),var.get('zt').put('WGS66', Js({'a':Js(6378145.0),'rf':Js(298.25),'ellipseName':Js('WGS 66')}))),var.get('zt').put('WGS7', Js({'a':Js(6378135.0),'rf':Js(298.26),'ellipseName':Js('WGS 72')})))
    PyJs_LONG_111_()
    var.put('Lt', var.get('zt').put('WGS84', Js({'a':Js(6378137.0),'rf':Js(298.257223563),'ellipseName':Js('WGS 84')})))
    var.get('zt').put('sphere', Js({'a':Js(6370997.0),'b':Js(6370997.0),'ellipseName':Js('Normal Sphere (r=6370997)')}))
    var.put('Dt', Js({}))
    def PyJs_LONG_112_(var=var):
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('Dt').put('wgs84', Js({'towgs84':Js('0,0,0'),'ellipse':Js('WGS84'),'datumName':Js('WGS84')})),var.get('Dt').put('ch1903', Js({'towgs84':Js('674.374,15.056,405.346'),'ellipse':Js('bessel'),'datumName':Js('swiss')}))),var.get('Dt').put('ggrs87', Js({'towgs84':Js('-199.87,74.79,246.62'),'ellipse':Js('GRS80'),'datumName':Js('Greek_Geodetic_Reference_System_1987')}))),var.get('Dt').put('nad83', Js({'towgs84':Js('0,0,0'),'ellipse':Js('GRS80'),'datumName':Js('North_American_Datum_1983')}))),var.get('Dt').put('nad27', Js({'nadgrids':Js('@conus,@alaska,@ntv2_0.gsb,@ntv1_can.dat'),'ellipse':Js('clrk66'),'datumName':Js('North_American_Datum_1927')}))),var.get('Dt').put('potsdam', Js({'towgs84':Js('606.0,23.0,413.0'),'ellipse':Js('bessel'),'datumName':Js('Potsdam Rauenberg 1950 DHDN')}))),var.get('Dt').put('carthage', Js({'towgs84':Js('-263.0,6.0,431.0'),'ellipse':Js('clark80'),'datumName':Js('Carthage 1934 Tunisia')}))),var.get('Dt').put('hermannskogel', Js({'towgs84':Js('653.0,-212.0,449.0'),'ellipse':Js('bessel'),'datumName':Js('Hermannskogel')}))),var.get('Dt').put('osni52', Js({'towgs84':Js('482.530,-130.596,564.557,-1.042,-0.214,-0.631,8.15'),'ellipse':Js('airy'),'datumName':Js('Irish National')}))),var.get('Dt').put('ire65', Js({'towgs84':Js('482.530,-130.596,564.557,-1.042,-0.214,-0.631,8.15'),'ellipse':Js('mod_airy'),'datumName':Js('Ireland 1965')}))),var.get('Dt').put('rassadiran', Js({'towgs84':Js('-133.63,-157.5,-158.62'),'ellipse':Js('intl'),'datumName':Js('Rassadiran')}))),var.get('Dt').put('nzgd49', Js({'towgs84':Js('59.47,-5.04,187.44,0.47,-0.1,1.024,-4.5993'),'ellipse':Js('intl'),'datumName':Js('New Zealand Geodetic Datum 1949')}))),var.get('Dt').put('osgb36', Js({'towgs84':Js('446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894'),'ellipse':Js('airy'),'datumName':Js('Airy 1830')}))),var.get('Dt').put('s_jtsk', Js({'towgs84':Js('589,76,480'),'ellipse':Js('bessel'),'datumName':Js('S-JTSK (Ferro)')}))),var.get('Dt').put('beduaram', Js({'towgs84':Js('-106,-87,188'),'ellipse':Js('clrk80'),'datumName':Js('Beduaram')}))),var.get('Dt').put('gunung_segara', Js({'towgs84':Js('-403,684,41'),'ellipse':Js('bessel'),'datumName':Js('Gunung Segara Jakarta')}))),var.get('Dt').put('rnb72', Js({'towgs84':Js('106.869,-52.2978,103.724,-0.33657,0.456955,-1.84218,1'),'ellipse':Js('intl'),'datumName':Js('Reseau National Belge 1972')}))),var.get('Projection').put('projections', var.get('jt'))),var.get('Projection').get('projections').callprop('start'))
    PyJs_LONG_112_()
    @Js
    def PyJs_anonymous_113_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        def PyJs_LONG_115_(var=var):
            def PyJs_LONG_114_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('b')(var.get('i'), var.get('t').get('es'), var.get('t').get('a'))),(var.get('E')(var.get('t').get('datum_type')) and var.put('i', var.get('A')(var.get('i'), var.get('t').get('datum_type'), var.get('t').get('datum_params'))))),(var.get('E')(var.get('s').get('datum_type')) and var.put('i', var.get('C')(var.get('i'), var.get('s').get('datum_type'), var.get('s').get('datum_params'))))),var.get('w')(var.get('i'), var.get('s').get('es'), var.get('s').get('a'), var.get('s').get('b')))
            return (var.get('i') if (PyJsStrictEq(var.get('t').get('datum_type'),var.get('it')) or PyJsStrictEq(var.get('s').get('datum_type'),var.get('it'))) else (PyJs_LONG_114_() if (((PyJsStrictNeq(var.get('t').get('es'),var.get('s').get('es')) or PyJsStrictNeq(var.get('t').get('a'),var.get('s').get('a'))) or var.get('E')(var.get('t').get('datum_type'))) or var.get('E')(var.get('s').get('datum_type'))) else var.get('i')))
        return (var.get('i') if var.get('g')(var.get('t'), var.get('s')) else PyJs_LONG_115_())
    PyJs_anonymous_113_._set_name('anonymous')
    var.put('Bt', PyJs_anonymous_113_)
    @Js
    def PyJs_anonymous_116_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('n', var.get('i').get('x'))
        var.put('r', var.get('i').get('y'))
        var.put('o', (var.get('i').get('z') or Js(0.0)))
        var.put('l', Js({}))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<Js(3.0)):
            try:
                if ((var.get('s').neg() or PyJsStrictNeq(Js(2.0),var.get('e'))) or PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('i').get('z'))):
                    while 1:
                        SWITCHED = False
                        def PyJs_LONG_117_(var=var):
                            return (PyJsComma(var.put('a', var.get('n')),var.put('h', (Js('x') if PyJsStrictNeq((-Js(1.0)),Js('ew').callprop('indexOf', var.get('t').get('axis').get(var.get('e')))) else Js('y')))) if PyJsStrictEq(Js(0.0),var.get('e')) else (PyJsComma(var.put('a', var.get('r')),var.put('h', (Js('y') if PyJsStrictNeq((-Js(1.0)),Js('ns').callprop('indexOf', var.get('t').get('axis').get(var.get('e')))) else Js('x')))) if PyJsStrictEq(Js(1.0),var.get('e')) else PyJsComma(var.put('a', var.get('o')),var.put('h', Js('z')))))
                        CONDITION = (PyJsComma(PyJs_LONG_117_(),var.get('t').get('axis').get(var.get('e'))))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('e')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('s')):
                            SWITCHED = True
                            var.get('l').put(var.get('h'), var.get('a'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('u')):
                            SWITCHED = True
                            (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('i').get(var.get('h'))) and var.get('l').put('z', var.get('a')))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                            SWITCHED = True
                            (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('i').get(var.get('h'))) and var.get('l').put('z', (-var.get('a'))))
                            break
                        if True:
                            SWITCHED = True
                            return var.get(u"null")
                        SWITCHED = True
                        break
            finally:
                    (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
        return var.get('l')
    PyJs_anonymous_116_._set_name('anonymous')
    var.put('Ut', PyJs_anonymous_116_)
    @Js
    def PyJs_anonymous_118_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', Js({'x':var.get('t').get('0'),'y':var.get('t').get('1')}))
        return PyJsComma(PyJsComma(((var.get('t').get('length')>Js(2.0)) and var.get('s').put('z', var.get('t').get('2'))),((var.get('t').get('length')>Js(3.0)) and var.get('s').put('m', var.get('t').get('3')))),var.get('s'))
    PyJs_anonymous_118_._set_name('anonymous')
    var.put('Ft', PyJs_anonymous_118_)
    @Js
    def PyJs_anonymous_119_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        PyJsComma(var.get('P')(var.get('t').get('x')),var.get('P')(var.get('t').get('y')))
    PyJs_anonymous_119_._set_name('anonymous')
    var.put('Qt', PyJs_anonymous_119_)
    var.put('Wt', var.get('Projection')(Js('WGS84')))
    var.put('Ht', Js(6.0))
    var.put('Xt', Js('AJSAJS'))
    var.put('Kt', Js('AFAFAF'))
    var.put('Jt', Js(65.0))
    var.put('Vt', Js(73.0))
    var.put('Zt', Js(79.0))
    var.put('Yt', Js(86.0))
    var.put('$t', Js(90.0))
    @Js
    def PyJs_anonymous_120_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', var.get('z')(var.get('Q')(var.get('t').callprop('toUpperCase'))))
        return (Js([var.get('s').get('lon'), var.get('s').get('lat'), var.get('s').get('lon'), var.get('s').get('lat')]) if (var.get('s').get('lat') and var.get('s').get('lon')) else Js([var.get('s').get('left'), var.get('s').get('bottom'), var.get('s').get('right'), var.get('s').get('top')]))
    PyJs_anonymous_120_._set_name('anonymous')
    var.put('ts', Js({'forward':var.get('O'),'inverse':PyJs_anonymous_120_,'toPoint':var.get('R')}))
    @Js
    def PyJs_anonymous_121_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('Point').create(var.get('R')(var.get('t')))
    PyJs_anonymous_121_._set_name('anonymous')
    @Js
    def PyJs_anonymous_122_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('O')(Js([var.get(u"this").get('x'), var.get(u"this").get('y')]), var.get('t'))
    PyJs_anonymous_122_._set_name('anonymous')
    PyJsComma(var.get('Point').put('fromMGRS', PyJs_anonymous_121_),var.get('Point').get('prototype').put('toMGRS', PyJs_anonymous_122_))
    var.put('ss', Js(0.01068115234375))
    @Js
    def PyJs_anonymous_123_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('s', Js([]))
        PyJsComma(var.get('s').put('0', (Js(1.0)-(var.get('t')*(Js(0.25)+(var.get('t')*(Js(0.046875)+(var.get('t')*(Js(0.01953125)+(var.get('t')*var.get('ss')))))))))),var.get('s').put('1', (var.get('t')*(Js(0.75)-(var.get('t')*(Js(0.046875)+(var.get('t')*(Js(0.01953125)+(var.get('t')*var.get('ss'))))))))))
        var.put('i', (var.get('t')*var.get('t')))
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('s').put('2', (var.get('i')*(Js(0.46875)-(var.get('t')*(Js(0.013020833333333334)+(Js(0.007120768229166667)*var.get('t'))))))),var.put('i', var.get('t'), '*')),var.get('s').put('3', (var.get('i')*(Js(0.3645833333333333)-(Js(0.005696614583333333)*var.get('t')))))),var.get('s').put('4', ((var.get('i')*var.get('t'))*Js(0.3076171875)))),var.get('s'))
    PyJs_anonymous_123_._set_name('anonymous')
    var.put('is', PyJs_anonymous_123_)
    @Js
    def PyJs_anonymous_124_(t, s, i, a, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        return PyJsComma(PyJsComma(var.put('i', var.get('s'), '*'),var.put('s', var.get('s'), '*')),((var.get('a').get('0')*var.get('t'))-(var.get('i')*(var.get('a').get('1')+(var.get('s')*(var.get('a').get('2')+(var.get('s')*(var.get('a').get('3')+(var.get('s')*var.get('a').get('4'))))))))))
    PyJs_anonymous_124_._set_name('anonymous')
    var.put('as', PyJs_anonymous_124_)
    @Js
    def PyJs_anonymous_125_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        #for JS loop
        var.put('a', (Js(1.0)/(Js(1.0)-var.get('s'))))
        var.put('h', var.get('t'))
        var.put('e', Js(20.0))
        while var.get('e'):
            try:
                var.put('n', var.get('Math').callprop('sin', var.get('h')))
                var.put('r', (Js(1.0)-((var.get('s')*var.get('n'))*var.get('n'))))
                if PyJsComma(PyJsComma(var.put('r', (((var.get('as')(var.get('h'), var.get('n'), var.get('Math').callprop('cos', var.get('h')), var.get('i'))-var.get('t'))*(var.get('r')*var.get('Math').callprop('sqrt', var.get('r'))))*var.get('a'))),var.put('h', var.get('r'), '-')),(var.get('Math').callprop('abs', var.get('r'))<var.get('ot'))):
                    return var.get('h')
            finally:
                    var.put('e',Js(var.get('e').to_number())-Js(1))
        return var.get('h')
    PyJs_anonymous_125_._set_name('anonymous')
    var.put('hs', PyJs_anonymous_125_)
    @Js
    def PyJs_anonymous_126_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_127_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('x0', (var.get(u"this").get('x0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('x0')) else Js(0.0))),var.get(u"this").put('y0', (var.get(u"this").get('y0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('y0')) else Js(0.0)))),var.get(u"this").put('long0', (var.get(u"this").get('long0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('long0')) else Js(0.0)))),var.get(u"this").put('lat0', (var.get(u"this").get('lat0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('lat0')) else Js(0.0)))),(var.get(u"this").get('es') and PyJsComma(var.get(u"this").put('en', var.get('is')(var.get(u"this").get('es'))),var.get(u"this").put('ml0', var.get('as')(var.get(u"this").get('lat0'), var.get('Math').callprop('sin', var.get(u"this").get('lat0')), var.get('Math').callprop('cos', var.get(u"this").get('lat0')), var.get(u"this").get('en'))))))
        PyJs_LONG_127_()
    PyJs_anonymous_126_._set_name('anonymous')
    @Js
    def PyJs_anonymous_128_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'd', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 'y', 's', 'r', 'f', 'a'])
        var.put('h', var.get('t').get('x'))
        var.put('e', var.get('t').get('y'))
        var.put('n', var.get('qt')((var.get('h')-var.get(u"this").get('long0'))))
        var.put('r', var.get('Math').callprop('sin', var.get('e')))
        var.put('o', var.get('Math').callprop('cos', var.get('e')))
        if var.get(u"this").get('es'):
            var.put('l', (var.get('o')*var.get('n')))
            var.put('M', var.get('Math').callprop('pow', var.get('l'), Js(2.0)))
            var.put('c', (var.get(u"this").get('ep2')*var.get('Math').callprop('pow', var.get('o'), Js(2.0))))
            var.put('u', var.get('Math').callprop('pow', var.get('c'), Js(2.0)))
            var.put('f', (var.get('Math').callprop('tan', var.get('e')) if (var.get('Math').callprop('abs', var.get('o'))>var.get('ot')) else Js(0.0)))
            var.put('m', var.get('Math').callprop('pow', var.get('f'), Js(2.0)))
            var.put('p', var.get('Math').callprop('pow', var.get('m'), Js(2.0)))
            PyJsComma(var.put('s', (Js(1.0)-(var.get(u"this").get('es')*var.get('Math').callprop('pow', var.get('r'), Js(2.0))))),var.put('l', var.get('Math').callprop('sqrt', var.get('s')), '/'))
            var.put('d', var.get('as')(var.get('e'), var.get('r'), var.get('o'), var.get(u"this").get('en')))
            def PyJs_LONG_129_(var=var):
                return (var.get(u"this").get('a')*((var.get(u"this").get('k0')*var.get('l'))*(Js(1.0)+((var.get('M')/Js(6.0))*(((Js(1.0)-var.get('m'))+var.get('c'))+((var.get('M')/Js(20.0))*(((((Js(5.0)-(Js(18.0)*var.get('m')))+var.get('p'))+(Js(14.0)*var.get('c')))-((Js(58.0)*var.get('m'))*var.get('c')))+((var.get('M')/Js(42.0))*(((Js(61.0)+(Js(179.0)*var.get('p')))-(var.get('p')*var.get('m')))-(Js(479.0)*var.get('m')))))))))))
            def PyJs_LONG_130_(var=var):
                return ((((var.get('r')*var.get('n'))*var.get('l'))/Js(2.0))*(Js(1.0)+((var.get('M')/Js(12.0))*((((Js(5.0)-var.get('m'))+(Js(9.0)*var.get('c')))+(Js(4.0)*var.get('u')))+((var.get('M')/Js(30.0))*(((((Js(61.0)+var.get('p'))-(Js(58.0)*var.get('m')))+(Js(270.0)*var.get('c')))-((Js(330.0)*var.get('m'))*var.get('c')))+((var.get('M')/Js(56.0))*(((Js(1385.0)+(Js(543.0)*var.get('p')))-(var.get('p')*var.get('m')))-(Js(3111.0)*var.get('m'))))))))))
            PyJsComma(var.put('i', (PyJs_LONG_129_()+var.get(u"this").get('x0'))),var.put('a', ((var.get(u"this").get('a')*(var.get(u"this").get('k0')*((var.get('d')-var.get(u"this").get('ml0'))+PyJs_LONG_130_())))+var.get(u"this").get('y0'))))
        else:
            var.put('y', (var.get('o')*var.get('Math').callprop('sin', var.get('n'))))
            if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('y'))-Js(1.0)))<var.get('ot')):
                return Js(93.0)
            def PyJs_LONG_131_(var=var):
                return PyJsComma(PyJsComma(var.put('i', ((((Js(0.5)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))*var.get('Math').callprop('log', ((Js(1.0)+var.get('y'))/(Js(1.0)-var.get('y')))))+var.get(u"this").get('x0'))),var.put('a', ((var.get('o')*var.get('Math').callprop('cos', var.get('n')))/var.get('Math').callprop('sqrt', (Js(1.0)-var.get('Math').callprop('pow', var.get('y'), Js(2.0))))))),(var.put('y', var.get('Math').callprop('abs', var.get('a')))>=Js(1.0)))
            if PyJs_LONG_131_():
                if ((var.get('y')-Js(1.0))>var.get('ot')):
                    return Js(93.0)
                var.put('a', Js(0.0))
            else:
                var.put('a', var.get('Math').callprop('acos', var.get('a')))
            PyJsComma(((var.get('e')<Js(0.0)) and var.put('a', (-var.get('a')))),var.put('a', (((var.get(u"this").get('a')*var.get(u"this").get('k0'))*(var.get('a')-var.get(u"this").get('lat0')))+var.get(u"this").get('y0'))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('i')),var.get('t').put('y', var.get('a'))),var.get('t'))
    PyJs_anonymous_128_._set_name('anonymous')
    @Js
    def PyJs_anonymous_132_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'd', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 'y', 'x', 's', 'r', 'f', '_', 'a'])
        var.put('e', ((var.get('t').get('x')-var.get(u"this").get('x0'))*(Js(1.0)/var.get(u"this").get('a'))))
        var.put('n', ((var.get('t').get('y')-var.get(u"this").get('y0'))*(Js(1.0)/var.get(u"this").get('a'))))
        if var.get(u"this").get('es'):
            if PyJsComma(PyJsComma(var.put('s', (var.get(u"this").get('ml0')+(var.get('n')/var.get(u"this").get('k0')))),var.put('i', var.get('hs')(var.get('s'), var.get(u"this").get('es'), var.get(u"this").get('en')))),(var.get('Math').callprop('abs', var.get('i'))<var.get('ht'))):
                var.put('r', var.get('Math').callprop('sin', var.get('i')))
                var.put('o', var.get('Math').callprop('cos', var.get('i')))
                var.put('l', (var.get('Math').callprop('tan', var.get('i')) if (var.get('Math').callprop('abs', var.get('o'))>var.get('ot')) else Js(0.0)))
                var.put('M', (var.get(u"this").get('ep2')*var.get('Math').callprop('pow', var.get('o'), Js(2.0))))
                var.put('c', var.get('Math').callprop('pow', var.get('M'), Js(2.0)))
                var.put('u', var.get('Math').callprop('pow', var.get('l'), Js(2.0)))
                var.put('f', var.get('Math').callprop('pow', var.get('u'), Js(2.0)))
                var.put('s', (Js(1.0)-(var.get(u"this").get('es')*var.get('Math').callprop('pow', var.get('r'), Js(2.0)))))
                var.put('m', ((var.get('e')*var.get('Math').callprop('sqrt', var.get('s')))/var.get(u"this").get('k0')))
                var.put('p', var.get('Math').callprop('pow', var.get('m'), Js(2.0)))
                def PyJs_LONG_133_(var=var):
                    return (((((Js(5.0)+(Js(3.0)*var.get('u')))-((Js(9.0)*var.get('M'))*var.get('u')))+var.get('M'))-(Js(4.0)*var.get('c')))-((var.get('p')/Js(30.0))*(((((Js(61.0)+(Js(90.0)*var.get('u')))-((Js(252.0)*var.get('M'))*var.get('u')))+(Js(45.0)*var.get('f')))+(Js(46.0)*var.get('M')))-((var.get('p')/Js(56.0))*(((Js(1385.0)+(Js(3633.0)*var.get('u')))+(Js(4095.0)*var.get('f')))+((Js(1574.0)*var.get('f'))*var.get('u')))))))
                def PyJs_LONG_134_(var=var):
                    return (var.get(u"this").get('long0')+((var.get('m')*(Js(1.0)-((var.get('p')/Js(6.0))*(((Js(1.0)+(Js(2.0)*var.get('u')))+var.get('M'))-((var.get('p')/Js(20.0))*(((((Js(5.0)+(Js(28.0)*var.get('u')))+(Js(24.0)*var.get('f')))+((Js(8.0)*var.get('M'))*var.get('u')))+(Js(6.0)*var.get('M')))-((var.get('p')/Js(42.0))*(((Js(61.0)+(Js(662.0)*var.get('u')))+(Js(1320.0)*var.get('f')))+((Js(720.0)*var.get('f'))*var.get('u'))))))))))/var.get('o')))
                PyJsComma(var.put('a', (var.get('i')-((((var.put('s', var.get('l'), '*')*var.get('p'))/(Js(1.0)-var.get(u"this").get('es')))*Js(0.5))*(Js(1.0)-((var.get('p')/Js(12.0))*PyJs_LONG_133_()))))),var.put('h', var.get('qt')(PyJs_LONG_134_())))
            else:
                PyJsComma(var.put('a', (var.get('ht')*var.get('kt')(var.get('n')))),var.put('h', Js(0.0)))
        else:
            var.put('d', var.get('Math').callprop('exp', (var.get('e')/var.get(u"this").get('k0'))))
            var.put('y', (Js(0.5)*(var.get('d')-(Js(1.0)/var.get('d')))))
            var.put('_', (var.get(u"this").get('lat0')+(var.get('n')/var.get(u"this").get('k0'))))
            var.put('x', var.get('Math').callprop('cos', var.get('_')))
            def PyJs_LONG_135_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('Math').callprop('sqrt', ((Js(1.0)-var.get('Math').callprop('pow', var.get('x'), Js(2.0)))/(Js(1.0)+var.get('Math').callprop('pow', var.get('y'), Js(2.0)))))),var.put('a', var.get('Math').callprop('asin', var.get('s')))),((var.get('n')<Js(0.0)) and var.put('a', (-var.get('a'))))),var.put('h', (Js(0.0) if (PyJsStrictEq(Js(0.0),var.get('y')) and PyJsStrictEq(Js(0.0),var.get('x'))) else var.get('qt')((var.get('Math').callprop('atan2', var.get('y'), var.get('x'))+var.get(u"this").get('long0'))))))
            PyJs_LONG_135_()
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('h')),var.get('t').put('y', var.get('a'))),var.get('t'))
    PyJs_anonymous_132_._set_name('anonymous')
    var.put('es', Js({'init':PyJs_anonymous_126_,'forward':PyJs_anonymous_128_,'inverse':PyJs_anonymous_132_,'names':Js([Js('Transverse_Mercator'), Js('Transverse Mercator'), Js('tmerc')])}))
    @Js
    def PyJs_anonymous_136_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', var.get('Math').callprop('exp', var.get('t')))
        return var.put('s', ((var.get('s')-(Js(1.0)/var.get('s')))/Js(2.0)))
    PyJs_anonymous_136_._set_name('anonymous')
    var.put('ns', PyJs_anonymous_136_)
    @Js
    def PyJs_anonymous_137_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        PyJsComma(var.put('t', var.get('Math').callprop('abs', var.get('t'))),var.put('s', var.get('Math').callprop('abs', var.get('s'))))
        var.put('i', var.get('Math').callprop('max', var.get('t'), var.get('s')))
        var.put('a', (var.get('Math').callprop('min', var.get('t'), var.get('s'))/(var.get('i') or Js(1.0))))
        return (var.get('i')*var.get('Math').callprop('sqrt', (Js(1.0)+var.get('Math').callprop('pow', var.get('a'), Js(2.0)))))
    PyJs_anonymous_137_._set_name('anonymous')
    var.put('rs', PyJs_anonymous_137_)
    @Js
    def PyJs_anonymous_138_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('s', (Js(1.0)+var.get('t')))
        var.put('i', (var.get('s')-Js(1.0)))
        return (var.get('t') if PyJsStrictEq(Js(0.0),var.get('i')) else ((var.get('t')*var.get('Math').callprop('log', var.get('s')))/var.get('i')))
    PyJs_anonymous_138_._set_name('anonymous')
    var.put('os', PyJs_anonymous_138_)
    @Js
    def PyJs_anonymous_139_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', var.get('Math').callprop('abs', var.get('t')))
        return PyJsComma(var.put('s', var.get('os')((var.get('s')*(Js(1.0)+(var.get('s')/(var.get('rs')(Js(1.0), var.get('s'))+Js(1.0))))))),((-var.get('s')) if (var.get('t')<Js(0.0)) else var.get('s')))
    PyJs_anonymous_139_._set_name('anonymous')
    var.put('ls', PyJs_anonymous_139_)
    @Js
    def PyJs_anonymous_140_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        #for JS loop
        var.put('a', (Js(2.0)*var.get('Math').callprop('cos', (Js(2.0)*var.get('s')))))
        var.put('h', (var.get('t').get('length')-Js(1.0)))
        var.put('e', var.get('t').get(var.get('h')))
        var.put('n', Js(0.0))
        while (var.put('h',Js(var.get('h').to_number())-Js(1))>=Js(0.0)):
            PyJsComma(PyJsComma(var.put('i', (((var.get('a')*var.get('e'))-var.get('n'))+var.get('t').get(var.get('h')))),var.put('n', var.get('e'))),var.put('e', var.get('i')))
        
        return (var.get('s')+(var.get('i')*var.get('Math').callprop('sin', (Js(2.0)*var.get('s')))))
    PyJs_anonymous_140_._set_name('anonymous')
    var.put('Ms', PyJs_anonymous_140_)
    @Js
    def PyJs_anonymous_141_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        #for JS loop
        var.put('a', (Js(2.0)*var.get('Math').callprop('cos', var.get('s'))))
        var.put('h', (var.get('t').get('length')-Js(1.0)))
        var.put('e', var.get('t').get(var.get('h')))
        var.put('n', Js(0.0))
        while (var.put('h',Js(var.get('h').to_number())-Js(1))>=Js(0.0)):
            PyJsComma(PyJsComma(var.put('i', (((var.get('a')*var.get('e'))-var.get('n'))+var.get('t').get(var.get('h')))),var.put('n', var.get('e'))),var.put('e', var.get('i')))
        
        return (var.get('Math').callprop('sin', var.get('s'))*var.get('i'))
    PyJs_anonymous_141_._set_name('anonymous')
    var.put('cs', PyJs_anonymous_141_)
    @Js
    def PyJs_anonymous_142_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('s', var.get('Math').callprop('exp', var.get('t')))
        return var.put('s', ((var.get('s')+(Js(1.0)/var.get('s')))/Js(2.0)))
    PyJs_anonymous_142_._set_name('anonymous')
    var.put('us', PyJs_anonymous_142_)
    @Js
    def PyJs_anonymous_143_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 't', 'i', 's', 'r', 'f', 'a'])
        #for JS loop
        var.put('e', var.get('Math').callprop('sin', var.get('s')))
        var.put('n', var.get('Math').callprop('cos', var.get('s')))
        var.put('r', var.get('ns')(var.get('i')))
        var.put('o', var.get('us')(var.get('i')))
        var.put('l', ((Js(2.0)*var.get('n'))*var.get('o')))
        var.put('M', (((-Js(2.0))*var.get('e'))*var.get('r')))
        var.put('c', (var.get('t').get('length')-Js(1.0)))
        var.put('u', var.get('t').get(var.get('c')))
        var.put('f', Js(0.0))
        var.put('m', Js(0.0))
        var.put('p', Js(0.0))
        while (var.put('c',Js(var.get('c').to_number())-Js(1))>=Js(0.0)):
            PyJsComma(PyJsComma(PyJsComma(var.put('a', var.get('m')),var.put('h', var.get('f'))),var.put('u', ((((var.get('l')*var.put('m', var.get('u')))-var.get('a'))-(var.get('M')*var.put('f', var.get('p'))))+var.get('t').get(var.get('c'))))),var.put('p', (((var.get('M')*var.get('m'))-var.get('h'))+(var.get('l')*var.get('f')))))
        
        return PyJsComma(PyJsComma(var.put('l', (var.get('e')*var.get('o'))),var.put('M', (var.get('n')*var.get('r')))),Js([((var.get('l')*var.get('u'))-(var.get('M')*var.get('p'))), ((var.get('l')*var.get('p'))+(var.get('M')*var.get('u')))]))
    PyJs_anonymous_143_._set_name('anonymous')
    var.put('fs', PyJs_anonymous_143_)
    @Js
    def PyJs_anonymous_144_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        if (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('es')) or (var.get(u"this").get('es')<=Js(0.0))):
            PyJsTempException = JsToPyException(var.get('Error').create(Js('incorrect elliptical usage')))
            raise PyJsTempException
        def PyJs_LONG_145_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('x0', (var.get(u"this").get('x0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('x0')) else Js(0.0))),var.get(u"this").put('y0', (var.get(u"this").get('y0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('y0')) else Js(0.0)))),var.get(u"this").put('long0', (var.get(u"this").get('long0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('long0')) else Js(0.0)))),var.get(u"this").put('lat0', (var.get(u"this").get('lat0') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get(u"this").get('lat0')) else Js(0.0)))),var.get(u"this").put('cgb', Js([]))),var.get(u"this").put('cbg', Js([]))),var.get(u"this").put('utg', Js([]))),var.get(u"this").put('gtu', Js([])))
        PyJs_LONG_145_()
        var.put('t', (var.get(u"this").get('es')/(Js(1.0)+var.get('Math').callprop('sqrt', (Js(1.0)-var.get(u"this").get('es'))))))
        var.put('s', (var.get('t')/(Js(2.0)-var.get('t'))))
        var.put('i', var.get('s'))
        def PyJs_LONG_146_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").get('cgb').put('0', (var.get('s')*(Js(2.0)+(var.get('s')*(((-Js(2.0))/Js(3.0))+(var.get('s')*((var.get('s')*((Js(116.0)/Js(45.0))+(var.get('s')*((Js(26.0)/Js(45.0))+(var.get('s')*((-Js(2854.0))/Js(675.0)))))))-Js(2.0)))))))),var.get(u"this").get('cbg').put('0', (var.get('s')*((var.get('s')*((Js(2.0)/Js(3.0))+(var.get('s')*((Js(4.0)/Js(3.0))+(var.get('s')*(((-Js(82.0))/Js(45.0))+(var.get('s')*((Js(32.0)/Js(45.0))+(var.get('s')*(Js(4642.0)/Js(4725.0)))))))))))-Js(2.0))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('cgb').put('1', (var.get('i')*((Js(7.0)/Js(3.0))+(var.get('s')*((var.get('s')*(((-Js(227.0))/Js(45.0))+(var.get('s')*((Js(2704.0)/Js(315.0))+(var.get('s')*(Js(2323.0)/Js(945.0)))))))-Js(1.6))))))),var.get(u"this").get('cbg').put('1', (var.get('i')*((Js(5.0)/Js(3.0))+(var.get('s')*(((-Js(16.0))/Js(15.0))+(var.get('s')*(((-Js(13.0))/Js(9.0))+(var.get('s')*((Js(904.0)/Js(315.0))+(var.get('s')*((-Js(1522.0))/Js(945.0))))))))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('cgb').put('2', (var.get('i')*((Js(56.0)/Js(15.0))+(var.get('s')*(((-Js(136.0))/Js(35.0))+(var.get('s')*(((-Js(1262.0))/Js(105.0))+(var.get('s')*(Js(73814.0)/Js(2835.0))))))))))),var.get(u"this").get('cbg').put('2', (var.get('i')*(((-Js(26.0))/Js(15.0))+(var.get('s')*((Js(34.0)/Js(21.0))+(var.get('s')*(Js(1.6)+(var.get('s')*((-Js(12686.0))/Js(2835.0))))))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('cgb').put('3', (var.get('i')*((Js(4279.0)/Js(630.0))+(var.get('s')*(((-Js(332.0))/Js(35.0))+(var.get('s')*((-Js(399572.0))/Js(14175.0))))))))),var.get(u"this").get('cbg').put('3', (var.get('i')*((Js(1237.0)/Js(630.0))+(var.get('s')*((var.get('s')*((-Js(24832.0))/Js(14175.0)))-Js(2.4))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('cgb').put('4', (var.get('i')*((Js(4174.0)/Js(315.0))+(var.get('s')*((-Js(144838.0))/Js(6237.0))))))),var.get(u"this").get('cbg').put('4', (var.get('i')*(((-Js(734.0))/Js(315.0))+(var.get('s')*(Js(109598.0)/Js(31185.0))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('cgb').put('5', (var.get('i')*(Js(601676.0)/Js(22275.0))))),var.get(u"this").get('cbg').put('5', (var.get('i')*(Js(444337.0)/Js(155925.0))))),var.put('i', var.get('Math').callprop('pow', var.get('s'), Js(2.0)))),var.get(u"this").put('Qn', ((var.get(u"this").get('k0')/(Js(1.0)+var.get('s')))*(Js(1.0)+(var.get('i')*(Js(0.25)+(var.get('i')*((Js(1.0)/Js(64.0))+(var.get('i')/Js(256.0)))))))))),var.get(u"this").get('utg').put('0', (var.get('s')*((var.get('s')*((Js(2.0)/Js(3.0))+(var.get('s')*(((-Js(37.0))/Js(96.0))+(var.get('s')*((Js(1.0)/Js(360.0))+(var.get('s')*((Js(81.0)/Js(512.0))+(var.get('s')*((-Js(96199.0))/Js(604800.0)))))))))))-Js(0.5))))),var.get(u"this").get('gtu').put('0', (var.get('s')*(Js(0.5)+(var.get('s')*(((-Js(2.0))/Js(3.0))+(var.get('s')*((Js(5.0)/Js(16.0))+(var.get('s')*((Js(41.0)/Js(180.0))+(var.get('s')*(((-Js(127.0))/Js(288.0))+(var.get('s')*(Js(7891.0)/Js(37800.0))))))))))))))),var.get(u"this").get('utg').put('1', (var.get('i')*(((-Js(1.0))/Js(48.0))+(var.get('s')*(((-Js(1.0))/Js(15.0))+(var.get('s')*((Js(437.0)/Js(1440.0))+(var.get('s')*(((-Js(46.0))/Js(105.0))+(var.get('s')*(Js(1118711.0)/Js(3870720.0))))))))))))),var.get(u"this").get('gtu').put('1', (var.get('i')*((Js(13.0)/Js(48.0))+(var.get('s')*((var.get('s')*((Js(557.0)/Js(1440.0))+(var.get('s')*((Js(281.0)/Js(630.0))+(var.get('s')*((-Js(1983433.0))/Js(1935360.0)))))))-Js(0.6))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('utg').put('2', (var.get('i')*(((-Js(17.0))/Js(480.0))+(var.get('s')*((Js(37.0)/Js(840.0))+(var.get('s')*((Js(209.0)/Js(4480.0))+(var.get('s')*((-Js(5569.0))/Js(90720.0))))))))))),var.get(u"this").get('gtu').put('2', (var.get('i')*((Js(61.0)/Js(240.0))+(var.get('s')*(((-Js(103.0))/Js(140.0))+(var.get('s')*((Js(15061.0)/Js(26880.0))+(var.get('s')*(Js(167603.0)/Js(181440.0))))))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('utg').put('3', (var.get('i')*(((-Js(4397.0))/Js(161280.0))+(var.get('s')*((Js(11.0)/Js(504.0))+(var.get('s')*(Js(830251.0)/Js(7257600.0))))))))),var.get(u"this").get('gtu').put('3', (var.get('i')*((Js(49561.0)/Js(161280.0))+(var.get('s')*(((-Js(179.0))/Js(168.0))+(var.get('s')*(Js(6601661.0)/Js(7257600.0))))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('utg').put('4', (var.get('i')*(((-Js(4583.0))/Js(161280.0))+(var.get('s')*(Js(108847.0)/Js(3991680.0))))))),var.get(u"this").get('gtu').put('4', (var.get('i')*((Js(34729.0)/Js(80640.0))+(var.get('s')*((-Js(3418889.0))/Js(1995840.0))))))),var.put('i', var.get('s'), '*')),var.get(u"this").get('utg').put('5', ((-Js(0.03233083094085698))*var.get('i')))),var.get(u"this").get('gtu').put('5', (Js(0.6650675310896665)*var.get('i'))))
        PyJs_LONG_146_()
        var.put('a', var.get('Ms')(var.get(u"this").get('cbg'), var.get(u"this").get('lat0')))
        var.get(u"this").put('Zb', ((-var.get(u"this").get('Qn'))*(var.get('a')+var.get('cs')(var.get(u"this").get('gtu'), (Js(2.0)*var.get('a'))))))
    PyJs_anonymous_144_._set_name('anonymous')
    @Js
    def PyJs_anonymous_147_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('s', var.get('qt')((var.get('t').get('x')-var.get(u"this").get('long0'))))
        var.put('i', var.get('t').get('y'))
        var.put('i', var.get('Ms')(var.get(u"this").get('cbg'), var.get('i')))
        var.put('a', var.get('Math').callprop('sin', var.get('i')))
        var.put('h', var.get('Math').callprop('cos', var.get('i')))
        var.put('e', var.get('Math').callprop('sin', var.get('s')))
        var.put('n', var.get('Math').callprop('cos', var.get('s')))
        PyJsComma(PyJsComma(var.put('i', var.get('Math').callprop('atan2', var.get('a'), (var.get('n')*var.get('h')))),var.put('s', var.get('Math').callprop('atan2', (var.get('e')*var.get('h')), var.get('rs')(var.get('a'), (var.get('h')*var.get('n')))))),var.put('s', var.get('ls')(var.get('Math').callprop('tan', var.get('s')))))
        var.put('r', var.get('fs')(var.get(u"this").get('gtu'), (Js(2.0)*var.get('i')), (Js(2.0)*var.get('s'))))
        PyJsComma(var.put('i', var.get('r').get('0'), '+'),var.put('s', var.get('r').get('1'), '+'))
        pass
        def PyJs_LONG_148_(var=var):
            return (PyJsComma(var.put('o', ((var.get(u"this").get('a')*(var.get(u"this").get('Qn')*var.get('s')))+var.get(u"this").get('x0'))),var.put('l', ((var.get(u"this").get('a')*((var.get(u"this").get('Qn')*var.get('i'))+var.get(u"this").get('Zb')))+var.get(u"this").get('y0')))) if (var.get('Math').callprop('abs', var.get('s'))<=Js(2.623395162778)) else PyJsComma(var.put('o', (Js(1.0)/Js(0.0))),var.put('l', (Js(1.0)/Js(0.0)))))
        return PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_148_(),var.get('t').put('x', var.get('o'))),var.get('t').put('y', var.get('l'))),var.get('t'))
    PyJs_anonymous_147_._set_name('anonymous')
    @Js
    def PyJs_anonymous_149_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('s', ((var.get('t').get('x')-var.get(u"this").get('x0'))*(Js(1.0)/var.get(u"this").get('a'))))
        var.put('i', ((var.get('t').get('y')-var.get(u"this").get('y0'))*(Js(1.0)/var.get(u"this").get('a'))))
        PyJsComma(var.put('i', ((var.get('i')-var.get(u"this").get('Zb'))/var.get(u"this").get('Qn'))),var.put('s', var.get(u"this").get('Qn'), '/'))
        pass
        if (var.get('Math').callprop('abs', var.get('s'))<=Js(2.623395162778)):
            var.put('e', var.get('fs')(var.get(u"this").get('utg'), (Js(2.0)*var.get('i')), (Js(2.0)*var.get('s'))))
            PyJsComma(PyJsComma(var.put('i', var.get('e').get('0'), '+'),var.put('s', var.get('e').get('1'), '+')),var.put('s', var.get('Math').callprop('atan', var.get('ns')(var.get('s')))))
            var.put('n', var.get('Math').callprop('sin', var.get('i')))
            var.put('r', var.get('Math').callprop('cos', var.get('i')))
            var.put('o', var.get('Math').callprop('sin', var.get('s')))
            var.put('l', var.get('Math').callprop('cos', var.get('s')))
            def PyJs_LONG_150_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('Math').callprop('atan2', (var.get('n')*var.get('l')), var.get('rs')(var.get('o'), (var.get('l')*var.get('r'))))),var.put('s', var.get('Math').callprop('atan2', var.get('o'), (var.get('l')*var.get('r'))))),var.put('a', var.get('qt')((var.get('s')+var.get(u"this").get('long0'))))),var.put('h', var.get('Ms')(var.get(u"this").get('cgb'), var.get('i'))))
            PyJs_LONG_150_()
        else:
            PyJsComma(var.put('a', (Js(1.0)/Js(0.0))),var.put('h', (Js(1.0)/Js(0.0))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('a')),var.get('t').put('y', var.get('h'))),var.get('t'))
    PyJs_anonymous_149_._set_name('anonymous')
    var.put('ms', Js({'init':PyJs_anonymous_144_,'forward':PyJs_anonymous_147_,'inverse':PyJs_anonymous_149_,'names':Js([Js('Extended_Transverse_Mercator'), Js('Extended Transverse Mercator'), Js('etmerc')])}))
    @Js
    def PyJs_anonymous_151_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('t')):
            if (var.put('t', (var.get('Math').callprop('floor', ((Js(30.0)*(var.get('qt')(var.get('s'))+var.get('Math').get('PI')))/var.get('Math').get('PI')))+Js(1.0)))<Js(0.0)):
                return Js(0.0)
            if (var.get('t')>Js(60.0)):
                return Js(60.0)
        return var.get('t')
    PyJs_anonymous_151_._set_name('anonymous')
    var.put('ps', PyJs_anonymous_151_)
    @Js
    def PyJs_anonymous_152_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        var.put('t', var.get('ps')(var.get(u"this").get('zone'), var.get(u"this").get('long0')))
        if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('t')):
            PyJsTempException = JsToPyException(var.get('Error').create(Js('unknown utm zone')))
            raise PyJsTempException
        def PyJs_LONG_153_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('lat0', Js(0.0)),var.get(u"this").put('long0', (((Js(6.0)*var.get('Math').callprop('abs', var.get('t')))-Js(183.0))*var.get('lt')))),var.get(u"this").put('x0', Js(500000.0))),var.get(u"this").put('y0', (Js(10000000.0) if var.get(u"this").get('utmSouth') else Js(0.0)))),var.get(u"this").put('k0', Js(0.9996))),var.get('ms').get('init').callprop('apply', var.get(u"this"))),var.get(u"this").put('forward', var.get('ms').get('forward'))),var.get(u"this").put('inverse', var.get('ms').get('inverse')))
        PyJs_LONG_153_()
    PyJs_anonymous_152_._set_name('anonymous')
    var.put('ds', Js({'init':PyJs_anonymous_152_,'names':Js([Js('Universal Transverse Mercator System'), Js('utm')]),'dependsOn':Js('etmerc')}))
    @Js
    def PyJs_anonymous_154_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        return var.get('Math').callprop('pow', ((Js(1.0)-var.get('t'))/(Js(1.0)+var.get('t'))), var.get('s'))
    PyJs_anonymous_154_._set_name('anonymous')
    var.put('ys', PyJs_anonymous_154_)
    var.put('_s', Js(20.0))
    @Js
    def PyJs_anonymous_155_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('t', var.get('Math').callprop('sin', var.get(u"this").get('lat0')))
        var.put('s', var.get('Math').callprop('cos', var.get(u"this").get('lat0')))
        def PyJs_LONG_156_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('s'), '*'),var.get(u"this").put('rc', (var.get('Math').callprop('sqrt', (Js(1.0)-var.get(u"this").get('es')))/(Js(1.0)-((var.get(u"this").get('es')*var.get('t'))*var.get('t')))))),var.get(u"this").put('C', var.get('Math').callprop('sqrt', (Js(1.0)+(((var.get(u"this").get('es')*var.get('s'))*var.get('s'))/(Js(1.0)-var.get(u"this").get('es'))))))),var.get(u"this").put('phic0', var.get('Math').callprop('asin', (var.get('t')/var.get(u"this").get('C'))))),var.get(u"this").put('ratexp', ((Js(0.5)*var.get(u"this").get('C'))*var.get(u"this").get('e')))),var.get(u"this").put('K', (var.get('Math').callprop('tan', ((Js(0.5)*var.get(u"this").get('phic0'))+var.get('ct')))/(var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((Js(0.5)*var.get(u"this").get('lat0'))+var.get('ct'))), var.get(u"this").get('C'))*var.get('ys')((var.get(u"this").get('e')*var.get('t')), var.get(u"this").get('ratexp'))))))
        PyJs_LONG_156_()
    PyJs_anonymous_155_._set_name('anonymous')
    @Js
    def PyJs_anonymous_157_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        def PyJs_LONG_158_(var=var):
            return PyJsComma(PyJsComma(var.get('t').put('y', ((Js(2.0)*var.get('Math').callprop('atan', ((var.get(u"this").get('K')*var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((Js(0.5)*var.get('i'))+var.get('ct'))), var.get(u"this").get('C')))*var.get('ys')((var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('i'))), var.get(u"this").get('ratexp')))))-var.get('ht'))),var.get('t').put('x', (var.get(u"this").get('C')*var.get('s')))),var.get('t'))
        return PyJs_LONG_158_()
    PyJs_anonymous_157_._set_name('anonymous')
    @Js
    def PyJs_anonymous_159_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        #for JS loop
        var.put('s', (var.get('t').get('x')/var.get(u"this").get('C')))
        var.put('i', var.get('t').get('y'))
        var.put('a', var.get('Math').callprop('pow', (var.get('Math').callprop('tan', ((Js(0.5)*var.get('i'))+var.get('ct')))/var.get(u"this").get('K')), (Js(1.0)/var.get(u"this").get('C'))))
        var.put('h', var.get('_s'))
        while ((var.get('h')>Js(0.0)) and PyJsComma(var.put('i', ((Js(2.0)*var.get('Math').callprop('atan', (var.get('a')*var.get('ys')((var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('t').get('y'))), ((-Js(0.5))*var.get(u"this").get('e'))))))-var.get('ht'))),(var.get('Math').callprop('abs', (var.get('i')-var.get('t').get('y')))<Js(1e-14)).neg())):
            try:
                var.get('t').put('y', var.get('i'))
            finally:
                    var.put('h',Js(var.get('h').to_number())-Js(1))
        return (PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t')) if var.get('h') else var.get(u"null"))
    PyJs_anonymous_159_._set_name('anonymous')
    var.put('xs', Js({'init':PyJs_anonymous_155_,'forward':PyJs_anonymous_157_,'inverse':PyJs_anonymous_159_,'names':Js([Js('gauss')])}))
    @Js
    def PyJs_anonymous_160_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_161_(var=var):
            return (var.get(u"this").get('rc') and PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('sinc0', var.get('Math').callprop('sin', var.get(u"this").get('phic0'))),var.get(u"this").put('cosc0', var.get('Math').callprop('cos', var.get(u"this").get('phic0')))),var.get(u"this").put('R2', (Js(2.0)*var.get(u"this").get('rc')))),(var.get(u"this").get('title') or var.get(u"this").put('title', Js('Oblique Stereographic Alternative')))))
        PyJsComma(var.get('xs').get('init').callprop('apply', var.get(u"this")),PyJs_LONG_161_())
    PyJs_anonymous_160_._set_name('anonymous')
    @Js
    def PyJs_anonymous_162_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_163_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get('qt')((var.get('t').get('x')-var.get(u"this").get('long0')))),var.get('xs').get('forward').callprop('apply', var.get(u"this"), Js([var.get('t')]))),var.put('s', var.get('Math').callprop('sin', var.get('t').get('y')))),var.put('i', var.get('Math').callprop('cos', var.get('t').get('y')))),var.put('a', var.get('Math').callprop('cos', var.get('t').get('x')))),var.put('h', ((var.get(u"this").get('k0')*var.get(u"this").get('R2'))/((Js(1.0)+(var.get(u"this").get('sinc0')*var.get('s')))+((var.get(u"this").get('cosc0')*var.get('i'))*var.get('a')))))),var.get('t').put('x', ((var.get('h')*var.get('i'))*var.get('Math').callprop('sin', var.get('t').get('x'))))),var.get('t').put('y', (var.get('h')*((var.get(u"this").get('cosc0')*var.get('s'))-((var.get(u"this").get('sinc0')*var.get('i'))*var.get('a')))))),var.get('t').put('x', ((var.get(u"this").get('a')*var.get('t').get('x'))+var.get(u"this").get('x0')))),var.get('t').put('y', ((var.get(u"this").get('a')*var.get('t').get('y'))+var.get(u"this").get('y0')))),var.get('t'))
        return PyJs_LONG_163_()
    PyJs_anonymous_162_._set_name('anonymous')
    @Js
    def PyJs_anonymous_164_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_165_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', ((var.get('t').get('x')-var.get(u"this").get('x0'))/var.get(u"this").get('a'))),var.get('t').put('y', ((var.get('t').get('y')-var.get(u"this").get('y0'))/var.get(u"this").get('a')))),var.get('t').put('x', var.get(u"this").get('k0'), '/')),var.get('t').put('y', var.get(u"this").get('k0'), '/')),var.put('e', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y'))))))
        if PyJs_LONG_165_():
            var.put('n', (Js(2.0)*var.get('Math').callprop('atan2', var.get('e'), var.get(u"this").get('R2'))))
            def PyJs_LONG_166_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('Math').callprop('sin', var.get('n'))),var.put('i', var.get('Math').callprop('cos', var.get('n')))),var.put('h', var.get('Math').callprop('asin', ((var.get('i')*var.get(u"this").get('sinc0'))+(((var.get('t').get('y')*var.get('s'))*var.get(u"this").get('cosc0'))/var.get('e')))))),var.put('a', var.get('Math').callprop('atan2', (var.get('t').get('x')*var.get('s')), (((var.get('e')*var.get(u"this").get('cosc0'))*var.get('i'))-((var.get('t').get('y')*var.get(u"this").get('sinc0'))*var.get('s'))))))
            PyJs_LONG_166_()
        else:
            PyJsComma(var.put('h', var.get(u"this").get('phic0')),var.put('a', Js(0.0)))
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get('a')),var.get('t').put('y', var.get('h'))),var.get('xs').get('inverse').callprop('apply', var.get(u"this"), Js([var.get('t')]))),var.get('t').put('x', var.get('qt')((var.get('t').get('x')+var.get(u"this").get('long0'))))),var.get('t'))
    PyJs_anonymous_164_._set_name('anonymous')
    var.put('vs', Js({'init':PyJs_anonymous_160_,'forward':PyJs_anonymous_162_,'inverse':PyJs_anonymous_164_,'names':Js([Js('Stereographic_North_Pole'), Js('Oblique_Stereographic'), Js('Polar_Stereographic'), Js('sterea'), Js('Oblique Stereographic Alternative'), Js('Double_Stereographic')])}))
    @Js
    def PyJs_anonymous_167_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_170_(var=var):
            def PyJs_LONG_169_(var=var):
                def PyJs_LONG_168_(var=var):
                    return (((Js(0.5)*var.get(u"this").get('cons'))*var.get('St')(var.get(u"this").get('e'), var.get('Math').callprop('sin', var.get(u"this").get('lat_ts')), var.get('Math').callprop('cos', var.get(u"this").get('lat_ts'))))/var.get('It')(var.get(u"this").get('e'), (var.get(u"this").get('con')*var.get(u"this").get('lat_ts')), (var.get(u"this").get('con')*var.get('Math').callprop('sin', var.get(u"this").get('lat_ts')))))
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get('Math').callprop('abs', var.get(u"this").get('coslat0'))<=var.get('ot')) and (var.get(u"this").put('con', Js(1.0)) if (var.get(u"this").get('lat0')>Js(0.0)) else var.get(u"this").put('con', (-Js(1.0))))),var.get(u"this").put('cons', var.get('Math').callprop('sqrt', (var.get('Math').callprop('pow', (Js(1.0)+var.get(u"this").get('e')), (Js(1.0)+var.get(u"this").get('e')))*var.get('Math').callprop('pow', (Js(1.0)-var.get(u"this").get('e')), (Js(1.0)-var.get(u"this").get('e'))))))),(((PyJsStrictEq(Js(1.0),var.get(u"this").get('k0')) and var.get('isNaN')(var.get(u"this").get('lat_ts')).neg()) and (var.get('Math').callprop('abs', var.get(u"this").get('coslat0'))<=var.get('ot'))) and var.get(u"this").put('k0', PyJs_LONG_168_()))),var.get(u"this").put('ms1', var.get('St')(var.get(u"this").get('e'), var.get(u"this").get('sinlat0'), var.get(u"this").get('coslat0')))),var.get(u"this").put('X0', ((Js(2.0)*var.get('Math').callprop('atan', var.get(u"this").callprop('ssfn_', var.get(u"this").get('lat0'), var.get(u"this").get('sinlat0'), var.get(u"this").get('e'))))-var.get('ht')))),var.get(u"this").put('cosX0', var.get('Math').callprop('cos', var.get(u"this").get('X0')))),var.get(u"this").put('sinX0', var.get('Math').callprop('sin', var.get(u"this").get('X0'))))
            return ((((PyJsStrictEq(Js(1.0),var.get(u"this").get('k0')) and var.get('isNaN')(var.get(u"this").get('lat_ts')).neg()) and (var.get('Math').callprop('abs', var.get(u"this").get('coslat0'))<=var.get('ot'))) and var.get(u"this").put('k0', (Js(0.5)*(Js(1.0)+(var.get('kt')(var.get(u"this").get('lat0'))*var.get('Math').callprop('sin', var.get(u"this").get('lat_ts'))))))) if var.get(u"this").get('sphere') else PyJs_LONG_169_())
        PyJsComma(PyJsComma(var.get(u"this").put('coslat0', var.get('Math').callprop('cos', var.get(u"this").get('lat0'))),var.get(u"this").put('sinlat0', var.get('Math').callprop('sin', var.get(u"this").get('lat0')))),PyJs_LONG_170_())
    PyJs_anonymous_167_._set_name('anonymous')
    @Js
    def PyJs_anonymous_171_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('r', var.get('t').get('x'))
        var.put('o', var.get('t').get('y'))
        var.put('l', var.get('Math').callprop('sin', var.get('o')))
        var.put('M', var.get('Math').callprop('cos', var.get('o')))
        var.put('c', var.get('qt')((var.get('r')-var.get(u"this").get('long0'))))
        def PyJs_LONG_177_(var=var):
            def PyJs_LONG_172_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(var.put('s', ((Js(2.0)*var.get(u"this").get('k0'))/((Js(1.0)+(var.get(u"this").get('sinlat0')*var.get('l')))+((var.get(u"this").get('coslat0')*var.get('M'))*var.get('Math').callprop('cos', var.get('c')))))),var.get('t').put('x', ((((var.get(u"this").get('a')*var.get('s'))*var.get('M'))*var.get('Math').callprop('sin', var.get('c')))+var.get(u"this").get('x0')))),var.get('t').put('y', (((var.get(u"this").get('a')*var.get('s'))*((var.get(u"this").get('coslat0')*var.get('l'))-((var.get(u"this").get('sinlat0')*var.get('M'))*var.get('Math').callprop('cos', var.get('c')))))+var.get(u"this").get('y0')))),var.get('t'))
            def PyJs_LONG_176_(var=var):
                def PyJs_LONG_173_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('e', var.get('It')(var.get(u"this").get('e'), (var.get('o')*var.get(u"this").get('con')), (var.get(u"this").get('con')*var.get('l')))),var.put('n', ((((Js(2.0)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))*var.get('e'))/var.get(u"this").get('cons')))),var.get('t').put('x', (var.get(u"this").get('x0')+(var.get('n')*var.get('Math').callprop('sin', (var.get('r')-var.get(u"this").get('long0'))))))),var.get('t').put('y', (var.get(u"this").get('y0')-((var.get(u"this").get('con')*var.get('n'))*var.get('Math').callprop('cos', (var.get('r')-var.get(u"this").get('long0'))))))),var.get('t'))
                def PyJs_LONG_175_(var=var):
                    def PyJs_LONG_174_(var=var):
                        return PyJsComma(var.put('s', ((((Js(2.0)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))*var.get(u"this").get('ms1'))/(var.get(u"this").get('cosX0')*((Js(1.0)+(var.get(u"this").get('sinX0')*var.get('a')))+((var.get(u"this").get('cosX0')*var.get('h'))*var.get('Math').callprop('cos', var.get('c'))))))),var.get('t').put('y', ((var.get('s')*((var.get(u"this").get('cosX0')*var.get('a'))-((var.get(u"this").get('sinX0')*var.get('h'))*var.get('Math').callprop('cos', var.get('c')))))+var.get(u"this").get('y0'))))
                    return PyJsComma(PyJsComma((PyJsComma(var.put('s', (((Js(2.0)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))/(Js(1.0)+(var.get('h')*var.get('Math').callprop('cos', var.get('c')))))),var.get('t').put('y', (var.get('s')*var.get('a')))) if (var.get('Math').callprop('abs', var.get(u"this").get('sinlat0'))<var.get('ot')) else PyJs_LONG_174_()),var.get('t').put('x', (((var.get('s')*var.get('h'))*var.get('Math').callprop('sin', var.get('c')))+var.get(u"this").get('x0')))),var.get('t'))
                return PyJsComma(PyJsComma(PyJsComma(var.put('i', ((Js(2.0)*var.get('Math').callprop('atan', var.get(u"this").callprop('ssfn_', var.get('o'), var.get('l'), var.get(u"this").get('e'))))-var.get('ht'))),var.put('h', var.get('Math').callprop('cos', var.get('i')))),var.put('a', var.get('Math').callprop('sin', var.get('i')))),(PyJs_LONG_173_() if (var.get('Math').callprop('abs', var.get(u"this").get('coslat0'))<=var.get('ot')) else PyJs_LONG_175_()))
            return (PyJsComma(PyJsComma(var.get('t').put('x', var.get('NaN')),var.get('t').put('y', var.get('NaN'))),var.get('t')) if ((var.get('Math').callprop('abs', (var.get('Math').callprop('abs', (var.get('r')-var.get(u"this").get('long0')))-var.get('Math').get('PI')))<=var.get('ot')) and (var.get('Math').callprop('abs', (var.get('o')+var.get(u"this").get('lat0')))<=var.get('ot'))) else (PyJs_LONG_172_() if var.get(u"this").get('sphere') else PyJs_LONG_176_()))
        return PyJs_LONG_177_()
    PyJs_anonymous_171_._set_name('anonymous')
    @Js
    def PyJs_anonymous_178_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-'))
        var.put('n', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))
        if var.get(u"this").get('sphere'):
            var.put('r', (Js(2.0)*var.get('Math').callprop('atan', (var.get('n')/((Js(2.0)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))))))
            def PyJs_LONG_180_(var=var):
                def PyJs_LONG_179_(var=var):
                    return (((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', var.get('t').get('x'), ((-Js(1.0))*var.get('t').get('y')))) if (var.get(u"this").get('lat0')>Js(0.0)) else (var.get(u"this").get('long0')+var.get('Math').callprop('atan2', var.get('t').get('x'), var.get('t').get('y')))) if (var.get('Math').callprop('abs', var.get(u"this").get('coslat0'))<var.get('ot')) else (var.get(u"this").get('long0')+var.get('Math').callprop('atan2', (var.get('t').get('x')*var.get('Math').callprop('sin', var.get('r'))), (((var.get('n')*var.get(u"this").get('coslat0'))*var.get('Math').callprop('cos', var.get('r')))-((var.get('t').get('y')*var.get(u"this").get('sinlat0'))*var.get('Math').callprop('sin', var.get('r')))))))
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get('r'))*var.get(u"this").get('sinlat0'))+(((var.get('t').get('y')*var.get('Math').callprop('sin', var.get('r')))*var.get(u"this").get('coslat0'))/var.get('n'))))),var.put('s', var.get('qt')(PyJs_LONG_179_()))),var.get('t').put('x', var.get('s'))),var.get('t').put('y', var.get('i'))),var.get('t'))
            return PyJsComma(PyJsComma(var.put('s', var.get(u"this").get('long0')),var.put('i', var.get(u"this").get('lat0'))),(PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t')) if (var.get('n')<=var.get('ot')) else PyJs_LONG_180_()))
        if (var.get('Math').callprop('abs', var.get(u"this").get('coslat0'))<=var.get('ot')):
            if (var.get('n')<=var.get('ot')):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get(u"this").get('lat0')),var.put('s', var.get(u"this").get('long0'))),var.get('t').put('x', var.get('s'))),var.get('t').put('y', var.get('i'))),var.get('t'))
            def PyJs_LONG_181_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('con'), '*'),var.get('t').put('y', var.get(u"this").get('con'), '*')),var.put('a', ((var.get('n')*var.get(u"this").get('cons'))/((Js(2.0)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))))),var.put('i', (var.get(u"this").get('con')*var.get('Ot')(var.get(u"this").get('e'), var.get('a'))))),var.put('s', (var.get(u"this").get('con')*var.get('qt')(((var.get(u"this").get('con')*var.get(u"this").get('long0'))+var.get('Math').callprop('atan2', var.get('t').get('x'), ((-Js(1.0))*var.get('t').get('y'))))))))
            PyJs_LONG_181_()
        else:
            def PyJs_LONG_183_(var=var):
                def PyJs_LONG_182_(var=var):
                    return PyJsComma(var.put('e', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get('h'))*var.get(u"this").get('sinX0'))+(((var.get('t').get('y')*var.get('Math').callprop('sin', var.get('h')))*var.get(u"this").get('cosX0'))/var.get('n'))))),var.put('s', var.get('qt')((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', (var.get('t').get('x')*var.get('Math').callprop('sin', var.get('h'))), (((var.get('n')*var.get(u"this").get('cosX0'))*var.get('Math').callprop('cos', var.get('h')))-((var.get('t').get('y')*var.get(u"this").get('sinX0'))*var.get('Math').callprop('sin', var.get('h')))))))))
                return PyJsComma(PyJsComma(PyJsComma(var.put('h', (Js(2.0)*var.get('Math').callprop('atan', ((var.get('n')*var.get(u"this").get('cosX0'))/(((Js(2.0)*var.get(u"this").get('a'))*var.get(u"this").get('k0'))*var.get(u"this").get('ms1')))))),var.put('s', var.get(u"this").get('long0'))),(var.put('e', var.get(u"this").get('X0')) if (var.get('n')<=var.get('ot')) else PyJs_LONG_182_())),var.put('i', ((-Js(1.0))*var.get('Ot')(var.get(u"this").get('e'), var.get('Math').callprop('tan', (Js(0.5)*(var.get('ht')+var.get('e'))))))))
            PyJs_LONG_183_()
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_178_._set_name('anonymous')
    @Js
    def PyJs_anonymous_184_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        return PyJsComma(var.put('s', var.get('i'), '*'),(var.get('Math').callprop('tan', (Js(0.5)*(var.get('ht')+var.get('t'))))*var.get('Math').callprop('pow', ((Js(1.0)-var.get('s'))/(Js(1.0)+var.get('s'))), (Js(0.5)*var.get('i')))))
    PyJs_anonymous_184_._set_name('anonymous')
    var.put('gs', Js({'init':PyJs_anonymous_167_,'forward':PyJs_anonymous_171_,'inverse':PyJs_anonymous_178_,'names':Js([Js('stere'), Js('Stereographic_South_Pole'), Js('Polar Stereographic (variant B)')]),'ssfn_':PyJs_anonymous_184_}))
    @Js
    def PyJs_anonymous_185_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('t', var.get(u"this").get('lat0'))
        var.get(u"this").put('lambda0', var.get(u"this").get('long0'))
        var.put('s', var.get('Math').callprop('sin', var.get('t')))
        var.put('i', var.get(u"this").get('a'))
        var.put('a', (Js(1.0)/var.get(u"this").get('rf')))
        var.put('h', ((Js(2.0)*var.get('a'))-var.get('Math').callprop('pow', var.get('a'), Js(2.0))))
        var.put('e', var.get(u"this").put('e', var.get('Math').callprop('sqrt', var.get('h'))))
        def PyJs_LONG_186_(var=var):
            return PyJsComma(PyJsComma(var.get(u"this").put('R', (((var.get(u"this").get('k0')*var.get('i'))*var.get('Math').callprop('sqrt', (Js(1.0)-var.get('h'))))/(Js(1.0)-(var.get('h')*var.get('Math').callprop('pow', var.get('s'), Js(2.0)))))),var.get(u"this").put('alpha', var.get('Math').callprop('sqrt', (Js(1.0)+((var.get('h')/(Js(1.0)-var.get('h')))*var.get('Math').callprop('pow', var.get('Math').callprop('cos', var.get('t')), Js(4.0))))))),var.get(u"this").put('b0', var.get('Math').callprop('asin', (var.get('s')/var.get(u"this").get('alpha')))))
        PyJs_LONG_186_()
        var.put('n', var.get('Math').callprop('log', var.get('Math').callprop('tan', ((var.get('Math').get('PI')/Js(4.0))+(var.get(u"this").get('b0')/Js(2.0))))))
        var.put('r', var.get('Math').callprop('log', var.get('Math').callprop('tan', ((var.get('Math').get('PI')/Js(4.0))+(var.get('t')/Js(2.0))))))
        var.put('o', var.get('Math').callprop('log', ((Js(1.0)+(var.get('e')*var.get('s')))/(Js(1.0)-(var.get('e')*var.get('s'))))))
        var.get(u"this").put('K', ((var.get('n')-(var.get(u"this").get('alpha')*var.get('r')))+(((var.get(u"this").get('alpha')*var.get('e'))/Js(2.0))*var.get('o'))))
    PyJs_anonymous_185_._set_name('anonymous')
    @Js
    def PyJs_anonymous_187_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('s', var.get('Math').callprop('log', var.get('Math').callprop('tan', ((var.get('Math').get('PI')/Js(4.0))-(var.get('t').get('y')/Js(2.0))))))
        var.put('i', ((var.get(u"this").get('e')/Js(2.0))*var.get('Math').callprop('log', ((Js(1.0)+(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('t').get('y'))))/(Js(1.0)-(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('t').get('y'))))))))
        var.put('a', (((-var.get(u"this").get('alpha'))*(var.get('s')+var.get('i')))+var.get(u"this").get('K')))
        var.put('h', (Js(2.0)*(var.get('Math').callprop('atan', var.get('Math').callprop('exp', var.get('a')))-(var.get('Math').get('PI')/Js(4.0)))))
        var.put('e', (var.get(u"this").get('alpha')*(var.get('t').get('x')-var.get(u"this").get('lambda0'))))
        var.put('n', var.get('Math').callprop('atan', (var.get('Math').callprop('sin', var.get('e'))/((var.get('Math').callprop('sin', var.get(u"this").get('b0'))*var.get('Math').callprop('tan', var.get('h')))+(var.get('Math').callprop('cos', var.get(u"this").get('b0'))*var.get('Math').callprop('cos', var.get('e')))))))
        var.put('r', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get(u"this").get('b0'))*var.get('Math').callprop('sin', var.get('h')))-((var.get('Math').callprop('sin', var.get(u"this").get('b0'))*var.get('Math').callprop('cos', var.get('h')))*var.get('Math').callprop('cos', var.get('e'))))))
        return PyJsComma(PyJsComma(var.get('t').put('y', (((var.get(u"this").get('R')/Js(2.0))*var.get('Math').callprop('log', ((Js(1.0)+var.get('Math').callprop('sin', var.get('r')))/(Js(1.0)-var.get('Math').callprop('sin', var.get('r'))))))+var.get(u"this").get('y0'))),var.get('t').put('x', ((var.get(u"this").get('R')*var.get('n'))+var.get(u"this").get('x0')))),var.get('t'))
    PyJs_anonymous_187_._set_name('anonymous')
    @Js
    def PyJs_anonymous_188_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        #for JS loop
        var.put('s', (var.get('t').get('x')-var.get(u"this").get('x0')))
        var.put('i', (var.get('t').get('y')-var.get(u"this").get('y0')))
        var.put('a', (var.get('s')/var.get(u"this").get('R')))
        var.put('h', (Js(2.0)*(var.get('Math').callprop('atan', var.get('Math').callprop('exp', (var.get('i')/var.get(u"this").get('R'))))-(var.get('Math').get('PI')/Js(4.0)))))
        var.put('e', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get(u"this").get('b0'))*var.get('Math').callprop('sin', var.get('h')))+((var.get('Math').callprop('sin', var.get(u"this").get('b0'))*var.get('Math').callprop('cos', var.get('h')))*var.get('Math').callprop('cos', var.get('a'))))))
        var.put('n', var.get('Math').callprop('atan', (var.get('Math').callprop('sin', var.get('a'))/((var.get('Math').callprop('cos', var.get(u"this").get('b0'))*var.get('Math').callprop('cos', var.get('a')))-(var.get('Math').callprop('sin', var.get(u"this").get('b0'))*var.get('Math').callprop('tan', var.get('h')))))))
        var.put('r', (var.get(u"this").get('lambda0')+(var.get('n')/var.get(u"this").get('alpha'))))
        var.put('o', Js(0.0))
        var.put('l', var.get('e'))
        var.put('M', (-Js(1000.0)))
        var.put('c', Js(0.0))
        while (var.get('Math').callprop('abs', (var.get('l')-var.get('M')))>Js(1e-07)):
            if (var.put('c',Js(var.get('c').to_number())+Js(1))>Js(20.0)):
                return var.get('undefined')
            def PyJs_LONG_189_(var=var):
                return (((Js(1.0)/var.get(u"this").get('alpha'))*(var.get('Math').callprop('log', var.get('Math').callprop('tan', ((var.get('Math').get('PI')/Js(4.0))+(var.get('e')/Js(2.0)))))-var.get(u"this").get('K')))+(var.get(u"this").get('e')*var.get('Math').callprop('log', var.get('Math').callprop('tan', ((var.get('Math').get('PI')/Js(4.0))+(var.get('Math').callprop('asin', (var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('l'))))/Js(2.0)))))))
            PyJsComma(PyJsComma(var.put('o', PyJs_LONG_189_()),var.put('M', var.get('l'))),var.put('l', ((Js(2.0)*var.get('Math').callprop('atan', var.get('Math').callprop('exp', var.get('o'))))-(var.get('Math').get('PI')/Js(2.0)))))
        
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('r')),var.get('t').put('y', var.get('l'))),var.get('t'))
    PyJs_anonymous_188_._set_name('anonymous')
    var.put('bs', Js({'init':PyJs_anonymous_185_,'forward':PyJs_anonymous_187_,'inverse':PyJs_anonymous_188_,'names':Js([Js('somerc')])}))
    @Js
    def PyJs_anonymous_190_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'f', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        PyJsComma(PyJsComma(var.get(u"this").put('no_off', (var.get(u"this").get('no_off') or Js(1.0).neg())),var.get(u"this").put('no_rot', (var.get(u"this").get('no_rot') or Js(1.0).neg()))),(var.get('isNaN')(var.get(u"this").get('k0')) and var.get(u"this").put('k0', Js(1.0))))
        var.put('t', var.get('Math').callprop('sin', var.get(u"this").get('lat0')))
        var.put('s', var.get('Math').callprop('cos', var.get(u"this").get('lat0')))
        var.put('i', (var.get(u"this").get('e')*var.get('t')))
        def PyJs_LONG_191_(var=var):
            return PyJsComma(var.get(u"this").put('bl', var.get('Math').callprop('sqrt', (Js(1.0)+((var.get(u"this").get('es')/(Js(1.0)-var.get(u"this").get('es')))*var.get('Math').callprop('pow', var.get('s'), Js(4.0)))))),var.get(u"this").put('al', ((((var.get(u"this").get('a')*var.get(u"this").get('bl'))*var.get(u"this").get('k0'))*var.get('Math').callprop('sqrt', (Js(1.0)-var.get(u"this").get('es'))))/(Js(1.0)-(var.get('i')*var.get('i'))))))
        PyJs_LONG_191_()
        var.put('a', var.get('It')(var.get(u"this").get('e'), var.get(u"this").get('lat0'), var.get('t')))
        var.put('h', ((var.get(u"this").get('bl')/var.get('s'))*var.get('Math').callprop('sqrt', ((Js(1.0)-var.get(u"this").get('es'))/(Js(1.0)-(var.get('i')*var.get('i')))))))
        (((var.get('h')*var.get('h'))<Js(1.0)) and var.put('h', Js(1.0)))
        pass
        if var.get('isNaN')(var.get(u"this").get('longc')):
            var.put('r', var.get('It')(var.get(u"this").get('e'), var.get(u"this").get('lat1'), var.get('Math').callprop('sin', var.get(u"this").get('lat1'))))
            var.put('o', var.get('It')(var.get(u"this").get('e'), var.get(u"this").get('lat2'), var.get('Math').callprop('sin', var.get(u"this").get('lat2'))))
            def PyJs_LONG_192_(var=var):
                return (var.get(u"this").put('el', ((var.get('h')+var.get('Math').callprop('sqrt', ((var.get('h')*var.get('h'))-Js(1.0))))*var.get('Math').callprop('pow', var.get('a'), var.get(u"this").get('bl')))) if (var.get(u"this").get('lat0')>=Js(0.0)) else var.get(u"this").put('el', ((var.get('h')-var.get('Math').callprop('sqrt', ((var.get('h')*var.get('h'))-Js(1.0))))*var.get('Math').callprop('pow', var.get('a'), var.get(u"this").get('bl')))))
            PyJs_LONG_192_()
            var.put('l', var.get('Math').callprop('pow', var.get('r'), var.get(u"this").get('bl')))
            var.put('M', var.get('Math').callprop('pow', var.get('o'), var.get(u"this").get('bl')))
            var.put('n', (Js(0.5)*(var.put('e', (var.get(u"this").get('el')/var.get('l')))-(Js(1.0)/var.get('e')))))
            var.put('c', (((var.get(u"this").get('el')*var.get(u"this").get('el'))-(var.get('M')*var.get('l')))/((var.get(u"this").get('el')*var.get(u"this").get('el'))+(var.get('M')*var.get('l')))))
            var.put('u', ((var.get('M')-var.get('l'))/(var.get('M')+var.get('l'))))
            var.put('f', var.get('qt')((var.get(u"this").get('long1')-var.get(u"this").get('long2'))))
            PyJsComma(var.get(u"this").put('long0', ((Js(0.5)*(var.get(u"this").get('long1')+var.get(u"this").get('long2')))-(var.get('Math').callprop('atan', ((var.get('c')*var.get('Math').callprop('tan', ((Js(0.5)*var.get(u"this").get('bl'))*var.get('f'))))/var.get('u')))/var.get(u"this").get('bl')))),var.get(u"this").put('long0', var.get('qt')(var.get(u"this").get('long0'))))
            var.put('m', var.get('qt')((var.get(u"this").get('long1')-var.get(u"this").get('long0'))))
            PyJsComma(var.get(u"this").put('gamma0', var.get('Math').callprop('atan', (var.get('Math').callprop('sin', (var.get(u"this").get('bl')*var.get('m')))/var.get('n')))),var.get(u"this").put('alpha', var.get('Math').callprop('asin', (var.get('h')*var.get('Math').callprop('sin', var.get(u"this").get('gamma0'))))))
        else:
            def PyJs_LONG_193_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('e', ((var.get('h')+var.get('Math').callprop('sqrt', ((var.get('h')*var.get('h'))-Js(1.0)))) if (var.get(u"this").get('lat0')>=Js(0.0)) else (var.get('h')-var.get('Math').callprop('sqrt', ((var.get('h')*var.get('h'))-Js(1.0)))))),var.get(u"this").put('el', (var.get('e')*var.get('Math').callprop('pow', var.get('a'), var.get(u"this").get('bl'))))),var.put('n', (Js(0.5)*(var.get('e')-(Js(1.0)/var.get('e')))))),var.get(u"this").put('gamma0', var.get('Math').callprop('asin', (var.get('Math').callprop('sin', var.get(u"this").get('alpha'))/var.get('h'))))),var.get(u"this").put('long0', (var.get(u"this").get('longc')-(var.get('Math').callprop('asin', (var.get('n')*var.get('Math').callprop('tan', var.get(u"this").get('gamma0'))))/var.get(u"this").get('bl')))))
            PyJs_LONG_193_()
        def PyJs_LONG_194_(var=var):
            return (var.get(u"this").put('uc', ((var.get(u"this").get('al')/var.get(u"this").get('bl'))*var.get('Math').callprop('atan2', var.get('Math').callprop('sqrt', ((var.get('h')*var.get('h'))-Js(1.0))), var.get('Math').callprop('cos', var.get(u"this").get('alpha'))))) if (var.get(u"this").get('lat0')>=Js(0.0)) else var.get(u"this").put('uc', ((((-Js(1.0))*var.get(u"this").get('al'))/var.get(u"this").get('bl'))*var.get('Math').callprop('atan2', var.get('Math').callprop('sqrt', ((var.get('h')*var.get('h'))-Js(1.0))), var.get('Math').callprop('cos', var.get(u"this").get('alpha'))))))
        (var.get(u"this").put('uc', Js(0.0)) if var.get(u"this").get('no_off') else PyJs_LONG_194_())
    PyJs_anonymous_190_._set_name('anonymous')
    @Js
    def PyJs_anonymous_195_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('h', var.get('t').get('x'))
        var.put('e', var.get('t').get('y'))
        var.put('n', var.get('qt')((var.get('h')-var.get(u"this").get('long0'))))
        if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('e'))-var.get('ht')))<=var.get('ot')):
            def PyJs_LONG_196_(var=var):
                return PyJsComma(PyJsComma(var.put('a', ((-Js(1.0)) if (var.get('e')>Js(0.0)) else Js(1.0))),var.put('i', ((var.get(u"this").get('al')/var.get(u"this").get('bl'))*var.get('Math').callprop('log', var.get('Math').callprop('tan', (var.get('ct')+((var.get('a')*var.get(u"this").get('gamma0'))*Js(0.5)))))))),var.put('s', (((((-Js(1.0))*var.get('a'))*var.get('ht'))*var.get(u"this").get('al'))/var.get(u"this").get('bl'))))
            PyJs_LONG_196_()
        else:
            var.put('r', var.get('It')(var.get(u"this").get('e'), var.get('e'), var.get('Math').callprop('sin', var.get('e'))))
            var.put('o', (var.get(u"this").get('el')/var.get('Math').callprop('pow', var.get('r'), var.get(u"this").get('bl'))))
            var.put('l', (Js(0.5)*(var.get('o')-(Js(1.0)/var.get('o')))))
            var.put('M', (Js(0.5)*(var.get('o')+(Js(1.0)/var.get('o')))))
            var.put('c', var.get('Math').callprop('sin', (var.get(u"this").get('bl')*var.get('n'))))
            var.put('u', (((var.get('l')*var.get('Math').callprop('sin', var.get(u"this").get('gamma0')))-(var.get('c')*var.get('Math').callprop('cos', var.get(u"this").get('gamma0'))))/var.get('M')))
            def PyJs_LONG_197_(var=var):
                return (((var.get(u"this").get('al')*var.get(u"this").get('bl'))*var.get('n')) if (var.get('Math').callprop('abs', var.get('Math').callprop('cos', (var.get(u"this").get('bl')*var.get('n'))))<=var.get('ot')) else ((var.get(u"this").get('al')*var.get('Math').callprop('atan2', ((var.get('l')*var.get('Math').callprop('cos', var.get(u"this").get('gamma0')))+(var.get('c')*var.get('Math').callprop('sin', var.get(u"this").get('gamma0')))), var.get('Math').callprop('cos', (var.get(u"this").get('bl')*var.get('n')))))/var.get(u"this").get('bl')))
            PyJsComma(var.put('i', (var.get('Number').get('POSITIVE_INFINITY') if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('u'))-Js(1.0)))<=var.get('ot')) else (((Js(0.5)*var.get(u"this").get('al'))*var.get('Math').callprop('log', ((Js(1.0)-var.get('u'))/(Js(1.0)+var.get('u')))))/var.get(u"this").get('bl')))),var.put('s', PyJs_LONG_197_()))
        def PyJs_LONG_198_(var=var):
            return PyJsComma(PyJsComma(var.put('s', var.get(u"this").get('uc'), '-'),var.get('t').put('x', ((var.get(u"this").get('x0')+(var.get('i')*var.get('Math').callprop('cos', var.get(u"this").get('alpha'))))+(var.get('s')*var.get('Math').callprop('sin', var.get(u"this").get('alpha')))))),var.get('t').put('y', ((var.get(u"this").get('y0')+(var.get('s')*var.get('Math').callprop('cos', var.get(u"this").get('alpha'))))-(var.get('i')*var.get('Math').callprop('sin', var.get(u"this").get('alpha'))))))
        return PyJsComma((PyJsComma(var.get('t').put('x', (var.get(u"this").get('x0')+var.get('s'))),var.get('t').put('y', (var.get(u"this").get('y0')+var.get('i')))) if var.get(u"this").get('no_rot') else PyJs_LONG_198_()),var.get('t'))
    PyJs_anonymous_195_._set_name('anonymous')
    @Js
    def PyJs_anonymous_199_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        pass
        def PyJs_LONG_200_(var=var):
            return PyJsComma(PyJsComma(var.put('i', (((var.get('t').get('x')-var.get(u"this").get('x0'))*var.get('Math').callprop('cos', var.get(u"this").get('alpha')))-((var.get('t').get('y')-var.get(u"this").get('y0'))*var.get('Math').callprop('sin', var.get(u"this").get('alpha'))))),var.put('s', (((var.get('t').get('y')-var.get(u"this").get('y0'))*var.get('Math').callprop('cos', var.get(u"this").get('alpha')))+((var.get('t').get('x')-var.get(u"this").get('x0'))*var.get('Math').callprop('sin', var.get(u"this").get('alpha')))))),var.put('s', var.get(u"this").get('uc'), '+'))
        (PyJsComma(var.put('i', (var.get('t').get('y')-var.get(u"this").get('y0'))),var.put('s', (var.get('t').get('x')-var.get(u"this").get('x0')))) if var.get(u"this").get('no_rot') else PyJs_LONG_200_())
        var.put('a', var.get('Math').callprop('exp', ((((-Js(1.0))*var.get(u"this").get('bl'))*var.get('i'))/var.get(u"this").get('al'))))
        var.put('h', (Js(0.5)*(var.get('a')-(Js(1.0)/var.get('a')))))
        var.put('e', (Js(0.5)*(var.get('a')+(Js(1.0)/var.get('a')))))
        var.put('n', var.get('Math').callprop('sin', ((var.get(u"this").get('bl')*var.get('s'))/var.get(u"this").get('al'))))
        var.put('r', (((var.get('n')*var.get('Math').callprop('cos', var.get(u"this").get('gamma0')))+(var.get('h')*var.get('Math').callprop('sin', var.get(u"this").get('gamma0'))))/var.get('e')))
        var.put('o', var.get('Math').callprop('pow', (var.get(u"this").get('el')/var.get('Math').callprop('sqrt', ((Js(1.0)+var.get('r'))/(Js(1.0)-var.get('r'))))), (Js(1.0)/var.get(u"this").get('bl'))))
        def PyJs_LONG_202_(var=var):
            def PyJs_LONG_201_(var=var):
                return PyJsComma(var.get('t').put('y', var.get('Ot')(var.get(u"this").get('e'), var.get('o'))),var.get('t').put('x', var.get('qt')((var.get(u"this").get('long0')-(var.get('Math').callprop('atan2', ((var.get('h')*var.get('Math').callprop('cos', var.get(u"this").get('gamma0')))-(var.get('n')*var.get('Math').callprop('sin', var.get(u"this").get('gamma0')))), var.get('Math').callprop('cos', ((var.get(u"this").get('bl')*var.get('s'))/var.get(u"this").get('al'))))/var.get(u"this").get('bl'))))))
            return PyJsComma((PyJsComma(var.get('t').put('x', var.get(u"this").get('long0')),var.get('t').put('y', var.get('ht'))) if (var.get('Math').callprop('abs', (var.get('r')-Js(1.0)))<var.get('ot')) else (PyJsComma(var.get('t').put('x', var.get(u"this").get('long0')),var.get('t').put('y', ((-Js(1.0))*var.get('ht')))) if (var.get('Math').callprop('abs', (var.get('r')+Js(1.0)))<var.get('ot')) else PyJs_LONG_201_())),var.get('t'))
        return PyJs_LONG_202_()
    PyJs_anonymous_199_._set_name('anonymous')
    var.put('ws', Js({'init':PyJs_anonymous_190_,'forward':PyJs_anonymous_195_,'inverse':PyJs_anonymous_199_,'names':Js([Js('Hotine_Oblique_Mercator'), Js('Hotine Oblique Mercator'), Js('Hotine_Oblique_Mercator_Azimuth_Natural_Origin'), Js('Hotine_Oblique_Mercator_Azimuth_Center'), Js('omerc')])}))
    @Js
    def PyJs_anonymous_203_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        def PyJs_LONG_204_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get(u"this").get('lat2') or var.get(u"this").put('lat2', var.get(u"this").get('lat1'))),(var.get(u"this").get('k0') or var.get(u"this").put('k0', Js(1.0)))),var.get(u"this").put('x0', (var.get(u"this").get('x0') or Js(0.0)))),var.get(u"this").put('y0', (var.get(u"this").get('y0') or Js(0.0)))),(var.get('Math').callprop('abs', (var.get(u"this").get('lat1')+var.get(u"this").get('lat2')))<var.get('ot')).neg())
        if PyJs_LONG_204_():
            var.put('t', (var.get(u"this").get('b')/var.get(u"this").get('a')))
            var.get(u"this").put('e', var.get('Math').callprop('sqrt', (Js(1.0)-(var.get('t')*var.get('t')))))
            var.put('s', var.get('Math').callprop('sin', var.get(u"this").get('lat1')))
            var.put('i', var.get('Math').callprop('cos', var.get(u"this").get('lat1')))
            var.put('a', var.get('St')(var.get(u"this").get('e'), var.get('s'), var.get('i')))
            var.put('h', var.get('It')(var.get(u"this").get('e'), var.get(u"this").get('lat1'), var.get('s')))
            var.put('e', var.get('Math').callprop('sin', var.get(u"this").get('lat2')))
            var.put('n', var.get('Math').callprop('cos', var.get(u"this").get('lat2')))
            var.put('r', var.get('St')(var.get(u"this").get('e'), var.get('e'), var.get('n')))
            var.put('o', var.get('It')(var.get(u"this").get('e'), var.get(u"this").get('lat2'), var.get('e')))
            var.put('l', var.get('It')(var.get(u"this").get('e'), var.get(u"this").get('lat0'), var.get('Math').callprop('sin', var.get(u"this").get('lat0'))))
            def PyJs_LONG_205_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get(u"this").put('ns', (var.get('Math').callprop('log', (var.get('a')/var.get('r')))/var.get('Math').callprop('log', (var.get('h')/var.get('o'))))) if (var.get('Math').callprop('abs', (var.get(u"this").get('lat1')-var.get(u"this").get('lat2')))>var.get('ot')) else var.get(u"this").put('ns', var.get('s'))),(var.get('isNaN')(var.get(u"this").get('ns')) and var.get(u"this").put('ns', var.get('s')))),var.get(u"this").put('f0', (var.get('a')/(var.get(u"this").get('ns')*var.get('Math').callprop('pow', var.get('h'), var.get(u"this").get('ns')))))),var.get(u"this").put('rh', ((var.get(u"this").get('a')*var.get(u"this").get('f0'))*var.get('Math').callprop('pow', var.get('l'), var.get(u"this").get('ns'))))),(var.get(u"this").get('title') or var.get(u"this").put('title', Js('Lambert Conformal Conic'))))
            PyJs_LONG_205_()
    PyJs_anonymous_203_._set_name('anonymous')
    @Js
    def PyJs_anonymous_206_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        ((var.get('Math').callprop('abs', ((Js(2.0)*var.get('Math').callprop('abs', var.get('i')))-var.get('Math').get('PI')))<=var.get('ot')) and var.put('i', (var.get('kt')(var.get('i'))*(var.get('ht')-(Js(2.0)*var.get('ot'))))))
        var.put('e', var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('i'))-var.get('ht'))))
        if (var.get('e')>var.get('ot')):
            PyJsComma(var.put('a', var.get('It')(var.get(u"this").get('e'), var.get('i'), var.get('Math').callprop('sin', var.get('i')))),var.put('h', ((var.get(u"this").get('a')*var.get(u"this").get('f0'))*var.get('Math').callprop('pow', var.get('a'), var.get(u"this").get('ns')))))
        else:
            if (var.put('e', (var.get('i')*var.get(u"this").get('ns')))<=Js(0.0)):
                return var.get(u"null")
            var.put('h', Js(0.0))
        var.put('n', (var.get(u"this").get('ns')*var.get('qt')((var.get('s')-var.get(u"this").get('long0')))))
        return PyJsComma(PyJsComma(var.get('t').put('x', ((var.get(u"this").get('k0')*(var.get('h')*var.get('Math').callprop('sin', var.get('n'))))+var.get(u"this").get('x0'))),var.get('t').put('y', ((var.get(u"this").get('k0')*(var.get(u"this").get('rh')-(var.get('h')*var.get('Math').callprop('cos', var.get('n')))))+var.get(u"this").get('y0')))),var.get('t'))
    PyJs_anonymous_206_._set_name('anonymous')
    @Js
    def PyJs_anonymous_207_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('n', ((var.get('t').get('x')-var.get(u"this").get('x0'))/var.get(u"this").get('k0')))
        var.put('r', (var.get(u"this").get('rh')-((var.get('t').get('y')-var.get(u"this").get('y0'))/var.get(u"this").get('k0'))))
        (PyJsComma(var.put('s', var.get('Math').callprop('sqrt', ((var.get('n')*var.get('n'))+(var.get('r')*var.get('r'))))),var.put('i', Js(1.0))) if (var.get(u"this").get('ns')>Js(0.0)) else PyJsComma(var.put('s', (-var.get('Math').callprop('sqrt', ((var.get('n')*var.get('n'))+(var.get('r')*var.get('r')))))),var.put('i', (-Js(1.0)))))
        var.put('o', Js(0.0))
        if PyJsComma((PyJsStrictNeq(Js(0.0),var.get('s')) and var.put('o', var.get('Math').callprop('atan2', (var.get('i')*var.get('n')), (var.get('i')*var.get('r'))))),(PyJsStrictNeq(Js(0.0),var.get('s')) or (var.get(u"this").get('ns')>Js(0.0)))):
            if PyJsComma(PyJsComma(var.put('i', (Js(1.0)/var.get(u"this").get('ns'))),var.put('a', var.get('Math').callprop('pow', (var.get('s')/(var.get(u"this").get('a')*var.get(u"this").get('f0'))), var.get('i')))),PyJsStrictEq((-Js(9999.0)),var.put('h', var.get('Ot')(var.get(u"this").get('e'), var.get('a'))))):
                return var.get(u"null")
        else:
            var.put('h', (-var.get('ht')))
        return PyJsComma(PyJsComma(PyJsComma(var.put('e', var.get('qt')(((var.get('o')/var.get(u"this").get('ns'))+var.get(u"this").get('long0')))),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('h'))),var.get('t'))
    PyJs_anonymous_207_._set_name('anonymous')
    var.put('As', Js({'init':PyJs_anonymous_203_,'forward':PyJs_anonymous_206_,'inverse':PyJs_anonymous_207_,'names':Js([Js('Lambert Tangential Conformal Conic Projection'), Js('Lambert_Conformal_Conic'), Js('Lambert_Conformal_Conic_2SP'), Js('lcc')])}))
    @Js
    def PyJs_anonymous_208_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_209_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('a', Js(6377397.155)),var.get(u"this").put('es', Js(0.006674372230614))),var.get(u"this").put('e', var.get('Math').callprop('sqrt', var.get(u"this").get('es')))),(var.get(u"this").get('lat0') or var.get(u"this").put('lat0', Js(0.863937979737193)))),(var.get(u"this").get('long0') or var.get(u"this").put('long0', Js(0.4334234309119251)))),(var.get(u"this").get('k0') or var.get(u"this").put('k0', Js(0.9999)))),var.get(u"this").put('s45', Js(0.785398163397448))),var.get(u"this").put('s90', (Js(2.0)*var.get(u"this").get('s45')))),var.get(u"this").put('fi0', var.get(u"this").get('lat0'))),var.get(u"this").put('e2', var.get(u"this").get('es'))),var.get(u"this").put('e', var.get('Math').callprop('sqrt', var.get(u"this").get('e2')))),var.get(u"this").put('alfa', var.get('Math').callprop('sqrt', (Js(1.0)+((var.get(u"this").get('e2')*var.get('Math').callprop('pow', var.get('Math').callprop('cos', var.get(u"this").get('fi0')), Js(4.0)))/(Js(1.0)-var.get(u"this").get('e2'))))))),var.get(u"this").put('uq', Js(1.04216856380474))),var.get(u"this").put('u0', var.get('Math').callprop('asin', (var.get('Math').callprop('sin', var.get(u"this").get('fi0'))/var.get(u"this").get('alfa'))))),var.get(u"this").put('g', var.get('Math').callprop('pow', ((Js(1.0)+(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get(u"this").get('fi0'))))/(Js(1.0)-(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get(u"this").get('fi0'))))), ((var.get(u"this").get('alfa')*var.get(u"this").get('e'))/Js(2.0))))),var.get(u"this").put('k', ((var.get('Math').callprop('tan', ((var.get(u"this").get('u0')/Js(2.0))+var.get(u"this").get('s45')))/var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((var.get(u"this").get('fi0')/Js(2.0))+var.get(u"this").get('s45'))), var.get(u"this").get('alfa')))*var.get(u"this").get('g')))),var.get(u"this").put('k1', var.get(u"this").get('k0'))),var.get(u"this").put('n0', ((var.get(u"this").get('a')*var.get('Math').callprop('sqrt', (Js(1.0)-var.get(u"this").get('e2'))))/(Js(1.0)-(var.get(u"this").get('e2')*var.get('Math').callprop('pow', var.get('Math').callprop('sin', var.get(u"this").get('fi0')), Js(2.0))))))),var.get(u"this").put('s0', Js(1.37008346281555))),var.get(u"this").put('n', var.get('Math').callprop('sin', var.get(u"this").get('s0')))),var.get(u"this").put('ro0', ((var.get(u"this").get('k1')*var.get(u"this").get('n0'))/var.get('Math').callprop('tan', var.get(u"this").get('s0'))))),var.get(u"this").put('ad', (var.get(u"this").get('s90')-var.get(u"this").get('uq'))))
        PyJs_LONG_209_()
    PyJs_anonymous_208_._set_name('anonymous')
    @Js
    def PyJs_anonymous_210_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('o', var.get('t').get('x'))
        var.put('l', var.get('t').get('y'))
        var.put('M', var.get('qt')((var.get('o')-var.get(u"this").get('long0'))))
        def PyJs_LONG_211_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('Math').callprop('pow', ((Js(1.0)+(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('l'))))/(Js(1.0)-(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('l'))))), ((var.get(u"this").get('alfa')*var.get(u"this").get('e'))/Js(2.0)))),var.put('i', (Js(2.0)*(var.get('Math').callprop('atan', ((var.get(u"this").get('k')*var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((var.get('l')/Js(2.0))+var.get(u"this").get('s45'))), var.get(u"this").get('alfa')))/var.get('s')))-var.get(u"this").get('s45'))))),var.put('a', ((-var.get('M'))*var.get(u"this").get('alfa')))),var.put('h', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get(u"this").get('ad'))*var.get('Math').callprop('sin', var.get('i')))+((var.get('Math').callprop('sin', var.get(u"this").get('ad'))*var.get('Math').callprop('cos', var.get('i')))*var.get('Math').callprop('cos', var.get('a'))))))),var.put('e', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get('i'))*var.get('Math').callprop('sin', var.get('a')))/var.get('Math').callprop('cos', var.get('h')))))),var.put('n', (var.get(u"this").get('n')*var.get('e')))),var.put('r', ((var.get(u"this").get('ro0')*var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((var.get(u"this").get('s0')/Js(2.0))+var.get(u"this").get('s45'))), var.get(u"this").get('n')))/var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((var.get('h')/Js(2.0))+var.get(u"this").get('s45'))), var.get(u"this").get('n'))))),var.get('t').put('y', ((var.get('r')*var.get('Math').callprop('cos', var.get('n')))/Js(1.0)))),var.get('t').put('x', ((var.get('r')*var.get('Math').callprop('sin', var.get('n')))/Js(1.0)))),(var.get(u"this").get('czech') or PyJsComma(var.get('t').put('y', (-Js(1.0)), '*'),var.get('t').put('x', (-Js(1.0)), '*')))),var.get('t'))
        return PyJs_LONG_211_()
    PyJs_anonymous_210_._set_name('anonymous')
    @Js
    def PyJs_anonymous_212_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('o', var.get('t').get('x'))
        def PyJs_LONG_213_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get('t').get('y')),var.get('t').put('y', var.get('o'))),(var.get(u"this").get('czech') or PyJsComma(var.get('t').put('y', (-Js(1.0)), '*'),var.get('t').put('x', (-Js(1.0)), '*')))),var.put('e', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))),var.put('h', (var.get('Math').callprop('atan2', var.get('t').get('y'), var.get('t').get('x'))/var.get('Math').callprop('sin', var.get(u"this").get('s0'))))),var.put('a', (Js(2.0)*(var.get('Math').callprop('atan', (var.get('Math').callprop('pow', (var.get(u"this").get('ro0')/var.get('e')), (Js(1.0)/var.get(u"this").get('n')))*var.get('Math').callprop('tan', ((var.get(u"this").get('s0')/Js(2.0))+var.get(u"this").get('s45')))))-var.get(u"this").get('s45'))))),var.put('s', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get(u"this").get('ad'))*var.get('Math').callprop('sin', var.get('a')))-((var.get('Math').callprop('sin', var.get(u"this").get('ad'))*var.get('Math').callprop('cos', var.get('a')))*var.get('Math').callprop('cos', var.get('h'))))))),var.put('i', var.get('Math').callprop('asin', ((var.get('Math').callprop('cos', var.get('a'))*var.get('Math').callprop('sin', var.get('h')))/var.get('Math').callprop('cos', var.get('s')))))),var.get('t').put('x', (var.get(u"this").get('long0')-(var.get('i')/var.get(u"this").get('alfa'))))),var.put('n', var.get('s'))),var.put('r', Js(0.0)))
        PyJs_LONG_213_()
        var.put('l', Js(0.0))
        while 1:
            def PyJs_LONG_214_(var=var):
                return ((var.get('Math').callprop('pow', var.get(u"this").get('k'), ((-Js(1.0))/var.get(u"this").get('alfa')))*var.get('Math').callprop('pow', var.get('Math').callprop('tan', ((var.get('s')/Js(2.0))+var.get(u"this").get('s45'))), (Js(1.0)/var.get(u"this").get('alfa'))))*var.get('Math').callprop('pow', ((Js(1.0)+(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('n'))))/(Js(1.0)-(var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('n'))))), (var.get(u"this").get('e')/Js(2.0))))
            PyJsComma(PyJsComma(PyJsComma(var.get('t').put('y', (Js(2.0)*(var.get('Math').callprop('atan', PyJs_LONG_214_())-var.get(u"this").get('s45')))),((var.get('Math').callprop('abs', (var.get('n')-var.get('t').get('y')))<Js(1e-10)) and var.put('r', Js(1.0)))),var.put('n', var.get('t').get('y'))),var.put('l', Js(1.0), '+'))
            if not (PyJsStrictEq(Js(0.0),var.get('r')) and (var.get('l')<Js(15.0))):
                break
        return (var.get(u"null") if (var.get('l')>=Js(15.0)) else var.get('t'))
    PyJs_anonymous_212_._set_name('anonymous')
    var.put('Cs', Js({'init':PyJs_anonymous_208_,'forward':PyJs_anonymous_210_,'inverse':PyJs_anonymous_212_,'names':Js([Js('Krovak'), Js('krovak')])}))
    @Js
    def PyJs_anonymous_215_(t, s, i, a, h, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'h':h, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        return ((((var.get('t')*var.get('h'))-(var.get('s')*var.get('Math').callprop('sin', (Js(2.0)*var.get('h')))))+(var.get('i')*var.get('Math').callprop('sin', (Js(4.0)*var.get('h')))))-(var.get('a')*var.get('Math').callprop('sin', (Js(6.0)*var.get('h')))))
    PyJs_anonymous_215_._set_name('anonymous')
    var.put('Es', PyJs_anonymous_215_)
    @Js
    def PyJs_anonymous_216_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (Js(1.0)-((Js(0.25)*var.get('t'))*(Js(1.0)+((var.get('t')/Js(16.0))*(Js(3.0)+(Js(1.25)*var.get('t')))))))
    PyJs_anonymous_216_._set_name('anonymous')
    var.put('Ps', PyJs_anonymous_216_)
    @Js
    def PyJs_anonymous_217_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return ((Js(0.375)*var.get('t'))*(Js(1.0)+((Js(0.25)*var.get('t'))*(Js(1.0)+(Js(0.46875)*var.get('t'))))))
    PyJs_anonymous_217_._set_name('anonymous')
    var.put('Ns', PyJs_anonymous_217_)
    @Js
    def PyJs_anonymous_218_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (((Js(0.05859375)*var.get('t'))*var.get('t'))*(Js(1.0)+(Js(0.75)*var.get('t'))))
    PyJs_anonymous_218_._set_name('anonymous')
    var.put('Ss', PyJs_anonymous_218_)
    @Js
    def PyJs_anonymous_219_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (((var.get('t')*var.get('t'))*var.get('t'))*(Js(35.0)/Js(3072.0)))
    PyJs_anonymous_219_._set_name('anonymous')
    var.put('ks', PyJs_anonymous_219_)
    @Js
    def PyJs_anonymous_220_(t, s, i, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 's'])
        var.put('a', (var.get('s')*var.get('i')))
        return (var.get('t')/var.get('Math').callprop('sqrt', (Js(1.0)-(var.get('a')*var.get('a')))))
    PyJs_anonymous_220_._set_name('anonymous')
    var.put('qs', PyJs_anonymous_220_)
    @Js
    def PyJs_anonymous_221_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (var.get('t') if (var.get('Math').callprop('abs', var.get('t'))<var.get('ht')) else (var.get('t')-(var.get('kt')(var.get('t'))*var.get('Math').get('PI'))))
    PyJs_anonymous_221_._set_name('anonymous')
    var.put('Is', PyJs_anonymous_221_)
    @Js
    def PyJs_anonymous_222_(t, s, i, a, h, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'i':i, 'a':a, 'h':h, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 'h', 'i', 's', 'r', 't', 'a'])
        pass
        var.put('e', (var.get('t')/var.get('s')))
        #for JS loop
        var.put('r', Js(0.0))
        while (var.get('r')<Js(15.0)):
            try:
                def PyJs_LONG_223_(var=var):
                    return ((var.get('t')-((((var.get('s')*var.get('e'))-(var.get('i')*var.get('Math').callprop('sin', (Js(2.0)*var.get('e')))))+(var.get('a')*var.get('Math').callprop('sin', (Js(4.0)*var.get('e')))))-(var.get('h')*var.get('Math').callprop('sin', (Js(6.0)*var.get('e'))))))/(((var.get('s')-((Js(2.0)*var.get('i'))*var.get('Math').callprop('cos', (Js(2.0)*var.get('e')))))+((Js(4.0)*var.get('a'))*var.get('Math').callprop('cos', (Js(4.0)*var.get('e')))))-((Js(6.0)*var.get('h'))*var.get('Math').callprop('cos', (Js(6.0)*var.get('e'))))))
                if PyJsComma(PyJsComma(var.put('n', PyJs_LONG_223_()),var.put('e', var.get('n'), '+')),(var.get('Math').callprop('abs', var.get('n'))<=Js(1e-10))):
                    return var.get('e')
            finally:
                    (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
        return var.get('NaN')
    PyJs_anonymous_222_._set_name('anonymous')
    var.put('Os', PyJs_anonymous_222_)
    @Js
    def PyJs_anonymous_224_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_225_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('e0', var.get('Ps')(var.get(u"this").get('es'))),var.get(u"this").put('e1', var.get('Ns')(var.get(u"this").get('es')))),var.get(u"this").put('e2', var.get('Ss')(var.get(u"this").get('es')))),var.get(u"this").put('e3', var.get('ks')(var.get(u"this").get('es')))),var.get(u"this").put('ml0', (var.get(u"this").get('a')*var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get(u"this").get('lat0')))))
        (var.get(u"this").get('sphere') or PyJs_LONG_225_())
    PyJs_anonymous_224_._set_name('anonymous')
    @Js
    def PyJs_anonymous_226_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('a', var.get('t').get('x'))
        var.put('h', var.get('t').get('y'))
        if PyJsComma(var.put('a', var.get('qt')((var.get('a')-var.get(u"this").get('long0')))),var.get(u"this").get('sphere')):
            PyJsComma(var.put('s', (var.get(u"this").get('a')*var.get('Math').callprop('asin', (var.get('Math').callprop('cos', var.get('h'))*var.get('Math').callprop('sin', var.get('a')))))),var.put('i', (var.get(u"this").get('a')*(var.get('Math').callprop('atan2', var.get('Math').callprop('tan', var.get('h')), var.get('Math').callprop('cos', var.get('a')))-var.get(u"this").get('lat0')))))
        else:
            var.put('e', var.get('Math').callprop('sin', var.get('h')))
            var.put('n', var.get('Math').callprop('cos', var.get('h')))
            var.put('r', var.get('qs')(var.get(u"this").get('a'), var.get(u"this").get('e'), var.get('e')))
            var.put('o', (var.get('Math').callprop('tan', var.get('h'))*var.get('Math').callprop('tan', var.get('h'))))
            var.put('l', (var.get('a')*var.get('Math').callprop('cos', var.get('h'))))
            var.put('M', (var.get('l')*var.get('l')))
            var.put('c', (((var.get(u"this").get('es')*var.get('n'))*var.get('n'))/(Js(1.0)-var.get(u"this").get('es'))))
            def PyJs_LONG_227_(var=var):
                return PyJsComma(var.put('s', ((var.get('r')*var.get('l'))*(Js(1.0)-((var.get('M')*var.get('o'))*((Js(1.0)/Js(6.0))-((((Js(8.0)-var.get('o'))+(Js(8.0)*var.get('c')))*var.get('M'))/Js(120.0))))))),var.put('i', (((var.get(u"this").get('a')*var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get('h')))-var.get(u"this").get('ml0'))+((((var.get('r')*var.get('e'))/var.get('n'))*var.get('M'))*(Js(0.5)+((((Js(5.0)-var.get('o'))+(Js(6.0)*var.get('c')))*var.get('M'))/Js(24.0)))))))
            PyJs_LONG_227_()
        return PyJsComma(PyJsComma(var.get('t').put('x', (var.get('s')+var.get(u"this").get('x0'))),var.get('t').put('y', (var.get('i')+var.get(u"this").get('y0')))),var.get('t'))
    PyJs_anonymous_226_._set_name('anonymous')
    @Js
    def PyJs_anonymous_228_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-'))
        var.put('a', (var.get('t').get('x')/var.get(u"this").get('a')))
        var.put('h', (var.get('t').get('y')/var.get(u"this").get('a')))
        if var.get(u"this").get('sphere'):
            var.put('e', (var.get('h')+var.get(u"this").get('lat0')))
            PyJsComma(var.put('s', var.get('Math').callprop('asin', (var.get('Math').callprop('sin', var.get('e'))*var.get('Math').callprop('cos', var.get('a'))))),var.put('i', var.get('Math').callprop('atan2', var.get('Math').callprop('tan', var.get('a')), var.get('Math').callprop('cos', var.get('e')))))
        else:
            var.put('n', ((var.get(u"this").get('ml0')/var.get(u"this").get('a'))+var.get('h')))
            var.put('r', var.get('Os')(var.get('n'), var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3')))
            if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('r'))-var.get('ht')))<=var.get('ot')):
                return PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('long0')),var.get('t').put('y', var.get('ht'))),((var.get('h')<Js(0.0)) and var.get('t').put('y', (-Js(1.0)), '*'))),var.get('t'))
            var.put('o', var.get('qs')(var.get(u"this").get('a'), var.get(u"this").get('e'), var.get('Math').callprop('sin', var.get('r'))))
            var.put('l', (((((var.get('o')*var.get('o'))*var.get('o'))/var.get(u"this").get('a'))/var.get(u"this").get('a'))*(Js(1.0)-var.get(u"this").get('es'))))
            var.put('M', var.get('Math').callprop('pow', var.get('Math').callprop('tan', var.get('r')), Js(2.0)))
            var.put('c', ((var.get('a')*var.get(u"this").get('a'))/var.get('o')))
            var.put('u', (var.get('c')*var.get('c')))
            def PyJs_LONG_229_(var=var):
                return PyJsComma(var.put('s', (var.get('r')-(((((var.get('o')*var.get('Math').callprop('tan', var.get('r')))/var.get('l'))*var.get('c'))*var.get('c'))*(Js(0.5)-((((Js(1.0)+(Js(3.0)*var.get('M')))*var.get('c'))*var.get('c'))/Js(24.0)))))),var.put('i', ((var.get('c')*(Js(1.0)-(var.get('u')*((var.get('M')/Js(3.0))+((((Js(1.0)+(Js(3.0)*var.get('M')))*var.get('M'))*var.get('u'))/Js(15.0))))))/var.get('Math').callprop('cos', var.get('r')))))
            PyJs_LONG_229_()
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('qt')((var.get('i')+var.get(u"this").get('long0')))),var.get('t').put('y', var.get('Is')(var.get('s')))),var.get('t'))
    PyJs_anonymous_228_._set_name('anonymous')
    var.put('Rs', Js({'init':PyJs_anonymous_224_,'forward':PyJs_anonymous_226_,'inverse':PyJs_anonymous_228_,'names':Js([Js('Cassini'), Js('Cassini_Soldner'), Js('cass')])}))
    @Js
    def PyJs_anonymous_230_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        pass
        return (PyJsComma(var.put('i', (var.get('t')*var.get('s'))),((Js(1.0)-(var.get('t')*var.get('t')))*((var.get('s')/(Js(1.0)-(var.get('i')*var.get('i'))))-((Js(0.5)/var.get('t'))*var.get('Math').callprop('log', ((Js(1.0)-var.get('i'))/(Js(1.0)+var.get('i')))))))) if (var.get('t')>Js(1e-07)) else (Js(2.0)*var.get('s')))
    PyJs_anonymous_230_._set_name('anonymous')
    var.put('Gs', PyJs_anonymous_230_)
    var.put('Ts', Js(0.3333333333333333))
    var.put('js', Js(0.17222222222222222))
    var.put('zs', Js(0.10257936507936508))
    var.put('Ls', Js(0.06388888888888888))
    var.put('Ds', Js(0.0664021164021164))
    var.put('Bs', Js(0.016415012942191543))
    @Js
    def PyJs_anonymous_231_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        var.put('t', var.get('Math').callprop('abs', var.get(u"this").get('lat0')))
        def PyJs_LONG_232_(var=var):
            return (var.get(u"this").put('mode', (var.get(u"this").get('S_POLE') if (var.get(u"this").get('lat0')<Js(0.0)) else var.get(u"this").get('N_POLE'))) if (var.get('Math').callprop('abs', (var.get('t')-var.get('ht')))<var.get('ot')) else (var.get(u"this").put('mode', var.get(u"this").get('EQUIT')) if (var.get('Math').callprop('abs', var.get('t'))<var.get('ot')) else var.get(u"this").put('mode', var.get(u"this").get('OBLIQ'))))
        if PyJsComma(PyJs_LONG_232_(),(var.get(u"this").get('es')>Js(0.0))):
            pass
            while 1:
                SWITCHED = False
                CONDITION = (PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('qp', var.get('Gs')(var.get(u"this").get('e'), Js(1.0))),var.get(u"this").put('mmf', (Js(0.5)/(Js(1.0)-var.get(u"this").get('es'))))),var.get(u"this").put('apa', var.get('K')(var.get(u"this").get('es')))),var.get(u"this").get('mode')))
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('N_POLE')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('S_POLE')):
                    SWITCHED = True
                    var.get(u"this").put('dd', Js(1.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('EQUIT')):
                    SWITCHED = True
                    PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('rq', var.get('Math').callprop('sqrt', (Js(0.5)*var.get(u"this").get('qp')))),var.get(u"this").put('dd', (Js(1.0)/var.get(u"this").get('rq')))),var.get(u"this").put('xmf', Js(1.0))),var.get(u"this").put('ymf', (Js(0.5)*var.get(u"this").get('qp'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('OBLIQ')):
                    SWITCHED = True
                    def PyJs_LONG_233_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('rq', var.get('Math').callprop('sqrt', (Js(0.5)*var.get(u"this").get('qp')))),var.put('s', var.get('Math').callprop('sin', var.get(u"this").get('lat0')))),var.get(u"this").put('sinb1', (var.get('Gs')(var.get(u"this").get('e'), var.get('s'))/var.get(u"this").get('qp')))),var.get(u"this").put('cosb1', var.get('Math').callprop('sqrt', (Js(1.0)-(var.get(u"this").get('sinb1')*var.get(u"this").get('sinb1')))))),var.get(u"this").put('dd', (var.get('Math').callprop('cos', var.get(u"this").get('lat0'))/((var.get('Math').callprop('sqrt', (Js(1.0)-((var.get(u"this").get('es')*var.get('s'))*var.get('s'))))*var.get(u"this").get('rq'))*var.get(u"this").get('cosb1'))))),var.get(u"this").put('ymf', (var.get(u"this").put('xmf', var.get(u"this").get('rq'))/var.get(u"this").get('dd')))),var.get(u"this").put('xmf', var.get(u"this").get('dd'), '*'))
                    PyJs_LONG_233_()
                SWITCHED = True
                break
        else:
            (PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) and PyJsComma(var.get(u"this").put('sinph0', var.get('Math').callprop('sin', var.get(u"this").get('lat0'))),var.get(u"this").put('cosph0', var.get('Math').callprop('cos', var.get(u"this").get('lat0')))))
    PyJs_anonymous_231_._set_name('anonymous')
    @Js
    def PyJs_anonymous_234_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('c', var.get('t').get('x'))
        var.put('u', var.get('t').get('y'))
        if PyJsComma(var.put('c', var.get('qt')((var.get('c')-var.get(u"this").get('long0')))),var.get(u"this").get('sphere')):
            if PyJsComma(PyJsComma(PyJsComma(var.put('e', var.get('Math').callprop('sin', var.get('u'))),var.put('M', var.get('Math').callprop('cos', var.get('u')))),var.put('a', var.get('Math').callprop('cos', var.get('c')))),(PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) or PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT')))):
                if (var.put('i', ((Js(1.0)+(var.get('M')*var.get('a'))) if PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT')) else ((Js(1.0)+(var.get(u"this").get('sinph0')*var.get('e')))+((var.get(u"this").get('cosph0')*var.get('M'))*var.get('a')))))<=var.get('ot')):
                    return var.get(u"null")
                PyJsComma(var.put('s', ((var.put('i', var.get('Math').callprop('sqrt', (Js(2.0)/var.get('i'))))*var.get('M'))*var.get('Math').callprop('sin', var.get('c')))),var.put('i', (var.get('e') if PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT')) else ((var.get(u"this").get('cosph0')*var.get('e'))-((var.get(u"this").get('sinph0')*var.get('M'))*var.get('a')))), '*'))
            else:
                if (PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('N_POLE')) or PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('S_POLE'))):
                    if PyJsComma((PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('N_POLE')) and var.put('a', (-var.get('a')))),(var.get('Math').callprop('abs', (var.get('u')+var.get(u"this").get('lat0')))<var.get('ot'))):
                        return var.get(u"null")
                    PyJsComma(PyJsComma(var.put('i', (var.get('ct')-(Js(0.5)*var.get('u')))),var.put('s', (var.put('i', (Js(2.0)*(var.get('Math').callprop('cos', var.get('i')) if PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('S_POLE')) else var.get('Math').callprop('sin', var.get('i')))))*var.get('Math').callprop('sin', var.get('c'))))),var.put('i', var.get('a'), '*'))
        else:
            while 1:
                SWITCHED = False
                def PyJs_LONG_235_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('r', Js(0.0)),var.put('o', Js(0.0))),var.put('l', Js(0.0))),var.put('a', var.get('Math').callprop('cos', var.get('c')))),var.put('h', var.get('Math').callprop('sin', var.get('c')))),var.put('e', var.get('Math').callprop('sin', var.get('u')))),var.put('n', var.get('Gs')(var.get(u"this").get('e'), var.get('e')))),((PyJsStrictNeq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) and PyJsStrictNeq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT'))) or PyJsComma(var.put('r', (var.get('n')/var.get(u"this").get('qp'))),var.put('o', var.get('Math').callprop('sqrt', (Js(1.0)-(var.get('r')*var.get('r')))))))),var.get(u"this").get('mode'))
                CONDITION = (PyJs_LONG_235_())
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('OBLIQ')):
                    SWITCHED = True
                    var.put('l', ((Js(1.0)+(var.get(u"this").get('sinb1')*var.get('r')))+((var.get(u"this").get('cosb1')*var.get('o'))*var.get('a'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('EQUIT')):
                    SWITCHED = True
                    var.put('l', (Js(1.0)+(var.get('o')*var.get('a'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('N_POLE')):
                    SWITCHED = True
                    PyJsComma(var.put('l', (var.get('ht')+var.get('u'))),var.put('n', (var.get(u"this").get('qp')-var.get('n'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('S_POLE')):
                    SWITCHED = True
                    PyJsComma(var.put('l', (var.get('u')-var.get('ht'))),var.put('n', (var.get(u"this").get('qp')+var.get('n'))))
                SWITCHED = True
                break
            if (var.get('Math').callprop('abs', var.get('l'))<var.get('ot')):
                return var.get(u"null")
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u"this").get('mode'))
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('OBLIQ')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('EQUIT')):
                    SWITCHED = True
                    def PyJs_LONG_236_(var=var):
                        return PyJsComma(PyJsComma(var.put('l', var.get('Math').callprop('sqrt', (Js(2.0)/var.get('l')))),var.put('i', (((var.get(u"this").get('ymf')*var.get('l'))*((var.get(u"this").get('cosb1')*var.get('r'))-((var.get(u"this").get('sinb1')*var.get('o'))*var.get('a')))) if PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) else ((var.put('l', var.get('Math').callprop('sqrt', (Js(2.0)/(Js(1.0)+(var.get('o')*var.get('a'))))))*var.get('r'))*var.get(u"this").get('ymf'))))),var.put('s', (((var.get(u"this").get('xmf')*var.get('l'))*var.get('o'))*var.get('h'))))
                    PyJs_LONG_236_()
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('N_POLE')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('S_POLE')):
                    SWITCHED = True
                    (PyJsComma(var.put('s', (var.put('l', var.get('Math').callprop('sqrt', var.get('n')))*var.get('h'))),var.put('i', (var.get('a')*(var.get('l') if PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('S_POLE')) else (-var.get('l')))))) if (var.get('n')>=Js(0.0)) else var.put('s', var.put('i', Js(0.0))))
                SWITCHED = True
                break
        return PyJsComma(PyJsComma(var.get('t').put('x', ((var.get(u"this").get('a')*var.get('s'))+var.get(u"this").get('x0'))),var.get('t').put('y', ((var.get(u"this").get('a')*var.get('i'))+var.get(u"this").get('y0')))),var.get('t'))
    PyJs_anonymous_234_._set_name('anonymous')
    @Js
    def PyJs_anonymous_237_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-'))
        var.put('o', (var.get('t').get('x')/var.get(u"this").get('a')))
        var.put('l', (var.get('t').get('y')/var.get(u"this").get('a')))
        if var.get(u"this").get('sphere'):
            var.put('c', Js(0.0))
            var.put('u', Js(0.0))
            if PyJsComma(var.put('M', var.get('Math').callprop('sqrt', ((var.get('o')*var.get('o'))+(var.get('l')*var.get('l'))))),(var.put('i', (Js(0.5)*var.get('M')))>Js(1.0))):
                return var.get(u"null")
            while 1:
                SWITCHED = False
                def PyJs_LONG_238_(var=var):
                    return PyJsComma(PyJsComma(var.put('i', (Js(2.0)*var.get('Math').callprop('asin', var.get('i')))),((PyJsStrictNeq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) and PyJsStrictNeq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT'))) or PyJsComma(var.put('u', var.get('Math').callprop('sin', var.get('i'))),var.put('c', var.get('Math').callprop('cos', var.get('i')))))),var.get(u"this").get('mode'))
                CONDITION = (PyJs_LONG_238_())
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('EQUIT')):
                    SWITCHED = True
                    PyJsComma(PyJsComma(var.put('i', (Js(0.0) if (var.get('Math').callprop('abs', var.get('M'))<=var.get('ot')) else var.get('Math').callprop('asin', ((var.get('l')*var.get('u'))/var.get('M'))))),var.put('o', var.get('u'), '*')),var.put('l', (var.get('c')*var.get('M'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('OBLIQ')):
                    SWITCHED = True
                    def PyJs_LONG_239_(var=var):
                        return PyJsComma(PyJsComma(var.put('i', (var.get(u"this").get('lat0') if (var.get('Math').callprop('abs', var.get('M'))<=var.get('ot')) else var.get('Math').callprop('asin', ((var.get('c')*var.get(u"this").get('sinph0'))+(((var.get('l')*var.get('u'))*var.get(u"this").get('cosph0'))/var.get('M')))))),var.put('o', (var.get('u')*var.get(u"this").get('cosph0')), '*')),var.put('l', ((var.get('c')-(var.get('Math').callprop('sin', var.get('i'))*var.get(u"this").get('sinph0')))*var.get('M'))))
                    PyJs_LONG_239_()
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('N_POLE')):
                    SWITCHED = True
                    PyJsComma(var.put('l', (-var.get('l'))),var.put('i', (var.get('ht')-var.get('i'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"this").get('S_POLE')):
                    SWITCHED = True
                    var.put('i', var.get('ht'), '-')
                SWITCHED = True
                break
            var.put('s', (var.get('Math').callprop('atan2', var.get('o'), var.get('l')) if (PyJsStrictNeq(Js(0.0),var.get('l')) or (PyJsStrictNeq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT')) and PyJsStrictNeq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')))) else Js(0.0)))
        else:
            if PyJsComma(var.put('r', Js(0.0)),(PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) or PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('EQUIT')))):
                if PyJsComma(PyJsComma(var.put('o', var.get(u"this").get('dd'), '/'),var.put('l', var.get(u"this").get('dd'), '*')),(var.put('n', var.get('Math').callprop('sqrt', ((var.get('o')*var.get('o'))+(var.get('l')*var.get('l')))))<var.get('ot'))):
                    return PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('long0')),var.get('t').put('y', var.get(u"this").get('lat0'))),var.get('t'))
                def PyJs_LONG_240_(var=var):
                    return (PyJsComma(PyJsComma(var.put('r', ((var.get('a')*var.get(u"this").get('sinb1'))+(((var.get('l')*var.get('h'))*var.get(u"this").get('cosb1'))/var.get('n')))),var.put('e', (var.get(u"this").get('qp')*var.get('r')))),var.put('l', (((var.get('n')*var.get(u"this").get('cosb1'))*var.get('a'))-((var.get('l')*var.get(u"this").get('sinb1'))*var.get('h'))))) if PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('OBLIQ')) else PyJsComma(PyJsComma(var.put('r', ((var.get('l')*var.get('h'))/var.get('n'))),var.put('e', (var.get(u"this").get('qp')*var.get('r')))),var.put('l', (var.get('n')*var.get('a')))))
                PyJsComma(PyJsComma(PyJsComma(var.put('h', (Js(2.0)*var.get('Math').callprop('asin', ((Js(0.5)*var.get('n'))/var.get(u"this").get('rq'))))),var.put('a', var.get('Math').callprop('cos', var.get('h')))),var.put('o', var.put('h', var.get('Math').callprop('sin', var.get('h'))), '*')),PyJs_LONG_240_())
            else:
                if (PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('N_POLE')) or PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('S_POLE'))):
                    if PyJsComma((PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('N_POLE')) and var.put('l', (-var.get('l')))),var.put('e', ((var.get('o')*var.get('o'))+(var.get('l')*var.get('l')))).neg()):
                        return PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('long0')),var.get('t').put('y', var.get(u"this").get('lat0'))),var.get('t'))
                    PyJsComma(var.put('r', (Js(1.0)-(var.get('e')/var.get(u"this").get('qp')))),(PyJsStrictEq(var.get(u"this").get('mode'),var.get(u"this").get('S_POLE')) and var.put('r', (-var.get('r')))))
            PyJsComma(var.put('s', var.get('Math').callprop('atan2', var.get('o'), var.get('l'))),var.put('i', var.get('J')(var.get('Math').callprop('asin', var.get('r')), var.get(u"this").get('apa'))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('qt')((var.get(u"this").get('long0')+var.get('s')))),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_237_._set_name('anonymous')
    var.put('Us', Js({'init':PyJs_anonymous_231_,'forward':PyJs_anonymous_234_,'inverse':PyJs_anonymous_237_,'names':Js([Js('Lambert Azimuthal Equal Area'), Js('Lambert_Azimuthal_Equal_Area'), Js('laea')]),'S_POLE':Js(1.0),'N_POLE':Js(2.0),'EQUIT':Js(3.0),'OBLIQ':Js(4.0)}))
    @Js
    def PyJs_anonymous_241_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return PyJsComma(((var.get('Math').callprop('abs', var.get('t'))>Js(1.0)) and var.put('t', (Js(1.0) if (var.get('t')>Js(1.0)) else (-Js(1.0))))),var.get('Math').callprop('asin', var.get('t')))
    PyJs_anonymous_241_._set_name('anonymous')
    var.put('Fs', PyJs_anonymous_241_)
    @Js
    def PyJs_anonymous_242_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_243_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('temp', (var.get(u"this").get('b')/var.get(u"this").get('a'))),var.get(u"this").put('es', (Js(1.0)-var.get('Math').callprop('pow', var.get(u"this").get('temp'), Js(2.0))))),var.get(u"this").put('e3', var.get('Math').callprop('sqrt', var.get(u"this").get('es')))),var.get(u"this").put('sin_po', var.get('Math').callprop('sin', var.get(u"this").get('lat1')))),var.get(u"this").put('cos_po', var.get('Math').callprop('cos', var.get(u"this").get('lat1')))),var.get(u"this").put('t1', var.get(u"this").get('sin_po'))),var.get(u"this").put('con', var.get(u"this").get('sin_po'))),var.get(u"this").put('ms1', var.get('St')(var.get(u"this").get('e3'), var.get(u"this").get('sin_po'), var.get(u"this").get('cos_po')))),var.get(u"this").put('qs1', var.get('Gs')(var.get(u"this").get('e3'), var.get(u"this").get('sin_po'), var.get(u"this").get('cos_po')))),var.get(u"this").put('sin_po', var.get('Math').callprop('sin', var.get(u"this").get('lat2')))),var.get(u"this").put('cos_po', var.get('Math').callprop('cos', var.get(u"this").get('lat2')))),var.get(u"this").put('t2', var.get(u"this").get('sin_po'))),var.get(u"this").put('ms2', var.get('St')(var.get(u"this").get('e3'), var.get(u"this").get('sin_po'), var.get(u"this").get('cos_po')))),var.get(u"this").put('qs2', var.get('Gs')(var.get(u"this").get('e3'), var.get(u"this").get('sin_po'), var.get(u"this").get('cos_po')))),var.get(u"this").put('sin_po', var.get('Math').callprop('sin', var.get(u"this").get('lat0')))),var.get(u"this").put('cos_po', var.get('Math').callprop('cos', var.get(u"this").get('lat0')))),var.get(u"this").put('t3', var.get(u"this").get('sin_po'))),var.get(u"this").put('qs0', var.get('Gs')(var.get(u"this").get('e3'), var.get(u"this").get('sin_po'), var.get(u"this").get('cos_po')))),(var.get(u"this").put('ns0', (((var.get(u"this").get('ms1')*var.get(u"this").get('ms1'))-(var.get(u"this").get('ms2')*var.get(u"this").get('ms2')))/(var.get(u"this").get('qs2')-var.get(u"this").get('qs1')))) if (var.get('Math').callprop('abs', (var.get(u"this").get('lat1')-var.get(u"this").get('lat2')))>var.get('ot')) else var.get(u"this").put('ns0', var.get(u"this").get('con')))),var.get(u"this").put('c', ((var.get(u"this").get('ms1')*var.get(u"this").get('ms1'))+(var.get(u"this").get('ns0')*var.get(u"this").get('qs1'))))),var.get(u"this").put('rh', ((var.get(u"this").get('a')*var.get('Math').callprop('sqrt', (var.get(u"this").get('c')-(var.get(u"this").get('ns0')*var.get(u"this").get('qs0')))))/var.get(u"this").get('ns0'))))
        ((var.get('Math').callprop('abs', (var.get(u"this").get('lat1')+var.get(u"this").get('lat2')))<var.get('ot')) or PyJs_LONG_243_())
    PyJs_anonymous_242_._set_name('anonymous')
    @Js
    def PyJs_anonymous_244_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        PyJsComma(var.get(u"this").put('sin_phi', var.get('Math').callprop('sin', var.get('i'))),var.get(u"this").put('cos_phi', var.get('Math').callprop('cos', var.get('i'))))
        var.put('a', var.get('Gs')(var.get(u"this").get('e3'), var.get(u"this").get('sin_phi'), var.get(u"this").get('cos_phi')))
        var.put('h', ((var.get(u"this").get('a')*var.get('Math').callprop('sqrt', (var.get(u"this").get('c')-(var.get(u"this").get('ns0')*var.get('a')))))/var.get(u"this").get('ns0')))
        var.put('e', (var.get(u"this").get('ns0')*var.get('qt')((var.get('s')-var.get(u"this").get('long0')))))
        var.put('n', ((var.get('h')*var.get('Math').callprop('sin', var.get('e')))+var.get(u"this").get('x0')))
        var.put('r', ((var.get(u"this").get('rh')-(var.get('h')*var.get('Math').callprop('cos', var.get('e'))))+var.get(u"this").get('y0')))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('n')),var.get('t').put('y', var.get('r'))),var.get('t'))
    PyJs_anonymous_244_._set_name('anonymous')
    @Js
    def PyJs_anonymous_245_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_247_(var=var):
            def PyJs_LONG_246_(var=var):
                return (PyJsComma(var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y'))))),var.put('a', Js(1.0))) if (var.get(u"this").get('ns0')>=Js(0.0)) else PyJsComma(var.put('s', (-var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))),var.put('a', (-Js(1.0)))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', ((var.get(u"this").get('rh')-var.get('t').get('y'))+var.get(u"this").get('y0')))),PyJs_LONG_246_()),var.put('h', Js(0.0))),(PyJsStrictNeq(Js(0.0),var.get('s')) and var.put('h', var.get('Math').callprop('atan2', (var.get('a')*var.get('t').get('x')), (var.get('a')*var.get('t').get('y')))))),var.put('a', ((var.get('s')*var.get(u"this").get('ns0'))/var.get(u"this").get('a')))),(var.put('n', var.get('Math').callprop('asin', ((var.get(u"this").get('c')-(var.get('a')*var.get('a')))/(Js(2.0)*var.get(u"this").get('ns0'))))) if var.get(u"this").get('sphere') else PyJsComma(var.put('i', ((var.get(u"this").get('c')-(var.get('a')*var.get('a')))/var.get(u"this").get('ns0'))),var.put('n', var.get(u"this").callprop('phi1z', var.get(u"this").get('e3'), var.get('i')))))),var.put('e', var.get('qt')(((var.get('h')/var.get(u"this").get('ns0'))+var.get(u"this").get('long0'))))),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('n'))),var.get('t'))
        return PyJs_LONG_247_()
    PyJs_anonymous_245_._set_name('anonymous')
    @Js
    def PyJs_anonymous_248_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('r', var.get('Fs')((Js(0.5)*var.get('s'))))
        if (var.get('t')<var.get('ot')):
            return var.get('r')
        #for JS loop
        var.put('o', (var.get('t')*var.get('t')))
        var.put('l', Js(1.0))
        while (var.get('l')<=Js(25.0)):
            try:
                def PyJs_LONG_249_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('Math').callprop('sin', var.get('r'))),var.put('a', var.get('Math').callprop('cos', var.get('r')))),var.put('h', (var.get('t')*var.get('i')))),var.put('e', (Js(1.0)-(var.get('h')*var.get('h'))))),var.put('n', ((((Js(0.5)*var.get('e'))*var.get('e'))/var.get('a'))*(((var.get('s')/(Js(1.0)-var.get('o')))-(var.get('i')/var.get('e')))+((Js(0.5)/var.get('t'))*var.get('Math').callprop('log', ((Js(1.0)-var.get('h'))/(Js(1.0)+var.get('h'))))))))),var.put('r', var.get('n'), '+')),(var.get('Math').callprop('abs', var.get('n'))<=Js(1e-07)))
                if PyJs_LONG_249_():
                    return var.get('r')
            finally:
                    (var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))
        return var.get(u"null")
    PyJs_anonymous_248_._set_name('anonymous')
    var.put('Qs', Js({'init':PyJs_anonymous_242_,'forward':PyJs_anonymous_244_,'inverse':PyJs_anonymous_245_,'names':Js([Js('Albers_Conic_Equal_Area'), Js('Albers'), Js('aea')]),'phi1z':PyJs_anonymous_248_}))
    @Js
    def PyJs_anonymous_250_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('sin_p14', var.get('Math').callprop('sin', var.get(u"this").get('lat0'))),var.get(u"this").put('cos_p14', var.get('Math').callprop('cos', var.get(u"this").get('lat0')))),var.get(u"this").put('infinity_dist', (Js(1000.0)*var.get(u"this").get('a')))),var.get(u"this").put('rc', Js(1.0)))
    PyJs_anonymous_250_._set_name('anonymous')
    @Js
    def PyJs_anonymous_251_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('o', var.get('t').get('x'))
        var.put('l', var.get('t').get('y'))
        def PyJs_LONG_253_(var=var):
            def PyJs_LONG_252_(var=var):
                return (PyJsComma(var.put('n', (var.get(u"this").get('x0')+((((Js(1.0)*var.get(u"this").get('a'))*var.get('i'))*var.get('Math').callprop('sin', var.get('a')))/var.get('e')))),var.put('r', (var.get(u"this").get('y0')+(((Js(1.0)*var.get(u"this").get('a'))*((var.get(u"this").get('cos_p14')*var.get('s'))-((var.get(u"this").get('sin_p14')*var.get('i'))*var.get('h'))))/var.get('e'))))) if ((var.put('e', ((var.get(u"this").get('sin_p14')*var.get('s'))+((var.get(u"this").get('cos_p14')*var.get('i'))*var.get('h'))))>Js(0.0)) or (var.get('Math').callprop('abs', var.get('e'))<=var.get('ot'))) else PyJsComma(var.put('n', (var.get(u"this").get('x0')+((var.get(u"this").get('infinity_dist')*var.get('i'))*var.get('Math').callprop('sin', var.get('a'))))),var.put('r', (var.get(u"this").get('y0')+(var.get(u"this").get('infinity_dist')*((var.get(u"this").get('cos_p14')*var.get('s'))-((var.get(u"this").get('sin_p14')*var.get('i'))*var.get('h'))))))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('a', var.get('qt')((var.get('o')-var.get(u"this").get('long0')))),var.put('s', var.get('Math').callprop('sin', var.get('l')))),var.put('i', var.get('Math').callprop('cos', var.get('l')))),var.put('h', var.get('Math').callprop('cos', var.get('a')))),PyJs_LONG_252_()),var.get('t').put('x', var.get('n'))),var.get('t').put('y', var.get('r'))),var.get('t'))
        return PyJs_LONG_253_()
    PyJs_anonymous_251_._set_name('anonymous')
    @Js
    def PyJs_anonymous_254_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_256_(var=var):
            def PyJs_LONG_255_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', var.get('Math').callprop('atan2', var.get('s'), var.get(u"this").get('rc'))),var.put('i', var.get('Math').callprop('sin', var.get('h')))),var.put('a', var.get('Math').callprop('cos', var.get('h')))),var.put('n', var.get('Fs')(((var.get('a')*var.get(u"this").get('sin_p14'))+(((var.get('t').get('y')*var.get('i'))*var.get(u"this").get('cos_p14'))/var.get('s')))))),var.put('e', var.get('Math').callprop('atan2', (var.get('t').get('x')*var.get('i')), (((var.get('s')*var.get(u"this").get('cos_p14'))*var.get('a'))-((var.get('t').get('y')*var.get(u"this").get('sin_p14'))*var.get('i')))))),var.put('e', var.get('qt')((var.get(u"this").get('long0')+var.get('e')))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', ((var.get('t').get('x')-var.get(u"this").get('x0'))/var.get(u"this").get('a'))),var.get('t').put('y', ((var.get('t').get('y')-var.get(u"this").get('y0'))/var.get(u"this").get('a')))),var.get('t').put('x', var.get(u"this").get('k0'), '/')),var.get('t').put('y', var.get(u"this").get('k0'), '/')),(PyJs_LONG_255_() if var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y'))))) else PyJsComma(var.put('n', var.get(u"this").get('phic0')),var.put('e', Js(0.0))))),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('n'))),var.get('t'))
        return PyJs_LONG_256_()
    PyJs_anonymous_254_._set_name('anonymous')
    var.put('Ws', Js({'init':PyJs_anonymous_250_,'forward':PyJs_anonymous_251_,'inverse':PyJs_anonymous_254_,'names':Js([Js('gnom')])}))
    @Js
    def PyJs_anonymous_257_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('i', (Js(1.0)-(((Js(1.0)-(var.get('t')*var.get('t')))/(Js(2.0)*var.get('t')))*var.get('Math').callprop('log', ((Js(1.0)-var.get('t'))/(Js(1.0)+var.get('t')))))))
        if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('s'))-var.get('i')))<Js(1e-06)):
            return (((-Js(1.0))*var.get('ht')) if (var.get('s')<Js(0.0)) else var.get('ht'))
        #for JS loop
        var.put('r', var.get('Math').callprop('asin', (Js(0.5)*var.get('s'))))
        var.put('o', Js(0.0))
        while (var.get('o')<Js(30.0)):
            try:
                def PyJs_LONG_258_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', var.get('Math').callprop('sin', var.get('r'))),var.put('e', var.get('Math').callprop('cos', var.get('r')))),var.put('n', (var.get('t')*var.get('h')))),var.put('a', ((var.get('Math').callprop('pow', (Js(1.0)-(var.get('n')*var.get('n'))), Js(2.0))/(Js(2.0)*var.get('e')))*(((var.get('s')/(Js(1.0)-(var.get('t')*var.get('t'))))-(var.get('h')/(Js(1.0)-(var.get('n')*var.get('n')))))+((Js(0.5)/var.get('t'))*var.get('Math').callprop('log', ((Js(1.0)-var.get('n'))/(Js(1.0)+var.get('n'))))))))),var.put('r', var.get('a'), '+')),(var.get('Math').callprop('abs', var.get('a'))<=Js(1e-10)))
                if PyJs_LONG_258_():
                    return var.get('r')
            finally:
                    (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
        return var.get('NaN')
    PyJs_anonymous_257_._set_name('anonymous')
    var.put('Hs', PyJs_anonymous_257_)
    @Js
    def PyJs_anonymous_259_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        (var.get(u"this").get('sphere') or var.get(u"this").put('k0', var.get('St')(var.get(u"this").get('e'), var.get('Math').callprop('sin', var.get(u"this").get('lat_ts')), var.get('Math').callprop('cos', var.get(u"this").get('lat_ts')))))
    PyJs_anonymous_259_._set_name('anonymous')
    @Js
    def PyJs_anonymous_260_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        var.put('a', var.get('t').get('x'))
        var.put('h', var.get('t').get('y'))
        var.put('e', var.get('qt')((var.get('a')-var.get(u"this").get('long0'))))
        if var.get(u"this").get('sphere'):
            PyJsComma(var.put('s', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*var.get('e'))*var.get('Math').callprop('cos', var.get(u"this").get('lat_ts'))))),var.put('i', (var.get(u"this").get('y0')+((var.get(u"this").get('a')*var.get('Math').callprop('sin', var.get('h')))/var.get('Math').callprop('cos', var.get(u"this").get('lat_ts'))))))
        else:
            var.put('n', var.get('Gs')(var.get(u"this").get('e'), var.get('Math').callprop('sin', var.get('h'))))
            PyJsComma(var.put('s', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*var.get(u"this").get('k0'))*var.get('e')))),var.put('i', (var.get(u"this").get('y0')+(((var.get(u"this").get('a')*var.get('n'))*Js(0.5))/var.get(u"this").get('k0')))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_260_._set_name('anonymous')
    @Js
    def PyJs_anonymous_261_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-'))
        pass
        def PyJs_LONG_262_(var=var):
            return (PyJsComma(var.put('s', var.get('qt')((var.get(u"this").get('long0')+((var.get('t').get('x')/var.get(u"this").get('a'))/var.get('Math').callprop('cos', var.get(u"this").get('lat_ts')))))),var.put('i', var.get('Math').callprop('asin', ((var.get('t').get('y')/var.get(u"this").get('a'))*var.get('Math').callprop('cos', var.get(u"this").get('lat_ts')))))) if var.get(u"this").get('sphere') else PyJsComma(var.put('i', var.get('Hs')(var.get(u"this").get('e'), (((Js(2.0)*var.get('t').get('y'))*var.get(u"this").get('k0'))/var.get(u"this").get('a')))),var.put('s', var.get('qt')((var.get(u"this").get('long0')+(var.get('t').get('x')/(var.get(u"this").get('a')*var.get(u"this").get('k0'))))))))
        return PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_262_(),var.get('t').put('x', var.get('s'))),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_261_._set_name('anonymous')
    var.put('Xs', Js({'init':PyJs_anonymous_259_,'forward':PyJs_anonymous_260_,'inverse':PyJs_anonymous_261_,'names':Js([Js('cea')])}))
    @Js
    def PyJs_anonymous_263_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_264_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('x0', (var.get(u"this").get('x0') or Js(0.0))),var.get(u"this").put('y0', (var.get(u"this").get('y0') or Js(0.0)))),var.get(u"this").put('lat0', (var.get(u"this").get('lat0') or Js(0.0)))),var.get(u"this").put('long0', (var.get(u"this").get('long0') or Js(0.0)))),var.get(u"this").put('lat_ts', (var.get(u"this").get('lat_ts') or Js(0.0)))),var.get(u"this").put('title', (var.get(u"this").get('title') or Js('Equidistant Cylindrical (Plate Carre)')))),var.get(u"this").put('rc', var.get('Math').callprop('cos', var.get(u"this").get('lat_ts'))))
        PyJs_LONG_264_()
    PyJs_anonymous_263_._set_name('anonymous')
    @Js
    def PyJs_anonymous_265_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        var.put('a', var.get('qt')((var.get('s')-var.get(u"this").get('long0'))))
        var.put('h', var.get('Is')((var.get('i')-var.get(u"this").get('lat0'))))
        return PyJsComma(PyJsComma(var.get('t').put('x', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*var.get('a'))*var.get(u"this").get('rc')))),var.get('t').put('y', (var.get(u"this").get('y0')+(var.get(u"this").get('a')*var.get('h'))))),var.get('t'))
    PyJs_anonymous_265_._set_name('anonymous')
    @Js
    def PyJs_anonymous_266_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('qt')((var.get(u"this").get('long0')+((var.get('s')-var.get(u"this").get('x0'))/(var.get(u"this").get('a')*var.get(u"this").get('rc')))))),var.get('t').put('y', var.get('Is')((var.get(u"this").get('lat0')+((var.get('i')-var.get(u"this").get('y0'))/var.get(u"this").get('a')))))),var.get('t'))
    PyJs_anonymous_266_._set_name('anonymous')
    var.put('Ks', Js({'init':PyJs_anonymous_263_,'forward':PyJs_anonymous_265_,'inverse':PyJs_anonymous_266_,'names':Js([Js('Equirectangular'), Js('Equidistant_Cylindrical'), Js('eqc')])}))
    var.put('Js', Js(20.0))
    @Js
    def PyJs_anonymous_267_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_268_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('temp', (var.get(u"this").get('b')/var.get(u"this").get('a'))),var.get(u"this").put('es', (Js(1.0)-var.get('Math').callprop('pow', var.get(u"this").get('temp'), Js(2.0))))),var.get(u"this").put('e', var.get('Math').callprop('sqrt', var.get(u"this").get('es')))),var.get(u"this").put('e0', var.get('Ps')(var.get(u"this").get('es')))),var.get(u"this").put('e1', var.get('Ns')(var.get(u"this").get('es')))),var.get(u"this").put('e2', var.get('Ss')(var.get(u"this").get('es')))),var.get(u"this").put('e3', var.get('ks')(var.get(u"this").get('es')))),var.get(u"this").put('ml0', (var.get(u"this").get('a')*var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get(u"this").get('lat0')))))
        PyJs_LONG_268_()
    PyJs_anonymous_267_._set_name('anonymous')
    @Js
    def PyJs_anonymous_269_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('h', var.get('t').get('x'))
        var.put('e', var.get('t').get('y'))
        var.put('n', var.get('qt')((var.get('h')-var.get(u"this").get('long0'))))
        if PyJsComma(var.put('a', (var.get('n')*var.get('Math').callprop('sin', var.get('e')))),var.get(u"this").get('sphere')):
            def PyJs_LONG_270_(var=var):
                return (PyJsComma(var.put('s', (var.get(u"this").get('a')*var.get('n'))),var.put('i', (((-Js(1.0))*var.get(u"this").get('a'))*var.get(u"this").get('lat0')))) if (var.get('Math').callprop('abs', var.get('e'))<=var.get('ot')) else PyJsComma(var.put('s', ((var.get(u"this").get('a')*var.get('Math').callprop('sin', var.get('a')))/var.get('Math').callprop('tan', var.get('e')))),var.put('i', (var.get(u"this").get('a')*(var.get('Is')((var.get('e')-var.get(u"this").get('lat0')))+((Js(1.0)-var.get('Math').callprop('cos', var.get('a')))/var.get('Math').callprop('tan', var.get('e'))))))))
            PyJs_LONG_270_()
        else:
            if (var.get('Math').callprop('abs', var.get('e'))<=var.get('ot')):
                PyJsComma(var.put('s', (var.get(u"this").get('a')*var.get('n'))),var.put('i', ((-Js(1.0))*var.get(u"this").get('ml0'))))
            else:
                var.put('r', (var.get('qs')(var.get(u"this").get('a'), var.get(u"this").get('e'), var.get('Math').callprop('sin', var.get('e')))/var.get('Math').callprop('tan', var.get('e'))))
                PyJsComma(var.put('s', (var.get('r')*var.get('Math').callprop('sin', var.get('a')))),var.put('i', (((var.get(u"this").get('a')*var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get('e')))-var.get(u"this").get('ml0'))+(var.get('r')*(Js(1.0)-var.get('Math').callprop('cos', var.get('a')))))))
        return PyJsComma(PyJsComma(var.get('t').put('x', (var.get('s')+var.get(u"this").get('x0'))),var.get('t').put('y', (var.get('i')+var.get(u"this").get('y0')))),var.get('t'))
    PyJs_anonymous_269_._set_name('anonymous')
    @Js
    def PyJs_anonymous_271_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 's', 'r', 'f', 'a'])
        pass
        if PyJsComma(PyJsComma(var.put('a', (var.get('t').get('x')-var.get(u"this").get('x0'))),var.put('h', (var.get('t').get('y')-var.get(u"this").get('y0')))),var.get(u"this").get('sphere')):
            if (var.get('Math').callprop('abs', (var.get('h')+(var.get(u"this").get('a')*var.get(u"this").get('lat0'))))<=var.get('ot')):
                PyJsComma(var.put('s', var.get('qt')(((var.get('a')/var.get(u"this").get('a'))+var.get(u"this").get('long0')))),var.put('i', Js(0.0)))
            else:
                PyJsComma(PyJsComma(var.put('n', (var.get(u"this").get('lat0')+(var.get('h')/var.get(u"this").get('a')))),var.put('r', ((((var.get('a')*var.get('a'))/var.get(u"this").get('a'))/var.get(u"this").get('a'))+(var.get('n')*var.get('n'))))),var.put('o', var.get('n')))
                pass
                #for JS loop
                var.put('e', var.get('Js'))
                while var.get('e'):
                    try:
                        def PyJs_LONG_272_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(var.put('M', var.get('Math').callprop('tan', var.get('o'))),var.put('l', (((-Js(1.0))*(((var.get('n')*((var.get('o')*var.get('M'))+Js(1.0)))-var.get('o'))-((Js(0.5)*((var.get('o')*var.get('o'))+var.get('r')))*var.get('M'))))/(((var.get('o')-var.get('n'))/var.get('M'))-Js(1.0))))),var.put('o', var.get('l'), '+')),(var.get('Math').callprop('abs', var.get('l'))<=var.get('ot')))
                        if PyJs_LONG_272_():
                            var.put('i', var.get('o'))
                            break
                    finally:
                            var.put('e',Js(var.get('e').to_number())-Js(1))
                var.put('s', var.get('qt')((var.get(u"this").get('long0')+(var.get('Math').callprop('asin', ((var.get('a')*var.get('Math').callprop('tan', var.get('o')))/var.get(u"this").get('a')))/var.get('Math').callprop('sin', var.get('i'))))))
        else:
            if (var.get('Math').callprop('abs', (var.get('h')+var.get(u"this").get('ml0')))<=var.get('ot')):
                PyJsComma(var.put('i', Js(0.0)),var.put('s', var.get('qt')((var.get(u"this").get('long0')+(var.get('a')/var.get(u"this").get('a'))))))
            else:
                PyJsComma(PyJsComma(var.put('n', ((var.get(u"this").get('ml0')+var.get('h'))/var.get(u"this").get('a'))),var.put('r', ((((var.get('a')*var.get('a'))/var.get(u"this").get('a'))/var.get(u"this").get('a'))+(var.get('n')*var.get('n'))))),var.put('o', var.get('n')))
                pass
                #for JS loop
                var.put('e', var.get('Js'))
                while var.get('e'):
                    try:
                        def PyJs_LONG_274_(var=var):
                            def PyJs_LONG_273_(var=var):
                                return ((((var.get('n')*((var.get('c')*var.get('m'))+Js(1.0)))-var.get('m'))-((Js(0.5)*var.get('c'))*((var.get('m')*var.get('m'))+var.get('r'))))/(((((var.get(u"this").get('es')*var.get('Math').callprop('sin', (Js(2.0)*var.get('o'))))*(((var.get('m')*var.get('m'))+var.get('r'))-((Js(2.0)*var.get('n'))*var.get('m'))))/(Js(4.0)*var.get('c')))+((var.get('n')-var.get('m'))*((var.get('c')*var.get('f'))-(Js(2.0)/var.get('Math').callprop('sin', (Js(2.0)*var.get('o')))))))-var.get('f')))
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('p', (var.get(u"this").get('e')*var.get('Math').callprop('sin', var.get('o')))),var.put('c', (var.get('Math').callprop('sqrt', (Js(1.0)-(var.get('p')*var.get('p'))))*var.get('Math').callprop('tan', var.get('o'))))),var.put('u', (var.get(u"this").get('a')*var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get('o'))))),var.put('f', (((var.get(u"this").get('e0')-((Js(2.0)*var.get(u"this").get('e1'))*var.get('Math').callprop('cos', (Js(2.0)*var.get('o')))))+((Js(4.0)*var.get(u"this").get('e2'))*var.get('Math').callprop('cos', (Js(4.0)*var.get('o')))))-((Js(6.0)*var.get(u"this").get('e3'))*var.get('Math').callprop('cos', (Js(6.0)*var.get('o'))))))),var.put('m', (var.get('u')/var.get(u"this").get('a')))),var.put('l', PyJs_LONG_273_())),var.put('o', var.get('l'), '-')),(var.get('Math').callprop('abs', var.get('l'))<=var.get('ot')))
                        if PyJs_LONG_274_():
                            var.put('i', var.get('o'))
                            break
                    finally:
                            var.put('e',Js(var.get('e').to_number())-Js(1))
                def PyJs_LONG_275_(var=var):
                    return PyJsComma(var.put('c', (var.get('Math').callprop('sqrt', (Js(1.0)-(var.get(u"this").get('es')*var.get('Math').callprop('pow', var.get('Math').callprop('sin', var.get('i')), Js(2.0)))))*var.get('Math').callprop('tan', var.get('i')))),var.put('s', var.get('qt')((var.get(u"this").get('long0')+(var.get('Math').callprop('asin', ((var.get('a')*var.get('c'))/var.get(u"this").get('a')))/var.get('Math').callprop('sin', var.get('i')))))))
                PyJs_LONG_275_()
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_271_._set_name('anonymous')
    var.put('Vs', Js({'init':PyJs_anonymous_267_,'forward':PyJs_anonymous_269_,'inverse':PyJs_anonymous_271_,'names':Js([Js('Polyconic'), Js('poly')])}))
    @Js
    def PyJs_anonymous_276_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_277_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('A', Js([])),var.get(u"this").get('A').put('1', Js(0.6399175073))),var.get(u"this").get('A').put('2', (-Js(0.1358797613)))),var.get(u"this").get('A').put('3', Js(0.063294409))),var.get(u"this").get('A').put('4', (-Js(0.02526853)))),var.get(u"this").get('A').put('5', Js(0.0117879))),var.get(u"this").get('A').put('6', (-Js(0.0055161)))),var.get(u"this").get('A').put('7', Js(0.0026906))),var.get(u"this").get('A').put('8', (-Js(0.001333)))),var.get(u"this").get('A').put('9', Js(0.00067))),var.get(u"this").get('A').put('10', (-Js(0.00034)))),var.get(u"this").put('B_re', Js([]))),var.get(u"this").put('B_im', Js([]))),var.get(u"this").get('B_re').put('1', Js(0.7557853228))),var.get(u"this").get('B_im').put('1', Js(0.0))),var.get(u"this").get('B_re').put('2', Js(0.249204646))),var.get(u"this").get('B_im').put('2', Js(0.003371507))),var.get(u"this").get('B_re').put('3', (-Js(0.001541739)))),var.get(u"this").get('B_im').put('3', Js(0.04105856))),var.get(u"this").get('B_re').put('4', (-Js(0.10162907)))),var.get(u"this").get('B_im').put('4', Js(0.01727609))),var.get(u"this").get('B_re').put('5', (-Js(0.26623489)))),var.get(u"this").get('B_im').put('5', (-Js(0.36249218)))),var.get(u"this").get('B_re').put('6', (-Js(0.6870983)))),var.get(u"this").get('B_im').put('6', (-Js(1.1651967)))),var.get(u"this").put('C_re', Js([]))),var.get(u"this").put('C_im', Js([]))),var.get(u"this").get('C_re').put('1', Js(1.3231270439))),var.get(u"this").get('C_im').put('1', Js(0.0))),var.get(u"this").get('C_re').put('2', (-Js(0.577245789)))),var.get(u"this").get('C_im').put('2', (-Js(0.007809598)))),var.get(u"this").get('C_re').put('3', Js(0.508307513))),var.get(u"this").get('C_im').put('3', (-Js(0.112208952)))),var.get(u"this").get('C_re').put('4', (-Js(0.15094762)))),var.get(u"this").get('C_im').put('4', Js(0.18200602))),var.get(u"this").get('C_re').put('5', Js(1.01418179))),var.get(u"this").get('C_im').put('5', Js(1.64497696))),var.get(u"this").get('C_re').put('6', Js(1.9660549))),var.get(u"this").get('C_im').put('6', Js(2.5127645))),var.get(u"this").put('D', Js([]))),var.get(u"this").get('D').put('1', Js(1.5627014243))),var.get(u"this").get('D').put('2', Js(0.5185406398))),var.get(u"this").get('D').put('3', (-Js(0.03333098)))),var.get(u"this").get('D').put('4', (-Js(0.1052906)))),var.get(u"this").get('D').put('5', (-Js(0.0368594)))),var.get(u"this").get('D').put('6', Js(0.007317))),var.get(u"this").get('D').put('7', Js(0.0122))),var.get(u"this").get('D').put('8', Js(0.00394))),var.get(u"this").get('D').put('9', (-Js(0.0013))))
        PyJs_LONG_277_()
    PyJs_anonymous_276_._set_name('anonymous')
    @Js
    def PyJs_anonymous_278_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 's', 'r', 'f', 'a'])
        var.put('i', var.get('t').get('x'))
        var.put('a', (var.get('t').get('y')-var.get(u"this").get('lat0')))
        var.put('h', (var.get('i')-var.get(u"this").get('long0')))
        var.put('e', ((var.get('a')/var.get('at'))*Js(1e-05)))
        var.put('n', var.get('h'))
        var.put('r', Js(1.0))
        var.put('o', Js(0.0))
        #for JS loop
        var.put('s', Js(1.0))
        while (var.get('s')<=Js(10.0)):
            try:
                PyJsComma(var.put('r', var.get('e'), '*'),var.put('o', (var.get(u"this").get('A').get(var.get('s'))*var.get('r')), '+'))
            finally:
                    (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
        var.put('M', var.get('o'))
        var.put('c', var.get('n'))
        var.put('u', Js(1.0))
        var.put('f', Js(0.0))
        var.put('m', Js(0.0))
        var.put('p', Js(0.0))
        #for JS loop
        var.put('s', Js(1.0))
        while (var.get('s')<=Js(6.0)):
            try:
                def PyJs_LONG_279_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('l', ((var.get('f')*var.get('M'))+(var.get('u')*var.get('c')))),var.put('u', ((var.get('u')*var.get('M'))-(var.get('f')*var.get('c'))))),var.put('f', var.get('l'))),var.put('m', ((var.get('m')+(var.get(u"this").get('B_re').get(var.get('s'))*var.get('u')))-(var.get(u"this").get('B_im').get(var.get('s'))*var.get('f'))))),var.put('p', ((var.get('p')+(var.get(u"this").get('B_im').get(var.get('s'))*var.get('u')))+(var.get(u"this").get('B_re').get(var.get('s'))*var.get('f')))))
                PyJs_LONG_279_()
            finally:
                    (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
        return PyJsComma(PyJsComma(var.get('t').put('x', ((var.get('p')*var.get(u"this").get('a'))+var.get(u"this").get('x0'))),var.get('t').put('y', ((var.get('m')*var.get(u"this").get('a'))+var.get(u"this").get('y0')))),var.get('t'))
    PyJs_anonymous_278_._set_name('anonymous')
    @Js
    def PyJs_anonymous_280_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 'n', 'e', 's', 'p', 'r', 'g', 't', 'M', 'c', 'E', 'b', 'h', 'A', 'i', 'y', 'x', 'm', 'C', 'v', 'w', 'd', 'l', 'o', 'f', '_', 'a'])
        var.put('a', var.get('t').get('x'))
        var.put('h', var.get('t').get('y'))
        var.put('e', (var.get('a')-var.get(u"this").get('x0')))
        var.put('n', ((var.get('h')-var.get(u"this").get('y0'))/var.get(u"this").get('a')))
        var.put('r', (var.get('e')/var.get(u"this").get('a')))
        var.put('o', Js(1.0))
        var.put('l', Js(0.0))
        var.put('M', Js(0.0))
        var.put('c', Js(0.0))
        #for JS loop
        var.put('s', Js(1.0))
        while (var.get('s')<=Js(6.0)):
            try:
                def PyJs_LONG_281_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', ((var.get('l')*var.get('n'))+(var.get('o')*var.get('r')))),var.put('o', ((var.get('o')*var.get('n'))-(var.get('l')*var.get('r'))))),var.put('l', var.get('i'))),var.put('M', ((var.get('M')+(var.get(u"this").get('C_re').get(var.get('s'))*var.get('o')))-(var.get(u"this").get('C_im').get(var.get('s'))*var.get('l'))))),var.put('c', ((var.get('c')+(var.get(u"this").get('C_im').get(var.get('s'))*var.get('o')))+(var.get(u"this").get('C_re').get(var.get('s'))*var.get('l')))))
                PyJs_LONG_281_()
            finally:
                    (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('u', Js(0.0))
        while (var.get('u')<var.get(u"this").get('iterations')):
            try:
                var.put('m', var.get('M'))
                var.put('p', var.get('c'))
                var.put('d', var.get('n'))
                var.put('y', var.get('r'))
                #for JS loop
                var.put('s', Js(2.0))
                while (var.get('s')<=Js(6.0)):
                    try:
                        def PyJs_LONG_282_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('f', ((var.get('p')*var.get('M'))+(var.get('m')*var.get('c')))),var.put('m', ((var.get('m')*var.get('M'))-(var.get('p')*var.get('c'))))),var.put('p', var.get('f'))),var.put('d', ((var.get('s')-Js(1.0))*((var.get(u"this").get('B_re').get(var.get('s'))*var.get('m'))-(var.get(u"this").get('B_im').get(var.get('s'))*var.get('p')))), '+')),var.put('y', ((var.get('s')-Js(1.0))*((var.get(u"this").get('B_im').get(var.get('s'))*var.get('m'))+(var.get(u"this").get('B_re').get(var.get('s'))*var.get('p')))), '+'))
                        PyJs_LONG_282_()
                    finally:
                            (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
                PyJsComma(var.put('m', Js(1.0)),var.put('p', Js(0.0)))
                var.put('_', var.get(u"this").get('B_re').get('1'))
                var.put('x', var.get(u"this").get('B_im').get('1'))
                #for JS loop
                var.put('s', Js(2.0))
                while (var.get('s')<=Js(6.0)):
                    try:
                        def PyJs_LONG_283_(var=var):
                            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('f', ((var.get('p')*var.get('M'))+(var.get('m')*var.get('c')))),var.put('m', ((var.get('m')*var.get('M'))-(var.get('p')*var.get('c'))))),var.put('p', var.get('f'))),var.put('_', (var.get('s')*((var.get(u"this").get('B_re').get(var.get('s'))*var.get('m'))-(var.get(u"this").get('B_im').get(var.get('s'))*var.get('p')))), '+')),var.put('x', (var.get('s')*((var.get(u"this").get('B_im').get(var.get('s'))*var.get('m'))+(var.get(u"this").get('B_re').get(var.get('s'))*var.get('p')))), '+'))
                        PyJs_LONG_283_()
                    finally:
                            (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
                var.put('v', ((var.get('_')*var.get('_'))+(var.get('x')*var.get('x'))))
                PyJsComma(var.put('M', (((var.get('d')*var.get('_'))+(var.get('y')*var.get('x')))/var.get('v'))),var.put('c', (((var.get('y')*var.get('_'))-(var.get('d')*var.get('x')))/var.get('v'))))
            finally:
                    (var.put('u',Js(var.get('u').to_number())+Js(1))-Js(1))
        var.put('g', var.get('M'))
        var.put('b', var.get('c'))
        var.put('w', Js(1.0))
        var.put('A', Js(0.0))
        #for JS loop
        var.put('s', Js(1.0))
        while (var.get('s')<=Js(9.0)):
            try:
                PyJsComma(var.put('w', var.get('g'), '*'),var.put('A', (var.get(u"this").get('D').get(var.get('s'))*var.get('w')), '+'))
            finally:
                    (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
        var.put('C', (var.get(u"this").get('lat0')+((var.get('A')*var.get('at'))*Js(100000.0))))
        var.put('E', (var.get(u"this").get('long0')+var.get('b')))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('E')),var.get('t').put('y', var.get('C'))),var.get('t'))
    PyJs_anonymous_280_._set_name('anonymous')
    var.put('Zs', Js({'init':PyJs_anonymous_276_,'forward':PyJs_anonymous_278_,'inverse':PyJs_anonymous_280_,'names':Js([Js('New_Zealand_Map_Grid'), Js('nzmg')])}))
    @Js
    def PyJs_anonymous_284_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        pass
    PyJs_anonymous_284_._set_name('anonymous')
    @Js
    def PyJs_anonymous_285_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'e', 'i', 's', 't', 'a'])
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        var.put('a', var.get('qt')((var.get('s')-var.get(u"this").get('long0'))))
        var.put('h', (var.get(u"this").get('x0')+(var.get(u"this").get('a')*var.get('a'))))
        var.put('e', (var.get(u"this").get('y0')+((var.get(u"this").get('a')*var.get('Math').callprop('log', var.get('Math').callprop('tan', ((var.get('Math').get('PI')/Js(4.0))+(var.get('i')/Js(2.5))))))*Js(1.25))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('h')),var.get('t').put('y', var.get('e'))),var.get('t'))
    PyJs_anonymous_285_._set_name('anonymous')
    @Js
    def PyJs_anonymous_286_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 's'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-'))
        var.put('s', var.get('qt')((var.get(u"this").get('long0')+(var.get('t').get('x')/var.get(u"this").get('a')))))
        var.put('i', (Js(2.5)*(var.get('Math').callprop('atan', var.get('Math').callprop('exp', ((Js(0.8)*var.get('t').get('y'))/var.get(u"this").get('a'))))-(var.get('Math').get('PI')/Js(4.0)))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_286_._set_name('anonymous')
    var.put('Ys', Js({'init':PyJs_anonymous_284_,'forward':PyJs_anonymous_285_,'inverse':PyJs_anonymous_286_,'names':Js([Js('Miller_Cylindrical'), Js('mill')])}))
    var.put('$s', Js(20.0))
    @Js
    def PyJs_anonymous_287_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_288_(var=var):
            return (PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('n', Js(1.0)),var.get(u"this").put('m', Js(0.0))),var.get(u"this").put('es', Js(0.0))),var.get(u"this").put('C_y', var.get('Math').callprop('sqrt', ((var.get(u"this").get('m')+Js(1.0))/var.get(u"this").get('n'))))),var.get(u"this").put('C_x', (var.get(u"this").get('C_y')/(var.get(u"this").get('m')+Js(1.0))))) if var.get(u"this").get('sphere') else var.get(u"this").put('en', var.get('is')(var.get(u"this").get('es'))))
        PyJs_LONG_288_()
    PyJs_anonymous_287_._set_name('anonymous')
    @Js
    def PyJs_anonymous_289_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('a', var.get('t').get('x'))
        var.put('h', var.get('t').get('y'))
        if PyJsComma(var.put('a', var.get('qt')((var.get('a')-var.get(u"this").get('long0')))),var.get(u"this").get('sphere')):
            if var.get(u"this").get('m'):
                #for JS loop
                var.put('e', (var.get(u"this").get('n')*var.get('Math').callprop('sin', var.get('h'))))
                var.put('n', var.get('$s'))
                while var.get('n'):
                    try:
                        var.put('r', ((((var.get(u"this").get('m')*var.get('h'))+var.get('Math').callprop('sin', var.get('h')))-var.get('e'))/(var.get(u"this").get('m')+var.get('Math').callprop('cos', var.get('h')))))
                        if PyJsComma(var.put('h', var.get('r'), '-'),(var.get('Math').callprop('abs', var.get('r'))<var.get('ot'))):
                            break
                    finally:
                            var.put('n',Js(var.get('n').to_number())-Js(1))
            else:
                var.put('h', (var.get('Math').callprop('asin', (var.get(u"this").get('n')*var.get('Math').callprop('sin', var.get('h')))) if PyJsStrictNeq(Js(1.0),var.get(u"this").get('n')) else var.get('h')))
            PyJsComma(var.put('s', (((var.get(u"this").get('a')*var.get(u"this").get('C_x'))*var.get('a'))*(var.get(u"this").get('m')+var.get('Math').callprop('cos', var.get('h'))))),var.put('i', ((var.get(u"this").get('a')*var.get(u"this").get('C_y'))*var.get('h'))))
        else:
            var.put('o', var.get('Math').callprop('sin', var.get('h')))
            var.put('l', var.get('Math').callprop('cos', var.get('h')))
            PyJsComma(var.put('i', (var.get(u"this").get('a')*var.get('as')(var.get('h'), var.get('o'), var.get('l'), var.get(u"this").get('en')))),var.put('s', (((var.get(u"this").get('a')*var.get('a'))*var.get('l'))/var.get('Math').callprop('sqrt', (Js(1.0)-((var.get(u"this").get('es')*var.get('o'))*var.get('o')))))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('s')),var.get('t').put('y', var.get('i'))),var.get('t'))
    PyJs_anonymous_289_._set_name('anonymous')
    @Js
    def PyJs_anonymous_290_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_293_(var=var):
            def PyJs_LONG_291_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get(u"this").get('C_y'), '/'),var.put('a', (var.get(u"this").get('C_x')*(var.get(u"this").get('m')+var.get('Math').callprop('cos', var.get('s')))), '/')),(var.put('s', var.get('Fs')((((var.get(u"this").get('m')*var.get('s'))+var.get('Math').callprop('sin', var.get('s')))/var.get(u"this").get('n')))) if var.get(u"this").get('m') else (PyJsStrictNeq(Js(1.0),var.get(u"this").get('n')) and var.put('s', var.get('Fs')((var.get('Math').callprop('sin', var.get('s'))/var.get(u"this").get('n'))))))),var.put('a', var.get('qt')((var.get('a')+var.get(u"this").get('long0'))))),var.put('s', var.get('Is')(var.get('s'))))
            def PyJs_LONG_292_(var=var):
                return (PyJsComma(PyJsComma(var.put('h', var.get('Math').callprop('sin', var.get('s'))),var.put('i', (var.get(u"this").get('long0')+((var.get('t').get('x')*var.get('Math').callprop('sqrt', (Js(1.0)-((var.get(u"this").get('es')*var.get('h'))*var.get('h')))))/(var.get(u"this").get('a')*var.get('Math').callprop('cos', var.get('s'))))))),var.put('a', var.get('qt')(var.get('i')))) if (var.put('h', var.get('Math').callprop('abs', var.get('s')))<var.get('ht')) else (((var.get('h')-var.get('ot'))<var.get('ht')) and var.put('a', var.get(u"this").get('long0'))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.put('a', (var.get('t').get('x')/var.get(u"this").get('a')))),var.get('t').put('y', var.get(u"this").get('y0'), '-')),var.put('s', (var.get('t').get('y')/var.get(u"this").get('a')))),(PyJs_LONG_291_() if var.get(u"this").get('sphere') else PyJsComma(var.put('s', var.get('hs')((var.get('t').get('y')/var.get(u"this").get('a')), var.get(u"this").get('es'), var.get(u"this").get('en'))),PyJs_LONG_292_()))),var.get('t').put('x', var.get('a'))),var.get('t').put('y', var.get('s'))),var.get('t'))
        return PyJs_LONG_293_()
    PyJs_anonymous_290_._set_name('anonymous')
    var.put('ti', Js({'init':PyJs_anonymous_287_,'forward':PyJs_anonymous_289_,'inverse':PyJs_anonymous_290_,'names':Js([Js('Sinusoidal'), Js('sinu')])}))
    @Js
    def PyJs_anonymous_294_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        pass
    PyJs_anonymous_294_._set_name('anonymous')
    @Js
    def PyJs_anonymous_295_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        #for JS loop
        var.put('s', var.get('t').get('x'))
        var.put('i', var.get('t').get('y'))
        var.put('a', var.get('qt')((var.get('s')-var.get(u"this").get('long0'))))
        var.put('h', var.get('i'))
        var.put('e', (var.get('Math').get('PI')*var.get('Math').callprop('sin', var.get('i'))))
        while 1:
            var.put('n', ((-((var.get('h')+var.get('Math').callprop('sin', var.get('h')))-var.get('e')))/(Js(1.0)+var.get('Math').callprop('cos', var.get('h')))))
            if PyJsComma(var.put('h', var.get('n'), '+'),(var.get('Math').callprop('abs', var.get('n'))<var.get('ot'))):
                break
        
        PyJsComma(var.put('h', Js(2.0), '/'),((((var.get('Math').get('PI')/Js(2.0))-var.get('Math').callprop('abs', var.get('i')))<var.get('ot')) and var.put('a', Js(0.0))))
        var.put('r', ((((Js(0.900316316158)*var.get(u"this").get('a'))*var.get('a'))*var.get('Math').callprop('cos', var.get('h')))+var.get(u"this").get('x0')))
        var.put('o', (((Js(1.4142135623731)*var.get(u"this").get('a'))*var.get('Math').callprop('sin', var.get('h')))+var.get(u"this").get('y0')))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('r')),var.get('t').put('y', var.get('o'))),var.get('t'))
    PyJs_anonymous_295_._set_name('anonymous')
    @Js
    def PyJs_anonymous_296_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        pass
        def PyJs_LONG_297_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-')),var.put('i', (var.get('t').get('y')/(Js(1.4142135623731)*var.get(u"this").get('a'))))),((var.get('Math').callprop('abs', var.get('i'))>Js(0.999999999999)) and var.put('i', Js(0.999999999999)))),var.put('s', var.get('Math').callprop('asin', var.get('i'))))
        PyJs_LONG_297_()
        var.put('a', var.get('qt')((var.get(u"this").get('long0')+(var.get('t').get('x')/((Js(0.900316316158)*var.get(u"this").get('a'))*var.get('Math').callprop('cos', var.get('s')))))))
        def PyJs_LONG_298_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(((var.get('a')<(-var.get('Math').get('PI'))) and var.put('a', (-var.get('Math').get('PI')))),((var.get('a')>var.get('Math').get('PI')) and var.put('a', var.get('Math').get('PI')))),var.put('i', (((Js(2.0)*var.get('s'))+var.get('Math').callprop('sin', (Js(2.0)*var.get('s'))))/var.get('Math').get('PI')))),((var.get('Math').callprop('abs', var.get('i'))>Js(1.0)) and var.put('i', Js(1.0))))
        PyJs_LONG_298_()
        var.put('h', var.get('Math').callprop('asin', var.get('i')))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('a')),var.get('t').put('y', var.get('h'))),var.get('t'))
    PyJs_anonymous_296_._set_name('anonymous')
    var.put('si', Js({'init':PyJs_anonymous_294_,'forward':PyJs_anonymous_295_,'inverse':PyJs_anonymous_296_,'names':Js([Js('Mollweide'), Js('moll')])}))
    @Js
    def PyJs_anonymous_299_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_301_(var=var):
            def PyJs_LONG_300_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('sinphi', var.get('Math').callprop('sin', var.get(u"this").get('lat2'))),var.get(u"this").put('cosphi', var.get('Math').callprop('cos', var.get(u"this").get('lat2')))),var.get(u"this").put('ms2', var.get('St')(var.get(u"this").get('e'), var.get(u"this").get('sinphi'), var.get(u"this").get('cosphi')))),var.get(u"this").put('ml2', var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get(u"this").get('lat2')))),var.get(u"this").put('ns', ((var.get(u"this").get('ms1')-var.get(u"this").get('ms2'))/(var.get(u"this").get('ml2')-var.get(u"this").get('ml1')))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('lat2', (var.get(u"this").get('lat2') or var.get(u"this").get('lat1'))),var.get(u"this").put('temp', (var.get(u"this").get('b')/var.get(u"this").get('a')))),var.get(u"this").put('es', (Js(1.0)-var.get('Math').callprop('pow', var.get(u"this").get('temp'), Js(2.0))))),var.get(u"this").put('e', var.get('Math').callprop('sqrt', var.get(u"this").get('es')))),var.get(u"this").put('e0', var.get('Ps')(var.get(u"this").get('es')))),var.get(u"this").put('e1', var.get('Ns')(var.get(u"this").get('es')))),var.get(u"this").put('e2', var.get('Ss')(var.get(u"this").get('es')))),var.get(u"this").put('e3', var.get('ks')(var.get(u"this").get('es')))),var.get(u"this").put('sinphi', var.get('Math').callprop('sin', var.get(u"this").get('lat1')))),var.get(u"this").put('cosphi', var.get('Math').callprop('cos', var.get(u"this").get('lat1')))),var.get(u"this").put('ms1', var.get('St')(var.get(u"this").get('e'), var.get(u"this").get('sinphi'), var.get(u"this").get('cosphi')))),var.get(u"this").put('ml1', var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get(u"this").get('lat1')))),(var.get(u"this").put('ns', var.get(u"this").get('sinphi')) if (var.get('Math').callprop('abs', (var.get(u"this").get('lat1')-var.get(u"this").get('lat2')))<var.get('ot')) else PyJs_LONG_300_())),var.get(u"this").put('g', (var.get(u"this").get('ml1')+(var.get(u"this").get('ms1')/var.get(u"this").get('ns'))))),var.get(u"this").put('ml0', var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get(u"this").get('lat0')))),var.get(u"this").put('rh', (var.get(u"this").get('a')*(var.get(u"this").get('g')-var.get(u"this").get('ml0')))))
        ((var.get('Math').callprop('abs', (var.get(u"this").get('lat1')+var.get(u"this").get('lat2')))<var.get('ot')) or PyJs_LONG_301_())
    PyJs_anonymous_299_._set_name('anonymous')
    @Js
    def PyJs_anonymous_302_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('i', var.get('t').get('x'))
        var.put('a', var.get('t').get('y'))
        if var.get(u"this").get('sphere'):
            var.put('s', (var.get(u"this").get('a')*(var.get(u"this").get('g')-var.get('a'))))
        else:
            var.put('h', var.get('Es')(var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'), var.get('a')))
            var.put('s', (var.get(u"this").get('a')*(var.get(u"this").get('g')-var.get('h'))))
        var.put('e', (var.get(u"this").get('ns')*var.get('qt')((var.get('i')-var.get(u"this").get('long0')))))
        var.put('n', (var.get(u"this").get('x0')+(var.get('s')*var.get('Math').callprop('sin', var.get('e')))))
        var.put('r', ((var.get(u"this").get('y0')+var.get(u"this").get('rh'))-(var.get('s')*var.get('Math').callprop('cos', var.get('e')))))
        return PyJsComma(PyJsComma(var.get('t').put('x', var.get('n')),var.get('t').put('y', var.get('r'))),var.get('t'))
    PyJs_anonymous_302_._set_name('anonymous')
    @Js
    def PyJs_anonymous_303_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 't', 'a'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', ((var.get(u"this").get('rh')-var.get('t').get('y'))+var.get(u"this").get('y0'))))
        pass
        def PyJs_LONG_304_(var=var):
            return (PyJsComma(var.put('i', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y'))))),var.put('s', Js(1.0))) if (var.get(u"this").get('ns')>=Js(0.0)) else PyJsComma(var.put('i', (-var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))),var.put('s', (-Js(1.0)))))
        PyJs_LONG_304_()
        var.put('e', Js(0.0))
        if PyJsComma((PyJsStrictNeq(Js(0.0),var.get('i')) and var.put('e', var.get('Math').callprop('atan2', (var.get('s')*var.get('t').get('x')), (var.get('s')*var.get('t').get('y'))))),var.get(u"this").get('sphere')):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', var.get('qt')((var.get(u"this").get('long0')+(var.get('e')/var.get(u"this").get('ns'))))),var.put('a', var.get('Is')((var.get(u"this").get('g')-(var.get('i')/var.get(u"this").get('a')))))),var.get('t').put('x', var.get('h'))),var.get('t').put('y', var.get('a'))),var.get('t'))
        var.put('n', (var.get(u"this").get('g')-(var.get('i')/var.get(u"this").get('a'))))
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('a', var.get('Os')(var.get('n'), var.get(u"this").get('e0'), var.get(u"this").get('e1'), var.get(u"this").get('e2'), var.get(u"this").get('e3'))),var.put('h', var.get('qt')((var.get(u"this").get('long0')+(var.get('e')/var.get(u"this").get('ns')))))),var.get('t').put('x', var.get('h'))),var.get('t').put('y', var.get('a'))),var.get('t'))
    PyJs_anonymous_303_._set_name('anonymous')
    var.put('ii', Js({'init':PyJs_anonymous_299_,'forward':PyJs_anonymous_302_,'inverse':PyJs_anonymous_303_,'names':Js([Js('Equidistant_Conic'), Js('eqdc')])}))
    @Js
    def PyJs_anonymous_305_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put('R', var.get(u"this").get('a'))
    PyJs_anonymous_305_._set_name('anonymous')
    @Js
    def PyJs_anonymous_306_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'd', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 's', 'r', 'f', 'a'])
        var.put('a', var.get('t').get('x'))
        var.put('h', var.get('t').get('y'))
        var.put('e', var.get('qt')((var.get('a')-var.get(u"this").get('long0'))))
        ((var.get('Math').callprop('abs', var.get('h'))<=var.get('ot')) and PyJsComma(var.put('s', (var.get(u"this").get('x0')+(var.get(u"this").get('R')*var.get('e')))),var.put('i', var.get(u"this").get('y0'))))
        var.put('n', var.get('Fs')((Js(2.0)*var.get('Math').callprop('abs', (var.get('h')/var.get('Math').get('PI'))))))
        def PyJs_LONG_307_(var=var):
            return (((var.get('Math').callprop('abs', var.get('e'))<=var.get('ot')) or (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('h'))-var.get('ht')))<=var.get('ot'))) and PyJsComma(var.put('s', var.get(u"this").get('x0')),var.put('i', ((var.get(u"this").get('y0')+((var.get('Math').get('PI')*var.get(u"this").get('R'))*var.get('Math').callprop('tan', (Js(0.5)*var.get('n'))))) if (var.get('h')>=Js(0.0)) else (var.get(u"this").get('y0')+((var.get('Math').get('PI')*var.get(u"this").get('R'))*(-var.get('Math').callprop('tan', (Js(0.5)*var.get('n'))))))))))
        PyJs_LONG_307_()
        var.put('r', (Js(0.5)*var.get('Math').callprop('abs', ((var.get('Math').get('PI')/var.get('e'))-(var.get('e')/var.get('Math').get('PI'))))))
        var.put('o', (var.get('r')*var.get('r')))
        var.put('l', var.get('Math').callprop('sin', var.get('n')))
        var.put('M', var.get('Math').callprop('cos', var.get('n')))
        var.put('c', (var.get('M')/((var.get('l')+var.get('M'))-Js(1.0))))
        var.put('u', (var.get('c')*var.get('c')))
        var.put('f', (var.get('c')*((Js(2.0)/var.get('l'))-Js(1.0))))
        var.put('m', (var.get('f')*var.get('f')))
        var.put('p', (((var.get('Math').get('PI')*var.get(u"this").get('R'))*((var.get('r')*(var.get('c')-var.get('m')))+var.get('Math').callprop('sqrt', (((var.get('o')*(var.get('c')-var.get('m')))*(var.get('c')-var.get('m')))-((var.get('m')+var.get('o'))*(var.get('u')-var.get('m')))))))/(var.get('m')+var.get('o'))))
        PyJsComma(((var.get('e')<Js(0.0)) and var.put('p', (-var.get('p')))),var.put('s', (var.get(u"this").get('x0')+var.get('p'))))
        var.put('d', (var.get('o')+var.get('c')))
        def PyJs_LONG_308_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('p', (((var.get('Math').get('PI')*var.get(u"this").get('R'))*((var.get('f')*var.get('d'))-(var.get('r')*var.get('Math').callprop('sqrt', (((var.get('m')+var.get('o'))*(var.get('o')+Js(1.0)))-(var.get('d')*var.get('d')))))))/(var.get('m')+var.get('o')))),var.put('i', ((var.get(u"this").get('y0')+var.get('p')) if (var.get('h')>=Js(0.0)) else (var.get(u"this").get('y0')-var.get('p'))))),var.get('t').put('x', var.get('s'))),var.get('t').put('y', var.get('i'))),var.get('t'))
        return PyJs_LONG_308_()
    PyJs_anonymous_306_._set_name('anonymous')
    @Js
    def PyJs_anonymous_309_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'n', 'o', 'h', 'e', 'i', 't', 's', 'r', 'f', 'a'])
        pass
        def PyJs_LONG_310_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-')),var.put('c', (var.get('Math').get('PI')*var.get(u"this").get('R')))),var.put('a', (var.get('t').get('x')/var.get('c')))),var.put('h', (var.get('t').get('y')/var.get('c')))),var.put('e', ((var.get('a')*var.get('a'))+(var.get('h')*var.get('h'))))),var.put('n', ((-var.get('Math').callprop('abs', var.get('h')))*(Js(1.0)+var.get('e'))))),var.put('r', ((var.get('n')-((Js(2.0)*var.get('h'))*var.get('h')))+(var.get('a')*var.get('a'))))),var.put('o', (((((-Js(2.0))*var.get('n'))+Js(1.0))+((Js(2.0)*var.get('h'))*var.get('h')))+(var.get('e')*var.get('e'))))),var.put('f', (((var.get('h')*var.get('h'))/var.get('o'))+((((((((Js(2.0)*var.get('r'))*var.get('r'))*var.get('r'))/var.get('o'))/var.get('o'))/var.get('o'))-((((Js(9.0)*var.get('n'))*var.get('r'))/var.get('o'))/var.get('o')))/Js(27.0))))),var.put('l', ((var.get('n')-(((var.get('r')*var.get('r'))/Js(3.0))/var.get('o')))/var.get('o')))),var.put('M', (Js(2.0)*var.get('Math').callprop('sqrt', ((-var.get('l'))/Js(3.0)))))),var.put('c', (((Js(3.0)*var.get('f'))/var.get('l'))/var.get('M')))),((var.get('Math').callprop('abs', var.get('c'))>Js(1.0)) and var.put('c', (Js(1.0) if (var.get('c')>=Js(0.0)) else (-Js(1.0)))))),var.put('u', (var.get('Math').callprop('acos', var.get('c'))/Js(3.0)))),var.put('i', (((((-var.get('M'))*var.get('Math').callprop('cos', (var.get('u')+(var.get('Math').get('PI')/Js(3.0)))))-((var.get('r')/Js(3.0))/var.get('o')))*var.get('Math').get('PI')) if (var.get('t').get('y')>=Js(0.0)) else ((-(((-var.get('M'))*var.get('Math').callprop('cos', (var.get('u')+(var.get('Math').get('PI')/Js(3.0)))))-((var.get('r')/Js(3.0))/var.get('o'))))*var.get('Math').get('PI'))))),var.put('s', (var.get(u"this").get('long0') if (var.get('Math').callprop('abs', var.get('a'))<var.get('ot')) else var.get('qt')((var.get(u"this").get('long0')+(((var.get('Math').get('PI')*((var.get('e')-Js(1.0))+var.get('Math').callprop('sqrt', ((Js(1.0)+(Js(2.0)*((var.get('a')*var.get('a'))-(var.get('h')*var.get('h')))))+(var.get('e')*var.get('e'))))))/Js(2.0))/var.get('a'))))))),var.get('t').put('x', var.get('s'))),var.get('t').put('y', var.get('i'))),var.get('t'))
        return PyJs_LONG_310_()
    PyJs_anonymous_309_._set_name('anonymous')
    var.put('ai', Js({'init':PyJs_anonymous_305_,'forward':PyJs_anonymous_306_,'inverse':PyJs_anonymous_309_,'names':Js([Js('Van_der_Grinten_I'), Js('VanDerGrinten'), Js('vandg')])}))
    @Js
    def PyJs_anonymous_311_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        PyJsComma(var.get(u"this").put('sin_p12', var.get('Math').callprop('sin', var.get(u"this").get('lat0'))),var.get(u"this").put('cos_p12', var.get('Math').callprop('cos', var.get(u"this").get('lat0'))))
    PyJs_anonymous_311_._set_name('anonymous')
    @Js
    def PyJs_anonymous_312_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 'P', 'n', 'e', 's', 'p', 'r', 'g', 't', 'M', 'c', 'E', 'b', 'h', 'A', 'i', 'y', 'x', 'm', 'C', 'v', 'w', 'N', 'd', 'l', 'o', 'f', '_', 'a'])
        var.put('A', var.get('t').get('x'))
        var.put('C', var.get('t').get('y'))
        var.put('E', var.get('Math').callprop('sin', var.get('t').get('y')))
        var.put('P', var.get('Math').callprop('cos', var.get('t').get('y')))
        var.put('N', var.get('qt')((var.get('A')-var.get(u"this").get('long0'))))
        def PyJs_LONG_315_(var=var):
            def PyJs_LONG_314_(var=var):
                def PyJs_LONG_313_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('_', ((var.get(u"this").get('sin_p12')*var.get('E'))+((var.get(u"this").get('cos_p12')*var.get('P'))*var.get('Math').callprop('cos', var.get('N'))))),var.put('d', var.get('Math').callprop('acos', var.get('_')))),var.put('y', ((var.get('d')/var.get('Math').callprop('sin', var.get('d'))) if var.get('d') else Js(1.0)))),var.get('t').put('x', (var.get(u"this").get('x0')+(((var.get(u"this").get('a')*var.get('y'))*var.get('P'))*var.get('Math').callprop('sin', var.get('N')))))),var.get('t').put('y', (var.get(u"this").get('y0')+((var.get(u"this").get('a')*var.get('y'))*((var.get(u"this").get('cos_p12')*var.get('E'))-((var.get(u"this").get('sin_p12')*var.get('P'))*var.get('Math').callprop('cos', var.get('N')))))))),var.get('t'))
                return (PyJsComma(PyJsComma(var.get('t').put('x', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*(var.get('ht')+var.get('C')))*var.get('Math').callprop('sin', var.get('N'))))),var.get('t').put('y', (var.get(u"this").get('y0')+((var.get(u"this").get('a')*(var.get('ht')+var.get('C')))*var.get('Math').callprop('cos', var.get('N')))))),var.get('t')) if (var.get('Math').callprop('abs', (var.get(u"this").get('sin_p12')+Js(1.0)))<=var.get('ot')) else PyJs_LONG_313_())
            return (PyJsComma(PyJsComma(var.get('t').put('x', (var.get(u"this").get('x0')+((var.get(u"this").get('a')*(var.get('ht')-var.get('C')))*var.get('Math').callprop('sin', var.get('N'))))),var.get('t').put('y', (var.get(u"this").get('y0')-((var.get(u"this").get('a')*(var.get('ht')-var.get('C')))*var.get('Math').callprop('cos', var.get('N')))))),var.get('t')) if (var.get('Math').callprop('abs', (var.get(u"this").get('sin_p12')-Js(1.0)))<=var.get('ot')) else PyJs_LONG_314_())
        def PyJs_LONG_320_(var=var):
            def PyJs_LONG_316_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('e', (var.get(u"this").get('a')*var.get('Es')(var.get('s'), var.get('i'), var.get('a'), var.get('h'), var.get('ht')))),var.put('n', (var.get(u"this").get('a')*var.get('Es')(var.get('s'), var.get('i'), var.get('a'), var.get('h'), var.get('C'))))),var.get('t').put('x', (var.get(u"this").get('x0')+((var.get('e')-var.get('n'))*var.get('Math').callprop('sin', var.get('N')))))),var.get('t').put('y', (var.get(u"this").get('y0')-((var.get('e')-var.get('n'))*var.get('Math').callprop('cos', var.get('N')))))),var.get('t'))
            def PyJs_LONG_317_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('e', (var.get(u"this").get('a')*var.get('Es')(var.get('s'), var.get('i'), var.get('a'), var.get('h'), var.get('ht')))),var.put('n', (var.get(u"this").get('a')*var.get('Es')(var.get('s'), var.get('i'), var.get('a'), var.get('h'), var.get('C'))))),var.get('t').put('x', (var.get(u"this").get('x0')+((var.get('e')+var.get('n'))*var.get('Math').callprop('sin', var.get('N')))))),var.get('t').put('y', (var.get(u"this").get('y0')+((var.get('e')+var.get('n'))*var.get('Math').callprop('cos', var.get('N')))))),var.get('t'))
            def PyJs_LONG_319_(var=var):
                def PyJs_LONG_318_(var=var):
                    return ((-var.get('Math').callprop('asin', ((var.get(u"this").get('cos_p12')*var.get('Math').callprop('sin', var.get('M')))-(var.get(u"this").get('sin_p12')*var.get('Math').callprop('cos', var.get('M')))))) if (var.get('Math').callprop('abs', (var.get('Math').callprop('abs', var.get('c'))-var.get('Math').get('PI')))<=var.get('ot')) else var.get('Math').callprop('asin', ((var.get('Math').callprop('sin', var.get('N'))*var.get('Math').callprop('cos', var.get('M')))/var.get('Math').callprop('sin', var.get('c')))))
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('r', (var.get('E')/var.get('P'))),var.put('o', var.get('qs')(var.get(u"this").get('a'), var.get(u"this").get('e'), var.get(u"this").get('sin_p12')))),var.put('l', var.get('qs')(var.get(u"this").get('a'), var.get(u"this").get('e'), var.get('E')))),var.put('M', var.get('Math').callprop('atan', (((Js(1.0)-var.get(u"this").get('es'))*var.get('r'))+(((var.get(u"this").get('es')*var.get('o'))*var.get(u"this").get('sin_p12'))/(var.get('l')*var.get('P'))))))),var.put('c', var.get('Math').callprop('atan2', var.get('Math').callprop('sin', var.get('N')), ((var.get(u"this").get('cos_p12')*var.get('Math').callprop('tan', var.get('M')))-(var.get(u"this").get('sin_p12')*var.get('Math').callprop('cos', var.get('N'))))))),var.put('x', (var.get('Math').callprop('asin', ((var.get(u"this").get('cos_p12')*var.get('Math').callprop('sin', var.get('M')))-(var.get(u"this").get('sin_p12')*var.get('Math').callprop('cos', var.get('M'))))) if PyJsStrictEq(Js(0.0),var.get('c')) else PyJs_LONG_318_()))),var.put('u', ((var.get(u"this").get('e')*var.get(u"this").get('sin_p12'))/var.get('Math').callprop('sqrt', (Js(1.0)-var.get(u"this").get('es')))))),var.put('f', (((var.get(u"this").get('e')*var.get(u"this").get('cos_p12'))*var.get('Math').callprop('cos', var.get('c')))/var.get('Math').callprop('sqrt', (Js(1.0)-var.get(u"this").get('es')))))),var.put('m', (var.get('u')*var.get('f')))),var.put('p', (var.get('f')*var.get('f')))),var.put('v', (var.get('x')*var.get('x')))),var.put('g', (var.get('v')*var.get('x')))),var.put('b', (var.get('g')*var.get('x')))),var.put('w', (var.get('b')*var.get('x')))),var.put('d', ((var.get('o')*var.get('x'))*((((Js(1.0)-(((var.get('v')*var.get('p'))*(Js(1.0)-var.get('p')))/Js(6.0)))+(((var.get('g')/Js(8.0))*var.get('m'))*(Js(1.0)-(Js(2.0)*var.get('p')))))+((var.get('b')/Js(120.0))*((var.get('p')*(Js(4.0)-(Js(7.0)*var.get('p'))))-(((Js(3.0)*var.get('u'))*var.get('u'))*(Js(1.0)-(Js(7.0)*var.get('p')))))))-((var.get('w')/Js(48.0))*var.get('m')))))),var.get('t').put('x', (var.get(u"this").get('x0')+(var.get('d')*var.get('Math').callprop('sin', var.get('c')))))),var.get('t').put('y', (var.get(u"this").get('y0')+(var.get('d')*var.get('Math').callprop('cos', var.get('c')))))),var.get('t'))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('Ps')(var.get(u"this").get('es'))),var.put('i', var.get('Ns')(var.get(u"this").get('es')))),var.put('a', var.get('Ss')(var.get(u"this").get('es')))),var.put('h', var.get('ks')(var.get(u"this").get('es')))),(PyJs_LONG_316_() if (var.get('Math').callprop('abs', (var.get(u"this").get('sin_p12')-Js(1.0)))<=var.get('ot')) else (PyJs_LONG_317_() if (var.get('Math').callprop('abs', (var.get(u"this").get('sin_p12')+Js(1.0)))<=var.get('ot')) else PyJs_LONG_319_())))
        return (PyJs_LONG_315_() if var.get(u"this").get('sphere') else PyJs_LONG_320_())
    PyJs_anonymous_312_._set_name('anonymous')
    @Js
    def PyJs_anonymous_321_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 'n', 'e', 's', 'p', 'r', 'g', 't', 'M', 'c', 'b', 'h', 'A', 'i', 'y', 'x', 'm', 'v', 'w', 'd', 'l', 'o', 'f', '_', 'a'])
        PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-'))
        pass
        if var.get(u"this").get('sphere'):
            if (var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))>((Js(2.0)*var.get('ht'))*var.get(u"this").get('a'))):
                return var.get('undefined')
            def PyJs_LONG_323_(var=var):
                def PyJs_LONG_322_(var=var):
                    return (((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', var.get('t').get('x'), (-var.get('t').get('y')))) if (var.get(u"this").get('lat0')>=Js(0.0)) else (var.get(u"this").get('long0')-var.get('Math').callprop('atan2', (-var.get('t').get('x')), var.get('t').get('y')))) if (var.get('Math').callprop('abs', var.get('r'))<=var.get('ot')) else (var.get(u"this").get('long0')+var.get('Math').callprop('atan2', (var.get('t').get('x')*var.get('a')), (((var.get('s')*var.get(u"this").get('cos_p12'))*var.get('h'))-((var.get('t').get('y')*var.get(u"this").get('sin_p12'))*var.get('a'))))))
                return (var.put('n', var.get(u"this").get('lat0')) if (var.get('Math').callprop('abs', var.get('s'))<=var.get('ot')) else PyJsComma(PyJsComma(var.put('n', var.get('Fs')(((var.get('h')*var.get(u"this").get('sin_p12'))+(((var.get('t').get('y')*var.get('a'))*var.get(u"this").get('cos_p12'))/var.get('s'))))),var.put('r', (var.get('Math').callprop('abs', var.get(u"this").get('lat0'))-var.get('ht')))),var.put('e', var.get('qt')(PyJs_LONG_322_()))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', (var.get('s')/var.get(u"this").get('a'))),var.put('a', var.get('Math').callprop('sin', var.get('i')))),var.put('h', var.get('Math').callprop('cos', var.get('i')))),var.put('e', var.get(u"this").get('long0'))),PyJs_LONG_323_()),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('n'))),var.get('t'))
        def PyJs_LONG_327_(var=var):
            def PyJs_LONG_324_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('u', (var.get(u"this").get('a')*var.get('Es')(var.get('o'), var.get('l'), var.get('M'), var.get('c'), var.get('ht')))),var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))),var.put('f', (var.get('u')-var.get('s')))),var.put('n', var.get('Os')((var.get('f')/var.get(u"this").get('a')), var.get('o'), var.get('l'), var.get('M'), var.get('c')))),var.put('e', var.get('qt')((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', var.get('t').get('x'), ((-Js(1.0))*var.get('t').get('y'))))))),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('n'))),var.get('t'))
            def PyJs_LONG_325_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('u', (var.get(u"this").get('a')*var.get('Es')(var.get('o'), var.get('l'), var.get('M'), var.get('c'), var.get('ht')))),var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))),var.put('f', (var.get('s')-var.get('u')))),var.put('n', var.get('Os')((var.get('f')/var.get(u"this").get('a')), var.get('o'), var.get('l'), var.get('M'), var.get('c')))),var.put('e', var.get('qt')((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', var.get('t').get('x'), var.get('t').get('y')))))),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('n'))),var.get('t'))
            def PyJs_LONG_326_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y'))))),var.put('d', var.get('Math').callprop('atan2', var.get('t').get('x'), var.get('t').get('y')))),var.put('m', var.get('qs')(var.get(u"this").get('a'), var.get(u"this").get('e'), var.get(u"this").get('sin_p12')))),var.put('y', var.get('Math').callprop('cos', var.get('d')))),var.put('_', ((var.get(u"this").get('e')*var.get(u"this").get('cos_p12'))*var.get('y')))),var.put('x', (((-var.get('_'))*var.get('_'))/(Js(1.0)-var.get(u"this").get('es'))))),var.put('v', ((((((Js(3.0)*var.get(u"this").get('es'))*(Js(1.0)-var.get('x')))*var.get(u"this").get('sin_p12'))*var.get(u"this").get('cos_p12'))*var.get('y'))/(Js(1.0)-var.get(u"this").get('es'))))),var.put('g', (var.get('s')/var.get('m')))),var.put('b', ((var.get('g')-(((var.get('x')*(Js(1.0)+var.get('x')))*var.get('Math').callprop('pow', var.get('g'), Js(3.0)))/Js(6.0)))-(((var.get('v')*(Js(1.0)+(Js(3.0)*var.get('x'))))*var.get('Math').callprop('pow', var.get('g'), Js(4.0)))/Js(24.0))))),var.put('w', ((Js(1.0)-(((var.get('x')*var.get('b'))*var.get('b'))/Js(2.0)))-((((var.get('g')*var.get('b'))*var.get('b'))*var.get('b'))/Js(6.0))))),var.put('p', var.get('Math').callprop('asin', ((var.get(u"this").get('sin_p12')*var.get('Math').callprop('cos', var.get('b')))+((var.get(u"this").get('cos_p12')*var.get('Math').callprop('sin', var.get('b')))*var.get('y')))))),var.put('e', var.get('qt')((var.get(u"this").get('long0')+var.get('Math').callprop('asin', ((var.get('Math').callprop('sin', var.get('d'))*var.get('Math').callprop('sin', var.get('b')))/var.get('Math').callprop('cos', var.get('p')))))))),var.put('A', var.get('Math').callprop('sin', var.get('p')))),var.put('n', var.get('Math').callprop('atan2', ((var.get('A')-((var.get(u"this").get('es')*var.get('w'))*var.get(u"this").get('sin_p12')))*var.get('Math').callprop('tan', var.get('p'))), (var.get('A')*(Js(1.0)-var.get(u"this").get('es')))))),var.get('t').put('x', var.get('e'))),var.get('t').put('y', var.get('n'))),var.get('t'))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('o', var.get('Ps')(var.get(u"this").get('es'))),var.put('l', var.get('Ns')(var.get(u"this").get('es')))),var.put('M', var.get('Ss')(var.get(u"this").get('es')))),var.put('c', var.get('ks')(var.get(u"this").get('es')))),(PyJs_LONG_324_() if (var.get('Math').callprop('abs', (var.get(u"this").get('sin_p12')-Js(1.0)))<=var.get('ot')) else (PyJs_LONG_325_() if (var.get('Math').callprop('abs', (var.get(u"this").get('sin_p12')+Js(1.0)))<=var.get('ot')) else PyJs_LONG_326_())))
        return PyJs_LONG_327_()
    PyJs_anonymous_321_._set_name('anonymous')
    var.put('hi', Js({'init':PyJs_anonymous_311_,'forward':PyJs_anonymous_312_,'inverse':PyJs_anonymous_321_,'names':Js([Js('Azimuthal_Equidistant'), Js('aeqd')])}))
    @Js
    def PyJs_anonymous_328_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        PyJsComma(var.get(u"this").put('sin_p14', var.get('Math').callprop('sin', var.get(u"this").get('lat0'))),var.get(u"this").put('cos_p14', var.get('Math').callprop('cos', var.get(u"this").get('lat0'))))
    PyJs_anonymous_328_._set_name('anonymous')
    @Js
    def PyJs_anonymous_329_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['l', 'n', 'o', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        var.put('o', var.get('t').get('x'))
        var.put('l', var.get('t').get('y'))
        def PyJs_LONG_331_(var=var):
            def PyJs_LONG_330_(var=var):
                return (((var.put('e', ((var.get(u"this").get('sin_p14')*var.get('s'))+((var.get(u"this").get('cos_p14')*var.get('i'))*var.get('h'))))>Js(0.0)) or (var.get('Math').callprop('abs', var.get('e'))<=var.get('ot'))) and PyJsComma(var.put('n', (((Js(1.0)*var.get(u"this").get('a'))*var.get('i'))*var.get('Math').callprop('sin', var.get('a')))),var.put('r', (var.get(u"this").get('y0')+((Js(1.0)*var.get(u"this").get('a'))*((var.get(u"this").get('cos_p14')*var.get('s'))-((var.get(u"this").get('sin_p14')*var.get('i'))*var.get('h'))))))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('a', var.get('qt')((var.get('o')-var.get(u"this").get('long0')))),var.put('s', var.get('Math').callprop('sin', var.get('l')))),var.put('i', var.get('Math').callprop('cos', var.get('l')))),var.put('h', var.get('Math').callprop('cos', var.get('a')))),PyJs_LONG_330_()),var.get('t').put('x', var.get('n'))),var.get('t').put('y', var.get('r'))),var.get('t'))
        return PyJs_LONG_331_()
    PyJs_anonymous_329_._set_name('anonymous')
    @Js
    def PyJs_anonymous_332_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'h', 'e', 'i', 's', 'r', 't', 'a'])
        pass
        def PyJs_LONG_336_(var=var):
            def PyJs_LONG_335_(var=var):
                def PyJs_LONG_334_(var=var):
                    def PyJs_LONG_333_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(var.put('n', var.get('qt')(((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', var.get('t').get('x'), (-var.get('t').get('y')))) if (var.get(u"this").get('lat0')>=Js(0.0)) else (var.get(u"this").get('long0')-var.get('Math').callprop('atan2', (-var.get('t').get('x')), var.get('t').get('y')))))),var.get('t').put('x', var.get('n'))),var.get('t').put('y', var.get('r'))),var.get('t'))
                    return (PyJs_LONG_333_() if (var.get('Math').callprop('abs', var.get('e'))<=var.get('ot')) else PyJsComma(PyJsComma(PyJsComma(var.put('n', var.get('qt')((var.get(u"this").get('long0')+var.get('Math').callprop('atan2', (var.get('t').get('x')*var.get('a')), (((var.get('s')*var.get(u"this").get('cos_p14'))*var.get('h'))-((var.get('t').get('y')*var.get(u"this").get('sin_p14'))*var.get('a'))))))),var.get('t').put('x', var.get('n'))),var.get('t').put('y', var.get('r'))),var.get('t')))
                return (PyJsComma(PyJsComma(PyJsComma(var.put('r', var.get(u"this").get('lat0')),var.get('t').put('x', var.get('n'))),var.get('t').put('y', var.get('r'))),var.get('t')) if (var.get('Math').callprop('abs', var.get('s'))<=var.get('ot')) else PyJsComma(PyJsComma(var.put('r', var.get('Fs')(((var.get('h')*var.get(u"this").get('sin_p14'))+(((var.get('t').get('y')*var.get('a'))*var.get(u"this").get('cos_p14'))/var.get('s'))))),var.put('e', (var.get('Math').callprop('abs', var.get(u"this").get('lat0'))-var.get('ht')))),PyJs_LONG_334_()))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('x0'), '-'),var.get('t').put('y', var.get(u"this").get('y0'), '-')),var.put('s', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y')))))),var.put('i', var.get('Fs')((var.get('s')/var.get(u"this").get('a'))))),var.put('a', var.get('Math').callprop('sin', var.get('i')))),var.put('h', var.get('Math').callprop('cos', var.get('i')))),var.put('n', var.get(u"this").get('long0'))),PyJs_LONG_335_())
        return PyJs_LONG_336_()
    PyJs_anonymous_332_._set_name('anonymous')
    var.put('ei', Js({'init':PyJs_anonymous_328_,'forward':PyJs_anonymous_329_,'inverse':PyJs_anonymous_332_,'names':Js([Js('ortho')])}))
    var.put('ni', Js({'FRONT':Js(1.0),'RIGHT':Js(2.0),'BACK':Js(3.0),'LEFT':Js(4.0),'TOP':Js(5.0),'BOTTOM':Js(6.0)}))
    var.put('ri', Js({'AREA_0':Js(1.0),'AREA_1':Js(2.0),'AREA_2':Js(3.0),'AREA_3':Js(4.0)}))
    @Js
    def PyJs_anonymous_337_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        def PyJs_LONG_339_(var=var):
            def PyJs_LONG_338_(var=var):
                return (var.get(u"this").put('face', var.get('ni').get('FRONT')) if (var.get('Math').callprop('abs', var.get(u"this").get('long0'))<=var.get('ct')) else (var.get(u"this").put('face', (var.get('ni').get('RIGHT') if (var.get(u"this").get('long0')>Js(0.0)) else var.get('ni').get('LEFT'))) if (var.get('Math').callprop('abs', var.get(u"this").get('long0'))<=(var.get('ht')+var.get('ct'))) else var.get(u"this").put('face', var.get('ni').get('BACK'))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('x0', (var.get(u"this").get('x0') or Js(0.0))),var.get(u"this").put('y0', (var.get(u"this").get('y0') or Js(0.0)))),var.get(u"this").put('lat0', (var.get(u"this").get('lat0') or Js(0.0)))),var.get(u"this").put('long0', (var.get(u"this").get('long0') or Js(0.0)))),var.get(u"this").put('lat_ts', (var.get(u"this").get('lat_ts') or Js(0.0)))),var.get(u"this").put('title', (var.get(u"this").get('title') or Js('Quadrilateralized Spherical Cube')))),(var.get(u"this").put('face', var.get('ni').get('TOP')) if (var.get(u"this").get('lat0')>=(var.get('ht')-(var.get('ct')/Js(2.0)))) else (var.get(u"this").put('face', var.get('ni').get('BOTTOM')) if (var.get(u"this").get('lat0')<=(-(var.get('ht')-(var.get('ct')/Js(2.0))))) else PyJs_LONG_338_()))),(PyJsStrictNeq(Js(0.0),var.get(u"this").get('es')) and PyJsComma(var.get(u"this").put('one_minus_f', (Js(1.0)-((var.get(u"this").get('a')-var.get(u"this").get('b'))/var.get(u"this").get('a')))),var.get(u"this").put('one_minus_f_squared', (var.get(u"this").get('one_minus_f')*var.get(u"this").get('one_minus_f'))))))
        PyJs_LONG_339_()
    PyJs_anonymous_337_._set_name('anonymous')
    @Js
    def PyJs_anonymous_340_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 's', 'r', 'f', 'a'])
        var.put('r', Js({'x':Js(0.0),'y':Js(0.0)}))
        var.put('o', Js({'value':Js(0.0)}))
        def PyJs_LONG_341_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', var.get(u"this").get('long0'), '-'),var.put('s', (var.get('Math').callprop('atan', (var.get(u"this").get('one_minus_f_squared')*var.get('Math').callprop('tan', var.get('t').get('y')))) if PyJsStrictNeq(Js(0.0),var.get(u"this").get('es')) else var.get('t').get('y')))),var.put('i', var.get('t').get('x'))),PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('TOP')))
        if PyJs_LONG_341_():
            def PyJs_LONG_342_(var=var):
                return (PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_1')),var.put('a', ((var.get('i')-var.get('ft')) if (var.get('i')>Js(0.0)) else (var.get('i')+var.get('ft'))))) if ((var.get('i')>(var.get('ht')+var.get('ct'))) or (var.get('i')<=(-(var.get('ht')+var.get('ct'))))) else (PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_2')),var.put('a', (var.get('i')+var.get('ht')))) if ((var.get('i')>(-(var.get('ht')+var.get('ct')))) and (var.get('i')<=(-var.get('ct')))) else PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_3')),var.put('a', var.get('i')))))
            PyJsComma(var.put('h', (var.get('ht')-var.get('s'))),(PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_0')),var.put('a', (var.get('i')-var.get('ht')))) if ((var.get('i')>=var.get('ct')) and (var.get('i')<=(var.get('ht')+var.get('ct')))) else PyJs_LONG_342_()))
        else:
            if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('BOTTOM')):
                def PyJs_LONG_343_(var=var):
                    return (PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_1')),var.put('a', (-var.get('i')))) if ((var.get('i')<var.get('ct')) and (var.get('i')>=(-var.get('ct')))) else (PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_2')),var.put('a', ((-var.get('i'))-var.get('ht')))) if ((var.get('i')<(-var.get('ct'))) and (var.get('i')>=(-(var.get('ht')+var.get('ct'))))) else PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_3')),var.put('a', (((-var.get('i'))+var.get('ft')) if (var.get('i')>Js(0.0)) else ((-var.get('i'))-var.get('ft')))))))
                PyJsComma(var.put('h', (var.get('ht')+var.get('s'))),(PyJsComma(var.get('o').put('value', var.get('ri').get('AREA_0')),var.put('a', ((-var.get('i'))+var.get('ht')))) if ((var.get('i')>=var.get('ct')) and (var.get('i')<=(var.get('ht')+var.get('ct')))) else PyJs_LONG_343_()))
            else:
                pass
                def PyJs_LONG_347_(var=var):
                    def PyJs_LONG_344_(var=var):
                        return (var.put('i', var.get('Z')(var.get('i'), (+var.get('ht')))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('RIGHT')) else (var.put('i', var.get('Z')(var.get('i'), (+var.get('ft')))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('BACK')) else (PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('LEFT')) and var.put('i', var.get('Z')(var.get('i'), (-var.get('ht')))))))
                    def PyJs_LONG_346_(var=var):
                        def PyJs_LONG_345_(var=var):
                            return (var.put('a', var.get('V')(var.put('h', var.get('Math').callprop('acos', (-var.get('l')))), var.get('c'), (-var.get('M')), var.get('o'))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('BACK')) else (var.put('a', var.get('V')(var.put('h', var.get('Math').callprop('acos', (-var.get('M')))), var.get('c'), var.get('l'), var.get('o'))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('LEFT')) else PyJsComma(var.put('h', var.put('a', Js(0.0))),var.get('o').put('value', var.get('ri').get('AREA_0')))))
                        return (var.put('a', var.get('V')(var.put('h', var.get('Math').callprop('acos', var.get('l'))), var.get('c'), var.get('M'), var.get('o'))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('FRONT')) else (var.put('a', var.get('V')(var.put('h', var.get('Math').callprop('acos', var.get('M'))), var.get('c'), (-var.get('l')), var.get('o'))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('RIGHT')) else PyJs_LONG_345_()))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_344_(),var.put('u', var.get('Math').callprop('sin', var.get('s')))),var.put('f', var.get('Math').callprop('cos', var.get('s')))),var.put('m', var.get('Math').callprop('sin', var.get('i')))),var.put('l', (var.get('f')*var.get('Math').callprop('cos', var.get('i'))))),var.put('M', (var.get('f')*var.get('m')))),var.put('c', var.get('u'))),PyJs_LONG_346_())
                PyJs_LONG_347_()
        def PyJs_LONG_348_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('n', var.get('Math').callprop('atan', ((Js(12.0)/var.get('ft'))*((var.get('a')+var.get('Math').callprop('acos', (var.get('Math').callprop('sin', var.get('a'))*var.get('Math').callprop('cos', var.get('ct')))))-var.get('ht'))))),var.put('e', var.get('Math').callprop('sqrt', (((Js(1.0)-var.get('Math').callprop('cos', var.get('h')))/(var.get('Math').callprop('cos', var.get('n'))*var.get('Math').callprop('cos', var.get('n'))))/(Js(1.0)-var.get('Math').callprop('cos', var.get('Math').callprop('atan', (Js(1.0)/var.get('Math').callprop('cos', var.get('a')))))))))),(var.put('n', var.get('ht'), '+') if PyJsStrictEq(var.get('o').get('value'),var.get('ri').get('AREA_1')) else (var.put('n', var.get('ft'), '+') if PyJsStrictEq(var.get('o').get('value'),var.get('ri').get('AREA_2')) else (PyJsStrictEq(var.get('o').get('value'),var.get('ri').get('AREA_3')) and var.put('n', (Js(1.5)*var.get('ft')), '+'))))),var.get('r').put('x', (var.get('e')*var.get('Math').callprop('cos', var.get('n'))))),var.get('r').put('y', (var.get('e')*var.get('Math').callprop('sin', var.get('n'))))),var.get('r').put('x', ((var.get('r').get('x')*var.get(u"this").get('a'))+var.get(u"this").get('x0')))),var.get('r').put('y', ((var.get('r').get('y')*var.get(u"this").get('a'))+var.get(u"this").get('y0')))),var.get('t').put('x', var.get('r').get('x'))),var.get('t').put('y', var.get('r').get('y'))),var.get('t'))
        return PyJs_LONG_348_()
    PyJs_anonymous_340_._set_name('anonymous')
    @Js
    def PyJs_anonymous_349_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['M', 'c', 'p', 'd', 'u', 'l', 'm', 'n', 'o', 'h', 'e', 'i', 't', 'y', 's', 'r', 'f', 'a'])
        var.put('M', Js({'lam':Js(0.0),'phi':Js(0.0)}))
        var.put('c', Js({'value':Js(0.0)}))
        def PyJs_LONG_351_(var=var):
            def PyJs_LONG_350_(var=var):
                return (PyJsComma(var.get('c').put('value', var.get('ri').get('AREA_1')),var.put('s', var.get('ht'), '-')) if ((var.get('t').get('y')>=Js(0.0)) and (var.get('t').get('y')>=var.get('Math').callprop('abs', var.get('t').get('x')))) else (PyJsComma(var.get('c').put('value', var.get('ri').get('AREA_2')),var.put('s', ((var.get('s')+var.get('ft')) if (var.get('s')<Js(0.0)) else (var.get('s')-var.get('ft'))))) if ((var.get('t').get('x')<Js(0.0)) and ((-var.get('t').get('x'))>=var.get('Math').callprop('abs', var.get('t').get('y')))) else PyJsComma(var.get('c').put('value', var.get('ri').get('AREA_3')),var.put('s', var.get('ht'), '+'))))
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('t').put('x', ((var.get('t').get('x')-var.get(u"this").get('x0'))/var.get(u"this").get('a'))),var.get('t').put('y', ((var.get('t').get('y')-var.get(u"this").get('y0'))/var.get(u"this").get('a')))),var.put('i', var.get('Math').callprop('atan', var.get('Math').callprop('sqrt', ((var.get('t').get('x')*var.get('t').get('x'))+(var.get('t').get('y')*var.get('t').get('y'))))))),var.put('s', var.get('Math').callprop('atan2', var.get('t').get('y'), var.get('t').get('x')))),(var.get('c').put('value', var.get('ri').get('AREA_0')) if ((var.get('t').get('x')>=Js(0.0)) and (var.get('t').get('x')>=var.get('Math').callprop('abs', var.get('t').get('y')))) else PyJs_LONG_350_())),var.put('l', ((var.get('ft')/Js(12.0))*var.get('Math').callprop('tan', var.get('s'))))),var.put('e', (var.get('Math').callprop('sin', var.get('l'))/(var.get('Math').callprop('cos', var.get('l'))-(Js(1.0)/var.get('Math').callprop('sqrt', Js(2.0))))))),var.put('n', var.get('Math').callprop('atan', var.get('e')))),var.put('a', var.get('Math').callprop('cos', var.get('s')))),var.put('h', var.get('Math').callprop('tan', var.get('i')))),(var.put('r', (-Js(1.0))) if (var.put('r', (Js(1.0)-((((var.get('a')*var.get('a'))*var.get('h'))*var.get('h'))*(Js(1.0)-var.get('Math').callprop('cos', var.get('Math').callprop('atan', (Js(1.0)/var.get('Math').callprop('cos', var.get('n')))))))))<(-Js(1.0))) else ((var.get('r')>Js(1.0)) and var.put('r', Js(1.0))))),PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('TOP')))
        if PyJs_LONG_351_():
            def PyJs_LONG_352_(var=var):
                return (var.get('M').put('lam', (var.get('n')+var.get('ht'))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_0')) else (var.get('M').put('lam', ((var.get('n')+var.get('ft')) if (var.get('n')<Js(0.0)) else (var.get('n')-var.get('ft')))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_1')) else (var.get('M').put('lam', (var.get('n')-var.get('ht'))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_2')) else var.get('M').put('lam', var.get('n')))))
            PyJsComma(PyJsComma(var.put('o', var.get('Math').callprop('acos', var.get('r'))),var.get('M').put('phi', (var.get('ht')-var.get('o')))),PyJs_LONG_352_())
        else:
            if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('BOTTOM')):
                def PyJs_LONG_353_(var=var):
                    return (var.get('M').put('lam', ((-var.get('n'))+var.get('ht'))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_0')) else (var.get('M').put('lam', (-var.get('n'))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_1')) else (var.get('M').put('lam', ((-var.get('n'))-var.get('ht'))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_2')) else var.get('M').put('lam', (((-var.get('n'))-var.get('ft')) if (var.get('n')<Js(0.0)) else ((-var.get('n'))+var.get('ft')))))))
                PyJsComma(PyJsComma(var.put('o', var.get('Math').callprop('acos', var.get('r'))),var.get('M').put('phi', (var.get('o')-var.get('ht')))),PyJs_LONG_353_())
            else:
                pass
                def PyJs_LONG_357_(var=var):
                    def PyJs_LONG_354_(var=var):
                        return (PyJsComma(PyJsComma(var.put('l', var.get('f')),var.put('f', (-var.get('m')))),var.put('m', var.get('l'))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_1')) else (PyJsComma(var.put('f', (-var.get('f'))),var.put('m', (-var.get('m')))) if PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_2')) else (PyJsStrictEq(var.get('c').get('value'),var.get('ri').get('AREA_3')) and PyJsComma(PyJsComma(var.put('l', var.get('f')),var.put('f', var.get('m'))),var.put('m', (-var.get('l')))))))
                    def PyJs_LONG_355_(var=var):
                        return (PyJsComma(PyJsComma(var.put('l', var.get('u')),var.put('u', (-var.get('f')))),var.put('f', var.get('l'))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('RIGHT')) else (PyJsComma(var.put('u', (-var.get('u'))),var.put('f', (-var.get('f')))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('BACK')) else (PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('LEFT')) and PyJsComma(PyJsComma(var.put('l', var.get('u')),var.put('u', var.get('f'))),var.put('f', (-var.get('l')))))))
                    def PyJs_LONG_356_(var=var):
                        return (var.get('M').put('lam', var.get('Z')(var.get('M').get('lam'), (-var.get('ht')))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('RIGHT')) else (var.get('M').put('lam', var.get('Z')(var.get('M').get('lam'), (-var.get('ft')))) if PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('BACK')) else (PyJsStrictEq(var.get(u"this").get('face'),var.get('ni').get('LEFT')) and var.get('M').put('lam', var.get('Z')(var.get('M').get('lam'), (+var.get('ht')))))))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('l', (var.put('u', var.get('r'))*var.get('u'))),var.put('f', (Js(0.0) if (var.put('l', (var.put('m', (Js(0.0) if (var.get('l')>=Js(1.0)) else (var.get('Math').callprop('sqrt', (Js(1.0)-var.get('l')))*var.get('Math').callprop('sin', var.get('n')))))*var.get('m')), '+')>=Js(1.0)) else var.get('Math').callprop('sqrt', (Js(1.0)-var.get('l')))))),PyJs_LONG_354_()),PyJs_LONG_355_()),var.get('M').put('phi', (var.get('Math').callprop('acos', (-var.get('m')))-var.get('ht')))),var.get('M').put('lam', var.get('Math').callprop('atan2', var.get('f'), var.get('u')))),PyJs_LONG_356_())
                PyJs_LONG_357_()
        if PyJsStrictNeq(Js(0.0),var.get(u"this").get('es')):
            pass
            def PyJs_LONG_358_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('p', (Js(1.0) if (var.get('M').get('phi')<Js(0.0)) else Js(0.0))),var.put('d', var.get('Math').callprop('tan', var.get('M').get('phi')))),var.put('y', (var.get(u"this").get('b')/var.get('Math').callprop('sqrt', ((var.get('d')*var.get('d'))+var.get(u"this").get('one_minus_f_squared')))))),var.get('M').put('phi', var.get('Math').callprop('atan', (var.get('Math').callprop('sqrt', ((var.get(u"this").get('a')*var.get(u"this").get('a'))-(var.get('y')*var.get('y'))))/(var.get(u"this").get('one_minus_f')*var.get('y')))))),(var.get('p') and var.get('M').put('phi', (-var.get('M').get('phi')))))
            PyJs_LONG_358_()
        return PyJsComma(PyJsComma(PyJsComma(var.get('M').put('lam', var.get(u"this").get('long0'), '+'),var.get('t').put('x', var.get('M').get('lam'))),var.get('t').put('y', var.get('M').get('phi'))),var.get('t'))
    PyJs_anonymous_349_._set_name('anonymous')
    var.put('oi', Js({'init':PyJs_anonymous_337_,'forward':PyJs_anonymous_340_,'inverse':PyJs_anonymous_349_,'names':Js([Js('Quadrilateralized Spherical Cube'), Js('Quadrilateralized_Spherical_Cube'), Js('qsc')])}))
    var.put('li', Js([Js([Js(1.0), Js(2.2199e-17), (-Js(7.15515e-05)), Js(3.1103e-06)]), Js([Js(0.9986), (-Js(0.000482243)), (-Js(2.4897e-05)), (-Js(1.3309e-06))]), Js([Js(0.9954), (-Js(0.00083103)), (-Js(4.48605e-05)), (-Js(9.86701e-07))]), Js([Js(0.99), (-Js(0.00135364)), (-Js(5.9661e-05)), Js(3.6777e-06)]), Js([Js(0.9822), (-Js(0.00167442)), (-Js(4.49547e-06)), (-Js(5.72411e-06))]), Js([Js(0.973), (-Js(0.00214868)), (-Js(9.03571e-05)), Js(1.8736e-08)]), Js([Js(0.96), (-Js(0.00305085)), (-Js(9.00761e-05)), Js(1.64917e-06)]), Js([Js(0.9427), (-Js(0.00382792)), (-Js(6.53386e-05)), (-Js(2.6154e-06))]), Js([Js(0.9216), (-Js(0.00467746)), (-Js(0.00010457)), Js(4.81243e-06)]), Js([Js(0.8962), (-Js(0.00536223)), (-Js(3.23831e-05)), (-Js(5.43432e-06))]), Js([Js(0.8679), (-Js(0.00609363)), (-Js(0.000113898)), Js(3.32484e-06)]), Js([Js(0.835), (-Js(0.00698325)), (-Js(6.40253e-05)), Js(9.34959e-07)]), Js([Js(0.7986), (-Js(0.00755338)), (-Js(5.00009e-05)), Js(9.35324e-07)]), Js([Js(0.7597), (-Js(0.00798324)), (-Js(3.5971e-05)), (-Js(2.27626e-06))]), Js([Js(0.7186), (-Js(0.00851367)), (-Js(7.01149e-05)), (-Js(8.6303e-06))]), Js([Js(0.6732), (-Js(0.00986209)), (-Js(0.000199569)), Js(1.91974e-05)]), Js([Js(0.6213), (-Js(0.010418)), Js(8.83923e-05), Js(6.24051e-06)]), Js([Js(0.5722), (-Js(0.00906601)), Js(0.000182), Js(6.24051e-06)]), Js([Js(0.5322), (-Js(0.00677797)), Js(0.000275608), Js(6.24051e-06)])]))
    var.put('Mi', Js([Js([(-Js(5.20417e-18)), Js(0.0124), Js(1.21431e-18), (-Js(8.45284e-11))]), Js([Js(0.062), Js(0.0124), (-Js(1.26793e-09)), Js(4.22642e-10)]), Js([Js(0.124), Js(0.0124), Js(5.07171e-09), (-Js(1.60604e-09))]), Js([Js(0.186), Js(0.0123999), (-Js(1.90189e-08)), Js(6.00152e-09)]), Js([Js(0.248), Js(0.0124002), Js(7.10039e-08), (-Js(2.24e-08))]), Js([Js(0.31), Js(0.0123992), (-Js(2.64997e-07)), Js(8.35986e-08)]), Js([Js(0.372), Js(0.0124029), Js(9.88983e-07), (-Js(3.11994e-07))]), Js([Js(0.434), Js(0.0123893), (-Js(3.69093e-06)), (-Js(4.35621e-07))]), Js([Js(0.4958), Js(0.0123198), (-Js(1.02252e-05)), (-Js(3.45523e-07))]), Js([Js(0.5571), Js(0.0121916), (-Js(1.54081e-05)), (-Js(5.82288e-07))]), Js([Js(0.6176), Js(0.0119938), (-Js(2.41424e-05)), (-Js(5.25327e-07))]), Js([Js(0.6769), Js(0.011713), (-Js(3.20223e-05)), (-Js(5.16405e-07))]), Js([Js(0.7346), Js(0.0113541), (-Js(3.97684e-05)), (-Js(6.09052e-07))]), Js([Js(0.7903), Js(0.0109107), (-Js(4.89042e-05)), (-Js(1.04739e-06))]), Js([Js(0.8435), Js(0.0103431), (-Js(6.4615e-05)), (-Js(1.40374e-09))]), Js([Js(0.8936), Js(0.00969686), (-Js(6.4636e-05)), (-Js(8.547e-06))]), Js([Js(0.9394), Js(0.00840947), (-Js(0.000192841)), (-Js(4.2106e-06))]), Js([Js(0.9761), Js(0.00616527), (-Js(0.000256)), (-Js(4.2106e-06))]), Js([Js(1.0), Js(0.00328947), (-Js(0.000319159)), (-Js(4.2106e-06))])]))
    var.put('ci', Js(0.8487))
    var.put('ui', Js(1.3523))
    var.put('fi', (var.get('Mt')/Js(5.0)))
    var.put('mi', (Js(1.0)/var.get('fi')))
    var.put('pi', Js(18.0))
    @Js
    def PyJs_anonymous_359_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        return (var.get('t').get('0')+(var.get('s')*(var.get('t').get('1')+(var.get('s')*(var.get('t').get('2')+(var.get('s')*var.get('t').get('3')))))))
    PyJs_anonymous_359_._set_name('anonymous')
    var.put('di', PyJs_anonymous_359_)
    @Js
    def PyJs_anonymous_360_(t, s, this, arguments, var=var):
        var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 's'])
        return (var.get('t').get('1')+(var.get('s')*((Js(2.0)*var.get('t').get('2'))+((Js(3.0)*var.get('s'))*var.get('t').get('3')))))
    PyJs_anonymous_360_._set_name('anonymous')
    var.put('yi', PyJs_anonymous_360_)
    @Js
    def PyJs_anonymous_361_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('x0', (var.get(u"this").get('x0') or Js(0.0))),var.get(u"this").put('y0', (var.get(u"this").get('y0') or Js(0.0)))),var.get(u"this").put('long0', (var.get(u"this").get('long0') or Js(0.0)))),var.get(u"this").put('es', Js(0.0))),var.get(u"this").put('title', (var.get(u"this").get('title') or Js('Robinson'))))
    PyJs_anonymous_361_._set_name('anonymous')
    @Js
    def PyJs_anonymous_362_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        var.put('s', var.get('qt')((var.get('t').get('x')-var.get(u"this").get('long0'))))
        var.put('i', var.get('Math').callprop('abs', var.get('t').get('y')))
        var.put('a', var.get('Math').callprop('floor', (var.get('i')*var.get('fi'))))
        PyJsComma((var.put('a', Js(0.0)) if (var.get('a')<Js(0.0)) else ((var.get('a')>=var.get('pi')) and var.put('a', (var.get('pi')-Js(1.0))))),var.put('i', (var.get('Mt')*(var.get('i')-(var.get('mi')*var.get('a'))))))
        var.put('h', Js({'x':(var.get('di')(var.get('li').get(var.get('a')), var.get('i'))*var.get('s')),'y':var.get('di')(var.get('Mi').get(var.get('a')), var.get('i'))}))
        return PyJsComma(PyJsComma(PyJsComma(((var.get('t').get('y')<Js(0.0)) and var.get('h').put('y', (-var.get('h').get('y')))),var.get('h').put('x', (((var.get('h').get('x')*var.get(u"this").get('a'))*var.get('ci'))+var.get(u"this").get('x0')))),var.get('h').put('y', (((var.get('h').get('y')*var.get(u"this").get('a'))*var.get('ui'))+var.get(u"this").get('y0')))),var.get('h'))
    PyJs_anonymous_362_._set_name('anonymous')
    @Js
    def PyJs_anonymous_363_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['h', 'i', 's', 't', 'a'])
        var.put('s', Js({'x':((var.get('t').get('x')-var.get(u"this").get('x0'))/(var.get(u"this").get('a')*var.get('ci'))),'y':(var.get('Math').callprop('abs', (var.get('t').get('y')-var.get(u"this").get('y0')))/(var.get(u"this").get('a')*var.get('ui')))}))
        if (var.get('s').get('y')>=Js(1.0)):
            PyJsComma(var.get('s').put('x', var.get('li').get(var.get('pi')).get('0'), '/'),var.get('s').put('y', ((-var.get('ht')) if (var.get('t').get('y')<Js(0.0)) else var.get('ht'))))
        else:
            var.put('i', var.get('Math').callprop('floor', (var.get('s').get('y')*var.get('pi'))))
            #for JS loop
            (var.put('i', Js(0.0)) if (var.get('i')<Js(0.0)) else ((var.get('i')>=var.get('pi')) and var.put('i', (var.get('pi')-Js(1.0)))))
            while 1:
                if (var.get('Mi').get(var.get('i')).get('0')>var.get('s').get('y')):
                    var.put('i',Js(var.get('i').to_number())-Js(1))
                else:
                    if (var.get('Mi').get((var.get('i')+Js(1.0))).get('0')<=var.get('s').get('y')).neg():
                        break
                    var.put('i',Js(var.get('i').to_number())+Js(1))
            
            var.put('a', var.get('Mi').get(var.get('i')))
            var.put('h', ((Js(5.0)*(var.get('s').get('y')-var.get('a').get('0')))/(var.get('Mi').get((var.get('i')+Js(1.0))).get('0')-var.get('a').get('0'))))
            @Js
            def PyJs_anonymous_364_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['t'])
                return ((var.get('di')(var.get('a'), var.get('t'))-var.get('s').get('y'))/var.get('yi')(var.get('a'), var.get('t')))
            PyJs_anonymous_364_._set_name('anonymous')
            PyJsComma(PyJsComma(PyJsComma(var.put('h', var.get('Y')(PyJs_anonymous_364_, var.get('h'), var.get('ot'), Js(100.0))),var.get('s').put('x', var.get('di')(var.get('li').get(var.get('i')), var.get('h')), '/')),var.get('s').put('y', (((Js(5.0)*var.get('i'))+var.get('h'))*var.get('lt')))),((var.get('t').get('y')<Js(0.0)) and var.get('s').put('y', (-var.get('s').get('y')))))
        return PyJsComma(var.get('s').put('x', var.get('qt')((var.get('s').get('x')+var.get(u"this").get('long0')))),var.get('s'))
    PyJs_anonymous_363_._set_name('anonymous')
    var.put('_i', Js({'init':PyJs_anonymous_361_,'forward':PyJs_anonymous_362_,'inverse':PyJs_anonymous_363_,'names':Js([Js('Robinson'), Js('robin')])}))
    @Js
    def PyJs_anonymous_365_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put('name', Js('geocent'))
    PyJs_anonymous_365_._set_name('anonymous')
    @Js
    def PyJs_anonymous_366_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('b')(var.get('t'), var.get(u"this").get('es'), var.get(u"this").get('a'))
    PyJs_anonymous_366_._set_name('anonymous')
    @Js
    def PyJs_anonymous_367_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get('w')(var.get('t'), var.get(u"this").get('es'), var.get(u"this").get('a'), var.get(u"this").get('b'))
    PyJs_anonymous_367_._set_name('anonymous')
    var.put('xi', Js({'init':PyJs_anonymous_365_,'forward':PyJs_anonymous_366_,'inverse':PyJs_anonymous_367_,'names':Js([Js('Geocentric'), Js('geocentric'), Js('geocent'), Js('Geocent')])}))
    def PyJs_LONG_370_(var=var):
        @Js
        def PyJs_anonymous_368_(proj4, this, arguments, var=var):
            var = Scope({'proj4':proj4, 'this':this, 'arguments':arguments}, var)
            var.registers(['proj4'])
            def PyJs_LONG_369_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('proj4').get('Proj').get('projections').callprop('add', var.get('es')),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ms'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ds'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('vs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('gs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('bs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ws'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('As'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Cs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Rs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Us'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Qs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Ws'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Xs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Ks'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Vs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Zs'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('Ys'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ti'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('si'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ii'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ai'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('hi'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('ei'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('oi'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('_i'))),var.get('proj4').get('Proj').get('projections').callprop('add', var.get('xi')))
            PyJs_LONG_369_()
        PyJs_anonymous_368_._set_name('anonymous')
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('I').put('defaultDatum', Js('WGS84')),var.get('I').put('Proj', var.get('Projection'))),var.get('I').put('WGS84', var.get('I').get('Proj').create(Js('WGS84')))),var.get('I').put('Point', var.get('Point'))),var.get('I').put('toPoint', var.get('Ft'))),var.get('I').put('defs', var.get('o'))),var.get('I').put('transform', var.get('S'))),var.get('I').put('mgrs', var.get('ts'))),var.get('I').put('version', Js('2.6.2'))),PyJs_anonymous_368_(var.get('I'))),var.get('I'))
    return PyJs_LONG_370_()
PyJs_anonymous_0_._set_name('anonymous')
@Js
def PyJs_anonymous_371_(t, s, this, arguments, var=var):
    var = Scope({'t':t, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 's'])
    (var.get('module').put('exports', var.get('s')()) if ((Js('object')==var.get('exports',throw=False).typeof()) and (Js('undefined')!=var.get('module',throw=False).typeof())) else (var.get('define')(var.get('s')) if ((Js('function')==var.get('define',throw=False).typeof()) and var.get('define').get('amd')) else var.get('t').put('proj4', var.get('s')())))
PyJs_anonymous_371_._set_name('anonymous')
PyJs_anonymous_371_(var.get(u"this"), PyJs_anonymous_0_).neg()
pass


# Add lib to the module scope
proj4 = var.to_python()