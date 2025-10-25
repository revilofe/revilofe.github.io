# Práctica 005 - Programación Modular y Algorítmica

## 📋 Descripción

Esta práctica contiene **10 ejercicios** que combinan algorítmica y problemas del mundo real para desarrollar habilidades de programación estructurada y modular. Los ejercicios están diseñados para ser evaluados automáticamente mediante tests unitarios en GitHub Classroom.

## 🎯 Objetivos de Aprendizaje

- ✅ Desarrollar algoritmos para resolver problemas reales
- ✅ Aplicar programación modular con funciones bien definidas
- ✅ Validar datos de entrada y manejar casos especiales
- ✅ Usar type hints para especificar tipos de datos
- ✅ Documentar código con docstrings
- ✅ Escribir código limpio sin `while True`, `break` o `continue`
- ✅ Aplicar el patrón: **Entrada → Procesamiento → Salida**

---

## 📚 Lista de Ejercicios

### **Ejercicio 01**: Calculadora de Propinas
**Problema**: Calcular propina según calidad del servicio (excelente 20%, bueno 15%, regular 10%)

**Función obligatoria**:
```python
def calcular_propina(importe: float, calidad: str) -> tuple[float, float]:
    """Retorna (propina, total_a_pagar)"""
```

---

### **Ejercicio 02**: Conversor de Temperatura con Validación
**Problema**: Convertir temperatura validando que no sea inferior al cero absoluto

**Función obligatoria**:
```python
def convertir_temperatura(valor: float, escala_origen: str, escala_destino: str) -> tuple[int, float]:
    """Retorna (codigo_estado, temperatura_convertida)
    Códigos: 0=éxito, 1=temp_invalida, 2=escala_invalida"""
```

---

### **Ejercicio 03**: Sistema de Descuentos por Cantidad
**Problema**: Aplicar descuentos escalonados según cantidad comprada

**Función obligatoria**:
```python
def calcular_precio_final(precio_unitario: float, cantidad: int) -> float:
    """Retorna precio_final con descuento aplicado
    Descuentos: 5-9→5%, 10-19→10%, 20+→15%"""
```

---

### **Ejercicio 04**: Calculadora de Interés Compuesto
**Problema**: Calcular inversión con interés compuesto

**Función obligatoria**:
```python
def calcular_inversion(capital_inicial: float, tasa_interes: float, años: int) -> tuple[float, float]:
    """Retorna (capital_final, intereses_ganados)"""
```

---

### **Ejercicio 05**: Validador de Contraseñas Seguras
**Problema**: Verificar requisitos de seguridad de contraseña

**Función obligatoria**:
```python
def validar_contraseña(contraseña: str) -> tuple[bool, int]:
    """Retorna (es_valida, codigo_fallo)
    Códigos: 0=válida, 1=corta, 2=sin_mayus, 3=sin_minus, 4=sin_num"""
```

---

### **Ejercicio 06**: Sistema de Calificaciones con Estadísticas
**Problema**: Procesar 5 notas y calcular estadísticas

**Función obligatoria**:
```python
def procesar_calificaciones(nota1: float, nota2: float, nota3: float, 
                           nota4: float, nota5: float) -> tuple[float, float, float, int]:
    """Retorna (promedio, nota_max, nota_min, codigo_resultado)
    Códigos: 0=aprobado, 1=reprobado, 2=datos_invalidos"""
```

---

### **Ejercicio 07**: Calculadora de Préstamos
**Problema**: Calcular cuota mensual de préstamo con interés

**Función obligatoria**:
```python
def calcular_cuota_prestamo(monto: float, tasa_anual: float, meses: int) -> tuple[float, float, float]:
    """Retorna (cuota_mensual, total_pagar, total_intereses)"""
```

---

### **Ejercicio 08**: Conversor de Tiempo con Validación
**Problema**: Convertir entre unidades de tiempo

**Función obligatoria**:
```python
def convertir_tiempo(valor: float, unidad_origen: str, unidad_destino: str) -> tuple[int, float]:
    """Retorna (codigo_estado, valor_convertido)
    Códigos: 0=éxito, 1=valor_negativo, 2=unidad_invalida"""
```

---

### **Ejercicio 09**: Calculadora de IMC con Recomendaciones
**Problema**: Calcular IMC y dar categoría

**Función obligatoria**:
```python
def calcular_imc(peso: float, altura: float) -> tuple[float, str]:
    """Retorna (imc, categoria)
    Categorías: "bajo_peso", "normal", "sobrepeso", "obesidad"""
```

---

### **Ejercicio 10**: Sistema de Facturación con IVA
**Problema**: Calcular factura con IVA y descuento por volumen

**Función obligatoria**:
```python
def calcular_factura(precio_unitario: float, cantidad: int, tipo_iva: str) -> tuple[float, float, float, float]:
    """Retorna (subtotal, descuento, iva, total)
    Tipos IVA: "general"→21%, "reducido"→10%, "superreducido"→4%"""
```

---

## 🚀 Configuración con GitHub Classroom

### **Paso 1: Estructura del Repositorio del Alumno**

El repositorio template debe contener:

```
practica005/
├── .github/
│   └── workflows/
│       └── tests.yml          # Workflow para tests automáticos
├── src/
│   ├── __init__.py
│   ├── ejercicio01.py         # Archivo donde el alumno escribe su código
│   ├── ejercicio02.py
│   ├── ...
│   └── ejercicio10.py
├── test/
│   ├── __init__.py
│   ├── test_ejercicio01.py    # Tests (solo lectura para el alumno)
│   ├── test_ejercicio02.py
│   ├── ...
│   └── test_ejercicio10.py
├── requirements.txt            # pytest
└── README.md                   # Instrucciones para el alumno
```

### **Paso 2: Archivo `.github/workflows/tests.yml`**

Crear este workflow para ejecución automática de tests:

```yaml
name: Tests Automáticos - Práctica 005

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout código del alumno
      uses: actions/checkout@v3
      
    - name: Configurar Python 3.11
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Instalar dependencias
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
        
    - name: Ejecutar tests con cobertura
      run: |
        pytest test/ -v --cov=src --cov-report=term-missing
        
    - name: Verificar cobertura mínima
      run: |
        pytest test/ --cov=src --cov-fail-under=80
```

### **Paso 3: Archivo `requirements.txt`**

```txt
pytest>=7.4.0
pytest-cov>=4.1.0
```

### **Paso 4: Crear Assignment en GitHub Classroom**

1. Ir a tu GitHub Classroom
2. Crear nuevo Assignment: **"Práctica 005 - Programación Modular"**
3. Seleccionar el repositorio template
4. Configurar:
   - ✅ Activar feedback automático
   - ✅ Deadline (fecha de entrega)
   - ✅ Tests automáticos (se ejecutarán con GitHub Actions)
5. Los alumnos reciben link de invitación

### **Paso 5: Flujo de Trabajo del Alumno**

1. **Aceptar assignment** → Se crea repositorio personal
2. **Clonar repositorio**:
   ```bash
   git clone https://github.com/tu-organizacion/practica005-nombre-alumno.git
   cd practica005-nombre-alumno
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Esto instalará:
   - `pytest` para ejecutar tests
   - `pytest-cov` para medir cobertura de código

4. **Desarrollar un ejercicio** (por ejemplo, ejercicio01.py)
   
   Los ejercicios deben estar en la carpeta `src/`:
   ```bash
   # Editar el archivo
   nano src/ejercicio01.py
   # o usar tu editor preferido
   code src/ejercicio01.py
   ```

5. **Ejecutar tests localmente**:
   ```bash
   # Test individual
   pytest test/test_ejercicio01.py -v
   
   # Todos los tests
   pytest test/ -v
   
   # Con cobertura de un ejercicio específico
   pytest --cov=ejercicio01 test/test_ejercicio01.py
   
   # Con cobertura de todos los ejercicios
   pytest --cov=src test/ -v
   ```

6. **Commit y push**:
   ```bash
   git add src/ejercicio01.py
   git commit -m "Ejercicio 01 completado"
   git push
   ```

7. **Ver resultados automáticos**:
   - GitHub Actions ejecuta tests automáticamente
   - Ver resultados en pestaña "Actions" del repositorio
   - ✅ Verde = todos los tests pasaron
   - ❌ Rojo = hay errores (ver logs para detalles)

---

## 🧪 Ejecución Manual de Tests

### Tests Individuales
```bash
# Ejecutar test de un ejercicio específico
pytest test/test_ejercicio01.py -v
pytest test/test_ejercicio02.py -v
# ... etc
```

### Todos los Tests
```bash
# Ejecutar todos los tests
pytest test/ -v

# Con resumen
pytest test/ --tb=short

# Detener en primer fallo
pytest test/ -x
```

### Con Cobertura
```bash
# Cobertura de un ejercicio específico
pytest --cov=ejercicio01 test/test_ejercicio01.py

# Cobertura total
pytest --cov=src --cov-report=term-missing

# Generar reporte HTML
pytest --cov=src --cov-report=html
```

### Ver Detalles de un Test Específico
```bash
# Ver todos los casos de prueba
pytest test/test_ejercicio01.py -v

# Ver con print statements
pytest test/test_ejercicio01.py -v -s
```

---

## ✅ Criterios de Evaluación

Cada ejercicio se evalúa mediante tests automáticos que verifican:

1. **Funcionalidad correcta** (70%)
   - Cálculos precisos
   - Manejo de casos normales y especiales
   - Validaciones de entrada

2. **Firma de función** (15%)
   - Nombre correcto
   - Parámetros correctos con tipos
   - Tipo de retorno correcto

3. **Buenas prácticas** (15%)
   - Sin `while True`, `break`, `continue`
   - Código modular (funciones auxiliares)
   - Comentarios claros
   - Type hints en funciones

---

## 📊 Feedback para el Alumno

GitHub Actions proporciona feedback inmediato:

- ✅ **Tests pasados**: Ejercicio correcto
- ❌ **Tests fallidos**: Ver logs para identificar errores
- 📝 **Cobertura**: Indica qué partes del código se ejecutaron

**Ejemplo de output**:
```
test_ejercicio01.py::test_calidad_excelente PASSED      [ 10%]
test_ejercicio01.py::test_calidad_buena PASSED          [ 20%]
test_ejercicio01.py::test_calidad_regular PASSED        [ 30%]
test_ejercicio01.py::test_importe_negativo PASSED       [ 40%]
...
======================== 10 passed in 0.23s ========================
```

---

## 🎓 Características Pedagógicas

### Patrón de Código Enseñado

Todos los ejercicios siguen esta estructura:

```python
def main():
    """Función principal que coordina el programa"""
    # 1. BLOQUE DE ENTRADA
    datos = leer_datos()
    
    # 2. BLOQUE DE PROCESAMIENTO
    resultado = procesar(datos)
    
    # 3. BLOQUE DE SALIDA
    mostrar_resultado(resultado)
```

### Prohibiciones (para fomentar código limpio)

❌ No usar `while True` → Usar condiciones explícitas  
❌ No usar `break` / `continue` → Usar lógica clara  
❌ No usar estructuras avanzadas (listas, diccionarios) → Aún no vistas  
✅ Se permiten tuplas solo para retorno múltiple de funciones

### Elementos Obligatorios

✅ **Type hints** en todas las funciones  
✅ **Docstrings** documentando propósito, args y returns  
✅ **Comentarios** explicativos (el "por qué", no el "qué")  
✅ **Validaciones** de entrada de datos  
✅ **Modularidad** dividiendo en funciones pequeñas

---

## 📁 Estructura de Archivos

La práctica está organizada en una estructura modular que separa el código fuente de los tests:

```
Practica005/
├── .gitignore                   # Archivos a ignorar en git
├── pytest.ini                   # Configuración de pytest
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias (pytest, pytest-cov)
├── src/                         # 📦 Código fuente de los ejercicios
│   ├── __init__.py
│   ├── ejercicio01.py           # Solución didáctica ej. 1
│   ├── ejercicio02.py           # Solución didáctica ej. 2
│   ├── ...
│   └── ejercicio10.py           # Solución didáctica ej. 10
└── test/                        # 🧪 Tests unitarios
    ├── __init__.py
    ├── test_ejercicio01.py      # Tests unitarios ej. 1
    ├── test_ejercicio02.py      # Tests unitarios ej. 2
    ├── ...
    └── test_ejercicio10.py      # Tests unitarios ej. 10
```

### **Ventajas de esta estructura:**

✅ **Separación clara** entre código y tests  
✅ **Escalabilidad** fácil para añadir más ejercicios  
✅ **Imports limpios** gracias a `pythonpath` configurado en `pytest.ini`  
✅ **Configuración centralizada** en `pytest.ini`  
✅ **Compatible con GitHub Classroom** y CI/CD

### **Configuración de pytest (`pytest.ini`):**

El archivo `pytest.ini` está configurado para que los imports sean simples:

```ini
[pytest]
pythonpath = src
testpaths = test
```

Esto permite importar directamente desde los módulos sin prefijo:
```python
# En los tests:
from ejercicio01 import calcular_propina  # ✅ Simple
# En lugar de:
# from src.ejercicio01 import calcular_propina  # ❌ Innecesario
```

---

## 👨‍🏫 Notas para el Profesor

### Personalización de Tests

Los tests se pueden ajustar modificando los archivos `test_ejercicioXX.py`. Por ejemplo, para cambiar umbrales de validación o añadir casos de prueba adicionales.

### Visualización de Progreso

En GitHub Classroom puedes ver:
- Qué alumnos han aceptado el assignment
- Último commit de cada alumno
- Estado de los tests (✅ o ❌)
- Tiempo dedicado (mediante commits)

### Retroalimentación Manual

Aunque los tests son automáticos, se recomienda:
- Revisar código manualmente para evaluar estilo
- Dar feedback en Pull Requests
- Destacar soluciones creativas

---

## 📞 Soporte

Para dudas sobre:
- **Tests que fallan**: Ver logs detallados en GitHub Actions
- **Configuración local**: Verificar Python 3.11+ y pytest instalado
- **GitHub Classroom**: Consultar documentación oficial

---

## 👤 Autor

**Eduardo Fernández**  
IES Rafael Alberti  
Módulo: Programación (DAM/DAW)  
Fecha: Octubre 2025

---

## 📄 Licencia

Material educativo de uso libre para fines docentes.
