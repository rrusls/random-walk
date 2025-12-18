# Random walk on PySDL 
Inspired by **Daniel Hirsch's** video **"Coding a Random Walk in C"** (https://youtu.be/ErA4U9WqNCE?si=Eh6SumtlEvTJXRTH). This is my realization of it in Python using SDL3.

Made purely for enjoyment.
# Features
  - Custom number of random walkers (agents) 
  - Each of the agents has it's unique random color
  - Real-time vizualization using SDL3
  - hsl / rgb random colors to make them look more vibrant
# Installation
  1. Clone the repository:
     ```
      git clone https://github.com/yourusername/random-walk-python.git
      cd random-walk-python
     ```
  2. Install dependencies:
     ```
     pip install pysdl3
     pip install pysdl3-dll <- Windows
     ```
# Usage
  Run with: 
  ```
  python random-walk.py 
  ```

You of course can modify pretty much everything in `random-walk.py` such as window size, amount of agents (which is N), <br>
their colors and direction e.t.c.
## Optional additions could include:
  - Background color
  - Edge behaviour
  - Pause / resume via keyboard controls
### Good to Know
When running, there is a chance there would be some problems with the version of pySDL3. Make sure you install a PySDL3 version which is compatible. Mine is 0.9.8b1.

Also when running, interpretator can show messages like ```Warning: Version mismatch with binary: 'SDL3_net.dll' (expected: 3.0.0, got: none)```. It is safe to not care about this, program will start regardless.

Would veery much appreciate any contributions to this repository. This code would be also avaliable on Github Gist. (https://gist.github.com/rrusls/6dfe00ea9d2988cafbc8eb4d44ab47b1)

Thank you for reading.





