from .. import common
import numpy as np
import wilson

class phi(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\varphi'
        self.ye = common.Coupling(scale, 'el', 0, r'y_{\varphi}^e')
        self.yd = common.Coupling(scale, 'dq', 0, r'y_{\varphi}^d')
        self.yu = common.Coupling(scale, 'qu', 0, r'y_{\varphi}^u')
        self.couplings = [self.ye, self.yd,]
        
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
                        v = np.conjugate(self.ye[j-1, i-1])*self.yd[k-1, l-1]/(self.mass**2)
                        wc |= {f'ledq_{i}{j}{k}{l}': v, f'lequ1_{i}{j}{k}{l}': np.conjugate(self.ye[j-1, i-1])*self.yu[k-1, l-1]/(self.mass**2)}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)