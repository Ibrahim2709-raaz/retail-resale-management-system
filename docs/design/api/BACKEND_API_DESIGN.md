# RRMS Backend & API Design

**Document ID:** RRMS-API-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.4 — Backend & API Design  
**Related Architecture:** RRMS-ARCH-001  
**Related Database Design:** RRMS-PDD-001  
**Related Requirements:** RRMS-SRS-001 v1.0  

---

## 1. Purpose

This document defines the backend structure and REST API conventions for the Retail Resale Management System (RRMS).

It specifies:

- backend module boundaries;
- resource-oriented endpoint groups;
- request and response conventions;
- validation behavior;
- authentication and authorization expectations;
- pagination and filtering conventions;
- error response format;
- transaction ownership;
- file handling boundaries.

This document does not implement the API. Framework-specific code, ORM models, controllers, migrations, and tests are deferred to implementation.

---

## 2. API Style

RRMS will use a JSON-based REST API over HTTPS.

Base path:

`/api/v1`

Versioning begins at `/api/v1` so future breaking changes can be introduced without immediately invalidating existing clients.

Primary principles:

1. nouns represent resources;
2. HTTP methods represent actions where practical;
3. business rules remain server-side;
4. clients do not receive direct database access;
5. all protected operations require authenticated identity;
6. error responses follow one consistent structure.

---

## 3. Backend Module Boundaries

The backend should be organized by business capability rather than by one large shared controller/service layer.

Recommended modules:

- auth
- users
- brands
- categories
- products
- purchases
- inventory
- customers
- reservations
- sales
- payments
- deliveries
- returns
- exchanges
- expenses
- reports
- files
- notifications

Each module may contain its own:

- route/controller layer;
- application/service logic;
- validation schemas;
- repository/data-access logic;
- domain-specific errors.

Shared infrastructure should remain outside individual business modules.

---

## 4. Request Processing Flow

Typical protected request:

1. request reaches API router;
2. authentication middleware verifies identity;
3. authorization policy verifies required permission;
4. request schema is validated;
5. application service executes business logic;
6. database transaction runs where required;
7. result is mapped to API response;
8. structured logs are emitted;
9. sensitive internal errors remain hidden from clients.

---

## 5. Authentication API

### POST `/api/v1/auth/login`

Purpose:

Authenticate an internal user.

Request conceptually includes:

- login identifier;
- password.

Successful response returns authenticated session/token information and basic user identity.

### POST `/api/v1/auth/logout`

Ends the current authenticated session where the chosen authentication mechanism requires server-side invalidation.

### GET `/api/v1/auth/me`

Returns the currently authenticated internal user and role information.

The exact session/token implementation is deferred to the security-design stage.

---

## 6. User Management API

Administrative endpoints:

### GET `/api/v1/users`
List internal users.

### POST `/api/v1/users`
Create a user.

### GET `/api/v1/users/{userId}`
Retrieve user details.

### PATCH `/api/v1/users/{userId}`
Update permitted fields.

### POST `/api/v1/users/{userId}/activate`
Activate an account.

### POST `/api/v1/users/{userId}/deactivate`
Deactivate an account.

Hard deletion of historically referenced users should not be a normal API operation.

---

## 7. Catalog API

### Brands

- `GET /api/v1/brands`
- `POST /api/v1/brands`
- `GET /api/v1/brands/{brandId}`
- `PATCH /api/v1/brands/{brandId}`

### Categories

- `GET /api/v1/categories`
- `POST /api/v1/categories`
- `GET /api/v1/categories/{categoryId}`
- `PATCH /api/v1/categories/{categoryId}`

### Products

- `GET /api/v1/products`
- `POST /api/v1/products`
- `GET /api/v1/products/{productId}`
- `PATCH /api/v1/products/{productId}`

Product list filters may include:

- search text;
- brand;
- category;
- status/active state;
- season.

---

## 8. Product Media API

Possible routes:

- `GET /api/v1/products/{productId}/images`
- `POST /api/v1/products/{productId}/images`
- `PATCH /api/v1/products/{productId}/images/{imageId}`
- `DELETE /api/v1/products/{productId}/images/{imageId}`

Deleting media does not delete the Product.

File content may be uploaded through multipart requests or an upload workflow determined during implementation.

---

## 9. Purchasing API

### Purchase collection

- `GET /api/v1/purchases`
- `POST /api/v1/purchases`
- `GET /api/v1/purchases/{purchaseId}`
- `PATCH /api/v1/purchases/{purchaseId}`

### Purchase items

Purchase creation should normally accept its line items within the purchase command rather than requiring separate client-side calls for every item.

### Receive inventory

Use an explicit command endpoint:

`POST /api/v1/purchases/{purchaseId}/receive`

Request conceptually includes:

- purchase item;
- quantity received;
- condition;
- received timestamp where necessary.

This operation owns the transaction that creates or updates received inventory.

---

## 10. Inventory API

### GET `/api/v1/inventory`

Supports filters such as:

- product;
- status;
- condition;
- brand;
- category.

### GET `/api/v1/inventory/{inventoryItemId}`

Returns tracked inventory details.

### POST `/api/v1/inventory/{inventoryItemId}/hold`

Optional administrative hold command.

### POST `/api/v1/inventory/{inventoryItemId}/release-hold`

Releases an explicit non-reservation hold.

Direct arbitrary editing of available quantity should not be exposed as a normal public application endpoint.

---

## 11. Customer API

- `GET /api/v1/customers`
- `POST /api/v1/customers`
- `GET /api/v1/customers/{customerId}`
- `PATCH /api/v1/customers/{customerId}`

Additional views:

### GET `/api/v1/customers/{customerId}/sales`

Customer transaction history.

### GET `/api/v1/customers/{customerId}/payments`

Customer payment history.

### GET `/api/v1/customers/{customerId}/balance`

Derived outstanding balance.

The balance endpoint returns a calculated view rather than an independently editable balance record.

---

## 12. Reservation API

- `GET /api/v1/reservations`
- `POST /api/v1/reservations`
- `GET /api/v1/reservations/{reservationId}`

Commands:

### POST `/api/v1/reservations/{reservationId}/extend`

Extends the expiry date/time.

### POST `/api/v1/reservations/{reservationId}/release`

Manually releases the reservation.

### POST `/api/v1/reservations/{reservationId}/cancel`

Cancels the reservation.

Expiry alone does not call release automatically.

---

## 13. Sales API

- `GET /api/v1/sales`
- `POST /api/v1/sales`
- `GET /api/v1/sales/{saleId}`

Sale creation is a transactional command.

The backend must:

1. verify inventory;
2. verify reservation ownership where applicable;
3. validate prices;
4. enforce below-cost warning/authorization rules;
5. create Sale;
6. create SaleItems;
7. update inventory;
8. close consumed reservations.

A failed step rolls back the transaction.

### GET `/api/v1/sales/{saleId}/receipt`

Returns receipt-ready data or generated receipt output.

---

## 14. Payment API

- `GET /api/v1/payments`
- `POST /api/v1/payments`
- `GET /api/v1/payments/{paymentId}`

Payments are append-only business events in normal operation.

Payment creation validates:

- sale;
- customer;
- amount;
- payment method;
- outstanding obligation.

The response may include the newly calculated payment status and remaining balance.

---

## 15. Delivery API

- `GET /api/v1/deliveries`
- `POST /api/v1/deliveries`
- `GET /api/v1/deliveries/{deliveryId}`
- `PATCH /api/v1/deliveries/{deliveryId}`

Status transition endpoint may alternatively be explicit:

`POST /api/v1/deliveries/{deliveryId}/status`

The backend must reject invalid status transitions.

---

## 16. Returns API

- `GET /api/v1/returns`
- `POST /api/v1/returns`
- `GET /api/v1/returns/{returnId}`

Return creation must verify:

- original Sale;
- original SaleItem;
- return quantity;
- return eligibility;
- return condition;
- prior returns.

The transaction may also restore inventory and record refund details.

---

## 17. Exchange API

- `GET /api/v1/exchanges`
- `POST /api/v1/exchanges`
- `GET /api/v1/exchanges/{exchangeId}`

Exchange processing may combine:

- original-item return;
- replacement inventory allocation;
- difference calculation;
- settlement selection.

This must execute transactionally.

---

## 18. Expense API

- `GET /api/v1/expenses`
- `POST /api/v1/expenses`
- `GET /api/v1/expenses/{expenseId}`
- `PATCH /api/v1/expenses/{expenseId}`

Filters may include:

- date range;
- expense type;
- linked sale;
- linked delivery.

---

## 19. Reporting API

Reporting endpoints should be read-only.

Examples:

- `GET /api/v1/reports/summary`
- `GET /api/v1/reports/sales`
- `GET /api/v1/reports/profit`
- `GET /api/v1/reports/inventory`
- `GET /api/v1/reports/aged-stock`
- `GET /api/v1/reports/customers`
- `GET /api/v1/reports/outstanding-balances`

Query parameters may define:

- date range;
- brand;
- category;
- customer;
- aggregation period.

Expensive reports may later be delegated to background jobs.

---

## 20. Pagination Convention

Collection endpoints should support pagination.

Recommended parameters:

- `page`
- `pageSize`

Default behavior:

- page begins at 1;
- page size has a sensible default;
- server enforces a maximum page size.

Response shape conceptually includes:

```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "pageSize": 25,
    "totalItems": 0,
    "totalPages": 0
  }
}
```

Cursor pagination may be introduced later where necessary but is not required for the initial system.

---

## 21. Filtering and Sorting

Common query conventions:

- `search=`
- `status=`
- `from=`
- `to=`
- `sort=`
- `order=asc|desc`

Only documented sortable/filterable fields should be accepted.

Clients must not be able to inject raw SQL column names or expressions.

---

## 22. Request Validation

Validation occurs before business execution.

Validation includes:

- required fields;
- data types;
- numeric ranges;
- string lengths;
- accepted status values;
- basic formatting.

Business validation occurs after basic request validation.

Examples:

- basic validation: payment amount must be numeric and positive;
- business validation: payment cannot exceed an allowed financial obligation if overpayment is disallowed.

---

## 23. Response Conventions

Successful single-resource response:

```json
{
  "data": {
    "...": "..."
  }
}
```

Successful collection response:

```json
{
  "data": [],
  "pagination": {}
}
```

Command responses may include:

- affected resource;
- recalculated state;
- warnings;
- relevant balances/status.

---

## 24. Error Response Format

All API errors should use one predictable structure.

Example:

```json
{
  "error": {
    "code": "INVENTORY_CONFLICT",
    "message": "The requested inventory is no longer available.",
    "details": {},
    "requestId": "..."
  }
}
```

Recommended error categories:

- `VALIDATION_ERROR`
- `AUTHENTICATION_REQUIRED`
- `ACCESS_DENIED`
- `RESOURCE_NOT_FOUND`
- `CONFLICT`
- `INVENTORY_CONFLICT`
- `RESERVATION_CONFLICT`
- `BUSINESS_RULE_VIOLATION`
- `INTERNAL_ERROR`

Internal exception details and stack traces are never returned to normal clients.

---

## 25. HTTP Status Conventions

Recommended use:

- `200 OK` — successful read/update/command;
- `201 Created` — new resource created;
- `204 No Content` — successful operation with no response body;
- `400 Bad Request` — malformed or invalid request;
- `401 Unauthorized` — authentication required or invalid;
- `403 Forbidden` — authenticated but not allowed;
- `404 Not Found` — resource does not exist;
- `409 Conflict` — inventory/reservation/state conflict;
- `422 Unprocessable Entity` — semantically invalid business input where preferred by framework convention;
- `500 Internal Server Error` — unexpected server failure.

Exact 400 vs 422 usage should remain consistent across the implementation.

---

## 26. Authorization Model

Authorization must be checked in the backend.

Initial roles:

- ADMINISTRATOR
- EMPLOYEE

Examples:

Administrator-only operations may include:

- user management;
- selected configuration;
- sensitive overrides;
- below-cost authorization where policy requires.

Employee access follows the SRS baseline and may include operational and financial data unless future role configuration restricts it.

Do not rely on hidden frontend buttons as authorization.

---

## 27. Transaction Ownership

Application services, not controllers, own transaction boundaries.

Examples:

### Sale Service

Owns:

- availability validation;
- sale creation;
- sale item creation;
- reservation consumption;
- inventory decrement.

### Return Service

Owns:

- return creation;
- returned quantity checks;
- inventory restoration;
- refund metadata.

### Exchange Service

Owns:

- returned item handling;
- replacement allocation;
- price difference settlement.

### Payment Service

Owns:

- payment creation;
- balance recalculation;
- resulting payment status.

---

## 28. Concurrency Rules

High-risk operations must be concurrency-safe.

These include:

- creating reservations;
- confirming sales;
- releasing reservations;
- processing returns that restore stock.

The implementation should use database transactions and row-level locking where needed.

The API must return conflict errors rather than silently overselling or corrupting quantities.

---

## 29. Idempotency

Certain commands may benefit from idempotency support to prevent accidental duplicate processing caused by retries.

Candidates include:

- creating payments;
- creating sales;
- processing returns;
- processing exchanges.

The exact idempotency-key mechanism may be introduced during implementation if client behavior requires it.

---

## 30. File Handling

The API controls file upload metadata and authorization.

Files may include:

- product images;
- purchase receipts;
- generated receipts.

The client must not directly write arbitrary paths into file metadata.

File type, size, and authorization validation are required before persistence.

---

## 31. Logging and Request Correlation

Each request should have a correlation/request identifier.

Structured logs should capture:

- request ID;
- authenticated user ID where available;
- route;
- result status;
- business failure category;
- execution time.

Never log:

- passwords;
- authentication secrets;
- sensitive tokens.

---

## 32. Deliberate Deferrals

Stage 3.4 does not yet define:

- exact backend framework;
- exact programming language;
- ORM choice;
- controller class names;
- validation library;
- exact token/session mechanism;
- OpenAPI generation tool;
- frontend implementation;
- deployment infrastructure;
- source-code folder structure.

These decisions belong to later design or implementation stages.

---

## 33. Diagram Files

- `BACKEND_API_ARCHITECTURE.drawio`
- `BACKEND_API_ARCHITECTURE.png`

---

## 34. Stage 3.4 Completion Gate

Stage 3.4 is complete when:

1. `BACKEND_API_DESIGN.md` is committed;
2. `BACKEND_API_ARCHITECTURE.drawio` is committed;
3. `BACKEND_API_ARCHITECTURE.png` is committed;
4. core Version 1 business capabilities have API ownership;
5. error and response conventions are defined;
6. transaction ownership is documented;
7. authorization remains backend-enforced;
8. no unresolved API-contract issue blocks frontend or implementation planning.
