from typing import Dict

# Types of ordinals:
# finite - 1, 10, 10^100
# wainer - omega(0), epsilon(1), zeta(2), eta(3)
class Ordinal:
    def __init__(self, ordinal: Dict["type": str, "base": int, "sub": int, "exp": int, "mul": int, "add": int]) -> None:
        self.type = ordinal.type
        self.base = ordinal.base
        self.sub = ordinal.sub
        self.exp = ordinal.exp
        self.mul = ordinal.mul
        self.add = ordinal.add