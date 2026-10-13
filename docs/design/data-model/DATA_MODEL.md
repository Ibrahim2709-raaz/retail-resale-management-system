# RRMS Logical Data Model

**Document ID:** RRMS-LDM-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.1 — Logical Data Model / ERD  
**Related Requirements:** RRMS-SRS-001 v1.0  
**Related Domain Model:** RRMS-DM-001  
**Related Use Case Specifications:** RRMS-UCS-001  

## 1. Purpose

This document defines the logical relational data model for the Retail Resale Management System (RRMS).

It translates the validated conceptual domain model into database-oriented entities with primary keys, foreign-key relationships, transactional fields, optional relationships, and historical-value snapshots.

This is not yet the physical database schema. SQL data types, indexes, vendor-specific constraints, migrations, and database DDL are intentionally deferred.

## 2. Main Logical Entities

The Stage 3.1 model contains:

- users
- brands
- categories
- products
- product_images
- purchase_sources
- purchases
- purchase_items
- inventory_items
- customers
- reservations
- sales
- sale_items
- payments
- deliveries
- returns
- return_items
- exchanges
- expenses

## 3. Key Design Decisions

### Product master data vs transactions

`products` stores reusable product information. Purchase costs and sale prices are stored on transaction records rather than relying on current Product values.

### Purchase structure

`purchases` represents the acquisition event and `purchase_items` stores the purchased products and unit costs.

Business and Personal purchases are distinguished at Purchase level.

### Inventory

`inventory_items` is created only from physically received business PurchaseItems.

It stores received and available quantity so rare duplicate units can be represented without forcing every unit into a separate master Product.

### Reservations

`reservations` links Customers to InventoryItems and records the reservation period and status.

Reservation expiry does not itself release inventory.

### Sales

`sales` stores the customer transaction as a whole.

`sale_items` stores individual sold inventory lines and snapshots the transaction price and historical unit cost.

### Payments

`payments` is a separate transaction table. A Sale may have multiple Payments, supporting deposits, partial payments, credit sales, and later settlement.

Customer outstanding balance should be derived from obligations and financial transactions rather than maintained as a freely editable balance.

### Delivery

A Sale may have zero or one primary Delivery in Version 1.

Delivery status is independent from payment status.

### Returns

`returns` references the original Sale.

`return_items` references the original SaleItems so the original transaction remains intact and each returned item remains traceable.

### Exchanges

`exchanges` references the original Sale and may reference a related Return and replacement SaleItem.

The financial difference is explicitly represented so the system can support additional payment, immediate refund, customer credit, or equal-value exchange.

### Expenses

`expenses` may be general or may optionally reference a Sale or Delivery.

## 4. Important Relationships

- one Brand can classify many Products;
- Categories may contain subcategories through a parent-category relationship;
- one Product may have multiple ProductImages;
- one Purchase contains one or more PurchaseItems;
- one Product may appear in many PurchaseItems;
- received PurchaseItems create or increase InventoryItems;
- one Customer may have many Reservations;
- one Customer may have many Sales;
- one Sale contains one or more SaleItems;
- one Sale may have many Payments;
- one Sale may have zero or one primary Delivery;
- one Sale may have many Returns;
- one Return contains one or more ReturnItems;
- ReturnItems reference original SaleItems;
- one Sale may have multiple Exchange records over time;
- Users are referenced by important operational records for accountability.

## 5. Historical Snapshot Fields

Historical financial values must not depend on later edits to master data.

Therefore the logical model preserves values such as:

- `purchase_items.unit_purchase_price`
- `purchase_items.final_unit_cost`
- `sale_items.unit_price`
- `sale_items.discount_amount`
- `sale_items.final_unit_price`
- `sale_items.unit_cost_snapshot`

These values support accurate historical reporting and profitability calculations.

## 6. Logical Integrity Rules

1. Inventory cannot originate from a Personal purchase.
2. Available inventory quantity cannot become negative.
3. A SaleItem must belong to a Sale.
4. A PurchaseItem must belong to a Purchase.
5. A ReturnItem must belong to a Return and reference an original SaleItem.
6. Reserved inventory cannot be consumed by an ordinary conflicting sale.
7. Historical transaction prices and cost snapshots must remain preserved.
8. Payment records must remain historically traceable.
9. Delivery status and payment status remain independent.
10. Deactivating reference/master records must not remove historical transactions.
11. General Expenses may exist without a Sale or Delivery reference.
12. Important operational transactions should retain the responsible User.

## 7. Derived Values

### Customer outstanding balance

Should be calculated from sale obligations and recorded financial transactions rather than maintained as an independently editable amount.

### Profit

Should be calculated using historical sale values and historical acquisition-cost snapshots.

### Available inventory

Must reflect received stock after reservations, sales, returns, damage, and other unavailable states are considered.

The exact inventory-ledger implementation is deferred to later database design.

## 8. Deliberate Deferrals

Stage 3.1 does not define:

- exact SQL data types;
- UUID vs integer key implementation;
- decimal precision;
- indexes;
- database triggers;
- physical check constraints;
- migration scripts;
- ORM classes;
- API schemas;
- audit-log implementation;
- notification storage.

## 9. Diagram Files

- `ERD.drawio`
- `ERD.png`

## 10. Stage 3.1 Completion Gate

Stage 3.1 is complete when:

1. `ERD.drawio`, `ERD.png`, and `DATA_MODEL.md` are committed;
2. the relationships are reviewed for consistency with the SRS and business rules;
3. all core Version 1 transactional data has a logical home;
4. historical cost, price, payment, return, and exchange information can be preserved;
5. the model is validated before physical database design begins.
