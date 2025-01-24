# ANN models for ship response transfer functions
Trained Artificial Neural Network (ANN) models for transfer function computation of wave-indcued ship responses.
The present ANN has been trained based on a linear strip thepry, so-called the New Strip Method (Takagi and Ganno [1]), in which the Lewis form approximation of ship cross-sections is adopted.
For more detail, refer to Takami et al. [2].

# 1. Input

Input values are:
- Ship length $L$ (m)
- Ship breadth $B$ (m)
- Draught $T$ (m)
- Ship speed $V$ (m/s)
- Shape parameter $\gamma$
- Relative wave direction $\beta$ (deg) (NB: head seas is $\beta=180$)　
- Logarithmic value of wavelength/ship length ratio (i.e. $\kappa$=`log10(λ/L)`), where $\lambda$ denotes the wavelength

The shape parameter $\gamma$ has a one-to-one relationship with Block coefficient $C_b$, see the figure below and ref. [2].
![gamma](https://github.com/user-attachments/assets/dd022ca7-df62-4186-88a6-f2af1b3184b1)

Note that before making prediction by ANN, each value should be normalized by (e.g. ship length $L$):
$\hat{L} = \frac{2 \left( L - \min\{L\} \right)}{\max\{L\} - \min\{L\}} - 1$

The min&max values for each parameter are shown in the table below.  

|  | $L$ (m) | $B$ (m) | $T$ (m) | $V$ (m/s)| $\gamma$  | $\beta$ (deg) |$\kappa$ |
|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
|Min| 100       | 10      | 5       |0       |0.7       |-180       |-1       |
|Max| 400      | 50       | 30       |30       |1.3       |180       |1       |

# 2. Output

Output values are:
- Heave amplitude (by my_model_heaveamp.keras)
- Heave phase (by my_model_heavephase.keras)
- Pitch amplitude (by my_model_pitchamp.keras)
- Pitch phase (by my_model_pitchphase.keras)
- Vertical Bending Moment (VBM) amplitude (amidships, by my_model_vbmamp.keras)
- VBM phase (amidships, by my_model_vbmphase.keras)

## Amplitude
Amplitude outputs by ANN have been normalized within [-1 1]. To revert to the actual values, the min&max values in the table below can be used.

|  | Heave (m/m)| Pitch (deg/m)| VBM | 
|---------------|---------------|---------------|---------------|
|Min| 8.82E-10       | 1.44E-08      | 0.000156591       |
|Max| 2      | 1       | 0.25     |

To get the VBM amplitude in (Nm/m) from the non-normalized value M, the following calculation should be made:
$M_v$ = $M^2 * B * L^2 * g$

where g denotes the gravitational acceleration ($m/s^2$).


