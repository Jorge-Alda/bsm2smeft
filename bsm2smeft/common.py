import wilson
import numpy as np

 
def combine_Wilson(w1: wilson.Wilson, w2: wilson.Wilson) -> wilson.Wilson:
    '''
    Combines two Wilson objects into one defined at the lowes energy scale.
    '''
    if w1.wc.scale < w2.wc.scale:
        w1run = w1.wc
        scale = w1.wc.scale
        w2run = w2.match_run(scale = scale, eft='SMEFT', basis='Warsaw')
    elif w1.wc.scale > w2.wc.scale:
        w2run = w2.wc
        scale = w2.wc.scale
        w1run = w1.match_run(scale = scale, eft='SMEFT', basis='Warsaw')
    else:
        w1run = w1.wc
        w2run = w2.wc
        scale = w2.wc.scale
    coeffs = {c: 0 for c in w1run.values.keys() | w2run.values.keys()}
    for w in [w1run, w2run]:
        for k, v in w.values.items():
            if isinstance(v, float):
                coeffs[k] += w.values[k]
            else:
                coeffs[k] += w.values[k]['Re'] + 1j*w.values[k]['Im']
    return wilson.Wilson(coeffs, scale=scale, eft='SMEFT', basis='Warsaw')


class Coupling(np.ndarray):
    def __new__(cls, scale: float, flavours: str, mdim: int=0, tex: str='', dtype=complex):
        if len(flavours) == 0:
            shape = [1,1]
        elif len(flavours) == 1:
            shape = [3,1]
        elif len(flavours) == 2:
            shape = [3,3]
        obj = super().__new__(cls, shape, dtype)
        obj.flavours = flavours
        obj.tex = tex
        obj.scale = scale
        obj.mdim = mdim
        return obj

    def mfv(self, c: float):
        wSM = wilson.run.smeft.SMEFT(wilson.Wilson({}, scale=self.scale, basis='Warsaw', eft='SMEFT').wc)
        ye = np.matrix(wSM.C_in['Ge'])
        yd = np.matrix(wSM.C_in['Gd'])
        yu = np.matrix(wSM.C_in['Gu'])
        match self.flavours:
            case '':
                self[:] = np.array([c])
            case 'qq' | 'uu' | 'dd' | 'll' | 'ee':
                self[:] = c * np.eye(3)
            case 'qu':
                self[:] = c * yu
            case 'qd':
                self[:] = c * yd
            case 'dq':
                self[:] = c * yd.H
            case 'ud':
                self[:] = c * (yu.H @ yd)
            case 'le':
                self[:] = c * ye
            case 'el':
                self[:] = c * ye.H
            case 'ql':
                self[:] = c * (np.conjugate(yu) @ ye.H)
            case 'lq':
                self[:] = c * (np.conjugate(yu) @ ye.H).H
            case 'ed':
                self[:] = c * (yd.H @ yu)
            case 'de':
                self[:] = c * (yd.H @ yu).H
            case 'ld':
                self[:] = c * (yd.T @ np.conjugate(yu))
            case 'dl':
                self[:] = c * (yd.T @ np.conjugate(yu)).H
            case 'eq':
                self[:] = c * (ye.T @ yu.T)
            case 'qe':
                self[:] = c * (ye.T @ yu.T).H

    def u2(self, c: float):
        y3 = np.zeros([3,3], dtype = self.dtype)
        y3[2,2] = 1.0
        match self.flavours:
            case '':
                self[:] = np.array([c])
            case 'qq' | 'uu' | 'dd' | 'll' | 'ee' | 'qu' | 'qd' | 'ud' | 'le' | 'lq' | 'ql' | 'ed' | 'de' | 'ld' | 'dl' | 'eq' | 'qe':
                self[:] = c * y3

    def universal(self, c: float):
        if len(self.flavours) == 2:
            self[:] = c * np.eye(3)
        

class Field:
    def __init__(self, mass: float, scale: float):
        self.mass = mass
        self.scale = scale
        self.couplings = []

    def match(self) -> wilson.Wilson:
        return wilson.Wilson({}, scale=self.scale, eft='SMEFT', basis='Warsaw')