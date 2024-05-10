from .. import common
import numpy as np
import wilson

class W(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\mathcal{W}'
        self.gl = common.Coupling(scale, 'll', 0, r'g_\mathcal{B}^\ell', dtype=float)
        self.gq = common.Coupling(scale, 'qq', 0, r'g_\mathcal{B}^q', dtype=float)
        self.couplings = [self.gl, self.gq]
        
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
                            f'lq1_{i}{j}{k}{l}': -self.gq[k-1, l-1]*self.gl[i-1, j-1]/(4*self.mass**2)}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)