# Scalars

## $\varphi \sim (1, 2)_{1/2}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(y_{\varphi}^e)_{ij}$ | $\varphi^\dagger \bar{e}_{Ri} \ell_{Lj}$ | 0 | No | $(Y_e^\dagger)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `phi.ye[i,j]` |
| $(y_{\varphi}^d)_{ij}$ | $\varphi^\dagger \bar{d}_{Ri} q_{Lj}$ | 0 | No | $(Y_d^\dagger)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `phi.yd[i,j]` |
| $(y_{\varphi}^u)_{ij}$ | $\varphi^\dagger i \sigma_2 \bar{q}^T_{Li} u_{Rj}$ | 0 | No | $(Y_u)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `phi.yu[i,j]` |

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell e d q})_{ijkl}$ | $\frac{(y_{\varphi}^e)^*_{ji} (y_{\varphi}^d)_{kl}}{M_{\varphi}^2}$ |
|$(C_{\ell e q u(1)})_{ijkl}$ | $\frac{(y_{\varphi}^e)^*_{ji} (y_{\varphi}^u)_{kl}}{M_{\varphi}^2}$ |

## $\omega_1 \sim (3, 3)_{-1/3}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(y_{\omega_1}^{q\ell})_{ij}$ | $\omega_1^\dagger \bar{q}_{Li}^c i \sigma_2 \ell_{Lj}$ | 0 | No | $(Y_u^* Y_e^\dagger)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `omega1.yql[i,j]` |
| $(y_{\omega_1}^{eu})_{ij}$ | $\omega_1^\dagger \bar{e}_{Ri}^c u_{Rj}$ | 0 | No | $\delta_{ij}$ | $\delta_{i3}\delta_{j3}$ | `omega1.yeu[i,j]` |

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell q(1)})_{ijkl}$ | $\frac{(y_{\omega_1}^{q\ell})^*_{ki} (y_{\omega_1}^{q\ell})_{lj}}{4 M_{\omega_1}^2}$ |
|$(C_{\ell q(3)})_{ijkl}$ | $-\frac{(y_{\omega_1}^{q\ell})^*_{ki} (y_{\omega_1}^{q\ell})_{lj}}{4 M_{\omega_1}^2}$ |
|$(C_{\ell equ(1)})_{ijkl}$ | $\frac{(y_{\omega_1}^{q\ell})^*_{ki} (y_{\omega_1}^{eu})_{lj}}{M_{\omega_1}^2}$ |
|$(C_{\ell equ(3)})_{ijkl}$ | $-\frac{(y_{\omega_1}^{q\ell})^*_{ki} (y_{\omega_1}^{eu})_{lj}}{8 M_{\omega_1}^2}$ |

## $\omega_4 \sim (3, 1)_{-4/3}$

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(y_{\omega_4}^{ed})_{ij}$ | $\omega_4^\dagger \bar{e}_{Ri}^c d_{Rj}$ | 0 | No | $(Y_d^\dagger Y_u)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `omega4.yed[i,j]` |

### Matching

| WC | Matching |
|----|----------|
|$(C_{ed})_{ijkl}$ | $\frac{(y_{\omega_4}^{ed})^*_{ik} (y_{\omega_4}^{ed})_{jl}}{4 M_{\omega_4}^2}$ |

## $\Pi_1 \sim (3,2)_{1/6}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(y_{\Pi_1})_{ij}$ | $\Pi_1^\dagger i \sigma_2 \bar{\ell}_{Li}^T  d_{Rj}$ | 0 | No | $(Y_d^T Y_u^*)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `pi1.y[i,j]` |

### Matching

| WC | Matching |
|----|----------|
|$(C_{ed})_{ijkl}$ | $-\frac{(y_{\Pi_1})^*_{jk} (y_{\Pi_1})_{il}}{2 M_{\Pi_1}^2}$ |

## $\Pi_7 \sim (3,2)_{7/6}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(y_{\Pi_7}^{eq})_{ij}$ | $\Pi_7^\dagger  \bar{e}_{Ri}  q_{Lj}$ | 0 | No | $(Y_e^\dagger Y_u^\dagger)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `pi7.yeq[i,j]` |
| $(y_{\Pi_7}^{\ell u})_{ij}$ | $\Pi_7^\dagger i \sigma_2 \bar{\ell}^T_{Li}  u_{Rj}$ | 0 | No | $\delta_{ij}$ | $\delta_{i3}\delta_{j3}$ | `pi7.yul[i,j]` |

### Matching

| WC | Matching |
|----|----------|
|$(C_{qe})_{ijkl}$ | $-\frac{(y_{\Pi_7}^{eq})^*_{li} (y_{\Pi_7}^{eq})_{kj}}{2 M_{\Pi_7}^2}$ |
|$(C_{\ell equ(1)})_{ijkl}$ | $\frac{(y_{\Pi_7}^{eq})^*_{jk} (y_{\Pi_7}^{\ell u})_{il}}{2 M_{\Pi_7}^2}$ |
|$(C_{\ell equ(3)})_{ijkl}$ | $\frac{(y_{\Pi_7}^{eq})^*_{jk} (y_{\Pi_7}^{\ell u})_{il}}{8 M_{\Pi_7}^2}$ |

## $\zeta \sim (3,3)_{-1/3}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(y_{\zeta}^{q\ell})_{ij}$ | $\zeta_a^\dagger \bar{q}_{Li}^c i \sigma_2 \sigma^a \ell_{Lj}$ | 0 | No | $(Y_u^* Y_e^\dagger)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `zeta.yql[i,j]` |


### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell q(1)})_{ijkl}$ | $3\frac{(y_{\zeta}^{q\ell})^*_{ki} (y_{\zeta}^{q\ell})_{lj}}{4 M_{\zeta}^2}$ |
|$(C_{\ell q(3)})_{ijkl}$ | $\frac{(y_{\zeta}^{q\ell})^*_{ki} (y_{\zeta}^{q\ell})_{lj}}{4 M_{\zeta}^2}$ |