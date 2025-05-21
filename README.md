# Mini-C Obfuscator

---

## Overview

This project is a source code obfuscator for the Mini-C language. Its goal is to transform clear, readable Mini-C code into a functionally equivalent but much harder to understand version.  
Key features include:

- Variable and function renaming
- Dead code insertion
- Expression complexity enhancement by rewriting simple expressions into more complex but semantically equivalent forms (e.g., converting `a = a * b` to `a *= b`, or `a = b + 1` to `a = b - (-1)`, and more)
- Control flow flattening
- Adding meaningless functions (recursive)

---

## Implemented Steps

1. **Parsing Mini-C source code**
   - Using ANTLR, the Mini-C grammar is defined, and a parser is generated.
2. **Building the Abstract Syntax Tree (AST)** of the input code
3. **Applying obfuscation transformations on the AST**
4. **Generating the obfuscated Mini-C code from the transformed AST**

---

## How to Run

### Prerequisites

- Java Development Kit (JDK) 11 or higher installed
- Python-3 installed

### Steps

1. Clone or download the project to your local machine.
2. Choose one of examples or put your own MiniC code in input.mc
3. Run this command to run the project : 

```bash
python src/main.py
```

This tool benchmarks execution time or other metrics to verify that obfuscation does not significantly degrade performance.

---

## Important Notes

- Ensure `input.mc` contains valid and tested Mini-C code before running the obfuscator.
- The output file `output.mc` contains obfuscated but functionally equivalent code.

---

## Team Info

Hamidreza Mortazavi

---

**Good luck and happy obfuscating!**
