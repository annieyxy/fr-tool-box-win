from common_func import isnum
import numpy as np
from PyQt6.QtGui import QFont,QStandardItemModel,QStandardItem
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtCore import Qt
r2d = 1 / np.pi * 180

def timegap(self):
    l_temp=self.input_tg_l.text()
    v1_temp=self.input_tg_v1.text()
    v2_temp=self.input_tg_v2.text()
    rcycle_temp=self.input_tg_rcycle.text()
    tcycle_temp=self.input_tg_tcycle.text()
    v1_unit=self.comboBox_tg_v1.currentText()
    v2_unit=self.comboBox_tg_v2.currentText()
    if isnum(l_temp) and isnum(v1_temp) and isnum(v2_temp):
        l=float(l_temp)
        v1=float(v1_temp)
        v2=float(v2_temp)
        if v1_unit=="kph":
            v1/=3.6
        if v2_unit=="kph":
            v2/=3.6
        timegap=l/abs(v1-v2)
        self.output_tg_t.setText(str(round(timegap,3)))
        if (isnum(rcycle_temp) and isnum(tcycle_temp)):
            rcycle=float(rcycle_temp)/1000
            tcycle=float(tcycle_temp)
            ddist=rcycle*tcycle*(v2-v1)+l
            self.output_tg_detectdist.setText(str(round(ddist,3)))
            
def follow_dist(self):
    v1_temp=self.input_follow_v1.text()
    headway_temp=self.input_follow_headway.text()
    lwidth_temp=self.input_follow_lwidth.text()
    v1_unit=self.comboBox_follow_v1.currentText()
    angle_unit=self.comboBox_follow_azi_err.currentText()
    if (isnum(v1_temp) and isnum(headway_temp) and isnum(lwidth_temp)):
        v1=float(v1_temp)
        headway=float(headway_temp)
        lwidth=float(lwidth_temp)
        if v1_unit=="kph":
            v1/=3.6
        tdist=v1*headway
        self.output_follow_tdist.setText(str(round(tdist,3)))
        # theta_error = rad2deg(atan(0.5 * Wlane / Target_dist));
        azi_err= np.arctan(0.5*lwidth/tdist)
        if angle_unit=="deg":
            azi_err*=r2d
        self.output_follow_azi_err.setText(str(round(azi_err,3)))

def acc_detect(self):
    v1_temp=self.input_detect_v1.text()
    v2_temp=self.input_detect_v2.text()
    tdist_temp=self.input_detect_tdist.text()
    fov_temp=self.input_detect_lfov.text()
    maxdecel_temp=self.input_detect_maxdecel.text()
    maxjerk_temp=self.input_detect_maxjerk.text()
    cycle_temp=self.input_detect_cycle.text()
    headway_temp=self.input_detect_headway.text()
    tdisplay_temp=self.input_detect_display.text()
    v1_unit=self.comboBox_detect_v1.currentText()
    v2_unit=self.comboBox_detect_v2.currentText()
    '''v1_temp="100"
    v2_temp="40"
    tdist_temp="110"
    fov_temp="100"
    maxdecel_temp="-3.5"
    maxjerk_temp="-2.5"
    cycle_temp="20"
    headway_temp="3"
    tdisplay_temp="20"
    v1_unit="kph"
    v2_unit="kph"'''
    if isnum(v1_temp) and isnum(v2_temp) and isnum(tdist_temp) and isnum(fov_temp) and isnum(maxdecel_temp) and isnum(maxjerk_temp) and isnum(cycle_temp) and isnum(headway_temp) and isnum(tdisplay_temp):
        v1=float(v1_temp)
        v2=float(v2_temp)
        tdist=float(tdist_temp)
        fov=float(fov_temp)
        maxdecel=float(maxdecel_temp)
        maxjerk=float(maxjerk_temp)
        cycle=float(cycle_temp)/1000
        headway=float(headway_temp)
        tdisplay=float(tdisplay_temp)
        if v1_unit=="kph":
            v1/=3.6
        if v2_unit=="kph":
            v2/=3.6
        count=int(np.ceil(tdisplay/cycle))
        jerk_flag=[0]
        timeline=[0]
        jerk=[0] #host jerk
        decel=[0] #host deceleration
        v1t=[v1] #host Speed
        v2t=[v2] #target Speed
        s1t=[0] #host move distance
        s2t=[tdist] #target move distance
        ht_dist=[tdist] #host-targetDistance
        target_clearance=[v2*headway] #target clearance
        # print(count)
        for i in range(1,count):
            '''print("count:" +str(i))
            print("time:" +str(timeline[-1]))
            print("v1: "+str(v1t[-1]))
            print("v2: "+str(v2t[-1]))
            print("decel: "+str(decel[-1]))
            print("jerk: "+str(jerk[-1]))
            print("s1: "+str(s1t[-1]))
            print("s2: "+str(s2t[-1]))
            print("distance: "+str(ht_dist[-1]))
            print("---------------")'''
            if decel[-1]>maxdecel and v1t[-1]>=v2 and ht_dist[-1]<fov : # can increase host deceleraion
                decel.append(decel[-1]+maxjerk*cycle)
                jerk.append(maxjerk)
            elif ht_dist[-1]<fov and v1t[-1]>v2: # host constant deceleration
                decel.append(decel[-1]) 
                jerk.append(0)
            else: # host no deceleration
                decel.append(0)
                jerk.append(0)
            s1t.append(s1t[-1]+v1t[-1]*cycle)
            v1t.append(v1t[-1]+decel[-1]*cycle)
            v2t.append(v2)
            s2t.append(s2t[-1]+v2*cycle)
            ht_dist.append(s2t[-1]-s1t[-1])
            target_clearance.append(v2*headway)
            timeline.append(timeline[-1]+cycle)
        self.detect_time=timeline
        self.detect_v1=v1t
        self.detect_decel=decel
        self.detect_jerk=jerk
        self.detect_v2=v2t
        self.detect_dist=ht_dist
        self.detect_clearance=target_clearance
        

def sensor_range(self):
    v1_temp=self.input_sensor_v1.text()
    v2_temp=self.input_sensor_v2.text()
    jerk_temp=self.input_sensor_jerk.text()
    accdecel_temp=self.input_sensor_accdecel.text()
    mintg_temp=self.input_sensor_mintg.text()
    tsensor_temp=self.input_sensor_tsensor.text()
    talgo_temp=self.input_sensor_talgo.text()
    tcomm_temp=self.input_sensor_tcomm.text()
    tactu_temp=self.input_sensor_tactu.text()
    treact_temp=self.input_sensor_treact.text()
    maxdecel_temp=self.input_sensor_maxdecel.text()
    minrange_temp=self.input_sensor_minrange.text()
    maxtg_temp=self.input_sensor_maxtg.text()
    if (isnum(v1_temp) and isnum(v2_temp) and isnum(jerk_temp) and 
        isnum(accdecel_temp) and isnum(mintg_temp) and isnum(tsensor_temp) and
        isnum(talgo_temp) and isnum(tcomm_temp)  and isnum(tactu_temp) and 
        isnum(treact_temp) and isnum(maxdecel_temp) and isnum(minrange_temp) 
        and isnum(maxtg_temp)):
        v1=float(v1_temp)
        v2=float(v2_temp)
        jerk=float(jerk_temp)
        accdecel=float(accdecel_temp)
        mintg=float(mintg_temp)
        tsensor=float(tsensor_temp)
        talgo=float(talgo_temp)
        tcomm=float(tcomm_temp)
        tactu=float(tactu_temp)
        treact=float(treact_temp)
        maxdecel=float(maxdecel_temp)
        minrange=float(minrange_temp)
        maxtg=float(maxtg_temp)
        clearance=maxtg*v2/3.6
        self.output_sensor_clearance.setText(str(round(clearance,3)))
        #app.MaximumrequiredclearanceEditField.Value = Max_timegap * Targetspeed(3)/3.6;
        host_speed=[v1-20]
        target_speed=[v2-20]
        table1 = [[0 for j in range(5)] for i in range(5)]
        table2 = [[0 for j in range(5)] for i in range(5)]
        for i in range(4):
            host_speed.append(host_speed[-1]+10)
            target_speed.append(target_speed[-1]+10)
        for i in range(5):
            if host_speed[i]<0:
                host_speed[i]=0
            if target_speed[i]<0:
                target_speed[i]=0
        for i,vh in enumerate(host_speed):
            vh/=3.6
            for j,vt in enumerate(target_speed):
                vt/=3.6
                # print(f"({i},{j}):vh={vh},vt={vt}")
                if vh>vt:
                    t_delay=accdecel/jerk
                    t_delta=(vt-(vh+t_delay*accdecel/2))/accdecel
                    # T_Delta = (Targetspeed(k)/3.6 - (Hostspeed(j)/3.6 + T_delay * A_max / 2)) / A_max;
                    d_processing=vh*(tsensor+talgo+tcomm)
                    # D_processing = Hostspeed(j)/3.6 * (T_Sensor + T_Algo + T_Com);
                    d_actuator=vh*tactu
                    # D_actuator = Hostspeed(j)/3.6 * T_Actuator;
                    d_braking1=accdecel*t_delay**2/6+vh*t_delay
                    # D_braking1 = A_max * T_delay ^ 2 / 6 + Hostspeed(j)/3.6 * T_delay;
                    d_braking2=((vt-vh)**2+2*vh*(vt-vh)-(accdecel*t_delay)**2/4-vt*accdecel*t_delay)/(2*accdecel)
                    # D_braking2 = ((Targetspeed(k)/3.6 - Hostspeed(j)/3.6) ^ 2 + 2 * Hostspeed(j)/3.6 * (Targetspeed(k)/3.6 - Hostspeed(j)/3.6) - (A_max * T_delay) ^ 2 / 4 - Targetspeed(k)/3.6 * A_max * T_delay) / (2 * A_max);
                    d_safe=mintg*vt+minrange
                    # D_safe = SftyGap_min * Targetspeed(k)/3.6 + SftyD_min;
                    d_tardriven=vt*(tsensor+talgo+tcomm+tactu+t_delay+t_delta)
                    # print(f"({i},{j}):vh={vh},vt={vt}, {d_processing+d_actuator+d_braking1+d_braking2+d_safe-d_tardriven}")
                    # D_tardriven = Targetspeed(k)/3.6 * (T_Sensor + T_Algo + T_Com + T_Actuator + T_delay + T_Delta);
                    table1[i][j]=d_processing+d_actuator+d_braking1+d_braking2+d_safe-d_tardriven
                    # table1(index) = D_processing + D_actuator + D_braking1 + D_braking2 + D_safe - D_tardriven;
                    #........................
                    t_delay1=t_delay
                    t_delay2=0.3
                    t_delta1=treact-tactu-t_delay1
                    # T_Delta1 = T_Reaction - T_Actuator - T_Delay1;
                    d_delay=accdecel*t_delay1**2/6+vh*t_delay1
                    # D_Delay = A_max * T_Delay1 ^ 2 / 6 + Hostspeed(j)/3.6 * T_Delay1;
                    d_delta1=accdecel*t_delta1**2/2+(vh+accdecel*t_delay1/2)*t_delta1
                    # D_Delta1 = A_max * T_Delta1 ^ 2 /2 + (Hostspeed(j)/3.6 + A_max * T_Delay1 / 2) * T_Delta1;
                    v_delta1=max(accdecel*t_delta1+accdecel*t_delay1/2+vh,vt)
                    # V_Delta1 = A_max * T_Delta1 + A_max * T_Delay1 / 2 + Hostspeed(j)/3.6;
                    # V_Delta1 = max(Targetspeed(k)/3.6, V_Delta1);
                    d_braking1=d_delay+d_delta1
                    # D_Braking1 = D_Delay + D_Delta1;
                    if v_delta1==vt:
                        d_braking2=0
                    else:
                        v_delay2=(maxdecel/t_delay2)*t_delay2**2/2+accdecel*t_delay2+v_delta1
                        # V_Delay2 = (A_drivermax / T_Delay2) * T_Delay2 ^ 2 / 2 + A_max * T_Delay2 + V_Delta1;
                        d_delay2=(maxdecel/t_delay2)*t_delay2**3/6+accdecel*t_delay2**2/2+v_delta1*t_delay2
                        # D_Delay2 = (A_drivermax / T_Delay2) * T_Delay2 ^ 3 / 6 + A_max * T_Delay2 ^ 2 / 2 + V_Delta1 * T_Delay2;
                        t_delta2=(vt-v_delay2)/maxdecel
                        # T_Delta2 = (Targetspeed(k)/ 3.6 - V_Delay2) / A_drivermax;
                        d_delta2=maxdecel*t_delta2**2/2+v_delay2*t_delta2
                        # D_Delta2 = A_drivermax * T_Delta2 ^ 2 / 2 + V_Delay2 * T_Delta2;
                        d_braking2=d_delay2+d_delta2
                        # D_Braking2 = D_Delay2 + D_Delta2;
                    d_tar_div=vt*(tsensor+talgo+tcomm+treact+t_delay2+t_delta2)
                    # D_TarDiv = Targetspeed(k) / 3.6 * (T_Sensor + T_Algo + T_Com + T_Reaction + T_Delay2 + T_Delta2);
                    table2[i][j]=d_processing+d_actuator+d_braking2+d_braking1+d_safe-d_tar_div
                    # table2(index) = D_processing + D_actuator + D_Braking2 + D_Braking1 + D_safe - D_TarDiv
                else:
                    table1[i][j]=0
                    table2[i][j]=0
                # print(f"table1({i},{j}):{table1[i][j]}")
                # print(f"table2({i},{j}):{table2[i][j]}")
        #-------------------- set up tableView ------------------------
        model1=QStandardItemModel()
        model1.setRowCount(5)
        model1.setColumnCount(5)
        model2=QStandardItemModel()
        model2.setRowCount(5)
        model2.setColumnCount(5)
        font=QFont()
        font.setPointSize(10)
        for row in range(5):
            for col in range(5):
                item1 = QStandardItem(str(round(table1[col][row],3)))
                item1.setFont(font)
                item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model1.setItem(row, col, item1)
                item2 = QStandardItem(str(round(table2[col][row],3)))
                item2.setFont(font)
                item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model2.setItem(row, col, item2)
        for col in range(5):
            item1 = QStandardItem(f"{host_speed[col]}")
            item1.setFont(font)
            model1.setHorizontalHeaderItem(col, item1)
            item2 = QStandardItem(f"{host_speed[col]}")
            item2.setFont(font)
            model2.setHorizontalHeaderItem(col, item2)
        for row in range(5):
            item1 = QStandardItem(f"{target_speed[row]}")
            item1.setFont(font)
            model1.setVerticalHeaderItem(row,item1)
            item2 = QStandardItem(f"{target_speed[row]}")
            item2.setFont(font)
            model2.setVerticalHeaderItem(row,item2)
        self.tableView_sensor_1.setModel(model1)
        self.tableView_sensor_2.setModel(model2)
        hheader1 = self.tableView_sensor_1.horizontalHeader()
        # header.setSectionResizeMode(QHeaderView.ResizeToContents)
        # header.setDefaultSectionSize(70)
        hheader1.setSectionResizeMode(QHeaderView.ResizeMode.Stretch) 
        vheader1 = self.tableView_sensor_1.verticalHeader()
        vheader1.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # self.tableView_sensor_1.verticalHeader().setVisible(False)
        # self.tableView_sensor_1.horizontalHeader().setVisible(False) 
        hheader2 = self.tableView_sensor_2.horizontalHeader()
        hheader2.setSectionResizeMode(QHeaderView.ResizeMode.Stretch) 
        vheader2 = self.tableView_sensor_2.verticalHeader()
        vheader2.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)