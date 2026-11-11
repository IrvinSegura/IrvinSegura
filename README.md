<p align="center">
  <img src="assets/hero.svg" width="100%" alt="Irvin Segura Ortiz, desarrollador full stack: Java y Spring Boot, C# y .NET, PHP y Laravel, Python y Flask, React y TypeScript" />
</p>

<p align="center">
  <a href="#sobre-mí"><b>Sobre mí</b></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#proyectos"><b>Proyectos</b></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#stack"><b>Stack</b></a>&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#contacto"><b>Contacto</b></a>
</p>

## Sobre mí

Soy desarrollador **Full Stack** con 3 años de experiencia. Construyo sistemas completos, desde el modelado de datos hasta la interfaz de usuario, creando soluciones eficientes, escalables y fáciles de mantener. Me enfoco en desarrollar software funcional, optimizar procesos y resolver problemas mediante buenas prácticas de desarrollo y seguridad.

**Lo que he construido:**

- **Un punto de venta** con Spring Boot y React donde el stock nunca queda negativo, aunque dos cajeros vendan la última unidad a la vez, y un doble clic nunca cobra dos veces. Tiene 49 clases de prueba contra PostgreSQL real y se despliega solo cuando el CI pasa.
- **Una billetera digital** con Spring Boot y React donde cada centavo pasa por un libro mayor de partida doble: depósitos con Stripe, retiros por SPEI, transferencias que un reintento nunca duplica, doble factor y un chat de soporte con bot que escala a una persona. Es un monolito modular cuyos límites verifican Spring Modulith y ArchUnit, con métricas y trazas en Prometheus y Grafana.
-  **Un Kanban en tiempo real** con ASP.NET Core, SignalR y Clean Architecture: chat con notas de voz, notificaciones y un outbox transaccional que entrega cada evento una sola vez, aunque corran varias instancias.
- **Un blog** con Laravel y permisos por rol que se validan en el servidor, con inicio de sesión con Google, Microsoft o Facebook.
- **Un sistema de créditos** con Python y Flask: tabla de amortización, control de atrasos y reportes en Excel y PDF, con seguridad lista para producción (CSRF, CSP y bloqueo por intentos), más del 90 % de cobertura de pruebas y pruebas en el navegador con Playwright.

Trabajo con **Java + Spring Boot**, **C# + ASP.NET Core**, **PHP + Laravel** y **Python + Flask** en el backend, y con **React + TypeScript** en el frontend.

## Proyectos

Cada tarjeta muestra cómo está construido el proyecto por dentro.

<a href="https://github.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Back">
  <img src="assets/project-pos.svg" width="100%" alt="Sistema de Inventario y Facturación: cliente web en React y TypeScript, API REST en Java 21 con Spring Boot y JWT, base de datos PostgreSQL, todo en Docker; stock seguro ante concurrencia, cobros idempotentes, refresh tokens rotativos, 49 clases de prueba y CI/CD" />
</a>
<p align="center">
  <a href="https://github.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Back"><b>API · Java + Spring Boot</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://github.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front"><b>Web · React + TypeScript</b></a>
</p>

<details>
<summary><b>Ver capturas del punto de venta (8)</b></summary>
<br>

| | |
| --- | --- |
| ![Panel con ventas, utilidad y stock bajo](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/dashboard.png) | ![Punto de venta](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/checkout.png) |
| Panel | Punto de venta |
| ![Cajas del día](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/cash-drawers-today.png) | ![Supervisión de vendedores](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/supervision.png) |
| Cajas del día (gerentes) | Supervisión |
| ![Ventas contra el periodo anterior](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/report-sales.png) | ![Corte de caja](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/report-cash-closing.png) |
| Ventas contra el periodo anterior | Corte de caja |
| ![Kardex de un producto](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/movements.png) | ![Panel en tema oscuro](https://raw.githubusercontent.com/IrvinSegura/Sistema-de-Inventario-y-Facturacion_Front/main/docs/screenshots/dashboard-dark.png) |
| Kardex | Tema oscuro |

</details>

<a href="https://github.com/IrvinSegura/BilleteraDigital-">
  <img src="assets/project-wallet.svg" width="100%" alt="Billetera Digital: cliente web en React 19 y TypeScript, API REST en Java 25 con Spring Boot 4 como monolito modular con OAuth2 y JWT RS256, base de datos PostgreSQL 17, todo en Docker; libro mayor de partida doble, transferencias idempotentes, doble factor TOTP, depósitos con Stripe, retiros por SPEI y bot de soporte" />
</a>
<p align="center">
  <a href="https://github.com/IrvinSegura/BilleteraDigital-"><b>API · Java + Spring Boot</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://github.com/IrvinSegura/BilleteraDigitalWeb"><b>Web · React + TypeScript</b></a>
</p>

<details>
<summary><b>Ver capturas de la billetera (8)</b></summary>
<br>

| | |
| --- | --- |
| ![Inicio del cliente: saldo, entradas y salidas, gráfica del saldo y actividad reciente](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/customer-dashboard.png) | ![Una billetera: gráfica del saldo, movimientos y filtros](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/customer-wallet.png) |
| Inicio del cliente | Una billetera y sus movimientos |
| ![Enviar dinero, paso de confirmación](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/customer-send.png) | ![Estados de cuenta, eligiendo las fechas en un calendario](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/customer-statements.png) |
| Envío: se revisa antes de salir | Estados de cuenta |
| ![Comprobante de un movimiento](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/customer-receipt.png) | ![Un caso de soporte: las operaciones del cliente, lo escalado y el chat](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/support-case.png) |
| Comprobante para imprimir o compartir | Un caso de soporte |
| ![Inicio de administración](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/admin-home.png) | ![Libro mayor: las cuentas del sistema por moneda](https://raw.githubusercontent.com/IrvinSegura/BilleteraDigitalWeb/main/docs/screenshots/admin-ledger.png) |
| Administración | Libro mayor |

</details>

<a href="https://github.com/IrvinSegura/TaskBoard">
  <img src="assets/project-taskboard.svg" width="100%" alt="TaskBoard: Kanban en tiempo real con varios navegadores React conectados a un hub de SignalR en ASP.NET Core y .NET 10, con PostgreSQL y Redis como backplane; outbox transaccional, pruebas de arquitectura y Testcontainers" />
</a>
<p align="center"><a href="https://github.com/IrvinSegura/TaskBoard"><b>Ver repositorio · ASP.NET Core + React</b></a></p>

<details>
<summary><b>Ver capturas de TaskBoard (8)</b></summary>
<br>

| | |
| --- | --- |
| ![Tablero Kanban](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/board.png) | ![Detalle de tarjeta con checklist, adjuntos y comentarios](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/card-detail.png) |
| Tablero Kanban | Detalle de tarjeta |
| ![Mensajes: chat directo, de grupo y por tablero](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/chat.png) | ![Inicio: resumen del día y actividad reciente](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/dashboard.png) |
| Mensajes | Inicio |
| ![Calendario de fechas límite](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/calendar.png) | ![Reportes exportables a PDF y Excel](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/reports.png) |
| Calendario | Reportes |
| ![Lista del tablero, ordenable y exportable](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/board-list.png) | ![Tablero en modo oscuro](https://raw.githubusercontent.com/IrvinSegura/TaskBoard/main/docs/screenshots/board-dark.png) |
| Vista de lista | Modo oscuro |

</details>

<a href="https://github.com/IrvinSegura/IRSO-BLOG">
  <img src="assets/project-blog.svg" width="100%" alt="IRSO-BLOG: login con Google, Microsoft o Facebook hacia Laravel 13 con Jetstream, que da acceso según el rol: administrador, editor o usuario" />
</a>
<p align="center"><a href="https://github.com/IrvinSegura/IRSO-BLOG"><b>Ver repositorio · Laravel + Livewire</b></a></p>

<details>
<summary><b>Ver capturas del blog (8)</b></summary>
<br>

| | |
| --- | --- |
| ![Blog público](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/blog.png) | ![Inicio de sesión con Google, Microsoft o Facebook](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/login.png) |
| Blog público | Inicio de sesión social |
| ![Panel del administrador](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/admin-panel.png) | ![Estadísticas](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/admin-estadisticas.png) |
| Panel del administrador | Estadísticas |
| ![Crear publicación con vista previa en vivo](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/usuario-crear-publicacion.png) | ![Roles](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/admin-roles.png) |
| Crear publicación (vista previa en vivo) | Roles |
| ![Página 403 para un editor sin permiso](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/editor-403.png) | ![Blog en tema oscuro](https://raw.githubusercontent.com/IrvinSegura/IRSO-BLOG/main/docs/screenshots/blog-oscuro.png) |
| Permisos validados en el servidor | Tema oscuro |

</details>

<a href="https://github.com/IrvinSegura/Registros-de-Creditos">
  <img src="assets/project-credits.svg" width="100%" alt="Gestión de Créditos: cliente web en JavaScript, Bootstrap y Chart.js, API REST en Python con Flask y OpenAPI, base de datos SQLite con SQLAlchemy y Alembic, servida con Waitress y con respaldos automáticos; tabla de amortización, edición segura con ETag, bloqueo por intentos, cobertura de pruebas de al menos 90 % y pruebas con pytest y Playwright" />
</a>
<p align="center"><a href="https://github.com/IrvinSegura/Registros-de-Creditos"><b>Ver repositorio · Python + Flask</b></a></p>

<details>
<summary><b>Ver capturas de créditos (6)</b></summary>
<br>

| | |
| --- | --- |
| ![Panel de la cartera](https://raw.githubusercontent.com/IrvinSegura/Registros-de-Creditos/main/docs/screenshots/dashboard.png) | ![Detalle de un crédito atrasado](https://raw.githubusercontent.com/IrvinSegura/Registros-de-Creditos/main/docs/screenshots/credit-detail.png) |
| Panel de la cartera | Detalle de un crédito atrasado |
| ![Listado de créditos](https://raw.githubusercontent.com/IrvinSegura/Registros-de-Creditos/main/docs/screenshots/credits.png) | ![Pestaña de pagos de un crédito](https://raw.githubusercontent.com/IrvinSegura/Registros-de-Creditos/main/docs/screenshots/payments.png) |
| Créditos | Pagos de un crédito |
| ![Administración de usuarios](https://raw.githubusercontent.com/IrvinSegura/Registros-de-Creditos/main/docs/screenshots/users.png) | <img src="https://raw.githubusercontent.com/IrvinSegura/Registros-de-Creditos/main/docs/screenshots/mobile.png" alt="Listado en el teléfono" width="260"> |
| Usuarios | Móvil (tema oscuro) |

</details>

## Stack

<img src="assets/stack.svg" width="100%" alt="Frontend: React, TypeScript, Vite, Next.js, Tailwind CSS, shadcn/ui, TanStack Query, React Hook Form, Zod, Recharts, Chart.js, Livewire, Alpine.js, Bootstrap. Backend: Java 21 / 25, Spring Boot, Spring Security, Spring Modulith, C#, ASP.NET Core, SignalR, PHP, Laravel, Python, Flask. Datos: PostgreSQL, MySQL, SQLite, Redis, JPA / Hibernate, EF Core, SQLAlchemy, Flyway, Alembic. Calidad: Testcontainers, JUnit, ArchUnit, xUnit, NetArchTest, PHPUnit, Vitest, pytest, Playwright, GitHub Actions. Infraestructura y seguridad: Docker, Git, JWT, OAuth 2.0, APIs REST, OpenAPI, Render, Stripe. Observabilidad: Prometheus, Grafana, OpenTelemetry, Sentry, Serilog" />

## Contacto

¿Tienes un proyecto, una vacante o una idea? Me encantará escucharte.

📧 **[irvin.segura.14@gmail.com](mailto:irvin.segura.14@gmail.com)**

[![Escríbeme](https://img.shields.io/badge/Escr%C3%ADbeme-0B1220?style=for-the-badge&logo=gmail&logoColor=38BDF8)](mailto:irvin.segura.14@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-IrvinSegura-0B1220?style=for-the-badge&logo=github&logoColor=38BDF8)](https://github.com/IrvinSegura)
