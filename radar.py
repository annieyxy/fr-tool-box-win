import numpy as np
from common_func import isnum
d2r = 1 / 180 * np.pi
r2d = 1 / np.pi * 180
c_speed = 299792458

def doppler_freq(self):
    v1_temp=self.input_dsf_v1.text()
    v2_temp=self.input_dsf_v2.text()
    base_freq_temp=self.input_dsf_base_fr.text()
    v1_unit=self.comboBox_dsf_v1.currentText()
    v2_unit=self.comboBox_dsf_v2.currentText()
    base_freq_unit=self.comboBox_dsf_base_fr.currentText()
    rx_freq_unit=self.comboBox_dsf_rx_fr.currentText()
    dsf_unit=self.comboBox_dsf_dsf.currentText()
    if isnum(v1_temp) and isnum(v2_temp) and isnum(base_freq_temp):
        v1=float(v1_temp)
        v2=float(v2_temp)
        base_freq=float(base_freq_temp)
        if v1_unit=="kph":
            v1/=3.6
        if v2_unit=="kph":
            v2/=3.6
        if base_freq_unit=="GHz":
            base_freq*=(10**9)
        rx_freq=base_freq*(c_speed-v1)/(c_speed-v2)
        dsf=rx_freq-base_freq
        if (rx_freq_unit=="GHz"):
            rx_freq/=(10**9)
        rx_freq="{:.3e}".format(rx_freq)
        if (dsf_unit=="KHz"):
            dsf/=1000
        self.output_dsf_rx_fr.setText(str(rx_freq))
        self.output_dsf_dsf.setText(str(round(dsf,3)))

def rcs(self):
    l_temp=self.input_rcs_l.text()
    fr_temp=self.input_rcs_fr.text()
    fr_unit=self.comboBox_rcs_fr.currentText()
    wl_unit=self.comboBox_rcs_wl.currentText()
    rcs_unit=self.comboBox_rcs_rcs.currentText()
    if isnum(l_temp) and isnum(fr_temp):
        l=float(l_temp)
        fr=float(fr_temp)
        if fr_unit=="GHz":
            fr*=(10**9)
        wl=c_speed/fr
        rcs=(4*np.pi*l**4)/(3*wl**2)
        if wl_unit=="mm":
            wl*=1000
        wl="{:.3e}".format(wl)
        if rcs_unit=="dBsm":
            rcs=10*np.log10(rcs)
        rcs="{:.3e}".format(rcs)
        self.output_rcs_wl.setText(str(wl))
        self.output_rcs_rcs.setText(str(rcs))

def dds(self):
    v1_temp=self.input_dds_v1.text()
    v2_temp=self.input_dds_v2.text()
    x_temp=self.input_dds_x.text()
    y_temp=self.input_dds_y.text()
    v1_unit=self.comboBox_dds_v1.currentText()
    v2_unit=self.comboBox_dds_v2.currentText()
    vr_unit=self.comboBox_dds_vr.currentText()
    azimuth_unit=self.comboBox_dds_azimuth.currentText()
    vdopp_unit=self.comboBox_dds_vdopp.currentText()
    if isnum(v1_temp) and isnum(v2_temp):
        v1=float(v1_temp)
        v2=float(v2_temp)
        if v1_unit=="kph":
            v1/=3.6
        if v2_unit=="kph":
            v2/=3.6
        vr=v2-v1
        if vr_unit=="kph":
            self.output_dds_vr.setText(str(round(vr*3.6,3)))
        else:
            self.output_dds_vr.setText(str(round(vr,3)))
        if isnum(x_temp) and isnum(y_temp):
            #app.TargetazimuthEditField.Value = atan(app.TargetyposEditField.Value / app.TargetxposEditField.Value);
            #app.DopplervelocityEditField.Value = app.RelativevelocityEditField.Value * cosd(app.TargetazimuthEditField_2.Value);
            x=float(x_temp)
            y=float(y_temp)
            azimuth=np.arctan(y/x)
            vdopp=vr*np.cos(azimuth)
            if azimuth_unit=="deg":
                azimuth*=r2d
            if vdopp_unit=="kph":
                vdopp*=3.6
            self.output_dds_azimuth.setText(str(round(azimuth,3)))
            self.output_dds_vdopp.setText(str(round(vdopp,3)))

def dda(self):
    dir_temp=self.input_dda_dir.text()
    vdetected_temp=self.input_dda_vdetected.text()
    vego_temp=self.input_dda_vego.text()
    dir_unit=self.comboBox_dda_dir.currentText()
    vdetected_unit=self.comboBox_dda_vdetected.currentText()
    vego_unit=self.comboBox_dda_vego.currentText()
    vx_unit=self.comboBox_dda_vx.currentText()
    vy_unit=self.comboBox_dda_vy.currentText()
    if isnum(dir_temp) and isnum(vdetected_temp) and isnum(vego_temp):
        dir1=float(dir_temp)
        vdetected=float(vdetected_temp)
        vego=float(vego_temp)
        if dir_unit=="deg":
            dir1*=d2r
        if vdetected_unit=="kph":
            vdetected/=3.6
        if vego_unit=="kph":
            vego/=3.6
        vx=vdetected*np.cos(dir1)+vego
        vy=vdetected*np.sin(dir1)
        if vx_unit=="kph":
            vx*=3.6
        if vy_unit=="kph":
            vy*=3.6
        self.output_dda_vx.setText(str(round(vx,3)))
        self.output_dda_vy.setText(str(round(vy,3)))

def radareq(self):
    pr_temp=self.input_radareq_pr.text()
    pt_temp=self.input_radareq_pt.text()
    gt_temp=self.input_radareq_gt.text()
    gr_temp=self.input_radareq_gr.text()
    rcs_temp=self.input_radareq_rcs.text()
    fr_temp=self.input_radareq_fr.text()
    pr_unit=self.comboBox_radareq_pr.currentText()
    pt_unit=self.comboBox_radareq_pt.currentText()
    if isnum(pr_temp) and isnum(pt_temp) and isnum(gt_temp) and isnum(gr_temp) and isnum(rcs_temp) and isnum(fr_temp):
        pr=float(pr_temp)
        pt=float(pt_temp)
        gt=float(gt_temp)
        gr=float(gr_temp)
        rcs=float(rcs_temp)
        fr=float(fr_temp)
        if pr_unit=="dBm":
            # pr=10*np.log10(pr)/1000
            pr=10**(pr/10)/1000
        else:
            pr/=1000
        if pt_unit=="dBm":
            # pt=10*np.log10(pt)/1000
            pt=10**(pt/10)/1000
        else:
            pt/=1000
        wl=c_speed/(fr*10**9)*1000
        # app.WaveLength.Value = 300000000 / (app.RadarFrequency.Value * 1E9) * 1000;
        # Gt_dec = 10 ^ (app.Tx_ANT_G.Value / 10);
        # Gr_dec = 10 ^ (app.Rx_ANT_G.Value / 10);
        # RCS_dec = 10 ^ (app.TargetRCS.Value / 10);
        # app.TargetRange.Value = power(((app.TxPowerinmw.Value / 1000) * Gt_dec * Gr_dec * (app.WaveLength.Value / 1000)^2 * RCS_dec) / (((4*pi)^3) * (app.RxPowerinmw.Value / 1000)), 1/4);
        gt_dec=10**(gt/10)
        gr_dec=10**(gr/10)
        rcs_dec=10**(rcs/10)
        rtarget=(pt*gt_dec*gr_dec*(wl/1000)**2*rcs_dec/((4*np.pi)**3*pr))**(1/4)
        self.output_radareq_rtarget.setText(str(round(rtarget,3)))
        self.output_radareq_wl.setText(str(round(wl,3)))