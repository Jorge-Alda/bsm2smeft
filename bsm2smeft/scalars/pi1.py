from .. import common
import numpy as np
import wilson

class Pi1(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\Pi_1'
        self.y = common.Coupling(scale, 'ld', 0, r'y_{\Pi_1}')
        self.couplings = [self.y,]
        
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
                        v = np.conjugate(self.y[j-1, k-1])*self.y[i-1, l-1]/(2*self.mass**2)
                        wc |= {f'ld_{i}{j}{k}{l}': -v}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)