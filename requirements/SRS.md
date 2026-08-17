# Software Requirements Specification

## Retail Resale Management System

**Document ID:** RRMS-SRS-001
**Version:** 0.1
**Status:** Draft
**Project Phase:** Requirements Engineering
**Author:** Ibrahim Salman
**Primary Stakeholder:** Business Owner
**Last Updated:** August 2026

---

## Document Revision History

| Version | Date        | Author         | Description                                                 | Status |
| ------- | ----------- | -------------- | ----------------------------------------------------------- | ------ |
| 0.1     | August 2026 | Ibrahim Salman | Initial SRS created from stakeholder requirements discovery | Draft  |

---

# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification defines the functional and non-functional requirements of the Retail Resale Management System.

The document establishes what the proposed system is required to accomplish from the perspectives of the business owners, employees, customers, and system administrators.

It serves as the primary requirements baseline for subsequent system design, implementation, testing, and validation activities.

No implementation technology, database structure, software architecture, or user-interface design is considered final unless it is derived from requirements defined and approved through this document.

---

## 1.2 Project Scope

The Retail Resale Management System is intended to digitize the operations of a clothing resale business that purchases discounted clothing from online retailers, physical stores, and supply markets and resells those products at a margin.

The system is intended to centralize business processes that are currently distributed across handwritten notebooks, Microsoft Excel, WhatsApp, purchase receipts, and manual communication.

The proposed system is expected to support the management of:

* Product purchasing.
* Inventory.
* Product information.
* Customers.
* Customer preferences.
* Sales and orders.
* Point-of-sale transactions.
* Reservations.
* Customer credit.
* Partial and full payments.
* Outstanding balances.
* Deliveries.
* Business expenses.
* Receipts.
* Business reporting and analytics.
* Notifications.
* Product publishing and online discovery.
* Guest customer ordering.

The system is intended initially to support the existing business while providing sufficient extensibility for future growth.

---

## 1.3 Business Background

The business purchases clothing primarily when products are available at discounted prices.

Products are sourced through both online retailers and physical supply markets. Multiple brands are handled, and products are selected primarily according to expected customer demand, season, discount availability, and the business owner's judgment.

The business currently purchases approximately 10 to 50 products per month.

Recent sales volume has averaged approximately 40 products per month.

The business has approximately 15 regular customers while also selling through personal contacts, recommendations, repeat customers, and word of mouth.

Customers currently discover products primarily through:

* WhatsApp Status.
* WhatsApp Catalog.
* Direct enquiries.
* Personal contacts.
* Word of mouth.

Customers generally view product photographs remotely before purchasing.

The business operates primarily in Lahore but may sell to customers throughout Pakistan.

International sales are currently outside the business model.

The business intends to grow substantially beyond its current scale.

---

## 1.4 Current Business Process

The current high-level business process is:

1. The business identifies discounted products online or through physical suppliers.
2. Products are purchased based primarily on discount availability, season, expected demand, and business judgment.
3. Purchase details are recorded in Microsoft Excel and/or handwritten notebooks.
4. Receipts and order numbers are retained.
5. Shipping costs are tracked where applicable.
6. Products ordered remotely remain outside sellable inventory until physically received.
7. Received products are added to available inventory.
8. Product information and photographs are prepared.
9. Products are promoted primarily through WhatsApp.
10. Customers enquire about available products.
11. Products may be reserved temporarily for customers.
12. Customers may purchase using full payment, partial payment, deposits, cash on delivery, or credit.
13. Products are delivered primarily through riders.
14. Customer balances and payments are tracked manually.
15. Sales and business performance are reviewed using existing records.

---

## 1.5 Existing Business Problems

Requirements discovery identified several limitations in the current operating model.

### 1.5.1 Fragmented Record Keeping

Business information is distributed between spreadsheets, notebooks, receipts, WhatsApp conversations, and personal knowledge.

This increases the risk of incomplete, duplicated, or inconsistent information.

### 1.5.2 Credit Management

Customers may purchase using:

* Credit.
* Partial payments.
* Deposits.
* Delayed payments.

The business currently lacks a centralized ledger for tracking each customer's outstanding balance and payment history.

### 1.5.3 Limited Customer Reach

The business currently relies heavily on WhatsApp, personal contacts, and word of mouth.

This restricts product discoverability and future growth.

### 1.5.4 Profit Visibility

The business currently does not use a fixed markup model and does not calculate potential profit before every purchase.

Different products may generate different profit amounts.

The system therefore needs to improve visibility into:

* Acquisition cost.
* Final product cost.
* Selling price.
* Discounts.
* Profit.
* Unsold stock.
* Customer profitability.
* Overall business performance.

### 1.5.5 Inventory Visibility

The business requires improved visibility into:

* Available inventory.
* Reserved inventory.
* Sold products.
* Products awaiting receipt.
* Old inventory.
* Damaged or defective products.

---

# 2. Stakeholders and User Classes

## 2.1 Primary Business Administrator

The primary business administrator is the business owner.

The administrator requires access to the complete operational and financial functionality of the system, including:

* Products.
* Purchases.
* Inventory.
* Customers.
* Orders.
* Payments.
* Credit balances.
* Deliveries.
* Expenses.
* Revenue.
* Profit.
* Analytics.
* User management.

---

## 2.2 Co-Administrator

A second business administrator may assist with management of the business.

The co-administrator is expected to have equivalent or near-equivalent administrative permissions.

The initial intended co-administrators are the business owner and her spouse.

---

## 2.3 Employee

The system is expected to support additional employees as the business grows.

The business currently anticipates an aunt and potentially two additional employees being involved in future operations.

Employees may require operational access while being restricted from selected administrative or sensitive financial functions.

Exact employee permissions shall be defined before implementation.

---

## 2.4 Customer

Customers interact with the business primarily to:

* Browse products.
* Enquire about products.
* Reserve products.
* Place orders.
* Provide delivery details.
* Make payments.
* Receive receipts.

Customers are not currently required to create system accounts.

The customer-facing ordering process shall therefore support guest usage.

---

# 3. Operating Environment and Business Constraints

## 3.1 Geographic Scope

The system shall initially support sales within Pakistan.

The business operates primarily within Lahore while also serving customers elsewhere in Pakistan.

International ordering and international delivery are outside the initial scope.

---

## 3.2 Currency

The primary business currency is Pakistani Rupees (PKR).

Multi-currency accounting is not required for the initial system.

---

## 3.3 Sales Channels

The business currently relies primarily on WhatsApp and direct customer relationships.

The proposed system must therefore complement rather than immediately replace WhatsApp-based communication.

---

## 3.4 Inventory Location

Inventory is currently stored at the business owner's residence.

A formal rack, shelf, or warehouse location system does not currently exist.

The initial system shall therefore not require storage-location information for every product.

The system should permit storage-location support to be added later.

---

## 3.5 Product Images

The current business process generally requires one photograph per product.

The system should not unnecessarily restrict the underlying design to exactly one image if future requirements change.

---

# 4. Assumptions

The following assumptions currently apply:

1. Products are primarily purchased for resale after being identified at discounted prices.
2. Products may also be purchased for personal use by the business owner.
3. Personal purchases must remain distinguishable from business inventory.
4. A product does not become sellable inventory until physically received.
5. Products cannot currently be sold before physical receipt.
6. Customers normally review product photographs remotely.
7. Customers do not require registered customer accounts for the initial online storefront.
8. WhatsApp remains an important communication and product-sharing channel.
9. Card-payment processing is not currently required.
10. The primary system currency is PKR.
11. Inventory is initially operated from a residential location.
12. The business expects future increases in products, employees, and customers.

---

# 5. Terminology

| Term                | Definition                                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Administrator       | Business owner or other authorized user with high-level system access.                                               |
| Employee            | Authorized staff member with restricted operational access.                                                          |
| Customer            | Individual purchasing or reserving products from the business.                                                       |
| Product             | Clothing item or product type managed by the business.                                                               |
| Inventory           | Products physically received and managed as business stock.                                                          |
| Purchase            | Acquisition of products by the business from a supplier or source.                                                   |
| Order               | Customer transaction containing one or more products.                                                                |
| Reservation         | Temporary allocation of available inventory to a customer before completion of a sale.                               |
| Credit Sale         | Sale in which some or all payment remains outstanding after the transaction is recorded.                             |
| Outstanding Balance | Amount still owed by a customer.                                                                                     |
| Final Purchase Cost | Total cost attributed to acquiring a product for the business.                                                       |
| Selling Price       | Price charged to the customer before or after any applicable discount, according to the transaction.                 |
| Gross Profit        | Selling revenue less direct product acquisition cost, subject to the accounting definition finalized for the system. |
| Source              | Retailer, website, physical store, or supply market from which products are purchased.                               |
| POS                 | Point of Sale.                                                                                                       |
| SKU                 | Stock Keeping Unit used to identify a product or inventory item.                                                     |
