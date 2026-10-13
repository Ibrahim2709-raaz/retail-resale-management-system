# RRMS System Architecture

**Document ID:** RRMS-ARCH-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.3 — System Architecture Design  
**Related Requirements:** RRMS-SRS-001 v1.0  
**Related Logical Model:** RRMS-LDM-001  
**Related Physical Database Design:** RRMS-PDD-001  

---

## 1. Purpose

This document defines the high-level system architecture of the Retail Resale Management System (RRMS).

It identifies the major runtime components, their responsibilities, communication boundaries, data ownership, and external integrations.

This stage does not define implementation classes, API endpoint details, frontend component trees, or deployment scripts.

---

## 2. Architectural Style

RRMS will use a **layered modular web application architecture**.

The primary layers are:

1. Web Frontend
2. Backend API
3. Application / Business Services
4. PostgreSQL Database
5. File / Image Storage
6. Reporting and Background Jobs

The design intentionally keeps business rules on the server side rather than distributing critical rules between the browser and database.

For the initial system, RRMS should remain a modular monolith rather than being split into microservices.

This is appropriate because:

- current business scale is modest;
- the domain is highly transactional;
- inventory, sales, payments, returns, and credit require consistent transactions;
- one developer is responsible for the initial system;
- deployment and debugging should remain simple;
- the architecture can still maintain clean module boundaries without separate services.

---

## 3. Web Frontend

The frontend provides the user interface for:

- business administrators;
- employees;
- future customer storefront users.

Primary responsibilities include:

- rendering screens and forms;
- collecting user input;
- basic client-side validation;
- calling the backend API;
- displaying errors and success states;
- presenting dashboards and reports;
- rendering receipt and transaction information.

The frontend must not be treated as the authoritative enforcement layer for business rules.

Rules such as inventory availability, reservation conflicts, below-cost authorization, and payment calculations must be enforced by the backend.

---

## 4. Backend API

The Backend API forms the controlled entry point to RRMS business functionality.

Responsibilities include:

- authenticating internal users;
- enforcing authorization;
- validating incoming requests;
- exposing application operations;
- translating application errors into consistent API responses;
- coordinating file upload/download operations;
- protecting internal database structure from direct client access.

The frontend must never connect directly to PostgreSQL.

---

## 5. Application / Business Services

The application-service layer contains the primary business behavior of RRMS.

Recommended logical modules include:

### 5.1 Authentication and User Management

Responsible for:

- login;
- password verification;
- user activation/deactivation;
- role-based authorization.

### 5.2 Product and Catalog

Responsible for:

- products;
- brands;
- categories;
- product images;
- product search and classification.

### 5.3 Purchasing

Responsible for:

- purchase recording;
- purchase sources;
- purchase items;
- business vs personal classification;
- acquisition cost calculations.

### 5.4 Inventory

Responsible for:

- receiving products;
- inventory state;
- available quantity;
- damaged/defective stock;
- reservation-safe availability checks.

### 5.5 Customers

Responsible for:

- customer profiles;
- customer preferences;
- transaction history;
- outstanding-balance views.

### 5.6 Reservations

Responsible for:

- creating reservations;
- extending reservations;
- releasing reservations;
- expiry tracking;
- conflict prevention.

Reservation expiry must not automatically release inventory.

### 5.7 Sales

Responsible for:

- sale creation;
- sale items;
- pricing;
- discounts;
- below-cost warnings and authorization;
- inventory consumption;
- receipt data.

### 5.8 Payments and Credit

Responsible for:

- payment recording;
- partial payments;
- deposits;
- customer credit;
- outstanding-balance calculation.

Payments remain separate historical financial events.

### 5.9 Delivery

Responsible for:

- delivery creation;
- internal tracking reference;
- delivery status;
- delivery fees;
- rider details.

Payment and delivery states remain independent.

### 5.10 Returns and Exchanges

Responsible for:

- return validation;
- inventory restoration where applicable;
- refunds;
- exchanges;
- customer credit;
- financial difference settlement.

Original sales history must remain preserved.

### 5.11 Expenses

Responsible for:

- general business expenses;
- sale-linked expenses;
- delivery-linked expenses.

### 5.12 Reporting

Responsible for calculations such as:

- revenue;
- gross profit;
- net profit;
- outstanding customer balances;
- sales by period;
- brand/category performance;
- aged inventory;
- customer activity.

---

## 6. PostgreSQL Database

PostgreSQL is the transactional source of truth for RRMS.

The database stores:

- users;
- product data;
- purchasing;
- inventory;
- customers;
- reservations;
- sales;
- payments;
- delivery records;
- returns;
- exchanges;
- expenses.

The backend is the only application component permitted to perform normal business writes to PostgreSQL.

The database enforces structural rules such as:

- primary keys;
- foreign keys;
- uniqueness;
- nullability;
- simple check constraints.

Complex multi-record business rules remain coordinated by backend transactions.

---

## 7. File and Image Storage

Binary or large-file content should not be stored directly inside ordinary relational database rows unless there is a specific reason.

File storage is used for:

- product images;
- purchase receipt images/documents;
- generated receipt files;
- future exported reports where applicable.

PostgreSQL stores metadata or references to these files.

The initial implementation may use local application-managed storage for development, while production may use external object/file storage.

The application must abstract file storage sufficiently to allow this change without rewriting the business domain.

---

## 8. Reporting and Background Jobs

Some RRMS operations do not require immediate synchronous user interaction.

Background jobs may be used for:

- reservation-expiry checks;
- 90-day inventory-age alerts;
- report generation;
- notification preparation;
- future scheduled business summaries.

Background processing must use the same business rules and database source of truth as synchronous application requests.

---

## 9. External Participants and Integrations

### 9.1 WhatsApp

WhatsApp remains outside the RRMS system boundary for Version 1.

RRMS may generate content suitable for sharing through WhatsApp, including:

- product information;
- receipts;
- order information.

Direct WhatsApp Business API integration is not required for Version 1.

### 9.2 Delivery Rider

Riders do not directly operate RRMS in Version 1.

Authorized business users manually record:

- rider details;
- delivery assignments;
- delivery outcomes;
- relevant expenses.

### 9.3 Product Source / Supplier

Suppliers and retailers do not directly integrate with RRMS in Version 1.

Purchase information, receipts, and order references are entered manually by authorized users.

---

## 10. Authentication and Authorization Boundary

Administrative and employee access requires authentication.

The architecture must ensure:

1. authentication happens through the backend;
2. authorization is checked on protected backend operations;
3. frontend visibility alone is never treated as security;
4. customers cannot access internal administrative functionality;
5. user identity is associated with important business operations.

The exact token/session mechanism is deferred to the detailed backend/security-design stage.

---

## 11. Transaction Boundaries

Certain operations must execute atomically.

Important transactional operations include:

### Confirming a Sale

A sale-confirmation transaction may include:

- checking inventory availability;
- checking reservation ownership;
- creating the sale;
- creating sale items;
- reducing available inventory;
- closing a reservation where applicable.

Either the transaction succeeds consistently or it must be rolled back.

### Recording a Payment

Payment recording must:

- create the payment event;
- preserve the original sale;
- recalculate the resulting payment state consistently.

### Processing a Return

A return transaction may include:

- creating the return;
- creating return items;
- restoring inventory where allowed;
- recording refund information.

### Processing an Exchange

An exchange may combine:

- return-side processing;
- replacement inventory consumption;
- financial difference settlement.

These operations require proper database transactions and may require row-level locks for inventory safety.

---

## 12. Major Data Flow

Typical internal flow:

**User → Web Frontend → Backend API → Application Service → PostgreSQL**

For file operations:

**Frontend → Backend API → File Storage**

with file metadata stored in PostgreSQL.

For reports:

**Frontend → Backend API → Reporting Service → PostgreSQL**

---

## 13. Error Handling

The architecture should provide consistent error categories such as:

- validation error;
- authentication failure;
- authorization failure;
- resource not found;
- inventory conflict;
- reservation conflict;
- business-rule violation;
- database or infrastructure failure.

Technical internal errors should not expose database credentials, stack traces, or sensitive implementation details to end users.

---

## 14. Logging and Observability

The application should maintain structured operational logs for:

- authentication events;
- failed requests;
- business-operation failures;
- unexpected server errors;
- background-job failures.

Sensitive information such as passwords and authentication secrets must never appear in logs.

Detailed monitoring infrastructure is deferred to later deployment design.

---

## 15. Deployment Boundary

The logical production deployment contains:

- frontend application;
- backend application;
- PostgreSQL database;
- persistent file/object storage;
- background-job execution where required.

These components may initially run on the same hosting platform or server while maintaining logical separation.

The architecture does not require microservices or multiple independently deployed backends for Version 1.

---

## 16. Architectural Principles

RRMS should follow these principles:

1. Keep the transactional source of truth centralized.
2. Keep critical business rules server-side.
3. Prefer a modular monolith over premature microservices.
4. Preserve historical financial and inventory records.
5. Use database transactions for multi-step business operations.
6. Keep frontend, business logic, and persistence responsibilities separated.
7. Keep external channels loosely coupled.
8. Avoid direct database access from the client.
9. Design file storage behind an abstraction.
10. Make security decisions at backend boundaries.

---

## 17. Deliberate Deferrals

Stage 3.3 does not yet define:

- exact frontend framework;
- exact backend framework;
- API endpoint paths;
- request/response schemas;
- ORM choice;
- authentication token/session implementation;
- cloud hosting vendor;
- CI/CD configuration;
- container definitions;
- detailed component classes;
- UI component hierarchy.

These decisions belong to subsequent technical-design steps.

---

## 18. Diagram Files

- `SYSTEM_ARCHITECTURE.drawio`
- `SYSTEM_ARCHITECTURE.png`

---

## 19. Stage 3.3 Completion Gate

Stage 3.3 is complete when:

1. `ARCHITECTURE.md` is committed;
2. `SYSTEM_ARCHITECTURE.drawio` is committed;
3. `SYSTEM_ARCHITECTURE.png` is committed;
4. component responsibilities are clear;
5. system boundaries remain consistent with the SRS;
6. PostgreSQL remains the transactional source of truth;
7. business-rule ownership and transaction boundaries are documented;
8. no unresolved architecture issue blocks detailed backend/API design.
