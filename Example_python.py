import os
import ctypes
import time

NIRezDll = ctypes.CDLL(os.path.abspath('NIRez20_SDK.dll'))
Init_status = NIRezDll._NIRez20_Initial()
print(Init_status)
time.sleep(2)

NIRezDll._NIRez20_Connect()
time.sleep(1)

Link_status = NIRezDll._NIRez20_Link_Status()
print(Link_status)
time.sleep(1)

i_lamp_switch = ctypes.c_int(0) # Lamp off
i_start_wavelength = ctypes.c_int(900)
i_end_wavelength = ctypes.c_int(1700)
d_width = ctypes.c_double(7.02) # 2.34, 3.51, 4.68, 5.85, 7.02, 8.19, 9.36, 10.53
i_gain = ctypes.c_int(1)
i_points = ctypes.c_int(400)
i_average = ctypes.c_int(4)
i_exposure = ctypes.c_int(2) # 2.54ms
i_scan_mode = ctypes.c_int(0)
confg_status = NIRezDll._NIRez20_Config(i_lamp_switch,
                                        i_start_wavelength,
                                        i_end_wavelength,
                                        d_width,
                                        i_gain,
                                        i_points,
                                        i_average,
                                        i_exposure,
                                        i_scan_mode)

print(confg_status)
time.sleep(1)

import numpy as np
i_total = ctypes.c_int(400)
d_wavelength = np.zeros(i_total.value, dtype='float64')
i_intensity = np.zeros(i_total.value, dtype='int')

# The first scan to initialize data array
tstart = time.time()
scan_status = NIRezDll._NIRez20_Scan(ctypes.byref(i_total),
                                     ctypes.byref(i_gain),
                                     d_wavelength.ctypes.data_as(ctypes.c_void_p),
                                     i_intensity.ctypes.data_as(ctypes.c_void_p))
data = np.vstack((d_wavelength, i_intensity))
print('Measurement 1 is OK...')

for i in range(5000-1):
    time.sleep(5)
    scan_status = NIRezDll._NIRez20_Scan(ctypes.byref(i_total),
                                         ctypes.byref(i_gain),
                                         d_wavelength.ctypes.data_as(ctypes.c_void_p),
                                         i_intensity.ctypes.data_as(ctypes.c_void_p))
    data = np.vstack((data, i_intensity))
    print('Measurement ' + str(i+2) + ' is OK...Scan_status is ' + str(scan_status))

tend = time.time()
print('Total time is ' + str(tend-tstart))
print('Time interval is ' + str((tend-tstart)/5000))

time_string = time.strftime('_%Y%m%d_%H%M%S')
np.savetxt('C:/NIRez_Data/' + 'NIRez' + time_string + '.csv', data, delimiter=",")


