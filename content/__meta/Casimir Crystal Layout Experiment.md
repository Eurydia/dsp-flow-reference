# Casimir Crystal Layout Experiment

**Controlled variables:**
- no proliferation
- Assembling Machine Mk. III only
- Conveyor Belt Mk.III only
- Planetary Logistic Station as source/sink
- space taken by power transmission buildings is ignored

## Batch A: Single-file 6-Assembler

![[Assembler 3I-1O.png]]

**I/O channels** (top to bottom):
- [[Casimir Crystal]]
- [[Hydrogen]]
- [[Graphene]]
- [[Titanium Crystal]]

**Blueprint**: [[Batch A.txt]]

$$
\begin{align*}
\text{production}_{A} &= \frac{22.5\text{ item}\cdot{\text{minute}^{-1}}}{1\text{ assembler}}\cdot{6}\text{ assembler}\\
&= 135\text{ item}\cdot\text{minute}^{-1}\\
\text{space taken}_{A} &= 27\text{ space}\cdot{7}\text{ space}\\
&= 189\text{ space}^{2}\\
\text{production-to-space-taken ratio}_{A} &= \frac{135\text{ item}\cdot\text{minute}^{-1}}{189\text{ space}^{2}}\\
\therefore&\approx{0.71}\text{ item}\cdot\text{minute}^{-1}\cdot\text{space}^{-2}\tag{1}
\end{align*}
$$

## Batch B: Single-file 13-Assembler

![[Assembler 4I-1O.png]]

**Blueprint**: [[Batch B.txt]]

**I/O channels** (top to bottom):
- [[Casimir Crystal]]
- [[Hydrogen]]
- [[Hydrogen]]
- [[Graphene]]
- [[Titanium Crystal]]

The number of facilities per factory is

$$
\begin{align*}
\text{production}_{B} &= \frac{22.5\text{ item}\cdot{\text{minute}^{-1}}}{1\text{ assembler}}\cdot{13}\text{ assembler}\\
&= 292.5\text{ item}\cdot\text{minute}^{-1}\\
\text{space taken}_{B} &= 55\text{ space}\cdot{8}\text{ space}\\
&= 440\text{ space}^{2}\\
\text{production-to-space-taken ratio}_{B} &= \frac{292.5\text{ item}\cdot\text{minute}^{-1}}{440\text{ space}^{2}}\\
\therefore&\approx{0.66}\text{ item}\cdot\text{minute}^{-1}\cdot\text{space}^{-2}\tag{2}
\end{align*}
$$

## Batch C: Single-file 20-Assembler

![[Assembler 5I-1O.png]]

**Blueprint**: [[Batch C.txt]]

**I/O channels** (top to bottom):
- [[Casimir Crystal]]
- [[Hydrogen]]
- [[Hydrogen]]
- [[Hydrogen]]
- [[Graphene]]
- [[Titanium Crystal]]

$$
\begin{align*}
\text{production}_{C} &= \frac{22.5\text{ item}\cdot{\text{minute}^{-1}}}{1\text{ assembler}}\cdot{20}\text{ assembler}\\
&= 450\text{ item}\cdot\text{minute}^{-1}\\
\text{space taken}_{C} &= 84\text{ space}\cdot{9}\text{ space}\\
&= 756\text{ space}^{2}\\
\text{production-to-space-taken ratio}_{C} &= \frac{450\text{ item}\cdot\text{minute}^{-1}}{756\text{ space}^{2}}\\
\therefore&\approx{0.60}\text{ item}\cdot\text{minute}^{-1}\cdot\text{space}^{-2}\tag{3}
\end{align*}
$$

## Batch D: Staggered 12-Assembler

![[Assembler 3I-1O (staggered).png]]

**Blueprint**: [[Batch D.txt]]

**I/O channels** (top to bottom):
- [[Hydrogen]]
- [[Graphene]]
- [[Titanium Crystal]]
- [[Casimir Crystal]]
- [[Hydrogen]]

$$
\begin{align*}
\text{production}_{D} &= \frac{22.5\text{ item}\cdot{\text{minute}^{-1}}}{1\text{ assembler}}\cdot{12}\text{ assembler}\\
&= 270\text{ item}\cdot\text{minute}^{-1}\\
\text{space taken}_{D} &= 28\text{ space}\cdot{11}\text{ space}\\
&= 308\text{ space}^{2}\\
\text{production-to-space-taken ratio}_{D} &= \frac{270\text{ item}\cdot\text{minute}^{-1}}{308\text{ space}^{2}}\\
\therefore&\approx{0.88}\text{ item}\cdot\text{minute}^{-1}\cdot\text{space}^{-2}\tag{4}
\end{align*}
$$

## Conclusion

In conclusion, [[#Batch D Staggered 12-Assembler]] layout has the greatest production-to-space-taken ratio at 0.88 (Equation $4$) and [[#Batch C Single-file 20-Assembler]] has the lowest at 0.60 (Equation $3$).

### Staggered vs Single-file

The staggered layout archives greater space efficiency by increasing its sorter density.

Looking at one segment, which contains two assemblers, of each layout, the sorter densities are:

| Layout                               | Sorter Density ($\text{sorter}\cdot\text{belt area}^{-2}$) |
| ------------------------------------ | ---------------------------------------------------------- |
| ![[Assembler 3I-1O.png]]             | $\frac{8}{56}\approx0.14$                                  |
| ![[Assembler 4I-1O.png]]             | $\frac{10}{64}\approx0.16$                                 |
| ![[Assembler 5I-1O.png]]             | $\frac{12}{72}\approx0.17$                                 |
| ![[Assembler 3I-1O (staggered).png]] | $\frac{8}{44}\approx0.18$                                  |

Therefore, the staggered layout is more preferable to the single-file layout due to the greater sorter density.