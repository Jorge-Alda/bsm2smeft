from .. import common
import numpy as np
import wilson

class omega1(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\omega_1'
        self.yql = common.Coupling(scale, 'ql', 0, r'y_{\omega_1}^{q\ell}')
        self.yeu = common.Coupling(scale, 'eu', 0, r'y_{\omega_1}^{eu}')
        self.couplings = [self.yql, self.yeu]
        
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
                        v = np.conjugate(self.yql[k-1, i-1])*self.yql[l-1, j-1]/(4*self.mass**2)
                        wc |= {f'lq1_{i}{j}{k}{l}': v, f'lq3_{i}{j}{k}{l}': -v, 
                               f'lequ1_{i}{j}{k}{l}':np.conjugate(self.yql[k-1, i-1])*self.yeu[l-1, j-1]/(2*self.mass**2),
                               f'lequ3_{i}{j}{k}{l}':-np.conjugate(self.yql[k-1, i-1])*self.yeu[l-1, j-1]/(8*self.mass**2)}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)