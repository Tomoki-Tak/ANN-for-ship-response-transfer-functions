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
- Relative wave direction $\beta$ (deg) (NB: head seas is $\beta=180$)　
- Logarithmic value of wavelength/ship length ratio (i.e. $\kappa$=`log10(λ/L)`), where $\lambda$ denotes the wavelength

The shape parameter $\gamma$ has a one-to-one relationship with Block coefficient $C_b$, see the figure below and ref. [2].
![gamma](https://github.com/user-attachments/assets/dd022ca7-df62-4186-88a6-f2af1b3184b1)

Note that before making prediction by ANN, each value should be normalized by (e.g. ship length $L$):
$\hat{L} = \frac{2 \left( L - \min\{L\} \right)}{\max\{L\} - \min\{L\}} - 1$

|  | $L$ (m) | $B$ (m) | $T$ (m) | $V$ | $\gamma$  | $\beta$ (deg) |$\kappa$ |
|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
|Min| 100       | データ2       | データ3       |データ3       |データ3       |データ3       |データ3       |
|Max| 400      | データ5       | データ6       |データ3       |データ3       |データ3       |データ3       |
