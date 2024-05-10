from .. import common
import numpy as np
import wilson

class X(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\mathcal{X}'
        self.g = common.Coupling(scale, 'lq', 0, r'g_\mathcal{X}')
        self.couplings = [self.g,]
        
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
                        v = np.conjugate(self.g[j-1, k-1])*self.g[i-1, l-1]/(8*self.mass**2)
                        wc |= {f'lq1_{i}{j}{k}{l}': -3*v, f'lq3_{i}{j}{k}{l}': v}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)