from flask import Flask,Response,request
import json
import os
import ctypes
import time
import numpy as np
app = Flask(__name__)
NIRezDll = ctypes.CDLL(os.path.abspath('NIRez20_SDK.dll'))


@app.route('/NIRez20_Connect')
def NIRez20_Connect():
    NIRezDll._NIRez20_Connect()
    return Response(f"{{'message':'done'}}", status=200, mimetype='application/json')

@app.route('/NIRez20_Link_Status')
def NIRez20_Link_Status():
    Link_status = NIRezDll._NIRez20_Link_Status()
    return Response(f"{{'message':'{Link_status}'}}", status=200, mimetype='application/json')

@app.route('/NIRez20_Config')
def NIRez20_Config():
    if "i_lamp_switch" not in request.values:
        return Response(f"{{'message':'i_lamp_switch not Found'}}", status=400, mimetype='application/json')
    if "i_start_wavelength" not in request.values:
        return Response(f"{{'message':'i_start_wavelength not Found'}}", status=400, mimetype='application/json')
    if "i_end_wavelength" not in request.values:
        return Response(f"{{'message':'i_end_wavelength not Found'}}", status=400, mimetype='application/json')
    if "d_width" not in request.values:
        return Response(f"{{'message':'d_width not Found'}}", status=400, mimetype='application/json')
    if "i_gain" not in request.values:
        return Response(f"{{'message':'i_gain not Found'}}", status=400, mimetype='application/json')
    if "i_points" not in request.values:
        return Response(f"{{'message':'i_points not Found'}}", status=400, mimetype='application/json')
    if "i_average" not in request.values:
        return Response(f"{{'message':'i_average not Found'}}", status=400, mimetype='application/json')
    if "i_exposure" not in request.values:
        return Response(f"{{'message':'i_exposure not Found'}}", status=400, mimetype='application/json')
    if "i_scan_mode" not in request.values:
        return Response(f"{{'message':'i_scan_mode not Found'}}", status=400, mimetype='application/json')
    try:
        i_lamp_switch = ctypes.c_int(int(request.values["i_lamp_switch"]))
        i_start_wavelength = ctypes.c_int(int(request.values["i_start_wavelength"]))
        i_end_wavelength = ctypes.c_int(int(request.values["i_end_wavelength"]))
        d_width = ctypes.c_double(float(request.values["d_width"]))
        i_gain = ctypes.c_int(int(request.values["i_gain"]))
        i_points = ctypes.c_int(int(request.values["i_points"]))
        i_average = ctypes.c_int(int(request.values["i_average"]))
        i_exposure = ctypes.c_int(int(request.values["i_exposure"]))
        i_scan_mode = ctypes.c_int(int(request.values["i_scan_mode"]))
        confg_status = NIRezDll._NIRez20_Config(i_lamp_switch,
                                        i_start_wavelength,
                                        i_end_wavelength,
                                        d_width,
                                        i_gain,
                                        i_points,
                                        i_average,
                                        i_exposure,
                                        i_scan_mode)
    except Exception as e:
        return Response(f"{{'message':'{e}'}}", status=400, mimetype='application/json')

    return Response(f"{{'message':'{confg_status}'}}", status=200, mimetype='application/json')

@app.route('/NIRez20_Scan')
def NIRez20_Scan():
    
    if "i_total" not in request.values:
        return Response(f"{{'message':'i_total not Found'}}", status=400, mimetype='application/json')
    if "i_gain" not in request.values:
        return Response(f"{{'message':'i_gain not Found'}}", status=400, mimetype='application/json')
    try:
        i_gain = ctypes.c_int(int(request.values["i_gain"]))
        i_total = ctypes.c_int(int(request.values["i_total"]))

        d_wavelength = np.zeros(i_total.value, dtype='float64')
        i_intensity = np.zeros(i_total.value, dtype='int')
        scan_status = NIRezDll._NIRez20_Scan(ctypes.byref(i_total),
                                     ctypes.byref(i_gain),
                                     d_wavelength.ctypes.data_as(ctypes.c_void_p),
                                     i_intensity.ctypes.data_as(ctypes.c_void_p))
    except Exception as e:
        return Response(f"{{'message':'{e}'}}", status=400, mimetype='application/json')
    data = np.vstack((d_wavelength, i_intensity)).tolist()
    return Response(f"{{'message':'{scan_status}','data':'{json.dumps(data)}'}}", status=200, mimetype='application/json')

@app.route('/NIRez20_Set_Key_Path')
def NIRez20_Set_Key_Path():
    return Response(f"{{'message':'not implement'}}", status=200, mimetype='application/json')

@app.route('/NIRez20_Get_Sn')
def NIRez20_Get_Sn():
    return Response(f"{{'message':'not implement'}}", status=200, mimetype='application/json')


def main():
    Init_status = NIRezDll._NIRez20_Initial()
    if Init_status != 1:
        print("Failed to initialize dll , abort")
        return
    app.debug = False
    app.run('0.0.0.0',port = 5500)
    return


if __name__ == "__main__":
    main()