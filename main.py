from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, \
    QWidget, QGridLayout, QPushButton, QLabel, QHBoxLayout, QGraphicsScene, QTableView,QHeaderView
from PyQt6.QtGui import QIcon, QFont,QStandardItemModel,QStandardItem,QPixmap
from PyQt6.QtCore import Qt, QTimer
import sys
from output import Ui_Ultiliy_Calc_Box
from common_func import isnum
import numpy as np
from graph_func import *
from unit_conversion import *
from basic_math import *
from basic_motion import *
from acc import *
from aeb import *
from esa import *
from radar import *
import pyqtgraph as pg
import os

r2d = 1 / np.pi * 180
d2r = 1 / 180 * np.pi
c_speed = 299792458
g=9.80665

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller 
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# parent class shall include QManWindow (which is used in QT designer) and Ui_MainWindow_RDT (class in UI.py)
class Window(QMainWindow, Ui_Ultiliy_Calc_Box):

    def __init__(self):
        super().__init__() 
        self.setupUi(self)  
        setupGraph(self)
        # -------------------------------------------------------------------------------------------------------------#
        # Initiate own variables
        self.detect_time=[]
        self.detect_v1=[]
        self.detect_decel=[]
        self.detect_jerk=[]
        self.detect_v2=[]
        self.detect_dist=[]
        self.detect_clearance=[]
        # -------------------------------------------------------------------------------------------------------------#
        # Unit Conversion slot
        self.comboBox_age.currentTextChanged.connect(lambda:age_unitconv(self))
        self.lineEdit_age.editingFinished.connect(lambda:age_unitconv(self))
        self.comboBox_speed.currentTextChanged.connect(lambda:speed_unitconv(self))
        self.lineEdit_speed.editingFinished.connect(lambda:speed_unitconv(self))
        self.comboBox_angleunit.currentTextChanged.connect(lambda:angle_unitconv(self))
        self.lineEdit_angle.editingFinished.connect(lambda:angle_unitconv(self))
        self.comboBox_trigonometry.currentTextChanged.connect(lambda:angle_unitconv(self))
        self.lineEdit_dBsm.editingFinished.connect(lambda:dbsm_unitconv(self))
        self.comboBox_dBsm.currentTextChanged.connect(lambda:dbsm_unitconv(self))
        self.lineEdit_freqinput.editingFinished.connect(lambda:freq_unitconv(self))
        self.comboBox_freq.currentTextChanged.connect(lambda:freq_unitconv(self))
        self.lineEdit_powerinput.editingFinished.connect(lambda:power_unitconv(self))
        self.comboBox_power.currentTextChanged.connect(lambda:power_unitconv(self))
        # -------------------------------------------------------------------------------------------------------------#
        # Basic Math slot
        self.input_arc_angle1.editingFinished.connect(lambda:arc_calc_1(self))
        self.input_arc_radius1.editingFinished.connect(lambda:arc_calc_1(self))
        self.comboBox_arc_angle1.currentTextChanged.connect(lambda:arc_calc_1(self))
        self.input_arc_len2.editingFinished.connect(lambda:arc_calc_2(self))
        self.input_arc_radius2.editingFinished.connect(lambda:arc_calc_2(self))
        self.comboBox_arc_angle2.currentTextChanged.connect(lambda:arc_calc_2(self))
        self.input_tri_angle1.editingFinished.connect(lambda:tri_calc_1(self))
        self.input_tri_side1.editingFinished.connect(lambda:tri_calc_1(self))
        self.comboBox_tri_angle_unit1.currentTextChanged.connect(lambda:tri_calc_1(self))
        self.comboBox_tri_baseorheight.currentTextChanged.connect(lambda:tri_calc_2(self))
        self.input_bitdec_bit.editingFinished.connect(lambda:bit2dec(self))
        self.input_curve_vx.editingFinished.connect(lambda:dist_curve(self))
        self.input_curve_yaw.editingFinished.connect(lambda:dist_curve(self))
        self.comboBox_curve_vx_unit.currentTextChanged.connect(lambda:dist_curve(self))
        self.comboBox_curve_yaw_unit.currentTextChanged.connect(lambda:dist_curve(self))
        self.input_curve_long.editingFinished.connect(lambda:dist_curve(self))
        # -------------------------------------------------------------------------------------------------------------#
        # Basic Motion slot
        self.input_lin_v0_1.editingFinished.connect(lambda:lin_acc_1(self))
        self.input_lin_v1_1.editingFinished.connect(lambda:lin_acc_1(self))
        self.input_lin_dt_1.editingFinished.connect(lambda:lin_acc_1(self))
        self.comboBox_lin_v0.currentTextChanged.connect(lambda:lin_acc_1(self))
        self.comboBox_lin_v1.currentTextChanged.connect(lambda:lin_acc_1(self))
        self.plot_lin_1.pressed.connect(lambda:lin_acc_1(self))
        self.plot_lin_1.pressed.connect(lambda:update_plot_lin(self,1))
        self.input_lin_v0_2.editingFinished.connect(lambda:lin_acc_2(self))
        self.input_lin_v1_2.editingFinished.connect(lambda:lin_acc_2(self))
        self.input_lin_a_2.editingFinished.connect(lambda:lin_acc_2(self))
        self.comboBox_lin_v0.currentTextChanged.connect(lambda:lin_acc_2(self))
        self.comboBox_lin_v1.currentTextChanged.connect(lambda:lin_acc_2(self))
        self.plot_lin_2.pressed.connect(lambda:lin_acc_2(self))
        self.plot_lin_2.pressed.connect(lambda:update_plot_lin(self,2))
        self.input_lin_v0_3.editingFinished.connect(lambda:lin_acc_3(self))
        self.input_lin_a_3.editingFinished.connect(lambda:lin_acc_3(self))
        self.input_lin_s_3.editingFinished.connect(lambda:lin_acc_3(self))
        self.comboBox_lin_v0.currentTextChanged.connect(lambda:lin_acc_3(self))
        self.comboBox_lin_v1.currentTextChanged.connect(lambda:lin_acc_3(self))
        self.plot_lin_3.pressed.connect(lambda:lin_acc_3(self))
        self.plot_lin_3.pressed.connect(lambda:update_plot_lin(self,3))
        self.input_lin_v0_4.editingFinished.connect(lambda:lin_acc_4(self))
        self.input_lin_dt_4.editingFinished.connect(lambda:lin_acc_4(self))
        self.input_lin_a_4.editingFinished.connect(lambda:lin_acc_4(self))
        self.comboBox_lin_v0.currentTextChanged.connect(lambda:lin_acc_4(self))
        self.comboBox_lin_v1.currentTextChanged.connect(lambda:lin_acc_4(self))
        self.plot_lin_4.pressed.connect(lambda:lin_acc_4(self))
        self.plot_lin_4.pressed.connect(lambda:update_plot_lin(self,4))
        self.input_cent_r_1.editingFinished.connect(lambda:cent_acc_1(self))
        self.input_cent_v_1.editingFinished.connect(lambda:cent_acc_1(self))
        self.comboBox_cent_a.currentTextChanged.connect(lambda:cent_acc_1(self))
        self.comboBox_cent_v.currentTextChanged.connect(lambda:cent_acc_1(self))
        self.input_cent_a_2.editingFinished.connect(lambda:cent_acc_2(self))
        self.input_cent_r_2.editingFinished.connect(lambda:cent_acc_2(self))
        self.comboBox_cent_a.currentTextChanged.connect(lambda:cent_acc_2(self))
        self.comboBox_cent_v.currentTextChanged.connect(lambda:cent_acc_2(self))
        self.input_cent_a_3.editingFinished.connect(lambda:cent_acc_3(self))
        self.input_cent_v_3.editingFinished.connect(lambda:cent_acc_3(self))
        self.comboBox_cent_a.currentTextChanged.connect(lambda:cent_acc_3(self))
        self.comboBox_cent_v.currentTextChanged.connect(lambda:cent_acc_3(self))
        self.input_lane_vrear.editingFinished.connect(lambda:lane_man(self))
        self.input_lane_vacsf.editingFinished.connect(lambda:lane_man(self))
        self.comboBox_lane_vacsf.currentTextChanged.connect(lambda:lane_man(self))
        self.comboBox_lane_vrear.currentTextChanged.connect(lambda:lane_man(self))
        self.comboBox_lane_vsmin.currentTextChanged.connect(lambda:lane_man(self))
        self.input_ttc_v1.editingFinished.connect(lambda:ttc(self))
        self.input_ttc_a1.editingFinished.connect(lambda:ttc(self))
        self.input_ttc_v2.editingFinished.connect(lambda:ttc(self))
        self.input_ttc_a2.editingFinished.connect(lambda:ttc(self))
        self.input_ttc_s.editingFinished.connect(lambda:ttc(self))
        self.comboBox_ttc_v1.currentTextChanged.connect(lambda:ttc(self))
        self.comboBox_ttc_v2.currentTextChanged.connect(lambda:ttc(self))
        self.plot_ttc.pressed.connect(lambda:update_plot_ttc(self))
        # -------------------------------------------------------------------------------------------------------------#
        # ACC slot
        self.input_tg_v1.editingFinished.connect(lambda:timegap(self))
        self.input_tg_v2.editingFinished.connect(lambda:timegap(self))
        self.input_tg_l.editingFinished.connect(lambda:timegap(self))
        self.input_tg_rcycle.editingFinished.connect(lambda:timegap(self))
        self.input_tg_tcycle.editingFinished.connect(lambda:timegap(self))
        self.comboBox_tg_v1.currentTextChanged.connect(lambda:timegap(self))
        self.comboBox_tg_v2.currentTextChanged.connect(lambda:timegap(self))
        self.input_follow_v1.editingFinished.connect(lambda:follow_dist(self))
        self.input_follow_headway.editingFinished.connect(lambda:follow_dist(self))
        self.input_follow_lwidth.editingFinished.connect(lambda:follow_dist(self))
        self.comboBox_follow_v1.currentTextChanged.connect(lambda:follow_dist(self))
        self.comboBox_follow_azi_err.currentTextChanged.connect(lambda:follow_dist(self))
        self.input_detect_v1.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_v2.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_cycle.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_headway.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_lfov.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_maxdecel.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_maxjerk.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_tdist.editingFinished.connect(lambda:acc_detect(self))
        self.input_detect_display.editingFinished.connect(lambda:acc_detect(self))
        self.comboBox_detect_v1.currentTextChanged.connect(lambda:acc_detect(self))
        self.comboBox_detect_v2.currentTextChanged.connect(lambda:acc_detect(self))
        self.plot_detect.pressed.connect(lambda:acc_detect(self))
        self.plot_detect.pressed.connect(lambda:update_plot_detect(self))
        self.checkBox_detect_v1.stateChanged.connect(lambda state:update_plot_detect_v1(self,state))
        self.checkBox_detect_decel.stateChanged.connect(lambda state:update_plot_detect_decel(self,state))
        self.checkBox_detect_v2.stateChanged.connect(lambda state:update_plot_detect_v2(self,state))
        self.checkBox_detect_jerk.stateChanged.connect(lambda state:update_plot_detect_jerk(self,state))
        self.checkBox_detect_dist.stateChanged.connect(lambda state:update_plot_detect_dist(self,state))
        self.calculate_sensor.pressed.connect(lambda:sensor_range(self))

        # -------------------------------------------------------------------------------------------------------------#
        # AEB slot
        self.calculate_aeb_1.pressed.connect(lambda:aeb_1(self))
        self.calculate_aeb_2.pressed.connect(lambda:aeb_2(self))
        self.plot_aeb2.pressed.connect(lambda:update_plot_aeb(self))
        # -------------------------------------------------------------------------------------------------------------#
        # ESA slot
        self.input_esa_v.editingFinished.connect(lambda: esa(self))
        self.input_esa_ttc_min.editingFinished.connect(lambda: esa(self))
        self.input_esa_ttc_max.editingFinished.connect(lambda: esa(self))
        self.plot_esa.pressed.connect(lambda:update_plot_esa(self))
        self.checkBox_esa_yaw.stateChanged.connect(lambda state:update_plot_esa_yaw(self,state))
        self.checkBox_esa_yaw_rate.stateChanged.connect(lambda state:update_plot_esa_yaw_rate(self,state))
        self.checkBox_esa_lat_offset.stateChanged.connect(lambda state:update_plot_esa_lat_offset(self,state))
        self.checkBox_esa_lat_accel.stateChanged.connect(lambda state:update_plot_esa_lat_accel(self,state))
        # -------------------------------------------------------------------------------------------------------------#
        # Radar slot
        self.input_dsf_v1.editingFinished.connect(lambda:doppler_freq(self))
        self.input_dsf_v2.editingFinished.connect(lambda:doppler_freq(self))
        self.input_dsf_base_fr.editingFinished.connect(lambda:doppler_freq(self))
        self.comboBox_dsf_v1.currentTextChanged.connect(lambda:doppler_freq(self))
        self.comboBox_dsf_v2.currentTextChanged.connect(lambda:doppler_freq(self))
        self.comboBox_dsf_base_fr.currentTextChanged.connect(lambda:doppler_freq(self))
        self.comboBox_dsf_rx_fr.currentTextChanged.connect(lambda:doppler_freq(self))
        self.comboBox_dsf_dsf.currentTextChanged.connect(lambda:doppler_freq(self))
        self.input_rcs_l.editingFinished.connect(lambda:rcs(self))
        self.input_rcs_fr.editingFinished.connect(lambda:rcs(self))
        self.comboBox_rcs_fr.currentTextChanged.connect(lambda:rcs(self))
        self.comboBox_rcs_wl.currentTextChanged.connect(lambda:rcs(self))
        self.comboBox_rcs_rcs.currentTextChanged.connect(lambda:rcs(self))
        self.input_dds_v1.editingFinished.connect(lambda:dds(self))
        self.input_dds_v2.editingFinished.connect(lambda:dds(self))
        self.input_dds_x.editingFinished.connect(lambda:dds(self))
        self.input_dds_y.editingFinished.connect(lambda:dds(self))
        self.comboBox_dds_v1.currentTextChanged.connect(lambda:dds(self))
        self.comboBox_dds_v2.currentTextChanged.connect(lambda:dds(self))
        self.comboBox_dds_vr.currentTextChanged.connect(lambda:dds(self))
        self.comboBox_dds_azimuth.currentTextChanged.connect(lambda:dds(self))
        self.comboBox_dds_vdopp.currentTextChanged.connect(lambda:dds(self))
        self.input_dda_dir.editingFinished.connect(lambda:dda(self))
        self.input_dda_vdetected.editingFinished.connect(lambda:dda(self))
        self.input_dda_vego.editingFinished.connect(lambda:dda(self))
        self.comboBox_dda_dir.currentTextChanged.connect(lambda:dda(self))
        self.comboBox_dda_vdetected.currentTextChanged.connect(lambda:dda(self))
        self.comboBox_dda_vego.currentTextChanged.connect(lambda:dda(self))
        self.comboBox_dda_vx.currentTextChanged.connect(lambda:dda(self))
        self.comboBox_dda_vy.currentTextChanged.connect(lambda:dda(self))
        self.input_radareq_pr.editingFinished.connect(lambda:radareq(self))
        self.input_radareq_pt.editingFinished.connect(lambda:radareq(self))
        self.input_radareq_gt.editingFinished.connect(lambda:radareq(self))
        self.input_radareq_gr.editingFinished.connect(lambda:radareq(self))
        self.input_radareq_rcs.editingFinished.connect(lambda:radareq(self))
        self.input_radareq_fr.editingFinished.connect(lambda:radareq(self))
        self.comboBox_radareq_pr.currentTextChanged.connect(lambda:radareq(self))
        self.comboBox_radareq_pt.currentTextChanged.connect(lambda:radareq(self))



        self.ttc_timerList=[]
        self.ttc_speedList_host=[]
        self.ttc_distList_host=[]
        self.ttc_speedList_target=[]
        self.ttc_distList_target=[]

        #---------- Set up image directories for pyinstaller-----------------
        arc_img_dir=resource_path("image/Arc.png")
        self.arc_image.setPixmap(QPixmap(arc_img_dir))
        tri_img_dir=resource_path("image/Triangle.png")
        self.tri_image.setPixmap(QPixmap(tri_img_dir))
        label_dir=resource_path("image/Distance_to_curve1.png")
        self.label.setPixmap(QPixmap(label_dir))
        label_2_dir=resource_path("image/Centrifugal acceleration.png")
        self.label_2.setPixmap(QPixmap(label_2_dir))
        label_30_dir=resource_path("image/Scritial1.PNG")
        self.label_30.setPixmap(QPixmap(label_30_dir))
        label_31_dir=resource_path("image/Vsmin.PNG")
        self.label_31.setPixmap(QPixmap(label_31_dir))
        label_116_dir=resource_path("image/braking performance.png")
        self.label_116.setPixmap(QPixmap(label_116_dir))
        label_168_dir=resource_path("image/corner reflector.png")
        self.label_168.setPixmap(QPixmap(label_168_dir))
        label_169_dir=resource_path("image/Doppler section sim.png")
        self.label_169.setPixmap(QPixmap(label_169_dir))
        label_212_dir=resource_path("image/Radar Equation.png")
        self.label_212.setPixmap(QPixmap(label_212_dir))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())