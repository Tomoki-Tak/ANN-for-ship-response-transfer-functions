import numpy as np
import math
from tensorflow.keras.models import load_model

# Load models
modelha = load_model('my_model_heaveamp.keras')
modelhp = load_model('my_model_heavephase.keras')
modelpa = load_model('my_model_pitchamp.keras')
modelpp = load_model('my_model_pitchphase.keras')
modelva = load_model('my_model_vbmamp.keras')
modelvp = load_model('my_model_vbmphase.keras')

# Input parameters
x_input = np.loadtxt('xtest.txt')  

# Min&max
hmax=2.
hmin=0.
pmax=1
pmin=0.
vmax=0.25
vmin=0.0

# Prediction
y_pred_ha = modelha.predict(x_input)
y_pred_hp = modelhp.predict(x_input)
y_pred_pa = modelpa.predict(x_input)
y_pred_pp = modelpp.predict(x_input)
y_pred_va = modelva.predict(x_input)
y_pred_vp = modelvp.predict(x_input)

hamp = (y_pred_ha+1.)*(hmax-hmin)/2.+hmin
hamp[hamp < 0] = 0
hamp[np.abs(x_input[:, 6]) >= 1] = 0 
hamp[x_input[:, 6] >= 1] = 1
hphase = np.arctan2(y_pred_hp[:, 1], y_pred_hp[:, 0])
pamp = (y_pred_pa+1.)*(pmax-pmin)/2.+pmin
pamp[pamp < 0] = 0
pamp[np.abs(x_input[:, 6]) >= 1] = 0 
pphase = np.arctan2(y_pred_pp[:, 1], y_pred_pp[:, 0])
vamptmp = (y_pred_va+1.)*(vmax-vmin)/2.+vmin
vamptmp_flat = vamptmp.flatten()
vamp = vamptmp_flat**2 * 9.80665 * ((x_input[:, 1] + 1.) * (50. - 10.) / 2. + 10.) * ((x_input[:, 0] + 1.) * (400. - 100.) / 2. + 100.)**2 / 1000.
vamp[np.abs(x_input[:, 6]) >= 1] = 0 
vamp[vamp < 0] = 0
vphase = np.arctan2(y_pred_vp[:, 1], y_pred_vp[:, 0])

data = np.column_stack((hamp, hphase, pamp, pphase, vamp, vphase))
np.savetxt('ypred.txt', data, delimiter=',')
