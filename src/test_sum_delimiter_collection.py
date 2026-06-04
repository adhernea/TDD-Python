from main import sum_delimiter_collection

# Test para delimitador ; y un solo número
# ("//;\n1") -> 1
def test_when_delimiter_onenumber_give_thatnumber():
    assert sum_delimiter_collection("//;/1") == 1

# Test para delimitador , y varios números
# ("//,\n1,2,3") -> 6

# Test con delimitador mayor
# ("//::\n4::5::6") -> 12

# Test con delimitador pero mala cadena de números:
# ("//.\n1.Hola.tal")

# Test con un texto cualquiera
# ("hola") -> -1

# Test sin delimitador
# ("//\n1,2,3") -> -1

# Tests sin delimitador válido
# (";\n1;2;3") -> -1
# ("\n1,2,3") -> -1
# ("/\n1,2,3") -> -1
