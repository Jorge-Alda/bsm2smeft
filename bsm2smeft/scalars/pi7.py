from .. import common
import numpy as np
import wilson

class Pi7(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\Pi_7'
        self.yeq = common.Coupling(scale, 'eq', 0, r'y_{\Pi_7}^{eq}')
        self.ylu = common.Coupling(scale, 'lu', 0, r'y_{\Pi_7}^{\ell u}')
        self.couplings = [self.yeq, self.ylu]
        
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
                        v = np.conjugate(self.yeq[l-1, i-1])*self.yeq[k-1, j-1]/(2*self.mass**2)
                        wc |= {f'qe_{i}{j}{k}{l}': -v,
                              f'lequ1_{i}{j}{k}{l}': np.conjugate(self.yeq[j-1, k-1])*self.ylu[i-1, l-1]/(2*self.mass**2),
                              f'lequ3_{i}{j}{k}{l}': np.conjugate(self.yeq[j-1, k-1])*self.ylu[i-1, l-1]/(8*self.mass**2)}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)