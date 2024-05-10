# Vectors

## $\mathcal{B} \sim (1, 1)_0$


### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
|$(g_\mathcal{B}^\ell)_{ij}$ | $\mathcal{B}^\mu \bar{\ell}_{Li} \gamma_\mu \ell_{Lj}$ | 0 | Yes | $\delta_{ij}$ |  $\delta_{i3}\delta_{j3}$ | `B.gl[i,j]` 
|$(g_\mathcal{B}^q)_{ij}$ | $\mathcal{B}^\mu \bar{q}_{Li} \gamma_\mu q_{Lj}$ | 0 | Yes | $\delta_{ij}$ |  $\delta_{i3}\delta_{j3}$ | `B.gq[i,j]` 
|$(g_\mathcal{B}^d)_{ij}$ | $\mathcal{B}^\mu \bar{d}_{Ri} \gamma_\mu d_{Rj}$ | 0 | Yes | $\delta_{ij}$ |  $\delta_{i3}\delta_{j3}$ | `B.gq[i,j]` 
|$(g_\mathcal{B}^e)_{ij}$ | $\mathcal{B}^\mu \bar{e}_{Ri} \gamma_\mu e_{Rj}$ | 0 | Yes | $\delta_{ij}$ |  $\delta_{i3}\delta_{j3}$ | `B.gq[i,j]` 

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell q(1)})_{ijkl}$ | $-\frac{(g_\mathcal{B}^q)_{kl} (g_\mathcal{B}^\ell)_{ij}}{M_\mathcal{B}^2}$ |
|$(C_{ed})_{ijkl}$ | $-\frac{(g_\mathcal{B}^d)_{kl} (g_\mathcal{B}^e)_{ij}}{M_\mathcal{B}^2}$ |
|$(C_{\ell d})_{ijkl}$ | $-\frac{(g_\mathcal{B}^d)_{kl} (g_\mathcal{B}^\ell)_{ij}}{M_\mathcal{B}^2}$ |
|$(C_{qe})_{ijkl}$ | $-\frac{(g_\mathcal{B}^e)_{kl} (g_\mathcal{B}^q)_{ij}}{M_\mathcal{B}^2}$ |

## $\mathcal{W} \sim (1, 3)_0$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
|$(g_\mathcal{W}^\ell)_{ij}$ | $\frac{1}{2}\mathcal{W}_a^\mu \bar{\ell}_{Li} \sigma^a \gamma_\mu \ell_{Lj}$ | 0 | Yes | $\delta_{ij}$ |  $\delta_{i3}\delta_{j3}$ | `W.gl[i,j]` 
|$(g_\mathcal{W}^q)_{ij}$ | $\frac{1}{2}\mathcal{W}_a^\mu \bar{q}_{Li}\sigma_a \gamma_\mu q_{Lj}$ | 0 | Yes | $\delta_{ij}$ |  $\delta_{i3}\delta_{j3}$ | `W.gq[i,j]` 

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell q(3)})_{ijkl}$ | $-\frac{(g_\mathcal{W}^q)_{kl} (g_\mathcal{W}^\ell)_{ij}}{4M_\mathcal{B}^2}$ |

## $\mathcal{U}_2 \sim (3, 1)_{2/3}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
|$(g_{\mathcal{U}_2}^{ed})_{ij}$| $\mathcal{U}_2^{\mu\dagger}\bar{e}_{Ri} \gamma_\mu d_{Rj}$ | 0 | No | $(Y_d^\dagger Y_u)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `U2.ged[i,j]`
|$(g_{\mathcal{U}_2}^{\ell q})_{ij}$| $\mathcal{U}_2^{\mu\dagger}\bar{\ell}_{Li} \gamma_\mu q_{Lj}$ | 0 | No | $(Y_e Y_u^T)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `U2.glq[i,j]`

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell q(1)})_{ijkl}$ | $-\frac{(g_{\mathcal{U}_2}^{\ell q})^*_{jk} (g_{\mathcal{U}_2}^{\ell q})_{il}}{2M_{\mathcal{U}_2}^2}$ |
|$(C_{\ell q(3)})_{ijkl}$ |$-\frac{(g_{\mathcal{U}_2}^{\ell q})^*_{jk} (g_{\mathcal{U}_2}^{\ell q})_{il}}{2M_{\mathcal{U}_2}^2}$ |
|$(C_{ed})_{ijkl}$ |$-\frac{(g_{\mathcal{U}_2}^{ed})^*_{jk} (g_{\mathcal{U}_2}^{ed})_{il}}{M_{\mathcal{U}_2}^2}$ |
|$(C_{\ell edq})_{ijkl}$ |$2\frac{(g_{\mathcal{U}_2}^{ed})^*_{jk} (g_{\mathcal{U}_2}^{\ell q})_{il}}{M_{\mathcal{U}_2}^2}$ |

## $\mathcal{X} \sim (3,3)_{2/3}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
| $(g_\mathcal{X})_{ij}$ | $\frac{1}{2}\mathcal{X}^{a\mu\dagger} \bar{\ell}_{Li}\gamma_\mu \sigma^a q_{Lj}$ | 0 | No | $(Y_e Y_u^T)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `X.g[i,j]` |

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell q(1)})_{ijkl}$ | $-3\frac{(g_\mathcal{X})^*_{jk} (g_\mathcal{X})_{il}}{8 M_{\mathcal{X}}^2}$ |
|$(C_{\ell q(3)})_{ijkl}$ | $\frac{(g_\mathcal{X})^*_{jk} (g_\mathcal{X})_{il}}{8 M_{\mathcal{X}}^2}$ |

## $\mathcal{Q}_5 \sim (3, 2)_{-5/6}$

### Parameters

| Parameter | Operator | dim | Real | MFV | $U(2)^5$ | Implementation |
|-----------|----------|-----|-----|-----|----------|----------------|
|$(g_{\mathcal{Q}_5}^{d\ell})_{ij}$| $\mathcal{Q}_5^{\mu\dagger}\bar{d}^c_{Ri} \gamma_\mu \ell_{Lj}$ | 0 | No | $(Y_u^T Y_d^*)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `Q5.gdl[i,j]`
|$(g_{\mathcal{Q}_5}^{eq})_{ij}$| $\mathcal{Q}_5^{\mu\dagger}\bar{e}^c_{Ri} \gamma_\mu q_{Lj}$ | 0 | No | $(Y_e^T Y_u^T)_{ij}$ | $\delta_{i3}\delta_{j3}$ | `Q5.geq[i,j]`

### Matching

| WC | Matching |
|----|----------|
|$(C_{\ell d})_{ijkl}$ | $\frac{(g_{\mathcal{Q}_5}^{d\ell})^*_{ki} (g_{\mathcal{Q}_5}^{d\ell})_{lj}}{M_{\mathcal{Q}_5}^2}$ |
|$(C_{qe})_{ijkl}$ | $\frac{(g_{\mathcal{Q}_5}^{eq})^*_{ki} (g_{\mathcal{Q}_5}^{eq})_{lj}}{M_{\mathcal{Q}_5}^2}$ |
|$(C_{\ell edq})_{ijkl}$ | $-2\frac{(g_{\mathcal{Q}_5}^{d\ell})^*_{ki} (g_{\mathcal{Q}_5}^{eq})_{lj}}{M_{\mathcal{Q}_5}^2}$ |