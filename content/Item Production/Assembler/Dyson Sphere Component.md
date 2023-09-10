# Dyson Sphere Component

## Blueprint

**Recommended standard blueprints**: [[content/Blueprints/Assembler/Assembler 3I-1O.txt|Assembler 3I-1O]]

**Item transportation table**

| Conveyor Belt # | Direction | Item                       | Ratio |
| --------------- | --------- | -------------------------- | ----- |
| 1               | Input     | [[Frame Material]]         | 3/3   |
| 2               | Input     | [[Processor]]              | 3/3   |
| 3               | Input     | [[Solar Sail]]             | 3/3   |
| 4               | Output    | [[Dyson Sphere Component]] | 1/1   |

### Assembling Machine Mk.I

The number of **Assembling Machine Mk.I** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                     | 720                      | 1800                       |
| ------------------------ | ----------------------- | ------------------------ | -------------------------- |
| None                     | `(3*21)+1=64`           | `(3*42)+2=128`           | `(3*106)+2=320`            |
| Extra Products +12.5%    | `(2*21)+14=56 [354.38]` | `(2*42)+29=113 [715.08]` | `(2*106)+72=284 [1797.19]` |
| Extra Products +20%      | `(2*21)+11=53 [357.75]` | `(2*42)+22=106 [715.5]`  | `(2*106)+54=266 [1795.5]`  |
| Extra Products +25%      | `(2*21)+9=51 [358.59]`  | `(2*42)+18=102 [717.19]` | `(2*106)+44=256`           |
| Production Speedup +25%  | `3*17=51 [358.59]`      | `3*34=102 [717.19]`      | `(3*85)+1=256`             |
| Production Speedup +50%  | `3*14=42 [354.38]`      | `(3*28)+1=85 [717.19]`   | `3*71=213 [1797.19]`       |
| Production Speedup +100% | `(3*10)+2=32`           | `(3*21)+1=64`            | `(3*53)+1=160`             |

### Assembling Machine Mk.II

The number of **Assembling Machine Mk.II** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                     | 720                     | 1800                      |
| ------------------------ | ----------------------- | ----------------------- | ------------------------- |
| None                     | `3*16=48`               | `3*32=96`               | `3*80=240`                |
| Extra Products +12.5%    | `(2*16)+10=42 [354.38]` | `(2*32)+21=85 [717.19]` | `(2*80)+53=213 [1797.19]` |
| Extra Products +20%      | `(2*16)+8=40`           | `(2*32)+16=80`          | `(2*80)+40=200`           |
| Extra Products +25%      | `(2*16)+6=38 [356.25]`  | `(2*32)+12=76 [712.5]`  | `(2*80)+32=192`           |
| Production Speedup +25%  | `(3*12)+2=38 [356.25]`  | `(3*25)+1=76 [712.5]`   | `3*64=192`                |
| Production Speedup +50%  | `(3*10)+2=32`           | `(3*21)+1=64`           | `(3*53)+1=160`            |
| Production Speedup +100% | `3*8=24`                | `3*16=48`               | `3*40=120`                |

### Assembling Machine Mk.III

The number of **Assembling Machine Mk.III** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

| Proliferation            | 360                    | 720                     | 1800                      |
| ------------------------ | ---------------------- | ----------------------- | ------------------------- |
| None                     | `(3*10)+2=32`          | `(3*21)+1=64`           | `(3*53)+1=160`            |
| Extra Products +12.5%    | `(2*10)+8=28 [354.38]` | `(2*21)+14=56 [708.75]` | `(2*53)+36=142 [1797.19]` |
| Extra Products +20%      | `(2*10)+6=26 [351.0]`  | `(2*21)+11=53 [715.5]`  | `(2*53)+27=133 [1795.5]`  |
| Extra Products +25%      | `(2*10)+5=25 [351.56]` | `(2*21)+9=51 [717.19]`  | `(2*53)+22=128`           |
| Production Speedup +25%  | `(3*8)+1=25 [351.56]`  | `3*17=51 [717.19]`      | `(3*42)+2=128`            |
| Production Speedup +50%  | `3*7=21 [354.38]`      | `3*14=42 [708.75]`      | `(3*35)+1=106 [1788.75]`  |
| Production Speedup +100% | `(3*5)+1=16`           | `(3*10)+2=32`           | `(3*26)+2=80`             |
