# Introduction to the Virus Spread Automaton

This automaton simluates the spread of a virus inspired by the spread of COVID-19.  
Imagine a square grid of healthy people on a 2-D grid, and each person (cell) can exist in 4 different states: Health, Infected, Recovered, or Dead. A similar model that inspired me is the Susceptible-Infected-Recovered model which is a system that demonstreates how complex and unpredictable viruses can be just from simple rules.

## Rules

At each step, there are these following rules that are applied to every cell on the grid simultaneously.

**Healthy -> Infected**  
If a healthy cell is adjacent to at least one infected neighbor, it becomes infected with a certain probability (can be changed in the code).  
This is inspired by real life scenarios how proximity with infected individuals increases transmission risk in real-life outbreaks.

**Infected -> Recovered or To The Underworld**  
An infected cell will either recover with a certain probability or  
Die with a certain probability  
This is of course inspired by real life scenarios.

**Recovered and Dead Stay the same**  
Recovered cells build immunity and cannot be reinfected  
Dead cells are permanently dead

## Parameters

- `p_infection` = chance that a healthy neighbor gets infected  
- `p_recovery` = chance that an infected person recovers  
- `p_death` = chance that an infected person dies
