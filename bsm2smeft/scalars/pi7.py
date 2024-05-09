from .. import common
import numpy as np
import wilson

class pi7(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\Pi_7'
        self.yeq = common.Coupling(scale, 'eq', 0, r'y_{\Pi_7}^{eq}')
        self.couplings = [self.yeq,]
        
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
                        wc |= {f'qe_{i}{j}{k}{l}': -v}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)