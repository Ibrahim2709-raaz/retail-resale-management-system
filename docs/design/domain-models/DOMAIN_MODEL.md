**Document ID:** RRMS-DM-001  
**Version:** 1.0  
**Status:** Baseline  
**Related Requirements:** RRMS-SRS-001 v1.0  
**Related Use Case Model:** RRMS-UCM-001  
**Related Use Case Specifications:** RRMS-UCS-001  

---

## 1. Purpose

This document defines the conceptual domain model for the Retail Resale Management System (RRMS).

The domain model identifies the major business concepts handled by the system and the important relationships between those concepts. Its purpose is to establish a shared understanding of the business domain before logical database design, API design, and implementation begin.

This is a **conceptual model**, not a database schema. It intentionally avoids database-specific details such as SQL data types, foreign-key column names, indexes, normalization decisions, table names, and implementation framework details.

---

## 2. Scope

The model covers the core Version 1 business domain for:

- purchasing;
- products;
- inventory;
- customers;
- reservations;
- sales;
- payments and credit;
- deliveries;
- returns;
- exchanges;
- expenses;
- user accountability.

Future storefront functionality may use the same domain concepts but does not require separate domain entities at this stage.

---

## 3. Core Domain Entities

### 3.1 User

Represents an authenticated internal RRMS user such as a business administrator or employee.

A User performs or records operational activity such as purchases, sales, payments, returns, exchanges, expenses, and delivery updates.

Authorization rules are handled by the application security model rather than by the conceptual domain model itself.

---

### 3.2 Product

Represents the reusable business description of an item that may be purchased and resold.

A Product may contain information such as:

- name;
- brand;
- category and subcategory;
- color;
- material;
- season;
- style;
- brand SKU or barcode where available.

Product information is conceptually separate from a specific purchase, inventory unit, or sale transaction.

---

### 3.3 ProductImage

Represents an image associated with a Product.

A Product may have zero or more ProductImages. Version 1 may initially use a single image while the domain supports multiple images in the future.

---

### 3.4 Purchase

Represents an acquisition transaction from an online retailer, physical store, supply market, or another product source.

A Purchase records the overall acquisition event and may include:

- source/store;
- purchase date;
- external order number;
- shipping/acquisition costs;
- receipt information;
- purchase classification.

A Purchase may be classified as either:

- BUSINESS; or
- PERSONAL.

Personal purchases are excluded from business inventory and profitability calculations.

---

### 3.5 PurchaseItem

Represents a product line within a Purchase.

A Purchase contains one or more PurchaseItems. Each PurchaseItem refers to a Product and captures transaction-specific acquisition information such as quantity and purchase cost.

The separation between Purchase and PurchaseItem allows a single purchase transaction to contain multiple products.

---

### 3.6 InventoryItem

Represents sellable or otherwise tracked stock held by the business.

Inventory exists only after relevant purchased products have been physically received.

An InventoryItem conceptually captures the stock state of a received product and may move through statuses such as:

- Received;
- Available;
- Reserved;
- Sold;
- Damaged;
- Returned;
- On Hold.

InventoryItem is distinct from Product because Product describes *what the item is*, while InventoryItem represents stock that the business actually owns and tracks.

---

### 3.7 Customer

Represents a person who purchases or reserves products from the business.

A Customer may have:

- contact information;
- delivery address;
- city;
- product preferences;
- sale history;
- payment history;
- outstanding balance.

A Customer may participate in many reservations, sales, payments, returns, exchanges, and deliveries over time.

---

### 3.8 Reservation

Represents a temporary hold of inventory for a Customer.

A Reservation connects a Customer to an InventoryItem and records the hold period and reservation state.

The normal reservation period is 48 hours, but it may be manually extended.

Reservation expiry generates a notification but does not automatically release inventory. Release, extension, cancellation, or override remains an authorized business decision.

---

### 3.9 Sale

Represents a confirmed customer sales transaction.

A Sale belongs to a Customer and contains one or more SaleItems.

A Sale is responsible for the commercial transaction as a whole, including:

- transaction total;
- discounts;
- payment obligation;
- sales history;
- profitability reporting.

Payment status and delivery status are conceptually independent.

---

### 3.10 SaleItem

Represents one product/inventory line within a Sale.

A Sale contains one or more SaleItems.

A SaleItem links a transaction to the InventoryItem being sold and preserves transaction-specific information such as the final selling price and discount.

Historical transaction prices must remain preserved even if the Product or future selling price later changes.

---

### 3.11 Payment

Represents money received from a Customer.

A Sale may have zero or more Payments, allowing:

- full payment;
- partial payment;
- deposits;
- credit sales;
- later settlement of outstanding balances.

Payment methods may include:

- Cash;
- Bank Transfer;
- JazzCash;
- Cash on Delivery.

Payments remain separate historical financial transactions and must not be silently overwritten.

---

### 3.12 Delivery

Represents fulfillment of a customer order through physical delivery.

A Sale may have no Delivery or one Delivery.

A Delivery may contain:

- internal tracking/reference number;
- customer delivery details;
- rider information;
- delivery fee;
- delivery status.

Typical delivery states include:

- Processing;
- Packed;
- Shipped;
- Out for Delivery;
- Delivered;
- Failed Delivery.

The Delivery Rider is an indirect participant in Version 1; rider interactions are recorded manually by authorized internal users.

---

### 3.13 Return

Represents a return transaction linked to an original Sale.

A Return preserves the original Sale rather than replacing or deleting it.

A Return may contain one or more ReturnItems and may result in:

- inventory restoration;
- damaged/non-sellable inventory;
- a cash refund;
- an online-transfer refund;
- no refund where no money is owed.

---

### 3.14 ReturnItem

Represents an individual returned SaleItem.

A Return contains one or more ReturnItems.

Each ReturnItem references the original SaleItem so that the system can preserve the history of:

- what was sold;
- what was returned;
- what inventory state changed;
- what financial adjustment occurred.

---

### 3.15 Exchange

Represents replacement of a previously purchased item with another product.

An Exchange is associated with the original Sale and typically includes a return side and a replacement side.

The replacement product may be:

- more expensive, causing the Customer to owe the difference;
- cheaper, causing the business to refund the difference or retain it as Customer credit;
- equal in value, requiring no financial difference.

Exchange history must remain traceable to the original transaction.

---

### 3.16 Expense

Represents a business expense used in net-profit calculations.

An Expense may be:

- general, with no specific order association; or
- linked to a particular Sale or Delivery.

Examples include rider charges and petrol costs.

The conceptual model therefore allows an Expense to exist independently or to relate to an operational transaction.

---

## 4. Major Domain Relationships

### 4.1 Purchasing and Product Relationships

- A Purchase contains one or more PurchaseItems.
- A PurchaseItem refers to one Product.
- A Product may appear in many PurchaseItems over time.
- A Product may have zero or more ProductImages.
- Receiving a business PurchaseItem creates or increases tracked InventoryItem stock.

---

## 4.2 Inventory and Reservation Relationships

- A Product may have associated InventoryItems.
- A Customer may place zero or more Reservations.
- A Reservation holds inventory for one Customer.
- A Reservation applies to an InventoryItem.
- Inventory held by an active reservation is unavailable for an ordinary conflicting sale unless an authorized override occurs.

---

## 4.3 Customer and Sales Relationships

- A Customer may have zero or more Sales.
- A Sale belongs to one Customer.
- A Sale contains one or more SaleItems.
- A SaleItem consumes or references tracked InventoryItem stock.

---

## 4.4 Payment Relationships

- A Sale may have zero or more Payments.
- Multiple Payments may settle a single Sale.
- Customer outstanding balance is derived from unpaid obligations and recorded Payments.
- A Payment remains an independent historical financial transaction.

---

## 4.5 Delivery Relationships

- A Sale may have zero or one Delivery.
- Delivery status does not determine payment status.
- Delivery-related expenses may optionally be associated with a Delivery or Sale.

---

## 4.6 Return Relationships

- A Sale may have zero or more Returns.
- A Return contains one or more ReturnItems.
- Each ReturnItem references an original SaleItem.
- A returned item may restore inventory when suitable for resale.

---

## 4.7 Exchange Relationships

- A Sale may have zero or more Exchanges.
- An Exchange may incorporate a return of an original SaleItem.
- An Exchange may reference a replacement SaleItem or replacement inventory.
- Financial difference may result in additional payment, immediate refund, or Customer credit.

---

## 4.8 Expense Relationships

- An Expense may exist independently as a general business expense.
- An Expense may optionally relate to a Sale.
- An Expense may optionally relate to a Delivery.
- Expenses contribute to net-profit reporting.

---

## 4.9 User Accountability Relationships

Users conceptually create, record, approve, or update business transactions.

Important operational records should retain sufficient information to identify the User responsible for relevant business activity.

Detailed audit-event modeling will be refined later and is not expanded into database tables at this stage.

---

## 5. Conceptual Multiplicities

The domain model uses the following important multiplicities:

| Relationship | Conceptual Multiplicity |
|---|---|
| Purchase → PurchaseItem | 1 to 1..* |
| Product → PurchaseItem | 1 to 0..* |
| Product → ProductImage | 1 to 0..* |
| Customer → Reservation | 1 to 0..* |
| Customer → Sale | 1 to 0..* |
| Sale → SaleItem | 1 to 1..* |
| Sale → Payment | 1 to 0..* |
| Sale → Delivery | 1 to 0..1 |
| Sale → Return | 1 to 0..* |
| Return → ReturnItem | 1 to 1..* |
| Sale → Exchange | 1 to 0..* |
| Sale / Delivery → Expense | optional |

These multiplicities describe business concepts only and may be refined during logical database design.

---

## 6. Domain Invariants

The following rules must remain true across the domain:

1. Inventory shall never become negative.
2. A product cannot be sold before it has been physically received.
3. Personal purchases shall not create business inventory.
4. Personal purchases shall not contribute to business profit calculations.
5. Reserved stock shall not be available for ordinary conflicting sales.
6. Reservation expiry does not automatically release stock.
7. Historical sale prices shall remain preserved.
8. Payment history shall remain preserved.
9. Payment status and delivery status are independent.
10. A Return must preserve the original Sale and SaleItem history.
11. An Exchange must preserve traceability to the original transaction.
12. Returned inventory may become Available only when it remains suitable for resale.
13. Below-cost sales are allowed only after the applicable warning/authorization flow.
14. Expenses may be general or transaction-linked.
15. Important business operations must remain attributable to an authenticated User.

---

## 7. Deliberate Exclusions

The following are intentionally excluded from this conceptual domain model:

- SQL data types;
- table and column definitions;
- primary-key implementation;
- foreign-key column names;
- indexes;
- database constraints;
- normalization decisions;
- API endpoints;
- frontend components;
- backend services;
- framework-specific classes;
- deployment architecture.

These decisions belong to later design stages.

---

## 8. Diagram Files

- `DOMAIN_MODEL.drawio` — editable conceptual domain model.
- `DOMAIN_MODEL.png` — exported visual representation.

---

## 9. Modeling Note

The domain model establishes the business vocabulary and relationships that later logical design must support.

It should not be treated as the final ERD.

The later ERD may introduce additional implementation entities, associative entities, audit structures, status/history structures, or normalized lookup tables where technically appropriate.