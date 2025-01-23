# ANN models for ship response transfer functions
Trained Artificial Neural Network (ANN) models for transfer function computation of wave-indcued ship responses.
The ANN has been trained based on a linear strip thepry, so-called the New Strip Method (Takagi and Ganno [1]), in which the Lewis form approximation of ship cross-sections is adopted.
For more detail, refer to Takami et al. [2].

Input values:
- Ship length $L$ (m)
- Ship breadth $B$ (m)
- Draught $T$ (m)
- Ship speed $V$ (m/s)
- Shape parameter $\gamma$
- Relative wave direction $\beta$ (deg)
- Logarithmic value of wavelength/ship length ratio (i.e. $\log_{10}\left(\lambda/L\right)$), where $\lambda$ denotes the wavelength
