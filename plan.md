# Plan: calculator (Python/Tkinter)

## Resumen
Calculadora de escritorio moderna escrita en Python con la librería gráfica Tkinter, con soporte de teclado, gestión de errores, tests unitarios y empaquetable como ejecutable mediante PyInstaller.

## Objetivos
- [x] Mostrar una calculadora de escritorio responsive con tema oscuro.
- [x] Permitir operaciones aritméticas (suma, resta, multiplicación, división).
- [x] Manejar errores de división por cero y sintaxis inválida.
- [x] Añadir soporte de teclado completo (Enter, Esc, Backspace).
- [x] Implementar tests unitarios con `unittest`.
- [x] Empaquetar como ejecutable `.exe` mediante PyInstaller (`calculator.spec`).

## 🏗️ Arquitectura

- **Patrón**: Aplicación de escritorio monolítica (GUI single-window con Tkinter).

```text
calculator/
├── calculator.py          # Clase Calculator (ventana, botones, lógica, binds)
├── test_calculator.py     # Suite de pruebas unitarias (unittest)
├── calculator.spec        # Configuración de PyInstaller (empaquetado)
└── plan.md
```

## 🧠 Paradigma de Programación

- **Orientado a Objetos (OOP) + Event-Driven**
- La calculadora se implementa como una **clase** `Calculator` que encapsula la ventana, el display y la lógica de operaciones.
- Tkinter opera bajo un modelo **event-driven** (mainloop, bindings de botones y eventos de teclado).

---

## 🌐 Propósito de Visibilidad y Destino Remoto

- **Visibilidad**: `Público (Open Source / Portafolio)`.
- **Plataforma Remota Asignada**: `GitHub`.
- **Plataforma de Despliegue CI/CD**: `GitHub Releases` / `GitHub Actions`.
- **Justificación**: Aplicación de escritorio Python / Tkinter con tests unitarios y spec de empaquetado PyInstaller; ideal como repositorio abierto para distribución de binarios.

---

> ⚠️ **Auditoría de UI / DESIGN.md:** La interfaz actual no cumple con las directrices visuales de [DESIGN.md](../DESIGN.md) (requiere paleta HSL, Google Fonts modernas y profundidad/glassmorphism). Pendiente refactor visual.
## Estado actual
- Estado: ✅ **Completado**
- `calculator.py`: Interfaz moderna con microinteracciones hover en botones, atajos de teclado y manejo robusto de excepciones.
- `test_calculator.py`: 6 tests unitarios superados con éxito.

## Tareas realizadas
- [x] Completar la lógica de los botones: `button_click()`, `equals_button()`, y `clear_button()`.
- [x] Manejar errores (división por cero, expresiones inválidas).
- [x] Añadir soporte de teclado (Enter, Esc, Backspace, números y operadores).
- [x] Documentar uso: `python calculator.py` y `pyinstaller calculator.spec`.
- [x] Añadir suite de tests con `unittest` (`test_calculator.py`).

## Stack / Tecnologías
- Python 3
- Tkinter (GUI estándar)
- PyInstaller
- unittest
