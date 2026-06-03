# Taller TDD con Jorge LEANMIND (jotamusik)

## Instalación de Pytest
Para crear el entorno virtual:
> python -m venv venv

Para activar el entorno virtual:
> source venv/bin/activate

Para instalar las dependencias:
> pip install -r requirements.txt

Para desactivar el entorno:
> deactivate

Para eliminar el entorno virtual después de desactivarlo:
> rm -r venv

Si instalas nuevas dependencias habría que hacer
> pip freeze > requierements.txt

## Teoría

### Partes del test AAA(Arrange Act Assert)
- Given: preparación
- When: accion a probar
- Then: Aserciones

### Pasos para realizar test
1. RED: Write a test that fails
2. GREEN: Make the code work
3. REFACTOR: Eliminate redundancy

### Tipos de test
  .   Tests E2E / UI: Probando el flujo completo del usuario y la interfaz.
 ...  Tests de integración: Probando la interacción entre componentes.
..... Tests unitarios: Probando funciones y métodos individuales.

Es como una pirámide:
- Cuanto más arriba es más costoso y lento.
- Cuanto más abajo es más rápido y económico.

### 📚 Testing libraries

- [UnitTest](https://docs.python.org/3/library/unittest.html)
- [Pytest](https://docs.pytest.org/en/7.1.x/getting-started.html#get-started)
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/quickstart.html)
- [Intro to property-based testing in Python](https://www.freecodecamp.org/news/intro-to-property-based-testing-in-python-6321e0c2f8b/)
