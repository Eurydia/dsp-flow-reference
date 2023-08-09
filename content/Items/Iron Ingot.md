# Iron Ingot

## Recipe

Material:

| Item     | Quantity |
| -------- | -------- |
| Iron Ore | 1        |

Product:

| Item       | Quantity |
| ---------- | -------- |
| Iron Ingot | 1        | 

## Scenarios

### Conveyor Belt Mk. I + Arc Smelter

> [!info] Attachment
> [[_Blueprints/Iron Ingot (Conveyor Belt Mk. I + Arc Smelter).txt|Iron Ingot (Conveyor Belt Mk. I + Arc Smelter)]]

**Blueprint**:
- 6 Arc Smelter

$$
\begin{align*}
n &= 360\ \text{items}\ \text{minute}^{-1}\cdot\frac{1\ \text{facility}}{60\ \text{items}\ \text{minute}^{-1}} = 6\ \text{facility}
\end{align*}
$$
- 

**Transport speed**:
- **Input**: 360 items per minute (Conveyor Belt Mk. I)
- **Output**: 360 items per minute (Conveyor Belt Mk. I)

**Material**:
- 360 Iron Ore per muinute

**Product**:
- 360 Iron Ingot per minute

**Power usage**:
- 



#### Production Speed Mode

**Formula**:

$$
\begin{align*}
n &= \frac{360}{60\cdot(1+k_{s})}
\end{align*}
$$

| Proliferator | Production Speed Multiplier ($k_{s}$) | Number of Facilities Required ($n$) |
| ------------ | ------------------------------------- | ----------------------------------- |
| None         | 0                                     | 6                                   |
| Mk. I        | 0.25                                  | 4.8                                 |
| Mk. II       | 0.5                                   | 4                                   |
| Mk. III      | 1                                     | 3                                   |

#### Extra Products Mode

**Formula**:

$$
\begin{align*}
n &= \frac{360}{60\cdot(1+k_{e})}
\end{align*}
$$

| Proliferator | Extra Products Multiplier ($k_{e}$) | Number of Facilities Required ($n$) |
| ------------ | ----------------------------------- | ----------------------------------- |
| None         | 0                                   | 6                                   |
| Mk. I        | 0.125                               | 5.333                               |
| Mk. II       | 0.2                                 | 5                                   |
| Mk. III      | 0.25                                | 4.8                                 |

Material consumption (items per minute)

| Proliferator | Iron Ore |
| ------------ | -------- |
| None         | 360      |
| Mk. I        | 319.8    |
| Mk. II       | 300      |
| Mk. III      | 288      |

### Conveyor Belt Mk. II + Arc Smelter

**Description**:
- **Production target**: 720 items per minute (Conveyor Belt Mk. II)
- **Processing speed**: 60 items per minute per facility (Arc Smelter)

#### Production Speed Mode

**Formula**:

$$
\begin{align*}
n &= \frac{720}{60\cdot(1+k_{s})}
\end{align*}
$$

| Proliferator | Production Speed Multiplier ($k_{s}$) | Number of Facilities Required ($n$) |
| ------------ | ------------------------------------- | ----------------------------------- |
| None         | 0                                     | 6                                   |
| Mk. I        | 0.25                                  | 9.6                                 |
| Mk. II       | 0.5                                   | 8                                   |
| Mk. III      | 1                                     | 6                                   |

#### Extra Products Mode

**Formula**:

$$
\begin{align*}
n &= \frac{720}{60\cdot(1+k_{e})}
\end{align*}
$$

| Proliferator | Extra Products Multiplier ($k_{e}$) | Number of Facilities Required ($n$) |
| ------------ | ----------------------------------- | ----------------------------------- |
| None         | 0                                   | 12                                  |
| Mk. I        | 0.125                               | 10.67                               |
| Mk. II       | 0.2                                 | 10                                  |
| Mk. III      | 0.25                                | 9.6                                 |

Material consumption (items per minute)

| Proliferator | Iron Ore |
| ------------ | -------- |
| None         | 720      |
| Mk. I        | 640.2    |
| Mk. II       | 600      |
| Mk. III      | 576      |

### Conveyor Belt Mk. III + Arc Smelter

**Description**:
- **Production target**: 1800 items per minute (Conveyor Belt Mk. III)
- **Processing speed**: 60 items per minute per facility (Arc Smelter)

#### Production Speed Mode

**Formula**:

$$
\begin{align*}
n &= \frac{1800}{60\cdot(1+k_{s})}
\end{align*}
$$

| Proliferator | Production Speed Multiplier ($k_{s}$) | Number of Facilities Required ($n$) |
| ------------ | ------------------------------------- | ----------------------------------- |
| None         | 0                                     | 30                                  |
| Mk. I        | 0.25                                  | 24                                  |
| Mk. II       | 0.5                                   | 20                                  |
| Mk. III      | 1                                     | 15                                  |

#### Extra Products Mode

**Formula**:

$$
\begin{align*}
n &= \frac{1800}{60\cdot(1+k_{e})}
\end{align*}
$$

| Proliferator | Extra Products Multiplier ($k_{e}$) | Number of Facilities Required ($n$) |
| ------------ | ----------------------------------- | ----------------------------------- |
| None         | 0                                   | 30                                  |
| Mk. I        | 0.125                               | 26.67                               |
| Mk. II       | 0.2                                 | 25                                  |
| Mk. III      | 0.25                                | 24                                  |

Material consumption (items per minute)

| Proliferator | Iron Ore |
| ------------ | -------- |
| None         | 1800     |
| Mk. I        | 1600.2   |
| Mk. II       | 1500     |
| Mk. III      | 1440     |


### Conveyor Belt Mk. III + Plane Smelter

**Description**:
- **Production target**: 1800 items per minute (Conveyor Belt Mk. III)
- **Processing speed**: 120 items per minute per facility (Plane Smelter)

#### Production Speed Mode

**Formula**:

$$
\begin{align*}
n &= \frac{1800}{120\cdot(1+k_{s})}
\end{align*}
$$

| Proliferator | Production Speed Multiplier ($k_{s}$) | Number of Facilities Required ($n$) |
| ------------ | ------------------------------------- | ----------------------------------- |
| None         | 0                                     | 15                                  |
| Mk. I        | 0.25                                  | 12                                  |
| Mk. II       | 0.5                                   | 10                                  |
| Mk. III      | 1                                     | 7.5                                 |

#### Extra Products Mode

**Formula**:

$$
\begin{align*}
n &= \frac{1800}{120\cdot(1+k_{e})}
\end{align*}
$$

| Proliferator | Extra Products Multiplier ($k_{e}$) | Number of Facilities Required ($n$) |
| ------------ | ----------------------------------- | ----------------------------------- |
| None         | 0                                   | 15                                  |
| Mk. I        | 0.125                               | 13.33                               |
| Mk. II       | 0.2                                 | 12.5                                |
| Mk. III      | 0.25                                | 12                                  |

Material consumption (items per minute)

| Proliferator | Iron Ore |
| ------------ | -------- |
| None         | 1800     |
| Mk. I        | 1599.6   |
| Mk. II       | 750      |
| Mk. III      | 720      |
