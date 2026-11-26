import sys

BITS_TO_BF = {
    "000": ">",
    "001": "<",
    "010": "+",
    "011": "-",
    "100": ".",
    "101": ",",
    "110": "[",
    "111": "]",
}


def execute(code: str, input_data: str = "") -> str:
    if any(ch != " " for ch in code):
        raise SyntaxError("Only spaces (' ') are allowed.")

    n = len(code)
    if n == 0:
        return ""

    bits = bin(n)[2:]
    if not bits.startswith("1"):
        raise ValueError("Invalid encoding.")

    payload = bits[1:]
    if len(payload) % 3 != 0:
        raise ValueError("Invalid bit length: not a multiple of 3.")

    bf = "".join(BITS_TO_BF[payload[i : i + 3]] for i in range(0, len(payload), 3))

    tape = [0] * 30000
    ptr = 0
    pc = 0
    inp_idx = 0
    out = []

    jumps = {}
    stack = []
    for i, c in enumerate(bf):
        if c == "[":
            stack.append(i)
        elif c == "]":
            if not stack:
                raise SyntaxError("Unmatched ']'")
            j = stack.pop()
            jumps[j] = i
            jumps[i] = j
    if stack:
        raise SyntaxError("Unmatched '['")

    while pc < len(bf):
        c = bf[pc]
        if c == ">":
            ptr = (ptr + 1) % len(tape)
        elif c == "<":
            ptr = (ptr - 1) % len(tape)
        elif c == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif c == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif c == ".":
            out.append(chr(tape[ptr]))
        elif c == ",":
            if inp_idx < len(input_data):
                tape[ptr] = ord(input_data[inp_idx]) % 256
                inp_idx += 1
            else:
                tape[ptr] = 0
        elif c == "[" and tape[ptr] == 0:
            pc = jumps[pc]
        elif c == "]" and tape[ptr] != 0:
            pc = jumps[pc]
        pc += 1

    return "".join(out)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as src:
            print(execute(src.read()), end="")
    else:
        print(execute(input()), end="")
