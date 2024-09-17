# 🚀 Metodología de Desarrollo con Jenkins, Docker y Odoo

## 🛠️ Proyecto: Pipeline Automatizado para Desarrollo e Integración Continua

Este repositorio implementa un pipeline automatizado utilizando **Jenkins** para gestionar el ciclo de vida completo de desarrollo de software, basado en el ecosistema de **Odoo** y utilizando **Docker** para los entornos de despliegue. Buscamos asegurar la calidad del código a través de pruebas automatizadas, integración continua y despliegue continuo.

---

### 📋 Características del Pipeline:
1. **Validación de Requerimientos** 📄:
   - Se verifica que los requerimientos del proyecto estén actualizados antes de realizar cambios en el código.
   - Implementación de scripts en Python para automatizar la validación.

2. **Integración Continua** 🔄:
   - Conexión a un repositorio Git (GitHub).
   - Verificación de estilo de código y análisis estático en cada commit.

3. **Pruebas Automáticas** 🧪:
   - Ejecución de pruebas unitarias y de integración automáticamente en cada push.
   - Reporte de resultados directamente en Jenkins.

4. **Despliegue Continuo** 🚢:
   - Uso de **Docker** para manejar los entornos de prueba y producción con **Odoo**.
   - Despliegue automático en caso de que las pruebas sean exitosas.

---

### 🧰 Tecnologías Utilizadas:
- **Jenkins**: Para la automatización de procesos de CI/CD.
- **Docker**: Para contenerizar Odoo y garantizar entornos consistentes.
- **Odoo**: Framework de desarrollo utilizado en este proyecto.
- **Python**: Para la validación de requerimientos y ejecución de pruebas.
- **pytest**: Para las pruebas automatizadas.
