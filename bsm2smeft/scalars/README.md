# Scalars

## $\mathcal{S} \equiv (1,1)_0$

### Lagrangian

#### Dim <= 4

|Coefficient | Operator | Dim | Rank | Real |
|----------|-----------|-----------|---------|--------|
| $(\kappa_\mathcal{S})_r$  | $\mathcal{S}_r \phi^\dagger \phi$| 1 | $n_\mathcal{S}$ | Yes |
|$(\lambda_\mathcal{S})_{rs}$ | $\mathcal{S}_r \mathcal{S}_s \phi^\dagger \phi$| 0 | $n_\mathcal{S}\times n_\mathcal{S}$ | Yes |
| $(\kappa_{\mathcal{S}^3})_{rst}$ | $\mathcal{S}_r\mathcal{S}_r \mathcal{S}_t$ | 1 | $n_\mathcal{S}\times n_\mathcal{S} \times n_\mathcal{S}$ | Yes |

#### Dim = 5

|Coefficient | Operator | Dim | Rank | Real |
|----------|-----------|-----------|-------|--------|
| $(\tilde{k}_\mathcal{S}^\phi)_r$ | $\mathcal{S}_r D_\mu \phi^\dagger D^\mu \phi$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{\lambda}_\mathcal{S})_r$| $\mathcal{S}_r |\phi|^4$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{k}_\mathcal{S}^B)_r$ | $\mathcal{S}_r B_{\mu\nu} B^{\mu\nu}$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{k}_\mathcal{S}^W)_r$ | $\mathcal{S}_r W^a_{\mu\nu} W^{a\,\mu\nu}$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{k}_\mathcal{S}^G)_r$ | $\mathcal{S}_r G^A_{\mu\nu} G^{A\,\mu\nu}$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{k}_\mathcal{S}^\tilde{B})_r$ | $\mathcal{S}_r B_{\mu\nu} \tilde{B}^{\mu\nu}$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{k}_\mathcal{S}^\tilde{W})_r$ | $\mathcal{S}_r W^a_{\mu\nu} \tilde{W}^{a\,\mu\nu}$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{k}_\mathcal{S}^\tilde{G})_r$ | $\mathcal{S}_r G^A_{\mu\nu} \tilde{G}^{A\,\mu\nu}$ | 0 | $n_\mathcal{S}$ | Yes |
| $(\tilde{y}^e_\mathcal{S})_{rij}$ | $\mathcal{S}_r \bar{e}_{Ri} \phi^\dagger l_{Lj}$ | 0 | $n_\mathcal{S} \times 3 \times 3$| No |
| $(\tilde{y}^d_\mathcal{S})_{rij}$ | $\mathcal{S}_r \bar{d}_{Ri} \phi^\dagger q_{Lj}$ | 0 | $n_\mathcal{S} \times 3 \times 3$| No |
| $(\tilde{y}^u_\mathcal{S})_{rij}$ | $\mathcal{S}_r \bar{u}_{Ri} \tilde{\phi}^\dagger q_{Lj}$ | 0 | $n_\mathcal{S} \times 3 \times 3$| No |

### SMEFT Matching

|WC | Matching |
|----|---------|
|$C_{\phi}$ | $-\frac{(\lambda_\mathcal{S})_{rs} (\kappa_\mathcal{S})_r(\kappa_\mathcal{S})_s}{M_{\mathcal{S}_r}^2 M_{\mathcal{S}_s}^2} + \frac{(\kappa_{\mathcal{S}^3})_{rst} (\kappa_\mathcal{S})_r (\kappa_\mathcal{S})_s (\kappa_\mathcal{S})_t}{M_{\mathcal{S}_r}^2 M_{\mathcal{S}_s}^2 M_{\mathcal{S}_t}^2} + \frac{2 \lambda_\phi (\tilde{k}_\mathcal{S}^\phi)_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$|
|$C_{\phi\square}$| $-\frac{(\kappa_\mathcal{S})_r(\kappa_\mathcal{S})_r}{2 M_{\mathcal{S}_r}^4} + \frac{(\tilde{k}_\mathcal{S}^\phi)_r(\kappa_\mathcal{S})_r}{2f M_{\mathcal{S}_r}^2}$ |
|$C_{\phi B}$ | $\frac{(\tilde{k}_\mathcal{S}^B)_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$ |
|$C_{\phi \tilde{B}}$ | $\frac{(\tilde{k}_\mathcal{S}^\tilde{B})_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$ |
|$C_{\phi W}$ | $\frac{(\tilde{k}_\mathcal{S}^W)_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$ |
|$C_{\phi \tilde{W}}$ | $\frac{(\tilde{k}_\mathcal{S}^\tilde{W})_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$ |
|$C_{\phi G}$ | $\frac{(\tilde{k}_\mathcal{S}^G)_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$ |
|$C_{\phi \tilde{G}}$ | $\frac{(\tilde{k}_\mathcal{S}^\tilde{G})_r (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$ |
|$(C_{e\phi})_{ij}$| $y^{e*}_{ji} \frac{(\tilde{k}_\mathcal{S}^\phi)_r (\kappa_\mathcal{S})_r}{2f M_{\mathcal{S}_r}^2} + \frac{(\tilde{y}^e_\mathcal{S})_{rji}^* (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$|
|$(C_{d\phi})_{ij}$| $y^{d*}_{ji} \frac{(\tilde{k}_\mathcal{S}^\phi)_r (\kappa_\mathcal{S})_r}{2f M_{\mathcal{S}_r}^2} + \frac{(\tilde{y}^d_\mathcal{S})_{rji}^* (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$|
|$(C_{u\phi})_{ij}$| $y^{u*}_{ji} \frac{(\tilde{k}_\mathcal{S}^\phi)_r (\kappa_\mathcal{S})_r}{2f M_{\mathcal{S}_r}^2} + \frac{(\tilde{y}^u_\mathcal{S})_{rji}^* (\kappa_\mathcal{S})_r}{f M_{\mathcal{S}_r}^2}$|