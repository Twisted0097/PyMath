"""
PyMath.py
A simple math expression solver.

Examples:
    5 + 3 * 2
    (10 + 5) / 3
    sqrt(81)
    log(100, 10)
    log10(1000)
    ln(e)
    sin(pi/2)
    cos(0)
    tan(pi/4)
    factorial(6)
    abs(-25)
    floor(3.9)
    ceil(3.1)
    degrees(pi)
    radians(180)
    2**10
"""

import math

# Allowed functions
ALLOWED_FUNCTIONS = {
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "ln": math.log,
    "exp": math.exp,

    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,

    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,

    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,

    "degrees": math.degrees,
    "radians": math.radians,

    "factorial": math.factorial,

    "floor": math.floor,
    "ceil": math.ceil,

    "fabs": math.fabs,
    "abs": abs,

    "pow": pow,

    "round": round,

    "min": min,
    "max": max,
}

# Allowed constants
ALLOWED_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
}

SAFE_GLOBALS = {
    "__builtins__": None
}

SAFE_LOCALS = {}
SAFE_LOCALS.update(ALLOWED_FUNCTIONS)
SAFE_LOCALS.update(ALLOWED_CONSTANTS)


def solve(expression: str):
    """
    Evaluate a mathematical expression safely.
    """
    try:
        result = eval(expression, SAFE_GLOBALS, SAFE_LOCALS)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero."
    except ValueError as e:
        return f"Math Error: {e}"
    except SyntaxError:
        return "Syntax Error: Invalid expression."
    except NameError:
        return "Error: Unknown function or constant."
    except TypeError:
        return "Error: Invalid use of a function."
    except Exception as e:
        return f"Error: {e}"


def main():
    print("=" * 50)
    print("PyMath - Math Expression Solver")
    print("=" * 50)
    print("Examples:")
    print("  5+2")
    print("  sqrt(144)")
    print("  log(100,10)")
    print("  log10(1000)")
    print("  ln(e)")
    print("  sin(pi/2)")
    print("  factorial(5)")
    print("Type 'exit' to quit.")
    print()

    while True:
        expression = input("Enter expression: ").strip()

        if expression.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not expression:
            continue

        result = solve(expression)
        print("Result:", result)
        print()


if __name__ == "__main__":
    main()