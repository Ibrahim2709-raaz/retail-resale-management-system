# RRMS Use Case Model

**Document ID:** RRMS-UCM-001  
**Version:** 1.0  
**Status:** Baseline  
**Related Requirements:** RRMS-SRS-001 v1.0

## 1. Purpose

This document describes the major user interactions with the Retail Resale Management System (RRMS).

It complements the system context model by identifying the direct actors that interact with RRMS and the major use cases the system must support.

The use case model is intended to support later activity including:
- domain modeling;
- ERD development;
- workflow design;
- UI planning;
- API planning;
- test-case creation.

## 2. Direct Actors

### 2.1 Business Administrator
The business administrator is the primary system user and can perform purchasing, inventory, customer, sales, payment, delivery, reporting, and user-management operations.

### 2.2 Employee
Employees perform authorized operational work in the system, including product, inventory, customer, sales, payment, delivery, return, and exchange activities.

### 2.3 Customer
Customers are future direct users of the customer-facing storefront and may browse products, view product information, and submit order requests.

## 3. Indirect / Non-Direct Participants

The following entities are relevant to the business context but are not modeled as direct system actors in the primary use case diagram because they do not directly use the software in Version 1:

- Product Source / Supplier
- Delivery Rider
- WhatsApp

Their information is represented in the system through actions performed by authorized internal users.

## 4. Use Case List

### 4.1 Internal Version 1 Use Cases

| ID | Use Case | Primary Actor |
|---|---|---|
| UC-001 | Manage Products | Business Administrator, Employee |
| UC-002 | Manage Brands & Categories | Business Administrator |
| UC-003 | Record Purchase | Business Administrator |
| UC-004 | Receive Product | Business Administrator, Employee |
| UC-005 | Manage Inventory | Business Administrator, Employee |
| UC-006 | Search Inventory | Business Administrator, Employee |
| UC-007 | Manage Customers | Business Administrator, Employee |
| UC-008 | View Customer History | Business Administrator, Employee |
| UC-009 | View Customer Outstanding Balance | Business Administrator, Employee |
| UC-010 | Reserve Product | Business Administrator, Employee |
| UC-011 | Create Sale | Business Administrator, Employee |
| UC-012 | Record Payment | Business Administrator, Employee |
| UC-013 | Manage Credit / Outstanding Balance | Business Administrator, Employee |
| UC-014 | Generate Receipt | Business Administrator, Employee |
| UC-015 | Manage Delivery | Business Administrator, Employee |
| UC-016 | Update Delivery Status | Business Administrator, Employee |
| UC-017 | Process Return | Business Administrator, Employee |
| UC-018 | Process Exchange | Business Administrator, Employee |
| UC-019 | Record Expense | Business Administrator, Employee |
| UC-020 | View Dashboard | Business Administrator, Employee |
| UC-021 | View Reports | Business Administrator, Employee |
| UC-022 | Manage Users | Business Administrator |

### 4.2 Future Customer-Facing Use Cases

| ID | Use Case | Primary Actor |
|---|---|---|
| UC-023 | Browse Products | Customer |
| UC-024 | View Product Details | Customer |
| UC-025 | Submit Order Request | Customer |

## 5. Use Case Relationships

### 5.1 Includes
- Create Sale includes Search Inventory.
- Create Sale includes Manage Customers or selecting an existing customer.
- Create Sale includes Record Payment.
- Create Sale includes Generate Receipt.
- Submit Order Request includes Browse Products.
- Submit Order Request includes View Product Details.

### 5.2 Additional Logical Relationships
- Process Exchange depends on return and replacement-item handling.
- Receive Product supports the transition from ordered/in-transit items to available inventory.
- Manage Credit / Outstanding Balance depends on payment recording and sales history.

## 6. Brief Use Case Descriptions

### UC-001 — Manage Products
Authorized internal users create, edit, and maintain product information including classification, pricing, image, notes, and condition.

### UC-003 — Record Purchase
An administrator records product acquisition details including source, cost, shipping, receipt reference, and business/personal purchase classification.

### UC-004 — Receive Product
An authorized internal user marks previously acquired product as physically received so that it may become sellable inventory.

### UC-007 — Manage Customers
Authorized internal users create and update customer records containing required business information.

### UC-010 — Reserve Product
An authorized internal user reserves inventory for a customer and records the reservation duration and status.

### UC-011 — Create Sale
An authorized internal user creates a customer sale, selects inventory, applies pricing and discounts, records transaction values, and confirms the sale.

### UC-012 — Record Payment
An authorized internal user records a full or partial payment against a sale or customer balance.

### UC-013 — Manage Credit / Outstanding Balance
An authorized internal user reviews and manages customer outstanding balances created by credit or partial-payment transactions.

### UC-014 — Generate Receipt
The system produces a receipt or invoice for a sale, including totals, amounts paid, and outstanding balance.

### UC-015 — Manage Delivery
An authorized internal user records delivery details, charges, and the internal delivery reference.

### UC-017 — Process Return
An authorized internal user records a valid return and its effect on the sale and inventory.

### UC-018 — Process Exchange
An authorized internal user records the exchange of a product, including inventory effects and any money owed by either party.

### UC-020 — View Dashboard
Authorized internal users review a summary of operational and financial activity.

### UC-021 — View Reports
Authorized internal users view reporting and analytics such as revenue, profit, credit, and inventory-ageing information.

### UC-022 — Manage Users
An administrator creates, enables, disables, and manages internal user accounts.

### UC-023 — Browse Products
A customer browses available product information through a future storefront.

### UC-024 — View Product Details
A customer views detailed information for a selected product.

### UC-025 — Submit Order Request
A customer submits an order request for later business approval.

## 7. Diagram Files

- `USE_CASE_DIAGRAM.drawio`
- `USE_CASE_DIAGRAM.png`