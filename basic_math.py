import common_func as CF
import numpy as np

r2d = 1 / np.pi * 180
d2r = 1 / 180 * np.pi
c_speed = 299792458

def arc_calc_1(self):
    input_angle_temp=self.input_arc_angle1.text()
    input_radius_temp=self.input_arc_radius1.text()
    input_unit=self.comboBox_arc_angle1.currentText()
    if (CF.isnum(input_angle_temp) and CF.isnum(input_radius_temp)):
        input_angle=float(input_angle_temp)
        input_radius=float(input_radius_temp)
        if(input_unit=="Degree"):
            output_arcLen=input_angle*d2r*input_radius
        else:
            output_arcLen=input_angle*input_radius
        self.output_arc_len1.setText(str(output_arcLen))

def arc_calc_2(self):
    input_arcLen_temp=self.input_arc_len2.text()
    input_radius_temp=self.input_arc_radius2.text()
    output_unit=self.comboBox_arc_angle2.currentText()
    if (CF.isnum(input_arcLen_temp) and CF.isnum(input_radius_temp)):
        input_arcLen=float(input_arcLen_temp)
        input_radius=float(input_radius_temp)
        if(output_unit=="Degree"):
            output_angle=r2d*input_arcLen/input_radius
        else:
            output_angle=input_arcLen/input_radius
        self.output_arc_angle2.setText(str(output_angle))


def tri_calc_1(self):
    input_angle_temp=self.input_tri_angle1.text()
    input_side_temp=self.input_tri_side1.text()
    input_unit=self.comboBox_tri_angle_unit1.currentText()
    input_side=self.comboBox_tri_baseorheight.currentText()
    if (CF.isnum(input_angle_temp) and CF.isnum(input_side_temp)):
        input_angle=float(input_angle_temp)
        input_side=float(input_side_temp)
        if(input_side=="Base"):
            if input_unit=="Degree":
                output_height=input_side*np.tan(input_angle*d2r)
            else:
                output_height=input_side*np.tan(input_angle)
        else:
            if input_unit=="Degree":
                output_height=input_side/np.tan(input_angle*d2r)
            else:
                output_height=input_side/np.tan(input_angle)
        self.output_tri_height1.setText(str(output_height))

def tri_calc_2(self):
    input_base_temp=self.input_tri_base2.text()
    input_height_temp=self.input_tri_height2.text()
    input_unit=self.comboBox_tri_angle_unit2.currentText()
    if (CF.isnum(input_base_temp) and CF.isnum(input_height_temp)):
        input_base=float(input_base_temp)
        input_height=float(input_height_temp)
        if input_unit=="Degree":
            output_angle=r2d*np.arctan(input_height/input_base)
        else:
            output_angle=np.arctan(input_height/input_base)
        self.output_tri_angle2.setText(str(output_angle))

def dist_curve(self):
    input_vx_temp=self.input_curve_vx.text()
    input_yaw_temp=self.input_curve_yaw.text()
    input_vx_unit=self.comboBox_curve_vx_unit.currentText()
    input_yaw_unit=self.comboBox_curve_yaw_unit.currentText()
    input_long_temp=self.input_curve_long.text()
    if (CF.isnum(input_vx_temp) and CF.isnum(input_yaw_temp)):
        input_vx=float(input_vx_temp)
        input_yaw=float(input_yaw_temp)
        if (input_vx_unit=="kph"):
            input_vx=input_vx/3.6
        if (input_yaw_unit=="deg/s"):
            input_yaw=input_yaw*d2r
        if (input_yaw>np.pi):
            input_yaw=np.pi
        output_curva=input_yaw/input_vx
        output_radius=1/output_curva
        self.output_curve_curva.setText(str(round(output_curva,3)))
        self.output_curve_radius.setText(str(round(output_radius,3)))
        if (CF.isnum(input_long_temp)):
            input_long=float(input_long_temp)
            theta=input_long/output_radius
            if theta>1:
                theta=1
            if theta<-1:
                theta=-1
            output_lat=output_radius*(1-np.cos(np.arcsin(theta)))
            self.output_curve_lat.setText(str(round(output_lat,3)))


def bit2dec(self):
    input=int(self.input_bitdec_bit.text())
    output=2**input-1
    self.output_bitdec_dec.setText(str(output))





