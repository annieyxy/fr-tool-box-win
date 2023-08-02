from common_func import isnum
import numpy as np
def aeb_1(self):
    lat_pre_temp=self.input_aeb1_lat_pre.text()
    ramp_pre_temp=self.input_aeb1_ramp_pre.text()
    dec_pre_temp=self.input_aeb1_dec_pre.text()
    dur_pre_temp=self.input_aeb1_dur_pre.text()
    lat_part_temp=self.input_aeb1_lat_part.text()
    ramp_part_temp=self.input_aeb1_ramp_part.text()
    dec_part_temp=self.input_aeb1_dec_part.text()
    dur_part_temp=self.input_aeb1_dur_part.text()
    lat_full_temp=self.input_aeb1_lat_full.text()
    ramp_full_temp=self.input_aeb1_ramp_full.text()
    dec_full_temp=self.input_aeb1_dec_full.text()
    dur_full_temp=self.input_aeb1_dur_full.text()
    if(isnum(lat_pre_temp)and isnum(ramp_pre_temp) and isnum(dec_pre_temp) and isnum(dur_pre_temp)):
        lat_pre=float(lat_pre_temp)
        ramp_pre=float(ramp_pre_temp)
        dec_pre=float(dec_pre_temp)
        dur_pre=float(dur_pre_temp)
        dv_pre=dec_pre*(dur_pre-lat_pre-0.5*ramp_pre)/1000*3.6
        # app.PreFull_SpdRed.Value = PreFill_aa * (PreFill_D - PreFill_L - 0.5 * PreFill_R) / 1000 * 3.6;
        self.output_aeb1_dv_pre.setText(str(round(dv_pre,3)))
        self.lat_pre=lat_pre
        self.ramp_pre=ramp_pre
        self.dec_pre=dec_pre
        self.dur_pre=dur_pre
        if(isnum(lat_part_temp)and isnum(ramp_part_temp) and isnum(dec_part_temp) and isnum(dur_part_temp)):
            lat_part=float(lat_part_temp)
            ramp_part=float(ramp_part_temp)
            dec_part=float(dec_part_temp)
            dur_part=float(dur_part_temp)
            dv_part= (dec_part*dur_part-(dec_part-dec_pre)*lat_part-0.5*(dec_part-dec_pre)*ramp_part)/1000*3.6
            # app.PartialBrake_SpdRed.Value = (PartialBrake_aa * PartialBrake_D - (PartialBrake_aa - PreFill_aa) * PartialBrake_L - 0.5 * (PartialBrake_aa - PreFill_aa) * PartialBrake_R) / 1000 * 3.6;
            self.output_aeb1_dv_part.setText(str(round(dv_part,3)))
            self.lat_part=lat_part
            self.ramp_part=ramp_part
            self.dec_part=dec_part
            self.dur_part=dur_part
            if(isnum(lat_full_temp)and isnum(ramp_full_temp) and isnum(dec_full_temp) and isnum(dur_full_temp)):
                lat_full=float(lat_full_temp)
                ramp_full=float(ramp_full_temp)
                dec_full=float(dec_full_temp)
                dur_full=float(dur_full_temp)
                dv_full= (dec_full*dur_full-(dec_full-dec_part)*lat_full-0.5*(dec_full-dec_part)*ramp_full)/1000*3.6
                # app.FullBrake_SpdRed.Value = (FullBrake_aa * FullBrake_D - (FullBrake_aa - PartialBrake_aa) * FullBrake_L - 0.5 * (FullBrake_aa - PartialBrake_aa) * FullBrake_R) / 1000 * 3.6;
                self.output_aeb1_dv_full.setText(str(round(dv_full,3)))
                self.lat_full=lat_full
                self.ramp_full=ramp_full
                self.dec_full=dec_full
                self.dur_full=dur_full

def aeb_2(self):
    sim_dt_temp=self.input_aeb2_dtsim.text()
    pre_start_t_temp=self.input_aeb2_prefill_time.text()
    v0_temp=self.input_aeb2_v0.text()
    v0_unit=self.comboBox_aeb2_v0.currentText()
    if (isnum(sim_dt_temp) and isnum(pre_start_t_temp) and isnum(v0_temp)):
        sim_dt=float(sim_dt_temp)
        pre_start_t=float(pre_start_t_temp)
        v0=float(v0_temp)
        if v0_unit=="kph":
            v0/=3.6
        prefill_lat_1=pre_start_t
        prefill_ramp_1=pre_start_t+self.lat_pre
        prefill_reach_1=prefill_ramp_1+self.ramp_pre
        part_lat_1=prefill_lat_1+self.dur_pre
        part_ramp_1=part_lat_1+self.lat_part
        part_reach_1=part_ramp_1+self.ramp_part
        full_lat_1=part_lat_1+self.dur_part
        full_ramp_1=full_lat_1+self.lat_full
        full_reach_1=full_ramp_1+self.ramp_full
        postaeb_1=full_lat_1+self.dur_full
        postaeb_2=9999
        pre_vramp=self.dec_pre/self.ramp_pre*1000
        part_vramp=(self.dec_part-self.dec_pre)/self.ramp_part*1000
        full_vramp=(self.dec_full-self.dec_part)/self.ramp_full*1000
        #----------------
        self.output_aeb2_preaeb_1.setText(str(0))
        self.output_aeb2_preaeb_2.setText(str(pre_start_t-1))
        self.output_aeb2_prefill_lat_1.setText(str(pre_start_t))
        self.output_aeb2_prefill_lat_2.setText(str(prefill_ramp_1-1))
        self.output_aeb2_prefill_ramp_1.setText(str(prefill_ramp_1))
        self.output_aeb2_prefill_ramp_2.setText(str(prefill_reach_1-1))
        self.output_aeb2_prefill_reach_1.setText(str(prefill_reach_1))
        self.output_aeb2_prefill_reach_2.setText(str(part_lat_1-1))
        self.output_aeb2_part_lat_1.setText(str(part_lat_1))
        self.output_aeb2_part_lat_2.setText(str(part_ramp_1-1))
        self.output_aeb2_part_ramp_1.setText(str(part_ramp_1))
        self.output_aeb2_part_ramp_2.setText(str(part_reach_1-1))
        self.output_aeb2_part_reach_1.setText(str(part_reach_1))
        self.output_aeb2_part_reach_2.setText(str(full_lat_1-1))
        self.output_aeb2_full_lat_1.setText(str(full_lat_1))
        self.output_aeb2_full_lat_2.setText(str(full_ramp_1-1))
        self.output_aeb2_full_ramp_1.setText(str(full_ramp_1))
        self.output_aeb2_full_ramp_2.setText(str(full_reach_1-1))
        self.output_aeb2_full_reach_1.setText(str(full_reach_1))
        self.output_aeb2_full_reach_2.setText(str(postaeb_1-1))
        self.output_aeb2_postaeb_1.setText(str(postaeb_1))
        self.output_aeb2_postaeb_2.setText(str(postaeb_2))
        self.output_aeb2_pre_vramp.setText(str(round(pre_vramp,3)))
        self.output_aeb2_part_vramp.setText(str(round(part_vramp,3)))
        self.output_aeb2_full_vramp.setText(str(round(full_vramp,3)))
        #-------------------
        count=np.ceil(postaeb_2/sim_dt)
        decel=0
        time=[0]
        v_host=[v0]
        dist=[0]
        decel_req=[0]
        decel_actual=[0]
        for i in range(1,int(count)):
            time.append(time[-1]+sim_dt)
            if (time[i]>=0 and time[i]<=pre_start_t-1):
                decel_req.append(0)
                decel_actual.append(0)
            elif (time[i]>=pre_start_t and time[i]<=prefill_ramp_1-1):
                decel_req.append(self.dec_pre)
                decel_actual.append(0)
            elif (time[i]>=prefill_ramp_1 and time[i]<=prefill_reach_1-1):
                decel_req.append(decel_req[-1])
                decel_actual.append(decel_actual[-1]+sim_dt/1000*pre_vramp)
            elif (time[i]>=prefill_reach_1 and time[i]<=part_lat_1-1):
                decel_req.append(decel_req[-1])
                decel_actual.append(decel_actual[-1])
            elif (time[i]>=part_lat_1 and time[i]<=part_ramp_1-1):
                decel_req.append(self.dec_part)
                decel_actual.append(decel_actual[-1])
            elif (time[i]>=part_ramp_1 and time[i]<=part_reach_1-1):
                decel_req.append(decel_req[-1])
                decel_actual.append(decel_actual[-1]+sim_dt/1000*part_vramp)
            elif (time[i]>=part_reach_1 and time[i]<=full_lat_1-1):
                decel_req.append(decel_req[-1])
                decel_actual.append(decel_actual[-1])
            elif (time[i]>=full_lat_1 and time[i]<=full_ramp_1-1):
                decel_req.append(self.dec_full)
                decel_actual.append(decel_actual[-1])
            elif (time[i]>=full_ramp_1-1 and time[i]<=full_reach_1-1):
                decel_req.append(decel_req[-1])
                decel_actual.append(decel_actual[-1]+sim_dt/1000*full_vramp)
            elif(time[i]>=full_reach_1 and time[i]<=postaeb_1-1):
                decel_req.append(decel_req[-1])
                decel_actual.append(decel_actual[-1])
            else:
                decel_req.append(0)
                decel_actual.append(0)
            if v_host[-1]>0:
                v_host.append(v_host[-1]-decel_actual[-1]*sim_dt/1000)
            else:
                v_host.append(0)
            if (time[i]<pre_start_t):
                dist.append(dist[-1])
            else:
                dist.append(dist[-1]+v_host[-1]*sim_dt/1000)
            # print(f"#{i}: dec={decel_actual[-1]},v={v_host[-1]},s={dist[-1]}")
        self.output_aeb2_dist.setText(str(round(dist[-1],3)))
        self.aeb_timeline=time
        self.aeb_decel_req=decel_req
        self.aeb_decel_actual=decel_actual
        self.aeb_v=v_host
        self.aeb_dist=dist

