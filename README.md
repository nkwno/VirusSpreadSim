# Introduction to the Virus Spread Automaton

This automaton simulates the spread of a virus, inspired by the spread of COVID-19.

Imagine a square grid of healthy people on a 2D grid, and each person (cell) can exist in **four different states**:  
- **Healthy**  
- **Infected**  
- **Recovered**  
- **Dead**

A similar model that inspired this design is the **Susceptible-Infected-Recovered (SIR) model**, which demonstrates how complex and unpredictable viruses can be, even when based on simple rules.

---

## 🔁 Rules

At each time step, the following rules are applied **simultaneously** to every cell in the grid:

### 1. Healthy → Infected  
- If a healthy cell is adjacent to **at least one infected neighbor**, it becomes infected with a certain probability (`p_infection`).  
- This is inspired by how proximity to infected individuals increases transmission risk in real outbreaks.

### 2. Infected → Recovered *or* Dead  
- An infected cell will either:
  - Recover with probability `p_recovery`, **or**
  - Die with probability `p_death`

This reflects real-life outcomes where infected individuals either survive or succumb to the disease.

### 3. Recovered and Dead  
- **Recovered** cells are immune and cannot be reinfected.
- **Dead** cells remain permanently dead and inactive in the simulation.

---

## ⚙️ Parameters

- `p_infection`: Probability that a **healthy neighbor gets infected**
- `p_recovery`: Probability that an **infected person recovers**
- `p_death`: Probability that an **infected person dies**

These parameters can be adjusted in the code to simulate different viral behaviors and public health outcomes.
