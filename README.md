# Graph Task for YSU

## Requirement

Կառուցել սովորական գրաֆ `a` գագաթային կապակցվածության թվով, `b` կողային կապակցվածության թվով և `c` գրաֆի նվազագույն գագաթի աստիճանով, որոնք բավարարում են `0 < a ≤ b ≤ c` պայմանին։

## Algorithm

1. Ստեղծում ենք երկու `c + 1` չափի ամբողջական գրաֆներ
2. Միացնում ենք երկու գրաֆների առաջին `a` գագաթները $$\{ (v_i, u_i) \mid v_i \in G_1, u_i \in G_2, 1 \leq i \leq a \}$$
3. Միացնում ենք `a`-րդ գագաթը 2-րդ գրաֆի մնացած `b - a` գագաթների հետ $$\{ (v_a, u_i) \mid u_i \in G_2, a + 1 \leq i \leq b \}$$

## Installation

### Prerequisites

- Python 3.6 or higher
- NetworkX
- Matplotlib
- NumPy

### Setup

1. Clone the repository:

```bash
git clone git@github.com:GarikHk/graph_task.git
cd graph-task
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Make the script executable (Linux/Mac):

```bash
chmod +x graph_tool.py
```

## Usage

### Command Line Arguments

```bash
python3 graph_task.py a b c [options]
```

#### Required Arguments:

- `a`: գագաթային կապակցվածության թիվը
- `b`: կողային կապակցվածության թիվը
- `c`: գրաֆի նվազագույն գագաթի աստիճանը

 `a`, `b`, և `c` պարամետրերը պետք է բավարարեն հետևյալ պայմանին: `0 < a ≤ b ≤ c`

#### Optional Arguments:

- `--no-viz`: Բաց թողնել գրաֆի վիզուալիզացիան
- `--layout`: Ընտրել դասավորության ալգորիթմ (տարբերակներ: `circular`, `spring`, `spiral`, `spectral`, `shell`, `kamada_kawai`)

### Example

3 գագաթային կապակցվածութուն, 5 կողային կապակցվածություն և 7 նվազագույն գագաթի աստիճան պարունակող գրաֆի օրինակ:

```bash
python3 graph_tool.py 3 5 7
```

Մեկ այլ դասավորության ալգորիթմով:

```bash
python3 graph_tool.py 3 5 7 --layout spring
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
