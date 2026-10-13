# RRMS Physical Database Design

**Document ID:** RRMS-PDD-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.2 — Physical Database Design  
**Related Logical Model:** RRMS-LDM-001  
**Related Requirements:** RRMS-SRS-001 v1.0  

## 1. Purpose

This document converts the Stage 3.1 logical data model into a database-ready physical design.

It defines the selected database engine, key strategy, PostgreSQL data types, nullability, uniqueness rules, checks, indexes, and referential behavior.

Executable schema files and migration scripts are intentionally deferred until this design is validated.

## 2. Database Engine

**Selected engine: PostgreSQL**

PostgreSQL is selected because RRMS is transaction-heavy and depends on strong relational integrity across inventory, sales, payments, returns, exchanges, and customer credit.

The system requires:

- ACID transactions;
- reliable foreign-key enforcement;
- strong constraint support;
- precise numeric types for money;
- mature indexing;
- good support for future reporting and analytics;
- straightforward use from common backend frameworks.

The project should target a currently supported PostgreSQL release at implementation time rather than coupling the design document to a single minor version.

## 3. Key Strategy

### Primary keys

All primary business tables use generated `BIGINT` surrogate keys.

Examples:

- `product_id`
- `customer_id`
- `sale_id`
- `payment_id`

Reasons:

- simple joins;
- compact indexes;
- easy debugging;
- sufficient capacity for expected growth.

Public-facing identifiers may later use separate opaque identifiers if exposing sequential IDs becomes undesirable.

### Foreign keys

Foreign-key columns use the same `BIGINT` type as their referenced primary keys.

## 4. Money

All PKR monetary values use:

`NUMERIC(12,2)`

This avoids floating-point rounding errors.

Examples:

- purchase price;
- final unit cost;
- selling price;
- discounts;
- payments;
- refunds;
- expenses;
- delivery fees.

Negative amounts are not used to encode financial direction unless a future accounting ledger explicitly requires that design.

## 5. Date and Time

Use:

- `DATE` for business dates that do not require a time, such as purchase date or due date;
- `TIMESTAMPTZ` for events whose exact time matters, such as sale creation, payment recording, reservation expiry, receiving, and delivery completion.

All application timestamps should be stored consistently and converted for display at the application layer.

## 6. Status Representation

Version 1 should use constrained `VARCHAR` fields with `CHECK` constraints rather than PostgreSQL native ENUM types.

This keeps status values explicit while making future changes easier.

Examples include:

### User role
- ADMINISTRATOR
- EMPLOYEE

### Purchase type
- BUSINESS
- PERSONAL

### Inventory status
- RECEIVED
- AVAILABLE
- RESERVED
- SOLD
- ON_HOLD
- RETURNED
- DAMAGED
- CANCELLED

### Condition
- NWT
- NWOT
- OPENED
- DEFECTIVE
- DAMAGED

### Reservation status
- ACTIVE
- EXTENDED
- RELEASED
- CANCELLED
- COMPLETED

### Sale payment status
- UNPAID
- PARTIALLY_PAID
- PAID

### Delivery status
- PROCESSING
- PACKED
- SHIPPED
- OUT_FOR_DELIVERY
- DELIVERED
- FAILED_DELIVERY

### Payment method
- CASH
- BANK_TRANSFER
- JAZZCASH
- COD

### Exchange settlement
- ADDITIONAL_PAYMENT
- REFUND
- CUSTOMER_CREDIT
- NONE

## 7. Important Table Rules

### users

- `login` must be unique.
- Passwords are never stored directly; only password hashes are stored.
- Deactivation is preferred over deletion.

### brands

- Brand name should be unique.
- Referenced brands are not hard-deleted.

### categories

- Supports self-reference through `parent_category_id`.
- Parent deletion should normally be restricted while child categories exist.

### products

- `internal_sku` is required and unique.
- `barcode` is optional but unique when present.
- Product rows referenced by transaction history should not be hard-deleted.

### product_images

- Each image belongs to one Product.
- At most one primary image per Product should be enforced through application logic or a partial unique index during schema implementation.

### purchases

- `purchase_type` distinguishes BUSINESS from PERSONAL.
- `shipping_cost >= 0`.
- Purchase rows with dependent PurchaseItems should not be hard-deleted.

### purchase_items

- `quantity_purchased > 0`.
- Monetary values must be non-negative.
- `final_unit_cost` preserves the acquisition-cost basis used later for profitability.

### inventory_items

- Inventory is valid only for BUSINESS purchases.
- `quantity_received > 0`.
- `quantity_available >= 0`.
- `quantity_available <= quantity_received`.
- Application transactions must prevent overselling.

### customers

- Phone is required because the business primarily communicates by phone/WhatsApp.
- Customers with historical transactions should be deactivated rather than deleted.

### reservations

- `quantity > 0`.
- `expires_at > reserved_at`.
- Expiry does not automatically imply RELEASED.
- Conflicting reservation/sale prevention requires transactional application logic in addition to database constraints.

### sales

- `subtotal >= 0`.
- `discount_total >= 0`.
- `grand_total >= 0`.
- `discount_total <= subtotal`.
- Historical sales should not be hard-deleted.

### sale_items

- `quantity > 0`.
- Monetary snapshots must remain immutable after transaction completion except through controlled correction procedures.
- Below-cost sale acknowledgement is stored explicitly.

### payments

- `amount > 0`.
- Each payment references a Sale and Customer.
- Payment rows should not be edited destructively once finalized.

### deliveries

- `sale_id` is unique for Version 1, enforcing at most one primary Delivery per Sale.
- `tracking_ref` is unique.
- Delivery status remains independent from payment status.

### returns

- Refund amount must be non-negative.
- Refund method is required only when an actual refund is issued.
- Return records preserve original Sale references.

### return_items

- `quantity > 0`.
- Returned quantity must not exceed the quantity originally sold minus previously returned quantity.
- This cross-row rule requires transaction-level validation.

### exchanges

- Must reference the original Sale.
- Replacement SaleItem is optional while an exchange is being prepared but required when completed.
- Difference amount represents the absolute financial difference; `settlement_type` determines direction.

### expenses

- `amount > 0`.
- Both `sale_id` and `delivery_id` may be NULL for general expenses.
- Transaction-linked expenses may reference one or both where applicable.

## 8. Referential Actions

Use conservative referential actions because RRMS depends heavily on history.

Recommended defaults:

- `ON UPDATE RESTRICT`
- `ON DELETE RESTRICT`

Exceptions:

- optional relationships may use `ON DELETE SET NULL` only when removing the parent is legitimately allowed and historical meaning remains intact;
- product images may use `ON DELETE CASCADE` only if Product hard-deletion is ever permitted before the Product participates in business transactions.

In normal business use, master and transaction records should be deactivated or status-changed rather than physically deleted.

## 9. Index Strategy

Primary keys and unique constraints automatically create important indexes.

Additional indexes should include:

### Products
- `products(brand_id)`
- `products(category_id)`
- `products(name)`
- `products(internal_sku)`
- optional barcode lookup

### Purchases
- `purchases(purchase_date)`
- `purchases(source_id)`
- `purchase_items(purchase_id)`
- `purchase_items(product_id)`

### Inventory
- `inventory_items(product_id)`
- `inventory_items(status)`
- combined index on `(status, quantity_available)` where useful

### Customers
- `customers(phone)`
- `customers(name)`

### Reservations
- `reservations(customer_id)`
- `reservations(inventory_item_id)`
- `reservations(status, expires_at)`

### Sales
- `sales(customer_id)`
- `sales(sale_date)`
- `sales(payment_status)`
- `sale_items(sale_id)`
- `sale_items(inventory_item_id)`

### Payments
- `payments(sale_id)`
- `payments(customer_id)`
- `payments(payment_date)`

### Deliveries
- `deliveries(status)`
- `deliveries(tracking_ref)`

### Returns / Exchanges
- `returns(sale_id)`
- `return_items(return_id)`
- `return_items(sale_item_id)`
- `exchanges(sale_id)`

### Expenses
- `expenses(expense_date)`
- `expenses(expense_type)`
- `expenses(sale_id)`
- `expenses(delivery_id)`

Indexes should be validated against real query patterns after implementation rather than added indiscriminately.

## 10. Inventory Consistency Strategy

Inventory correctness is one of the highest-risk parts of RRMS.

The database must enforce simple invariants such as:

- non-negative quantities;
- valid foreign keys;
- positive transaction quantities.

However, multi-row business rules such as:

- checking active reservations;
- preventing simultaneous sales of the same available stock;
- ensuring returned quantity does not exceed sold quantity;

must be enforced inside database transactions by the application service layer.

Implementation should use row-level locking where necessary during reservation and sale confirmation.

A dedicated inventory-movement ledger may be introduced in a later design revision if auditability or growth requires it.

## 11. Outstanding Balance Strategy

Do not store customer outstanding balance as an independently editable value.

It should be derived from:

- confirmed Sale totals;
- Payments;
- refunds;
- exchange settlements;
- customer credits where implemented.

A cached balance may be introduced later for performance, but the transactional records remain the source of truth.

## 12. Audit Strategy

Version 1 should preserve the responsible user directly on major operational records using fields such as:

- `recorded_by_user_id`
- `created_by_user_id`
- `processed_by_user_id`

A generalized `audit_log` table may be introduced later for field-level or event-level history.

## 13. Backup and Data Protection Requirements

Physical deployment should provide:

- automated database backups;
- periodic restore testing;
- restricted database credentials;
- environment-separated credentials;
- encrypted connections to the database;
- no plaintext passwords;
- no secrets stored in the repository.

Exact infrastructure design is handled in later deployment/security stages.

## 14. Physical Diagram Files

- `PHYSICAL_ERD.drawio`
- `PHYSICAL_ERD.png`

## 15. Deliberate Deferrals

Stage 3.2 does not yet create:

- executable `CREATE TABLE` statements;
- migration files;
- seed files;
- ORM entities;
- database containers;
- deployed PostgreSQL instances.

Those will be created only after this design is accepted.

## 16. Stage 3.2 Completion Gate

Stage 3.2 is complete when:

1. `PHYSICAL_DATABASE_DESIGN.md` is committed;
2. `PHYSICAL_ERD.drawio` and `PHYSICAL_ERD.png` are committed;
3. PostgreSQL is accepted as the database engine;
4. types, nullability, constraints, referential actions, and indexes are reviewed;
5. the physical design remains consistent with the logical ERD and requirements;
6. no unresolved data-model issue blocks schema implementation.
