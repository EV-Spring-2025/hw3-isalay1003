# EV HW3
**PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics**  
[[Project Page](https://xpandora.github.io/PhysGaussian/)]
 
## Overview
This experiment explores how varying key parameters (`n_grid`, `substeps`, `grid_v_damping_scale`, and `softening`) affects the physical behavior and visual output of simulations using the Material Point Method (MPM). Two materials were selected for systematic parameter testing. The evaluation was done using simulation videos and quantitative comparison via **PSNR** against a defined baseline.

<img src="./jelly_base.gif" width="300"/>

## Materials and Baseline

### Materials:
Two materials: **Jelly**,  **Plasticine**  
- Jelly: Soft texture, easy to deform  
- Plasticine: highly elastic, bendable


### Baseline Configuration:

  ```json
  {
    "n_grid": 50,
    "substep_dt": 1e-4,
    "grid_v_damping_scale": 0.9999,
    "softening": 0.1
  }
  ```

## MPM Parameter Effects Experiments

For each parameter, I varied the value while keeping others constant (same as baseline).  
The effects were analyzed both visually and numerically (using **PSNR vs. the baseline**).

### `n_grid` 
Resolution of the MPM background grid per dimension.

| Material | n_grid | PSNR  |
| -------- | ------ | ----- |
| Jelly | 10 | 22.18 dB |
| Jelly | 100 | 41.95 dB |
| Plasticine | 10 | 22.18 dB |
| Plasticine | 100 | 41.84 dB |

Observation:  
Increasing n_grid from 10 to 100 leads to a significant improvement in PSNR for both jelly and plasticine.  
A higher grid resolution better captures fine details of the simulation, hence increasing fidelity. This suggests grid resolution is one important factor for visual accuracy in MPM simulations.

### `substeps` 
Via `substep_dt`, number of p2g2p substeps per frame

| Material | substep_dt | PSNR  |
| -------- | ---------- | ----- |
| Jelly | 1e-5 | 20.97 dB | 
| Plasticine | 1e-5 | 20.99 dB | 

Observation:  
Reducing substep_dt lowers the PSNR vs. baseline.  
From the output video, lower substep_dt results in less smooth deformation.


### `grid_v_damping_scale`
Grid velocity damping factor

| Material | damping_scale | PSNR |
| -------- | ------------- | ---- |
| Jelly | 0.6 | 22.22 dB | 
| Jelly | 1.2 | 20.30 dB | 
| Plasticine | 0.6 | 22.22 dB | 
| Plasticine | 1.2 | 20.29 dB | 

Observation:  
Both jelly and plasticine show lower PSNR when having lower or higher values of damping value.  
When having low grid_v_damping_scale, it shows overdamping. This suppresses motion too much, making the material behave unnaturally.  
High damping value shows underdamping and causes instability or exaggerated motion.  
The baseline damping seems to strike the right balance between realism and stability.


### `softening`
Stress softening factor in the constitutive model

| Material | softening | PSNR |
| -------- | --------- | ---- |
| Jelly | 0     | 41.70 dB |
| Jelly | 0.001 | 41.68 dB |
| Jelly | 0.5   | 41.74 dB |
| Plasticine | 0      | 41.97 dB |
| Plasticine | 0.001  | 41.93 dB |
| Plasticine | 0.5    | 42.06 dB |

Observation:  
PSNR remains very stable across different softening values.  
The softening factor has minimal visual effect in this test case. This might suggest that the chosen material models or simulation scenarios aren’t highly sensitive to softening under the current configurations.


## Full Result Video Link

[Youtube](https://youtu.be/na8MSLoEwOI)

## Conclusion

This task demonstrated how individual physical parameters affect the stability, realism, and accuracy of MPM simulations. Careful tuning is essential for each material to strike a balance between simulation fidelity and computational efficiency.

### Bonus
To extend PhysGaussian for arbitrary target materials, maybe we can design a **learning-based parameter inference framework** that collects dataset of simulation videos and corresponding material parameters from sources.
To do this, use a neural network to extract features from target material videos or images, then train the network to predict material parameters by minimizing simulation-to-target differences. Futhermore, we can integrate some simulator for fine-tuning predictions via self-supervised learning.
This method enables the model to generalize to unseen materials by learning parameter-material relationships from data.

