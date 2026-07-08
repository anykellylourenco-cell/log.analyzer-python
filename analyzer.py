# Projeto: Log Analyzer
# Autor: Any Kelly
info = 0
warning = 0
error = 0
with open("sample.log", "r") as arquivo:
    for linha in arquivo:
        if "INFO" in linha:
            info += 1
        elif "WARNING" in linha:
            warning += 1
        elif "ERROR" in linha:
            error += 1

print(f"Info: {info}")
print(f"Warning: {warning}")
print(f"Error: {error}")

