# RRMS Technology Stack & Implementation Plan

**Document ID:** RRMS-TECH-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.7 — Technology Stack & Implementation Plan  
**Related Architecture:** RRMS-ARCH-001  
**Related API Design:** RRMS-API-001  
**Related UI Architecture:** RRMS-UI-001  
**Related Security Design:** RRMS-SEC-001  
**Related Database Design:** RRMS-PDD-001  

---

## 1. Purpose

This document selects the implementation technology stack for RRMS and defines the initial implementation sequence.

The goal is to remove major technology uncertainty before coding begins while keeping the project simple enough for one developer to build, test, deploy, and maintain.

---

## 2. Implementation Strategy

RRMS will be implemented as a **modular monolith**.

The system will contain separate frontend and backend applications, while the backend remains a single deployable application with clearly separated business modules.

This approach is selected because:

- the project is developed primarily by one developer;
- the current business scale does not justify microservices;
- transactions span multiple business areas;
- debugging and deployment remain simpler;
- domain modules can remain cleanly separated;
- the application can later be decomposed if genuine scaling requirements appear.

---

## 3. Selected Technology Stack

### 3.1 Frontend

**Language:** TypeScript  
**Framework:** React  
**Build Tool:** Vite  

Supporting libraries:

- React Router — application routing;
- TanStack Query — server-state fetching/caching;
- React Hook Form — form handling;
- Zod — client-side schema validation where useful;
- a lightweight accessible component library or internally maintained UI components.

Why React:

- strong ecosystem;
- suitable for dashboard-style applications;
- excellent portfolio relevance;
- good support for tables, forms, routing, and responsive interfaces.

TypeScript is required to reduce avoidable frontend type errors and make API integration safer.

---

## 4. Backend

**Language:** Python  
**Framework:** FastAPI  

Supporting technologies:

- Pydantic — request/response validation;
- SQLAlchemy — ORM/data-access layer;
- Alembic — database migrations;
- Argon2id library — password hashing;
- standard/framework-supported session and CSRF tooling;
- structured Python logging.

Why FastAPI:

- clean API-first architecture;
- automatic OpenAPI documentation;
- strong Pydantic validation;
- good fit with PostgreSQL;
- suitable for a modular monolith;
- aligns well with Python-based backend development.

---

## 5. Database

**Database:** PostgreSQL

PostgreSQL remains the authoritative transactional data store.

The application will use:

- SQLAlchemy models;
- Alembic migrations;
- explicit transactions for inventory-sensitive operations;
- database constraints defined from the physical design;
- indexes added according to the approved database design.

Direct manual production schema changes should be avoided.

Schema changes should flow through migrations.

---

## 6. Authentication

RRMS will use:

- server-managed sessions;
- secure HttpOnly cookies;
- Argon2id password hashes;
- CSRF protection;
- backend-enforced role authorization.

The initial implementation should use an explicit persisted session model or equivalent server-managed session store.

Authentication state must not depend on tokens stored in browser localStorage.

---

## 7. File Storage

Development:

- local application-managed file storage.

Production:

- S3-compatible object storage or equivalent managed file storage.

Stored files may include:

- product images;
- purchase receipts;
- generated receipt files;
- exported report files where required.

The backend owns access rules and file metadata.

---

## 8. API Documentation

FastAPI-generated OpenAPI documentation will act as the implementation-level API reference.

The source-of-truth design remains:

`docs/design/api/BACKEND_API_DESIGN.md`

Implementation documentation should not silently diverge from the approved API design.

---

## 9. Backend Testing

Primary tools:

- Pytest;
- FastAPI test client / HTTP testing utilities;
- temporary/test PostgreSQL database;
- fixtures/factories for test records.

Test layers:

1. unit tests for pure business logic;
2. service tests;
3. repository/database tests;
4. API integration tests;
5. authorization tests;
6. concurrency-sensitive tests where appropriate.

SQLite should not be treated as a complete substitute for PostgreSQL because RRMS relies on PostgreSQL behavior and relational constraints.

---

## 10. Frontend Testing

Primary tools:

- Vitest;
- React Testing Library;
- Playwright for browser-level workflows.

Testing priorities:

- form validation;
- navigation;
- permission-sensitive controls;
- error states;
- sale workflow;
- reservation workflow;
- payment workflow;
- return/exchange workflow.

---

## 11. End-to-End Testing

Playwright should cover critical workflows such as:

1. login;
2. create Product;
3. record Purchase;
4. receive inventory;
5. create Customer;
6. reserve inventory;
7. create Sale;
8. record Payment;
9. manage Delivery;
10. process Return / Exchange.

End-to-end coverage should focus on high-value business flows rather than attempting to automate every visual detail.

---

## 12. Local Development Environment

Use Docker Compose for supporting infrastructure.

Initial development services:

- PostgreSQL;
- backend;
- frontend.

File storage may initially use a local mounted directory.

The developer may run frontend/backend directly on the host during active development while PostgreSQL runs in Docker.

---

## 13. Repository Structure

Recommended future structure:

```text
retail-resale-management-system/
├── README.md
├── docs/
├── requirements/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── modules/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── tests/
│   ├── alembic/
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── features/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   └── types/
│   └── package.json
├── storage/
├── docker-compose.yml
├── .env.example
└── .gitignore
```

Exact internal folders may evolve slightly during implementation, but business-feature boundaries must remain clear.

---

## 14. Backend Module Structure

Recommended business modules:

```text
modules/
├── auth/
├── users/
├── catalog/
├── products/
├── purchasing/
├── inventory/
├── customers/
├── reservations/
├── sales/
├── payments/
├── deliveries/
├── returns/
├── exchanges/
├── expenses/
├── reports/
├── notifications/
└── files/
```

Each module should own its relevant:

- API routes;
- schemas;
- service logic;
- repository/query logic;
- domain-specific errors.

Avoid creating one giant `services.py` or `models.py` containing the entire application.

---

## 15. Frontend Feature Structure

Recommended feature organization:

```text
features/
├── auth/
├── dashboard/
├── products/
├── purchasing/
├── inventory/
├── customers/
├── reservations/
├── sales/
├── payments/
├── deliveries/
├── returns/
├── expenses/
├── reports/
└── users/
```

Feature modules should contain their page-level logic, hooks, forms, and related UI.

Reusable generic UI components should live separately.

---

## 16. Dependency Management

### Python

Use a modern Python project configuration based on:

`pyproject.toml`

A tool such as `uv` may be used for fast environment and dependency management.

### Frontend

Use the standard Node package ecosystem with a committed lock file.

The exact package manager may be npm, pnpm, or equivalent, but one must be selected and used consistently once implementation begins.

---

## 17. Code Quality

Recommended Python tooling:

- Ruff — linting/formatting;
- type checking where valuable.

Recommended frontend tooling:

- ESLint;
- Prettier or equivalent formatting;
- TypeScript strict mode.

The project should enforce consistent formatting automatically rather than relying on manual style.

---

## 18. CI

Use GitHub Actions.

Initial CI pipeline should run:

### Backend

- dependency installation;
- lint/format check;
- tests.

### Frontend

- dependency installation;
- TypeScript check;
- lint;
- tests;
- production build.

Later stages may add:

- integration tests;
- migration validation;
- Playwright tests;
- deployment steps.

---

## 19. Environment Configuration

Use environment variables for environment-specific values.

Examples:

- database URL;
- session secret;
- allowed frontend origin;
- file-storage configuration;
- production hostname.

Commit:

`.env.example`

Do not commit:

`.env`

The `.gitignore` must cover secret-containing local environment files.

---

## 20. Logging

Backend logging should be structured.

Logs should include:

- timestamp;
- severity;
- request ID;
- route;
- authenticated user ID when appropriate;
- error/business-event category.

Do not log secrets, passwords, full session IDs, or unnecessary sensitive customer information.

---

## 21. Error Tracking

Version 1 can begin with structured logs.

A hosted error-tracking service may be introduced later if deployment experience shows a clear need.

Do not make external observability tooling a blocker for initial implementation.

---

## 22. Receipt Generation

Receipts should be generated on the backend from transaction data.

Target outputs:

- printable browser/PDF representation;
- WhatsApp-shareable format.

Receipt generation must use preserved Sale/SaleItem/Payment data rather than current Product pricing.

---

## 23. Reporting Implementation

Reports should initially use PostgreSQL queries through the backend.

Do not introduce a separate analytics database at this scale.

If reporting becomes expensive in the future, options may include:

- cached summaries;
- materialized views;
- background-generated reports.

These are optimizations, not initial requirements.

---

## 24. Deployment Direction

Production should be container-friendly.

Expected deployment units:

- frontend;
- backend;
- managed PostgreSQL;
- persistent object/file storage.

HTTPS is mandatory in production.

Exact hosting provider selection is deferred until deployment planning.

---

# 25. Implementation Order

Implementation should proceed vertically rather than creating the entire database, entire API, and entire frontend separately before integration.

## Milestone 1 — Project Foundation

Build:

- backend project;
- frontend project;
- Docker Compose;
- PostgreSQL connection;
- Alembic;
- environment configuration;
- lint/test tooling;
- CI baseline.

Deliverable:

Application boots locally with frontend, backend, and database connectivity.

---

## Milestone 2 — Authentication & Users

Build:

- User model;
- session storage;
- login/logout;
- Argon2id hashing;
- authorization helpers;
- Administrator/Employee roles;
- User Management basics.

Deliverable:

Secure internal login and protected routes.

---

## Milestone 3 — Catalog & Products

Build:

- brands;
- categories;
- products;
- product images;
- product list/detail/create/edit UI.

Deliverable:

Business can maintain its product catalog.

---

## Milestone 4 — Purchasing & Receiving

Build:

- purchase sources;
- purchases;
- purchase items;
- receipt files;
- receiving workflow;
- inventory creation.

Deliverable:

Products can move from acquisition into physically received inventory.

---

## Milestone 5 — Inventory & Reservations

Build:

- inventory screens;
- condition/status;
- available quantity;
- reservations;
- extend/release/cancel;
- concurrency-safe reservation logic.

Deliverable:

Available and reserved stock is reliably tracked.

---

## Milestone 6 — Customers

Build:

- customer creation/editing;
- customer profile;
- transaction-history shell;
- customer search.

Deliverable:

Customer information is centralized.

---

## Milestone 7 — Sales

Build:

- Sale/SaleItem;
- create-sale workflow;
- pricing;
- discounts;
- below-cost warning;
- inventory decrement;
- reservation consumption;
- receipt data.

Deliverable:

Core POS/sales transaction works end to end.

---

## Milestone 8 — Payments & Credit

Build:

- payment transactions;
- partial payments;
- deposits;
- payment status;
- outstanding balance calculation;
- customer balance UI.

Deliverable:

Credit and payment tracking replaces manual records.

---

## Milestone 9 — Delivery

Build:

- Delivery model/API/UI;
- tracking reference;
- status transitions;
- delivery fee/rider details.

Deliverable:

Orders can be tracked through delivery.

---

## Milestone 10 — Returns & Exchanges

Build:

- returns;
- return items;
- inventory restoration;
- refunds;
- exchanges;
- value differences;
- customer credit handling.

Deliverable:

Post-sale workflows are traceable without modifying original sales.

---

## Milestone 11 — Expenses & Reporting

Build:

- expenses;
- linked/general expenses;
- dashboard metrics;
- revenue/profit reports;
- inventory aging;
- customer balances;
- sales analytics.

Deliverable:

Business receives operational and financial visibility.

---

## Milestone 12 — Notifications & Operational Polish

Build:

- reservation-expiry alerts;
- aged-stock alerts;
- pending delivery alerts;
- relevant outstanding-balance alerts;
- workflow usability improvements.

Deliverable:

The internal V1 application becomes operationally usable.

---

## Milestone 13 — Storefront

Only after the internal system is stable:

- public product browsing;
- public product detail;
- guest order requests;
- manual approval;
- non-expiring temporary holds.

Deliverable:

Customers can discover products beyond WhatsApp while the business retains order approval control.

---

## 26. Definition of Implementation Ready

Stage 3 Technical Design is implementation-ready when:

- database model is approved;
- physical DB design is approved;
- system architecture is approved;
- API contract is approved;
- frontend architecture is approved;
- security model is approved;
- technology stack is selected;
- implementation sequence is documented.

---

## 27. Deliberate Deferrals

This stage does not yet:

- create the frontend/backend projects;
- create database migrations;
- install dependencies;
- write application code;
- deploy infrastructure;
- create production secrets;
- implement CI;
- choose the final hosting provider.

Those activities begin after Technical Design closes.

---

## 28. Diagram Files

- `IMPLEMENTATION_ARCHITECTURE.drawio`
- `IMPLEMENTATION_ARCHITECTURE.png`

---

## 29. Stage 3.7 Completion Gate

Stage 3.7 is complete when:

1. `TECH_STACK_IMPLEMENTATION_PLAN.md` is committed;
2. `IMPLEMENTATION_ARCHITECTURE.drawio` is committed;
3. `IMPLEMENTATION_ARCHITECTURE.png` is committed;
4. frontend/backend/database/testing technologies are accepted;
5. repository implementation structure is accepted;
6. implementation milestones are accepted;
7. no unresolved technology decision prevents development from beginning.

Completion of this gate makes the project ready for **Stage 3 Technical Design closeout**.
