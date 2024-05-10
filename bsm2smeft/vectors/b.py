from .. import common
import numpy as np
import wilson

class B(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\mathcal{B}'
        self.gl = common.Coupling(scale, 'll', 0, r'g_\mathcal{B}^\ell', dtype=float)
        self.ge = common.Coupling(scale, 'ee', 0, r'g_\mathcal{B}^\e', dtype=float)
        self.gq = common.Coupling(scale, 'qq', 0, r'g_\mathcal{B}^q', dtype=float)
        self.gd = common.Coupling(scale, 'dd', 0, r'g_\mathcal{B}^d', dtype=float)
        self.couplings = [self.gl, self.ge, self.gq, self.gd]
        
    def match(self) -> wilson.Wilson:
        wc = {}
        for i in range(1,4):
            for j in range(i,4):
                for k in range(1,4):
                    if i == j:
                        s = k                            
                    else:
                        s = 1
                    for l in range(s,4):
                        wc |= {
                            f'lq1_{i}{j}{k}{l}': -self.gq[k-1, l-1]*self.gl[i-1, j-1]/self.mass**2,
                            f'ed_{i}{j}{k}{l}': -self.gd[k-1, l-1]*self.ge[i-1, j-1]/self.mass**2,
                            f'ld_{i}{j}{k}{l}': -self.gd[k-1, l-1]*self.gl[i-1, j-1]/self.mass**2, 
                            f'qe_{i}{j}{k}{l}': -self.gq[i-1, j-1]*self.ge[k-1, l-1]/self.mass**2}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)