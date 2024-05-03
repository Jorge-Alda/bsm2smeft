from .. import common
import numpy as np
import wilson

class S(common.Field):
    def __init__(self, masses):
        super().__init__(masses)
        self.kappa = np.zeros([self.generations], dtype=float)
        self.lamb = np.zeros([self.generations, self.generations], dtype=float)
        self.kappa3 = np.zeros([self.generations, self.generations, self.generations], dtype=float)
        self.k_phi = np.zeros([self.generations], dtype=float)
        self.lamb_tilde = np.zeros([self.generations], dtype=float)
        self.k_B = np.zeros([self.generations], dtype=float)
        self.k_W = np.zeros([self.generations], dtype=float)
        self.k_G = np.zeros([self.generations], dtype=float)
        self.k_B_tilde = np.zeros([self.generations], dtype=float)
        self.k_W_tilde = np.zeros([self.generations], dtype=float)
        self.k_G_tilde = np.zeros([self.generations], dtype=float)
        self.y_e = np.zeros([self.generations, 3, 3], dtype=complex)
        self.y_d = np.zeros([self.generations, 3, 3], dtype=complex)
        self.y_u = np.zeros([self.generations, 3, 3], dtype=complex)

    def match(self, scale):
        coeffs = {'phi': 0, 'phiBox': 0, 'phiB': 0, 'phiBtilde': 0, 'phiW': 0, 'phiWtilde': 0, 'phiG': 0, 'phiGtilde': 0 }
        #SM parameters
        wSM = wilson.run.smeft.SMEFT(wilson.Wilson({}, scale=scale, basis='Warsaw', eft='SMEFT').wc)
        lambda_phi = wSM.C_in['Lambda']
        ye = wSM.C_in['Ge']
        yd = wSM.C_in['Gd']
        yu = wSM.C_in['Gu']
        for i in range(1,4):
            for j in range(1,4):
                coeffs |= {f'ephi_{i}{j}': 0, f'dphi_{i}{j}': 0, f'uphi_{i}{j}': 0}
        for r in range(self.generations):
            for s in range(self.generations):
                for t in range(self.generations):
                    coeffs['phi'] += self.kappa3[r,s,t] * self.kappa[r] * self.kappa[s] * self.kappa[t]/(self.masses[r]*self.masses[s]*self.masses[t])**2
                coeffs['phi'] -= self.lamb[r,s] * self.kappa[r] * self.kappa[s]/(self.masses[r]*self.masses[s])**2
            coeffs['phi'] += 2 * lambda_phi * self.k_phi[r] * self.kappa[r]/(scale*self.masses[r]**2)
            coeffs['phiBox'] += self.k_phi[r] * self.kappa[r]/(2*scale*self.masses[r]**2) - self.kappa[r]**2/(2*self.masses[r]**4)
            coeffs['phiB'] += self.k_B[r] * self.kappa[r]/(scale*self.masses[r]**2)
            coeffs['phiW'] += self.k_W[r] * self.kappa[r]/(scale*self.masses[r]**2)
            coeffs['phiG'] += self.k_G[r] * self.kappa[r]/(scale*self.masses[r]**2)
            coeffs['phiBtilde'] += self.k_B_tilde[r] * self.kappa[r]/(scale*self.masses[r]**2)
            coeffs['phiWtilde'] += self.k_W_tilde[r] * self.kappa[r]/(scale*self.masses[r]**2)
            coeffs['phiGtilde'] += self.k_G_tilde[r] * self.kappa[r]/(scale*self.masses[r]**2)
            for i in range(1,4):
                for j in range(1,4):
                    coeffs[f'ephi_{i}{j}'] += np.conjugate(ye[j-1,i-1])*self.k_phi[r] * self.kappa[r]/(2*scale*self.masses[r]**2) + np.conjugate(self.y_e[r,j-1,i-1])*self.k_phi[r] * self.kappa[r]/(scale*self.masses[r]**2)
                    coeffs[f'dphi_{i}{j}'] += np.conjugate(yd[j-1,i-1])*self.k_phi[r] * self.kappa[r]/(2*scale*self.masses[r]**2) + np.conjugate(self.y_d[r,j-1,i-1])*self.k_phi[r] * self.kappa[r]/(scale*self.masses[r]**2)
                    coeffs[f'uphi_{i}{j}'] += np.conjugate(yu[j-1,i-1])*self.k_phi[r] * self.kappa[r]/(2*scale*self.masses[r]**2) + np.conjugate(self.y_u[r,j-1,i-1])*self.k_phi[r] * self.kappa[r]/(scale*self.masses[r]**2)
        return wilson.Wilson(coeffs, scale=scale, eft='SMEFT', basis='Warsaw')