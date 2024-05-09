from .. import common
import numpy as np
import wilson

class omega4(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\omega_4'
        self.yed = common.Coupling(scale, 'ed', 0, r'y_{\omega_4}^{ed}')
        self.couplings = [self.yed,]
        
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
                        v = np.conjugate(self.yed[i-1, k-1])*self.yed[j-1, l-1]/(4*self.mass**2)
                        wc |= {f'ed_{i}{j}{k}{l}': v}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)