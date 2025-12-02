from typing import TypeVar, Generic

T = TypeVar('T')

class ListaGenerica(Generic[T]):
    def __init__(self) -> None:
        self.datos: list[T] = []

    def push(self, dato: T) -> None:
        self.datos.append(dato)
        
    def pop(self) -> T:
        return self.datos.pop()
    
    def __repr__(self) -> str:
        return f"ListaGenerica({self.datos})"