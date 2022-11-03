# Datasets



---
## QG Simulation (idealized)

> This is a QG simulation 

$$
\partial_t q + \det\boldsymbol{J}(\psi,q) = \nu\nabla^2q-\mu q - \beta\partial_x \psi + F
$$

where:
* $u = (-\partial_y\psi, \partial_x\psi)$ - velocity
* $q = \nabla^2\psi$ - vorticity
* $\det\boldsymbol{J}(\psi,q)=\partial_y \psi\partial_x q - \partial_x \psi\partial_y q$ - determinant Jacobian term
* $\nu$ - viscosity
* $\mu$ - linear drag coefficient
* $\beta$ - Rossby parameter
* $F$ - source term

**Source**:
* A posteriori learning from quasi-geostrophic turbulence parameterization - Frezat et al (2022)
* (Majda & Wang, 2006)

---
## QG Simulation - Forced


---

## QG Simulation (SSH)

> This simulation comes from a QG model initialized from a sea surface height condition.



---

## OSSE

**Simulation Data** (NATL60)

**Observation Data** (NADIR)

**Observation Data** (SWOT)


---

## OSE 

**Altimetry Data** (NADIR)

**Reconstruction** (DUACS)

**Reconstruction** (MIOST)

**Reconstruction** (NerF)

**Source**: SSH Mapping Challenge ([github repo](https://github.com/ocean-data-challenges/2020a_SSH_mapping_NATL60/tree/master))


