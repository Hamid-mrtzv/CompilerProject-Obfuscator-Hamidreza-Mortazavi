import os
import subprocess
import time
import tempfile
from antlr4 import FileStream, CommonTokenStream
from generated.MiniCLexer import MiniCLexer
from generated.MiniCParser import MiniCParser
from obfuscator import ObfuscatorVisitor

INPUT_PATH = "examples/input.mc"
OUTPUT_PATH = "examples/output.mc"
CC = "gcc"

def colorize(txt, clr): return f"\033[{clr}m{txt}\033[0m"
def green(txt): return colorize(txt, "92")
def red(txt): return colorize(txt, "91")
def yellow(txt): return colorize(txt, "93")
def blue(txt): return colorize(txt, "96")

def compile_run(source_code, tag, add_stdio=False, add_stdbool=False):
    with tempfile.TemporaryDirectory(prefix=f"run_{tag}_") as temp_dir:
        src_path = os.path.join(temp_dir, f"{tag}.c")
        exe_path = os.path.join(temp_dir, f"{tag}.exe" if os.name == "nt" else tag)

        headers = []
        if add_stdio: headers.append("#include <stdio.h>")
        if add_stdbool: headers.append("#include <stdbool.h>")
        full_code = "\n".join(headers) + "\n" + source_code

        with open(src_path, "w", encoding="utf-8") as f:
            f.write(full_code)

        result = subprocess.run([CC, src_path, "-o", exe_path, "-w"], capture_output=True, text=True)
        if result.returncode != 0:
            print(red(f"💥 Compilation failed for {tag}"))
            print(result.stderr)
            return None, None, None

        start = time.perf_counter()
        try:
            exec_result = subprocess.run([exe_path], capture_output=True, text=True, timeout=10)
        except subprocess.TimeoutExpired:
            print(red(f"⏰ Execution timed out for {tag}"))
            return None, None, None
        end = time.perf_counter()

        runtime = end - start
        return runtime, exec_result.stdout.strip(), exec_result.stderr.strip()

def main_func():
    print(blue("🔍 Starting Mini-C obfuscation workflow...\n"))

    if not os.path.exists(INPUT_PATH):
        print(red(f"❗ Input file missing: {INPUT_PATH}"))
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        original_code = f.read()

    stream = FileStream(INPUT_PATH, encoding="utf-8")
    lexer = MiniCLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)
    syntax_tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(red("❌ Syntax errors detected. Aborting obfuscation."))
        return

    print(green("✅ Parsing successful."))
    techniques = {
        "rename": True,
        "dead_code": True,
        "flatten_control_flow": True,
        "transform_expressions": True,
        "meaningless_funcs": True
    }

    print("⚙️  Applying transformations...")
    obfuscator = ObfuscatorVisitor(techniques)
    obf_code = obfuscator.visit(syntax_tree)

    headers = []
    if obfuscator.uses_stdio: headers.append("#include <stdio.h>")
    if obfuscator.uses_stdbool: headers.append("#include <stdbool.h>")
    full_obf_code = "\n".join(headers) + "\n\n" + obf_code if headers else obf_code

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(full_obf_code)

    print(green(f"💾 Obfuscated code saved to: {OUTPUT_PATH}"))

    print(yellow("\n⚔️  Comparing original vs obfuscated runtime...\n"))

    use_stdio = "printf" in original_code or "scanf" in original_code
    use_stdbool = any(x in original_code for x in ["bool", "true", "false"])

    t_obf, out_obf, err_obf = compile_run(obf_code, "obf", obfuscator.uses_stdio, obfuscator.uses_stdbool)
    t_orig, out_orig, err_orig = compile_run(original_code, "orig", use_stdio, use_stdbool)

    if t_obf is not None and t_orig is not None:
        print(f"{blue('⏳ Original time:')} {t_orig:.6f}s")
        print(f"{blue('🔐 Obfuscated time:')} {t_obf:.6f}s")

        diff = t_obf - t_orig
        if abs(diff) < 1e-4:
            print(green("⚖️  Same runtime."))
        elif diff > 0:
            print(yellow(f"🐢 Obfuscated is slower by {diff:.6f}s"))
        else:
            print(green(f"🚀 Obfuscated is faster by {-diff:.6f}s"))

        print("\n📤 Output comparison:")
        print(f"{blue('[Original STDOUT]')}\n{out_orig or '<empty>'}")
        print(f"{blue('[Obfuscated STDOUT]')}\n{out_obf or '<empty>'}")

        if err_orig or err_obf:
            print(f"\n{red('⚠️ Runtime warnings/errors:')}")
            if err_orig: print(f"{yellow('[Original STDERR]')}\n{err_orig}")
            if err_obf: print(f"{yellow('[Obfuscated STDERR]')}\n{err_obf}")
    else:
        print(red("❌ Runtime comparison failed."))

    print(green("\n🎉 Done."))

if __name__ == "__main__":
    main_func()
