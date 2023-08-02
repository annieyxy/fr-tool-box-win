from common_func import isnum
import numpy as np
g=9.80665

def lin_acc_1(self):
    v0_temp=self.input_lin_v0_1.text()
    v1_temp=self.input_lin_v1_1.text()
    dt_temp=self.input_lin_dt_1.text()
    if (isnum(v0_temp) and isnum(v1_temp) and isnum(dt_temp)):
        v0=float(v0_temp)
        v1=float(v1_temp)
        dt=float(dt_temp)
        if (self.comboBox_lin_v0.currentText()=="kph"):
            v0=v0/3.6
        if (self.comboBox_lin_v1.currentText()=="kph"):
            v1=v1/3.6
        a=(v1-v0)/dt
        s=(v0+v1)*dt/2
        self.output_lin_a_1.setText(str(round(a,3)))
        self.output_lin_s_1.setText(str(round(s,3)))

def lin_acc_2(self):
    v0_temp=self.input_lin_v0_2.text()
    v1_temp=self.input_lin_v1_2.text()
    a_temp=self.input_lin_a_2.text()
    if (isnum(v0_temp) and isnum(v1_temp) and isnum(a_temp)):
        v0=float(v0_temp)
        v1=float(v1_temp)
        a=float(a_temp)
        if (self.comboBox_lin_v0.currentText()=="kph"):
            v0=v0/3.6
        if (self.comboBox_lin_v1.currentText()=="kph"):
            v1=v1/3.6
        dt=(v1-v0)/a
        s=(v0+v1)*dt/2
        self.output_lin_dt_2.setText(str(round(dt,3)))
        self.output_lin_s_2.setText(str(round(s,3)))

def lin_acc_3(self):
    v0_temp=self.input_lin_v0_3.text()
    a_temp=self.input_lin_a_3.text()
    s_temp=self.input_lin_s_3.text()
    if (isnum(v0_temp) and isnum(s_temp) and isnum(a_temp)):
        v0=float(v0_temp)
        a=float(a_temp)
        s=float(s_temp)
        if (self.comboBox_lin_v0.currentText()=="kph"):
            v0=v0/3.6
        v1=np.sqrt(v0**2+2*a*s)
        dt=(v1-v0)/a
        if(self.comboBox_lin_v1.currentText()=="kph"):
            v1=v1*3.6
        self.output_lin_v1_3.setText(str(round(v1,3)))
        self.output_lin_dt_3.setText(str(round(dt,3)))

def lin_acc_4(self):
    v0_temp=self.input_lin_v0_4.text()
    dt_temp=self.input_lin_dt_4.text()
    a_temp=self.input_lin_a_4.text()
    if (isnum(v0_temp) and isnum(dt_temp) and isnum(a_temp)):
        v0=float(v0_temp)
        a=float(a_temp)
        dt=float(dt_temp)
        if (self.comboBox_lin_v0.currentText()=="kph"):
            v0=v0/3.6
        v1=v0+a*dt
        s=v0*dt+0.5*a*(dt**2)
        if(self.comboBox_lin_v1.currentText()=="kph"):
            v1=v1*3.6
        self.output_lin_v1_4.setText(str(round(v1,3)))
        self.output_lin_s_4.setText(str(round(s,3)))

def cent_acc_1(self):
    r_temp=self.input_cent_r_1.text()
    v_temp=self.input_cent_v_1.text()
    v_unit=self.comboBox_cent_v.currentText()
    a_unit=self.comboBox_cent_a.currentText()
    if (isnum(r_temp) and isnum(v_temp)):
        v=float(v_temp)
        r=float(r_temp)
        if v_unit=="kph":
            v=v/3.6
        a=v**2/r
        if a_unit=="G":
            a=a/g
        self.output_cent_a_1.setText(str(round(a,3)))

def cent_acc_2(self):
    r_temp=self.input_cent_r_2.text()
    a_temp=self.input_cent_a_2.text()
    v_unit=self.comboBox_cent_v.currentText()
    a_unit=self.comboBox_cent_a.currentText()
    if (isnum(r_temp) and isnum(a_temp)):
        r=float(r_temp)
        a=float(a_temp)
        if a_unit=="G":
            a=a*g
        v=np.sqrt(a*r)
        if v_unit=="kph":
            v=v*3.6
        self.output_cent_v_2.setText(str(round(v,3)))

def cent_acc_3(self):
    v_temp=self.input_cent_v_3.text()
    a_temp=self.input_cent_a_3.text()
    v_unit=self.comboBox_cent_v.currentText()
    a_unit=self.comboBox_cent_a.currentText()
    if (isnum(v_temp) and isnum(a_temp)):
        v=float(v_temp)
        a=float(a_temp)
        if v_unit=="kph":
            v=v/3.6
        if a_unit=="G":
            a=a/g
        r=v**2/a
        self.output_cent_r_3.setText(str(round(r,3)))

def lane_man(self):
    v_rear_temp=self.input_lane_vrear.text()
    v_acsf_temp=self.input_lane_vacsf.text()
    v_rear_unit=self.comboBox_lane_vrear.currentText()
    v_acsf_unit=self.comboBox_lane_vacsf.currentText()
    v_smin_unit=self.comboBox_lane_vsmin.currentText()
    a=3
    tB=0.4
    tG=1
    if (isnum(v_rear_temp) and isnum(v_acsf_temp)):
        v_rear=float(v_rear_temp)
        v_acsf=float(v_acsf_temp)
        if (v_rear_unit=="kph"):
            v_rear=v_rear/3.6
        if (v_acsf_unit=="kph"):
            v_acsf=v_acsf/3.6
        if (v_rear>130/3.6):
            v_rear=130/3.6
        s_crit=(v_rear-v_acsf)*tB+((v_rear-v_acsf)**2)/(2*a)+v_acsf*tG
        v_smin=a*(tB-tG)+v_rear-np.sqrt(a**2*((tB-tG)**2)-2*a*(v_rear*tG-s_crit))
        if(v_smin_unit=="kph"):
            v_smin=v_smin/3.6
        self.output_lane_scrit.setText(str(round(s_crit,3)))
        self.output_lane_vsmin.setText(str(round(v_smin,3)))
            

def ttc(self):
    v1_temp=self.input_ttc_v1.text()
    a1_temp=self.input_ttc_a1.text()
    v2_temp=self.input_ttc_v2.text()
    a2_temp=self.input_ttc_a2.text()
    s_temp=self.input_ttc_s.text()
    v1_unit=self.comboBox_ttc_v1.currentText()
    v2_unit=self.comboBox_ttc_v2.currentText()
    if (isnum(v1_temp) and isnum(a1_temp) and isnum(v2_temp) and isnum(a2_temp) and isnum(s_temp)):
        v1=float(v1_temp)
        a1=float(a1_temp)
        v2=float(v2_temp)
        a2=float(a2_temp)
        s=float(s_temp)
        if v1_unit=="kph":
            v1=v1/3.6
        if v2_unit=="kph":
            v2=v2/3.6
        timer=0
        s1=0
        s2=s
        timestep=0.001
        hostStopFlag=False
        collisionFlag=False
        collisionTimer=0
        self.ttc_timerList=[]
        self.ttc_speedList_host=[]
        self.ttc_distList_host=[]
        self.ttc_speedList_target=[]
        self.ttc_distList_target=[]
        while (timer<=5):
            timer+=timestep
            v1+=a1*timestep
            s1+=v1*timestep+0.5*a1*timestep**2
            v2+=a2*timestep
            s2+=v2*timestep+0.5*a2*timestep**2
            self.ttc_timerList.append(timer)
            self.ttc_speedList_host.append(v1)
            self.ttc_distList_host.append(s1)
            self.ttc_speedList_target.append(v2)
            self.ttc_distList_target.append(s2)
            if (v1<=0):
                hostStopFlag=True
                v1=0
                a1=0
            if (v2<=0):
                v2=0
                a2=0
            if (s1>=s2):
                if (not collisionFlag):
                    collisionFlag=True
                    collisionTimer=timer
                    break
        if (hostStopFlag or not collisionFlag):
            self.text_ttc_outcome.setText("No foreseeable collision in 5s.")
            self.output_ttc.setText(">5")
        if (collisionFlag):
            outcome="Foreseeable collision in "+str(round(collisionTimer,3))+"s."
            self.text_ttc_outcome.setText(outcome)
            self.output_ttc.setText(str(round(collisionTimer,3)))
    