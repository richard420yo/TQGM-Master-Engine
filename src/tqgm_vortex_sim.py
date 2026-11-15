"""
TQGM Galactic Rotation Curve Simulation (Fluid Vortex Entrainment vs. Newtonian)
Author: Sovereign Research Framework (TQGM-SIM-02)
"""

import numpy as np


class TQGMGalacticVortexSimulator:

  def __init__(
      self, core_mass_solar: float = 1.0e10, substrate_viscosity: float = 1.45
  ):
    self.G = 6.6743e-11
    self.solar_mass = 1.989e30
    self.M = core_mass_solar * self.solar_mass
    self.mu = substrate_viscosity

  def compute_rotation_curves(self, radius_kpc_array: np.ndarray) -> dict:
    r_meters = radius_kpc_array * 3.086e19
    v_newtonian = np.sqrt((self.G * self.M) / r_meters)
    v_tqgm_fluid = np.sqrt(
        ((self.G * self.M) / r_meters)
        + (self.mu * np.log(1.0 + (r_meters / 1.0e20))) * 1.5e4
    )
    return {
        "radius_kpc": radius_kpc_array,
        "v_newtonian_kms": v_newtonian / 1000.0,
        "v_tqgm_fluid_kms": v_tqgm_fluid / 1000.0,
    }


if __name__ == "__main__":
  radii = np.linspace(1.0, 50.0, 50)
  simulator = TQGMGalacticVortexSimulator()
  res = simulator.compute_rotation_curves(radii)
  print(f"Sample Outer Radius Velocity (TQGM Fluid): {res['v_tqgm_fluid_kms'][-1]:.2f} km/s")
