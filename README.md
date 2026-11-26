# BlankUnary

BlankUnary is a Whitespace-inspired variant of Unary (a unary-based variant of Brainfuck) that differs solely by using the space character (`' '`, ASCII 32 / U+0020) instead of `0` as its only allowed character, making programs written in BlankUnary invisible.

`blankunary.py` provides a simple example interpreter written in Python that accepts no characters other than spaces and does not allow line breaks. It is meant as a minimal reference rather than a full-featured interpreter (for example, it does not pass separate input data for `,` commands when running `.bu` files).

## Usage

```bash
python blankunary.py program.bu
```
