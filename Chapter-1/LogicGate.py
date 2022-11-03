# Basic Gate
from typing import Any


class LogicGate:
    def __init__(self, n) -> None:
        self.label = n
        self.output = None

    def get_label(self) -> str:
        return self.label

    def get_output(self) -> "Any":
        self.output = self.perform_gate_logic()
        return self.output

    def perform_gate_logic(self):
        return

    def set_next_pin(self, source: "Connector"):
        return


# Gate need 2 input
class BinaryGate(LogicGate):
    def __init__(self, n) -> None:
        super().__init__(n)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            return int(input(f"Enter Pin A input for gate {self.get_label()} -->"))
        else:
            return self.pin_a.get_from_gate().get_output()

    def get_pin_b(self):
        if self.pin_b is None:
            return int(input(f"Enter Pin B input for gate {self.get_label()} -->"))
        else:
            return self.pin_b.get_from_gate().get_output()

    def set_next_pin(self, source: "Connector"):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


# Gate need 1 input
class UnaryGate(LogicGate):
    def __init__(self, n) -> None:
        super().__init__(n)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input(f"Enter Pin input for gate {self.get_label()} -->"))
        else:
            return self.pin.get_from_gate().get_output()

    def set_next_pin(self, source: "Connector"):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n) -> None:
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n) -> None:
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, n) -> None:
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, from_gate: LogicGate, to_gate: LogicGate) -> None:
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from_gate(self):
        return self.from_gate

    def get_to_gate(self):
        return self.to_gate


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

print(g4.get_output())
