from common_func import isnum
import numpy as np

r2d = 1 / np.pi * 180
d2r = 1 / 180 * np.pi
c_speed = 299792458

def age_unitconv(self):
    item = self.comboBox_age.currentText()
    temp = self.lineEdit_age.text()
    if isnum(temp):
        age_input = float(temp)
        if item == "Year(s)":
            self.label_ageresulty.setText(temp)
            self.label_ageresultm.setText(str(age_input * 12))
            self.label_ageresultd.setText(str(age_input * 365))
        elif item == "Month(s)":
            self.label_ageresulty.setText(str(round(age_input / 12, 3)))
            self.label_ageresultm.setText(temp)
            self.label_ageresultd.setText(str(age_input * 30))
        else:
            self.label_ageresulty.setText(str(round(age_input / 365, 3)))
            self.label_ageresultm.setText(str(round(age_input / 30, 3)))
            self.label_ageresultd.setText(temp)
    else:
        self.label_ageresulty.setText('Invalid input')
        self.label_ageresultm.setText('Invalid input')
        self.label_ageresultd.setText('Invalid input')


def speed_unitconv(self):
    item = self.comboBox_speed.currentText()
    temp = self.lineEdit_speed.text()
    if isnum(temp):
        speed_input = float(temp)
        if item == "kph":
            self.label_speedkph.setText(temp)
            self.label_speedms.setText(str(round(speed_input / 3.6, 3)))
            self.label_speedmph.setText(str(round(speed_input / 1.609344, 3)))
        elif item == "m/s":
            self.label_speedkph.setText(str(round(speed_input * 3.6, 3)))
            self.label_speedms.setText(temp)
            self.label_speedmph.setText(str(round(speed_input * 3.6 / 1.609344, 3)))
        else:
            self.label_speedkph.setText(str(round(speed_input * 1.609344, 3)))
            self.label_speedms.setText(str(round(speed_input * 1.609344 / 3.6, 3)))
            self.label_speedmph.setText(temp)
    else:
        self.label_speedkph.setText('Invalid input')
        self.label_speedms.setText('Invalid input')
        self.label_speedmph.setText('Invalid input')

def angle_unitconv(self):
    item = self.comboBox_angleunit.currentText()
    item2 = self.comboBox_trigonometry.currentText()
    temp = self.lineEdit_angle.text()
    if isnum(temp):
        angle_input = float(temp)
        if item == "Degree":
            angle_result = angle_input * d2r
            self.label_angleunitresult.setText(str(round(angle_result, 3)))
            self.label_angleunit.setText(str('Rad'))
            self.label_angleunitresult_2.setText(str(round(angle_input, 3))+" deg")
            if item2 == 'Sin':
                trig_result = np.sin(angle_result)
                self.label_angletrigresult.setText(str(round(trig_result, 3)))
            elif item2 == 'Cos':
                trig_result = np.cos(angle_result)
                self.label_angletrigresult.setText(str(round(trig_result, 3)))
            else:
                trig_result = np.tan(angle_result)
                self.label_angletrigresult.setText(str(round(trig_result, 3)))
        else:
            angle_result = angle_input * r2d
            self.label_angleunitresult.setText(str(round(angle_result, 3)))
            self.label_angleunit.setText(str('Degree'))
            self.label_angleunitresult_2.setText(str(round(angle_input, 3))+" rad")
            if item2 == 'Sin':
                trig_result = np.sin(angle_input)
                self.label_angletrigresult.setText(str(round(trig_result, 3)))
            elif item2 == 'Cos':
                trig_result = np.cos(angle_input)
                self.label_angletrigresult.setText(str(round(trig_result, 3)))
            else:
                trig_result = np.tan(angle_input)
                self.label_angletrigresult.setText(str(round(trig_result, 3)))
    else:
        self.label_angleunitresult.setText('Invalid input')
        self.label_angletrigresult.setText('Invalid input')

def dbsm_unitconv(self):
    item = self.comboBox_dBsm.currentText()
    temp = self.lineEdit_dBsm.text()
    if isnum(temp):
        dbsm_input = float(temp)
        if item == "dBsm":
            dbsm_result = np.power(10, dbsm_input / 10)
            self.label_dBsmresult.setText(str(round(dbsm_result, 3)))
            self.label_dbsmunit.setText(str('m^2'))
        else:
            if dbsm_input < 0:
                self.label_dBsmresult.setText('Invalid input')
                self.label_dBsmresult.setText('Invalid input')
            else:
                dbsm_result = 10 * np.log10(dbsm_input)
                self.label_dBsmresult.setText(str(round(dbsm_result, 3)))
                self.label_dbsmunit.setText(str('dBsm'))
    else:
        self.label_dBsmresult.setText('Invalid input')
        self.label_dBsmresult.setText('Invalid input')

def freq_unitconv(self):
    item = self.comboBox_freq.currentText()
    temp = self.lineEdit_freqinput.text()
    if isnum(temp):
        freq_input = float(temp)
        if freq_input > 0:
            if item == "GHz":
                freq_hz=freq_input * 1e9
                freq_s = 1 / (freq_input * 1e9)
                freq_ms = freq_s * 1e3
                freq_us = freq_ms * 1e3
                freq_ns = freq_us * 1e3
                self.label_freq_hz.setText(str('%.3e' % freq_hz))
                self.label_freq_s.setText(str('%.3e' % freq_s))
                self.label_freq_ms.setText(str('%.3e' % freq_ms))
                self.label_freq_us.setText(str('%.3e' % freq_us))
                self.label_freq_ns.setText(str('%.3e' % freq_ns))
                freqlambda_m = c_speed / (freq_input * 1e9)
                freqlambda_mm = freqlambda_m * 1e3
                self.label_freqlambda_m.setText(str('%.3e' % freqlambda_m))
                self.label_freqlambda_mm.setText(str('%.3e' % freqlambda_mm))
            elif item == 'MHz':
                freq_hz=freq_input * 1e6
                freq_s = 1 / (freq_input * 1e6)
                freq_ms = freq_s * 1e3
                freq_us = freq_ms * 1e3
                freq_ns = freq_us * 1e3
                self.label_freq_hz.setText(str('%.3e' % freq_hz))
                self.label_freq_s.setText(str('%.3e' % freq_s))
                self.label_freq_ms.setText(str('%.3e' % freq_ms))
                self.label_freq_us.setText(str('%.3e' % freq_us))
                self.label_freq_ns.setText(str('%.3e' % freq_ns))
                freqlambda_m = c_speed / (freq_input * 1e6)
                freqlambda_mm = freqlambda_m * 1e3
                self.label_freqlambda_m.setText(str('%.3e' % freqlambda_m))
                self.label_freqlambda_mm.setText(str('%.3e' % freqlambda_mm))
            else:
                freq_hz=freq_input * 1e3
                freq_s = 1 / (freq_input * 1e3)
                freq_ms = freq_s * 1e3
                freq_us = freq_ms * 1e3
                freq_ns = freq_us * 1e3
                self.label_freq_hz.setText(str('%.3e' % freq_hz))
                self.label_freq_s.setText(str('%.3e' % freq_s))
                self.label_freq_ms.setText(str('%.3e' % freq_ms))
                self.label_freq_us.setText(str('%.3e' % freq_us))
                self.label_freq_ns.setText(str('%.3e' % freq_ns))
                freqlambda_m = c_speed / (freq_input * 1e3)
                freqlambda_mm = freqlambda_m * 1e3
                self.label_freqlambda_m.setText(str('%.3e' % freqlambda_m))
                self.label_freqlambda_mm.setText(str('%.3e' % freqlambda_mm))
        elif freq_input == 0:
            self.label_freq_hz.setText('0')
            self.label_freq_s.setText('inf ')
            self.label_freq_ms.setText('inf ')
            self.label_freq_us.setText('inf ')
            self.label_freq_ns.setText('inf ')
            self.label_freqlambda_m.setText('inf ')
            self.label_freqlambda_mm.setText('inf ')
        else:
            self.label_freq_hz.setText('Invalid input')
            self.label_freq_s.setText('Invalid input')
            self.label_freq_ms.setText('Invalid input')
            self.label_freq_us.setText('Invalid input')
            self.label_freq_ns.setText('Invalid input')
            self.label_freqlambda_m.setText('Invalid input')
            self.label_freqlambda_mm.setText('Invalid input')
    else:
        self.label_freq_hz.setText('Invalid input')
        self.label_freq_s.setText('Invalid input')
        self.label_freq_ms.setText('Invalid input')
        self.label_freq_us.setText('Invalid input')
        self.label_freq_ns.setText('Invalid input')
        self.label_freqlambda_m.setText('Invalid input')
        self.label_freqlambda_mm.setText('Invalid input')

def power_unitconv(self):
    item = self.comboBox_power.currentText()
    temp = self.lineEdit_powerinput.text()
    if isnum(temp):
        power_input = float(temp)
        if item == "dBm":
            self.label_powerdbm.setText(temp)
            power_resultmw = np.power(10, power_input / 10)
            self.label_powermw.setText(str(round(power_resultmw, 3)))
            self.label_powerw.setText(str(round(power_resultmw / 1e3, 6)))
        elif item == "mW":
            if power_input != 0:
                self.label_powermw.setText(temp)
                power_resultdbm = 10 * np.log10(power_input)
                self.label_powerdbm.setText(str(round(power_resultdbm, 3)))
                self.label_powerw.setText(str(round(power_input / 1e3, 6)))
            else:
                self.label_powermw.setText(temp)
                self.label_powerdbm.setText(str('inf'))
                self.label_powerw.setText(str(round(power_input / 1e3, 6)))
        else:
            if power_input != 0:
                self.label_powerw.setText(temp)
                power_resultdbm = 10 * np.log10(power_input) + 30
                self.label_powerdbm.setText(str(round(power_resultdbm, 3)))
                self.label_powermw.setText(str(round(power_input * 1e3, 6)))
            else:
                self.label_powerw.setText(temp)
                self.label_powerdbm.setText(str('inf'))
                self.label_powermw.setText(str(round(power_input * 1e3, 6)))
    else:
        self.label_powerdbm.setText('Invalid input')
        self.label_powermw.setText('Invalid input')
        self.label_powerw.setText('Invalid input')