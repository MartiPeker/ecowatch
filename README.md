# EcoWatch

Sistema modular para análisis de datos ambientales. Lee datos de sensores y genera reportes agrupados por sala, estado, y ventanas de 5 minutos.

## Ejecutar

```bash
pip install -r requirements.txt
python main.py
```

## Estructura

- `models/`: entidades base
- `readers/`: lógica de lectura (Factory)
- `cache/`: almacenamiento en memoria (Singleton)
- `reports/`: estrategias de reporte (Strategy, Builder, Decorator)

## Requiere

- Python 3.8+
- prettytable

--------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------Documentación Técnica------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

Principios del Proyecto: modularidad, escalabilidad y mantenibilidad. El uso de la Programación Orientada a Objetos y con ello Patrones de Diseño.

Patrones de Diseño
-Factory Method
	-Utilizado para desacoplar la lógica de lectura de logs desde distintos formatos.
	-Permite incorporar nuevas fuentes (como JSON o APIs) sin modificar el código existente.

-Singleton
	-Aplicado al módulo de caché, asegurando que exista una única instancia de acceso a los datos en memoria.

-Strategy
	-Implementado para permitir múltiples tipos de reportes con lógica propia (por sala, estadísticas, alertas).
	-Facilita agregar nuevos tipos de reportes sin alterar los existentes.

-Decorator
	-Usado para agregar visualización en consola en formato tabla, sin alterar la lógica de generación de reportes.

Criterio del desarrrollo:
	-Código orientado a objetos, modular y con nombres claros.
	-Se pueden agregar nuevas funcionalidades sin romper el código existente.
	-Agrupación por períodos con truncamiento de minutos (timestamp // 5min) para análisis por intervalos.
	-Uso de PrettyTable para legibilidad sin costo de rendimiento significativo.
	-Uso de dict y listas para agregaciones: Se usaron para agrupar por sala o por períodos, permitiendo simular la realidad de un microservicio.
	-Con respecto a lo anterior, se implemento tambien datetime para el manejo preciso de tiempos y agrupación por intervalos.

Cosas a implementar en el futuro:
-Analisis con Pandas y matplotlib para una visualizacion mas accesible.
-Aprovechar el analisis por agrupamiento de logs (analizar mas a fondo los detalles, buscar patrones, etc)
-Testear el funcionamiento correcto del cache. 

