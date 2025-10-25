# Pre-Entrega | Automatización QA - Saucedemo

## Propósito
Proyecto de automatización QA utilizando Selenium y Pytest para validar el flujo de login, navegación y carrito en el sitio [saucedemo.com](https://www.saucedemo.com).

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Git & GitHub

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/maxiflores9902/pre-entrega-automation-testing-maximiliano-flores.git
   cd pre-entrega-automation-testing-maximiliano-flores
   ```

2. Crear y activar el entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # o venv\Scripts\activate en Windows
    ```

3. Instalar dependencias
    ```bash
    python -m pip install -r requirements.txt 
    ```

## Ejecución de tests
Ejecutar todas las pruebas y generar reporte HTML:

    pytest -v --html=reports/reporte.html
