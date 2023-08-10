from common_func import isnum
import numpy as np
import PyQt6
from PyQt6.QtWidgets import QVBoxLayout
import pyqtgraph as pg
from PyQt6.QtGui import QIcon, QFont

def onMouseMoved(plot_widget, event, crosshair_v, crosshair_h):
    pos = event
    if plot_widget.sceneBoundingRect().contains(pos):
        mouse_point = plot_widget.plotItem.vb.mapSceneToView(pos)
        plot_widget.window().statusBar().showMessage(f"Mouse Position: x={round(mouse_point.x(), 4)}, y={round(mouse_point.y(), 4)}")
        crosshair_v.setPos(mouse_point.x())
        crosshair_h.setPos(mouse_point.y())

def setupGraph(self):
    self.crosshair_v = pg.InfiniteLine(angle=90, movable=False)
    self.crosshair_h = pg.InfiniteLine(angle=0, movable=False)
    #-----------------Set up linear accel. graph-------------------
    layout1=QVBoxLayout()
    self.graphicsView_lin.setLayout(layout1)
    self.plot_widget_lin=pg.PlotWidget()
    layout1.addWidget(self.plot_widget_lin)
    self.plot_widget_lin.setBackground('w')
    self.plot_widget_lin.addLegend()
    self.plot_widget_lin.getPlotItem().showAxes(True)
    self.plot_widget_lin.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_lin, event, self.crosshair_v, self.crosshair_h))
    #-----------------Set up ttc graph-----------------------------
    #font=QFont()
    #font.setPixelSize(10)
    layout2=QVBoxLayout()
    self.graphicsView_ttc_v.setLayout(layout2)
    self.plot_widget_ttc_v=pg.PlotWidget()
    layout2.addWidget(self.plot_widget_ttc_v)
    self.plot_widget_ttc_v.setBackground('w')
    self.plot_widget_ttc_v.addLegend()
    self.plot_widget_ttc_v.getPlotItem().showAxes(True)
    self.plot_widget_ttc_v.setLabel("bottom", "Time (s)")
    self.plot_widget_ttc_v.setLabel("left", "Velocity (m/s)")
    #self.plot_widget_ttc_v.getAxis("bottom").setTickFont(font)
    #self.plot_widget_ttc_v.getAxis("left").setTickFont(font)
    self.plot_widget_ttc_v.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_ttc_v, event, self.crosshair_v, self.crosshair_h))
    layout3=QVBoxLayout()
    self.graphicsView_ttc_s.setLayout(layout3)
    self.plot_widget_ttc_s=pg.PlotWidget()
    layout3.addWidget(self.plot_widget_ttc_s)
    self.plot_widget_ttc_s.setBackground('w')
    self.plot_widget_ttc_s.addLegend()
    self.plot_widget_ttc_s.getPlotItem().showAxes(True)
    self.plot_widget_ttc_s.setLabel("bottom", "Time (s)")
    self.plot_widget_ttc_s.setLabel("left", "Distance (m)")
    self.plot_widget_ttc_s.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_ttc_s, event, self.crosshair_v, self.crosshair_h))
    #----------------Set up detect & follow dist graph-------------
    layout4=QVBoxLayout()
    self.graphicsView_detect.setLayout(layout4)
    self.plot_widget_detect=pg.PlotWidget()
    layout4.addWidget(self.plot_widget_detect)
    self.plot_widget_detect.setBackground('w')
    self.plot_widget_detect.addLegend()
    self.plot_widget_detect.getPlotItem().showAxes(True)
    self.plot_widget_detect.setLabel("bottom", "Time (s)")
    self.plot_widget_detect.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_detect, event, self.crosshair_v, self.crosshair_h))
    #----------------Set up AEB decel graph-------------
    layout5=QVBoxLayout()
    self.graphicsView_aeb_dec.setLayout(layout5)
    self.plot_widget_aeb_dec=pg.PlotWidget()
    layout5.addWidget(self.plot_widget_aeb_dec)
    self.plot_widget_aeb_dec.setBackground('w')
    self.plot_widget_aeb_dec.addLegend()
    self.plot_widget_aeb_dec.getPlotItem().showAxes(True)
    self.plot_widget_aeb_dec.setLabel("bottom", "Time (ms)")
    self.plot_widget_aeb_dec.setLabel("left", "Deceleration (m/s^2)")
    self.plot_widget_aeb_dec.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_aeb_dec, event, self.crosshair_v, self.crosshair_h))
    #----------------Set up AEB speed graph-------------
    layout6=QVBoxLayout()
    self.graphicsView_aeb_v.setLayout(layout6)
    self.plot_widget_aeb_v=pg.PlotWidget()
    layout6.addWidget(self.plot_widget_aeb_v)
    self.plot_widget_aeb_v.setBackground('w')
    self.plot_widget_aeb_v.addLegend()
    self.plot_widget_aeb_v.getPlotItem().showAxes(True)
    self.plot_widget_aeb_v.setLabel("bottom", "Time (ms)")
    self.plot_widget_aeb_v.setLabel("left", "Speed (m/s)")
    self.plot_widget_aeb_v.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_aeb_v, event, self.crosshair_v, self.crosshair_h))
    #----------------Set up AEB dist graph-------------
    layout7=QVBoxLayout()
    self.graphicsView_aeb_dist.setLayout(layout7)
    self.plot_widget_aeb_dist=pg.PlotWidget()
    layout7.addWidget(self.plot_widget_aeb_dist)
    self.plot_widget_aeb_dist.setBackground('w')
    self.plot_widget_aeb_dist.addLegend()
    self.plot_widget_aeb_dist.getPlotItem().showAxes(True)
    self.plot_widget_aeb_dist.setLabel("bottom", "Time (ms)")
    self.plot_widget_aeb_dist.setLabel("left", "Distance (m)")
    self.plot_widget_aeb_dist.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_aeb_dist, event, self.crosshair_v, self.crosshair_h))
    #----------------Set up ESA graph-------------
    layout8=QVBoxLayout()
    self.graphicsView_esa.setLayout(layout8)
    self.plot_widget_esa=pg.PlotWidget()
    layout8.addWidget(self.plot_widget_esa)
    self.plot_widget_esa.setBackground('w')
    self.plot_widget_esa.addLegend()
    self.plot_widget_esa.getPlotItem().showAxes(True)
    self.plot_widget_esa.setLabel("bottom", "Time (s)")
    self.plot_widget_esa.scene().sigMouseMoved.connect(lambda event: onMouseMoved(self.plot_widget_esa, event, self.crosshair_v, self.crosshair_h))


def update_plot_lin(self,a):
    if (a==1):
        v0_temp=self.input_lin_v0_1.text()
        v1_temp=self.input_lin_v1_1.text()
        dt_temp=self.input_lin_dt_1.text()
        a_temp=self.output_lin_a_1.text()
    elif (a==2):
        v0_temp=self.input_lin_v0_2.text()
        v1_temp=self.input_lin_v1_2.text()
        dt_temp=self.output_lin_dt_2.text()
        a_temp=self.input_lin_a_2.text()
    elif (a==3):
        v0_temp=self.input_lin_v0_3.text()
        v1_temp=self.output_lin_v1_3.text()
        dt_temp=self.output_lin_dt_3.text()
        a_temp=self.input_lin_a_3.text()
    elif (a==4):
        v0_temp=self.input_lin_v0_4.text()
        v1_temp=self.output_lin_v1_4.text()
        dt_temp=self.input_lin_dt_4.text()
        a_temp=self.input_lin_a_4.text()
    if (isnum(v0_temp) and isnum(v1_temp) and isnum(dt_temp)and isnum(a_temp)):
        v0=float(v0_temp)
        v1=float(v1_temp)
        dt=float(dt_temp)
        a=float(a_temp)
        if (self.comboBox_lin_v0=="kph"):
            v0=v0*3.6
        if (self.comboBox_lin_v1=="kph"):
            v1=v1*3.6
        self.plot_widget_lin.clear()
        self.plot_widget_lin.addItem(self.crosshair_v, ignoreBounds=True)
        self.plot_widget_lin.addItem(self.crosshair_h, ignoreBounds=True)
        t_lins=np.linspace(0,dt,100)
        v_lins=np.linspace(v0,v1,100)
        s_lins=[v0*ti+0.5*a*(ti**2) for ti in t_lins]
        self.plot_widget_lin.plot(t_lins,v_lins,pen=pg.mkPen("black", width=2),name="Velocity (m/s)")
        self.plot_widget_lin.plot(t_lins,s_lins,pen=pg.mkPen("blue", width=2),name="Distance (m)")
        
def update_plot_ttc(self):
    v1_lins=self.ttc_speedList_host
    v2_lins=self.ttc_speedList_target
    s1_lins=self.ttc_distList_host
    s2_lins=self.ttc_distList_target
    t_lins=self.ttc_timerList
    self.plot_widget_ttc_v.clear()
    self.plot_widget_ttc_v.plot(t_lins,v1_lins,pen=pg.mkPen("black", width=1),name="Host Velocity")
    self.plot_widget_ttc_v.plot(t_lins,v2_lins,pen=pg.mkPen("blue", width=1),name="Target Velocity")
    self.plot_widget_ttc_s.clear()
    self.plot_widget_ttc_s.plot(t_lins,s1_lins,pen=pg.mkPen("black", width=1),name="Host Position")
    self.plot_widget_ttc_s.plot(t_lins,s2_lins,pen=pg.mkPen("blue", width=1),name="Target Position")

def update_plot_detect(self):
    self.plot_widget_detect.clear()
    if self.checkBox_detect_v1.isChecked():
        self.plot_detect_v1=self.plot_widget_detect.plot(self.detect_time,self.detect_v1,pen=pg.mkPen("red", width=2),name="Host Speed (m/s)")
    if self.checkBox_detect_v2.isChecked():
        self.plot_detect_v2=self.plot_widget_detect.plot(self.detect_time,self.detect_v2,pen=pg.mkPen("blue", width=2),name="Target Speed (m/s)")
    if self.checkBox_detect_decel.isChecked():
        self.plot_detect_decel=self.plot_widget_detect.plot(self.detect_time,self.detect_decel,pen=pg.mkPen("orange", width=2),name="Host Decel (m/s^2)")
    if self.checkBox_detect_jerk.isChecked():
        self.plot_detect_jerk=self.plot_widget_detect.plot(self.detect_time,self.detect_jerk,pen=pg.mkPen("gray", width=2),name="Host Jerk (m/s^2)")
    if self.checkBox_detect_dist.isChecked():
        self.plot_detect_dist=self.plot_widget_detect.plot(self.detect_time,self.detect_dist,pen=pg.mkPen("green", width=2),name="Host-Target Distance (m)")

def update_plot_detect_v1(self,state):
    if state==2:
        self.plot_detect_v1=self.plot_widget_detect.plot(self.detect_time,self.detect_v1,pen=pg.mkPen("red", width=2),name="Host Speed (m/s)")
    else:
        self.plot_widget_detect.removeItem(self.plot_detect_v1)

def update_plot_detect_v2(self,state):
    if state==2:
        self.plot_detect_v2=self.plot_widget_detect.plot(self.detect_time,self.detect_v2,pen=pg.mkPen("blue", width=2),name="Target Speed (m/s)")
    else:
        self.plot_widget_detect.removeItem(self.plot_detect_v2)

def update_plot_detect_decel(self,state):
    if state==2:
        self.plot_detect_decel=self.plot_widget_detect.plot(self.detect_time,self.detect_decel,pen=pg.mkPen("orange", width=2),name="Host Decel (m/s^2)")
    else:
        self.plot_widget_detect.removeItem(self.plot_detect_decel)

def update_plot_detect_jerk(self,state):
    if state==2:
        self.plot_detect_jerk=self.plot_widget_detect.plot(self.detect_time,self.detect_jerk,pen=pg.mkPen("gray", width=2),name="Host Jerk (m/s^2)")
    else:
        self.plot_widget_detect.removeItem(self.plot_detect_jerk)

def update_plot_detect_dist(self,state):
    if state==2:
        self.plot_detect_dist=self.plot_widget_detect.plot(self.detect_time,self.detect_dist,pen=pg.mkPen("green", width=2),name="Host-Target Distance (m)")
    else:
        self.plot_widget_detect.removeItem(self.plot_detect_dist)

def update_plot_aeb(self):
    self.plot_widget_aeb_dec.clear()
    self.plot_widget_aeb_dec.plot(self.aeb_timeline,self.aeb_decel_req,pen=pg.mkPen("blue",width=1.5),name="Required Decel.")
    self.plot_widget_aeb_dec.plot(self.aeb_timeline,self.aeb_decel_actual,pen=pg.mkPen("black",width=1.5),name="Actual Decel.")
    self.plot_widget_aeb_v.clear()
    self.plot_widget_aeb_v.plot(self.aeb_timeline,self.aeb_v,pen=pg.mkPen("black",width=1.5),name="Host Speed")
    self.plot_widget_aeb_dist.clear()
    self.plot_widget_aeb_dist.plot(self.aeb_timeline,self.aeb_dist,pen=pg.mkPen("black",width=1.5),name="Distance")

    
def update_plot_esa(self):
    self.plot_widget_esa.clear()
    if self.checkBox_esa_yaw.isChecked():
        self.plot_esa_yaw=self.plot_widget_esa.plot(self.esa_timeline,self.esa_yaw,pen=pg.mkPen("blue",width=1.5),name="Yaw (deg)")
    if self.checkBox_esa_yaw_rate.isChecked():
        self.plot_esa_yaw_rate=self.plot_widget_esa.plot(self.esa_timeline,self.esa_yaw_rate,pen=pg.mkPen("grey",width=1.5),name="Yaw Rate (deg/s)")
    if self.checkBox_esa_lat_offset.isChecked():
        self.plot_esa_lat_offset=self.plot_widget_esa.plot(self.esa_timeline,self.esa_lat_offset,pen=pg.mkPen("orange",width=1.5),name="Lateral Offset (m)")
    if self.checkBox_esa_lat_accel.isChecked():
        self.plot_esa_lat_accel=self.plot_widget_esa.plot(self.esa_timeline,self.esa_lat_accel,pen=pg.mkPen("green",width=1.5),name="Lateral Accel. (m/s^2)")

def update_plot_esa_yaw(self,state):
    if state==2:
        self.plot_esa_yaw=self.plot_widget_esa.plot(self.esa_timeline,self.esa_yaw,pen=pg.mkPen("blue",width=1.5),name="Yaw (deg)")
    else:
        self.plot_widget_esa.removeItem(self.plot_esa_yaw)

def update_plot_esa_yaw_rate(self,state):
    if state==2:
        self.plot_esa_yaw_rate=self.plot_widget_esa.plot(self.esa_timeline,self.esa_yaw_rate,pen=pg.mkPen("grey",width=1.5),name="Yaw Rate (deg/s)")
    else:
        self.plot_widget_esa.removeItem(self.plot_esa_yaw_rate)

def update_plot_esa_lat_offset(self,state):
    if state==2:
        self.plot_esa_lat_offset=self.plot_widget_esa.plot(self.esa_timeline,self.esa_lat_offset,pen=pg.mkPen("orange",width=1.5),name="Lateral Offset (m)")
    else:
        self.plot_widget_esa.removeItem(self.plot_esa_lat_offset)

def update_plot_esa_lat_accel(self,state):
    if state==2:
        self.plot_esa_lat_accel=self.plot_widget_esa.plot(self.esa_timeline,self.esa_lat_accel,pen=pg.mkPen("green",width=1.5),name="Lateral Accel. (m/s^2)")
    else:
        self.plot_widget_esa.removeItem(self.plot_esa_lat_accel)

