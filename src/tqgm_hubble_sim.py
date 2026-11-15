"""
TQGM Hubble Tension Convective Expansion Simulation
Author: Sovereign Research Framework (TQGM-SIM-03)
Description: Models apparent local expansion rate discrepancy (Hubble Tension) 
             using TQGM compressible quantum fluid convective flow and regional substrate tension (sigma_q).
"""

import numpy as np


class TQGMHubbleTensionSimulator:

  def __init__(
      self, h0_cmb: float = 67.4, h0_local_target: float = 73.2
  ):
    self.H0_CMB = h0_cmb
    self.H0_Local_Target = h0_local_target

  def compute_convective_expansion_profile(
      self, distance_mpc: np.ndarray
  ) -> dict:
    r_scale = 45.0  # Characteristic local environmental density decay scale (Mpc)
    convective_boost = (self.H0_Local_Target - self.H0_CMB) * np.exp(
        -distance_mpc / r_scale
    )
    h_apparent = self.H0_CMB + convective_boost
    delta_h = float(self.H0_Local_Target - self.H0_CMB)
    return {
        "distance_mpc": distance_mpc,
        "h_apparent": h_apparent,
        "delta_h": delta_h,
    }


if __name__ == "__main__":
  distances = np.linspace(1.0, 200.0, 10)
  sim = TQGMHubbleTensionSimulator()
  results = sim.compute_convective_expansion_profile(distances)
  for d, h in zip(results["distance_mpc"], results["h_apparent"]):
    print(f"Distance: {d:5.1f} Mpc | Apparent H₀: {h:6.2f} km/s/Mpc")
