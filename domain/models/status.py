from dataclasses import dataclass

@dataclass
class Status:
    in_stock: bool = None
    message: str = None