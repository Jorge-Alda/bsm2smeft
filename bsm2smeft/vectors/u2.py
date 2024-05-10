from .. import common
import numpy as np
import wilson

class U2(common.Field):
    def __init__(self, mass: float, scale: float):
        super().__init__(mass, scale)
        self.tex = r'\mathcal{U}_2'
        self.glq = common.Coupling(scale, 'lq', 0, r'g_\mathcal{X}')
        self.ged = common.Coupling(scale, 'ed', 0, r'g_\mathcal{X}')
        self.couplings = [self.glq, self.ged]
        
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
                        v = np.conjugate(self.glq[j-1, k-1])*self.glq[i-1, l-1]/(2*self.mass**2)
                        ved = np.conjugate(self.ged[j-1, k-1])*self.ged[i-1, l-1]/(2*self.mass**2)
                        vledq = 2*np.conjugate(self.ged[j-1, k-1])*self.glq[i-1, l-1]/self.mass**2
                        wc |= {f'lq1_{i}{j}{k}{l}': -v, f'lq3_{i}{j}{k}{l}': -v, f'ed_{i}{j}{k}{l}': -ved, f'ledq_{i}{j}{k}{l}': vledq}
        return wilson.Wilson({k: v for k, v in wc.items() if v != 0}, eft='SMEFT', basis='Warsaw', scale=self.scale)