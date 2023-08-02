import numpy as np
from common_func import isnum
d2r = 1 / 180 * np.pi

def esa(self):
    v_temp=self.input_esa_v.text()
    ttc_min_temp=self.input_esa_ttc_min.text()
    ttc_max_temp=self.input_esa_ttc_max.text()
    if isnum(v_temp) and isnum(ttc_min_temp) and isnum(ttc_max_temp):
        v=float(v_temp)/3.6
        ttc_min=float(ttc_min_temp)
        ttc_max=float(ttc_max_temp)
        yaw_slew=float(self.label_esa_yawslew.text())
        yaw_max=float(self.label_esa_yaw_max.text())
        timestep=0.01
        timeline=np.arange(0, ttc_max+timestep, timestep)
        yaw=[0]
        yaw_rate=[0]
        lat_offset=[0]
        lat_accel=[0]
        for i in range(1,len(timeline)):
            yaw.append(yaw[-1]+yaw_rate[-1]*timestep)
            lat_offset.append(v*np.sin(yaw[-1]*d2r)*timestep+lat_offset[-1])
            lat_accel.append(v*yaw_rate[-1]*d2r)
            if yaw_rate[-1]<=yaw_max:
                yaw_rate.append(yaw_rate[-1]+yaw_slew*timestep)
            else:
                yaw_rate.append(yaw_rate[-1])
            if timeline[i]==ttc_min:
                self.output_esa_lat_offset_1.setText(str(round(lat_offset[-1],3)))
                self.output_esa_lat_a_1.setText(str(round(lat_accel[-1],3)))
            if timeline[i]==ttc_max:
                self.output_esa_lat_offset_2.setText(str(round(lat_offset[-1],3)))
                self.output_esa_lat_a_2.setText(str(round(lat_accel[-1],3)))
        self.esa_timeline=timeline
        self.esa_yaw=yaw
        self.esa_yaw_rate=yaw_rate
        self.esa_lat_offset=lat_offset
        self.esa_lat_accel=lat_accel