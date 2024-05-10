from .. import common
import numpy as np
import wilson

class Q5(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\mathcal{Q}_5'
        self.gdl = common.Coupling(scale, 'dl', 0, r'g_{\mathcal{Q}_5}^{dl}')
        self.geq = common.Coupling(scale, 'eq', 0, r'g_{\mathcal{Q}_5}^{eq}')
        self.couplings = [self.gdl, self.geq]
        
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
                        vld = np.conjugate(self.gdl[k-1, i-1])*self.gdl[l-1, j-1]/self.mass**2
                        vqe = np.conjugate(self.geq[k-1, i-1])*self.geq[l-1, j-1]/self.mass**2
                        vledq = -2*np.conjugate(self.gdl[k-1, i-1])*self.geq[l-1, j-1]/self.mass**2
                        wc |= {f'ld_{i}{j}{k}{l}': vld, f'qe_{i}{j}{k}{l}': vqe, f'ledq_{i}{j}{k}{l}': vledq}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)