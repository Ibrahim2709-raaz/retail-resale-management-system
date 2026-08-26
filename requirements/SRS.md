# Software Requirements Specification

## Retail Resale Management System

**Document ID:** RRMS-SRS-001
**Version:** 0.5
**Status:** Draft
**Project Phase:** Requirements Engineering
**Author:** Ibrahim Salman
**Primary Stakeholder:** Business Owner
**Last Updated:** August 2026

---

## Document Revision History

| Version | Date        | Author         | Description                                                 | Status |
| ------- | ----------- | -------------- | ----------------------------------------------------------- | ------ |
| 0.5     | August 2026 | Ibrahim Salman | Defined release scope, exclusions, constraints, dependencies and Version 1 acceptance criteria      | Draft  |

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

# 6. Functional Requirements

This section defines the required functional behavior of the Retail Resale Management System.

Requirements are grouped by functional domain and assigned unique identifiers for future traceability, testing, and change management.

The keyword **shall** indicates a mandatory system requirement.

---

## 6.1 Authentication and User Management

**FR-AUTH-001**
The system shall require administrative and employee users to authenticate before accessing protected business functionality.

**FR-AUTH-002**
The system shall support at least two internal user roles:

* Administrator
* Employee

**FR-AUTH-003**
The system shall permit multiple administrator accounts.

**FR-AUTH-004**
The system shall allow an administrator to create employee accounts.

**FR-AUTH-005**
The system shall allow an administrator to activate or deactivate employee accounts.

**FR-AUTH-006**
The system shall restrict access to functionality based on the authenticated user's assigned role.

**FR-AUTH-007**
The system shall prevent customers from accessing administrative functionality.

**FR-AUTH-008**
Employee users may access product cost, product profit, business revenue,
and customer outstanding-balance information unless future role configuration
explicitly restricts such access.

---

# 6.2 Brand, Category, and Product Classification

**FR-CAT-001**
The system shall allow administrators to create and manage product brands.

**FR-CAT-002**
The system shall allow administrators to create and manage product categories.

**FR-CAT-003**
The system shall allow categories to contain subcategories.

**FR-CAT-004**
The system shall allow products to be associated with a brand.

**FR-CAT-005**
The system shall allow products to be associated with a category and, where applicable, a subcategory.

---

# 6.3 Product Management

**FR-PROD-001**
The system shall allow authorized users to create product records.

**FR-PROD-002**
The system shall assign an internal unique identifier to every product record.

**FR-PROD-003**
The system shall support an internal SKU for products.

**FR-PROD-004**
The system shall allow a brand-provided SKU to be recorded when available.

**FR-PROD-005**
The system shall allow a barcode value to be recorded for a product when available.

**FR-PROD-006**
The system shall store the product name.

**FR-PROD-007**
The system shall store the product brand.

**FR-PROD-008**
The system shall store the product category.

**FR-PROD-009**
The system shall optionally store a product subcategory.

**FR-PROD-010**
The system shall store the product color.

**FR-PROD-011**
The system shall store the product material where applicable.

**FR-PROD-012**
The system shall store the product style where applicable.

**FR-PROD-013**
The system shall store the intended season where applicable.

**FR-PROD-014**
The system shall not require a clothing size for products.

This reflects the current business model, which primarily sells unstitched clothing.

**FR-PROD-015**
The system shall allow notes to be attached to a product.

**FR-PROD-016**
The system shall allow an authorized user to edit product information.

**FR-PROD-017**
The system shall preserve product records required for historical sales and reporting rather than permanently removing referenced products.

---

# 6.4 Product Images and Documents

**FR-MEDIA-001**
The system shall allow at least one image to be associated with each product.

**FR-MEDIA-002**
The underlying system shall permit support for multiple images per product even though the current business generally uses one image.

**FR-MEDIA-003**
The system shall allow purchase receipts to be stored or referenced digitally.

---

# 6.5 Product Condition

**FR-COND-001**
The system shall allow the condition of a product to be recorded.

**FR-COND-002**
The system shall support at least the following conditions:

* New with tags
* New without tags
* Opened
* Defective
* Damaged

**FR-COND-003**
The system shall prevent damaged or defective products from appearing as normally available stock unless explicitly authorized.

---

# 6.6 Purchasing and Product Acquisition

**FR-PUR-001**
The system shall allow authorized users to record business purchases.

**FR-PUR-002**
The system shall record the source or store from which a purchase was made.

**FR-PUR-003**
The system shall support both online and physical purchase sources.

**FR-PUR-004**
The system shall allow an external order number to be recorded for online purchases.

**FR-PUR-005**
The system shall record the purchase date.

**FR-PUR-006**
The system shall record the purchase price paid for each purchased product.

**FR-PUR-007**
The system shall allow shipping costs associated with a purchase to be recorded.

**FR-PUR-008**
The system shall allow rider-related or transport expenses associated with purchasing to be recorded where applicable.

**FR-PUR-009**
The system shall allow petrol expenses associated with business purchasing or delivery activity to be recorded.

**FR-PUR-010**
The system shall distinguish between purchases intended for:

* Business resale
* Personal use

**FR-PUR-011**
Products designated as personal purchases shall not be included in business inventory calculations.

**FR-PUR-012**
Personal purchases shall not contribute to business revenue or profit reports.

---

# 6.7 Purchase and Inventory Status

**FR-INV-001**
The system shall distinguish between products that have been ordered and products that have physically been received.

**FR-INV-002**
A product shall not be considered sellable inventory until it has been physically received.

**FR-INV-003**
The system shall support the following relevant acquisition and inventory states:

* Ordered
* In Transit
* Received
* Available
* Reserved
* On Hold
* Sold
* Delivered
* Damaged
* Cancelled
* Returned
* Exchanged

**FR-INV-004**
The system shall allow an authorized user to mark an ordered product as received.

**FR-INV-005**
Once a valid business product has been received, the system shall allow it to become available inventory.

**FR-INV-006**
The system shall not permit a product to be sold before it has been physically received.

---

# 6.8 Inventory Quantity

**FR-QTY-001**
The system shall allow a quantity to be associated with a product.

**FR-QTY-002**
The system shall support products for which only one physical unit exists.

**FR-QTY-003**
The system shall support rare situations in which multiple identical units of the same product are purchased.

**FR-QTY-004**
The system shall reduce available quantity when a unit is sold.

**FR-QTY-005**
The system shall prevent available inventory quantity from becoming negative.

**FR-QTY-006**
The system shall not require low-stock notifications.

---

# 6.9 Product Pricing

**FR-PRICE-001**
The system shall store the original retail price when available.

**FR-PRICE-002**
The system shall store the sale or acquisition price paid by the business.

**FR-PRICE-003**
The system shall calculate or store the final purchase cost attributable to a product.

**FR-PRICE-004**
The system shall store the intended selling price.

**FR-PRICE-005**
The system shall allow a minimum acceptable selling price to be recorded.

**FR-PRICE-006**
The system shall calculate the monetary discount between original retail price and current selling price where the original retail price is available.

**FR-PRICE-007**
The system shall calculate the percentage discount from the original retail price where appropriate.

**FR-PRICE-008**
The system shall display estimated profit for a proposed selling price.

**FR-PRICE-009**
The system shall allow authorized users to manually change the final selling price during a sale.

**FR-PRICE-010**
The system shall allow a custom discount to be applied to a sale.

**FR-PRICE-011**
The system shall permit products to be sold at cost.

**FR-PRICE-012**
The system shall warn an authorized user when a proposed selling price
is below the product's final cost.

**FR-PRICE-013**
The system shall not require a fixed percentage markup.

**FR-PRICE-014**
An authorized user shall be able to acknowledge the below-cost warning
and continue the transaction.
---

# 6.10 Product Search and Filtering

**FR-SEARCH-001**
The system shall allow authorized users to search inventory by product name.

**FR-SEARCH-002**
The system shall allow products to be searched or filtered by brand.

**FR-SEARCH-003**
The system shall allow products to be searched or filtered by category or clothing type.

**FR-SEARCH-004**
The system shall allow products to be searched or filtered by color.

**FR-SEARCH-005**
The system should support additional filtering by:

* Material
* Style
* Season
* Inventory status
* Purchase source
* Purchase date
* Price range

---

# 6.11 Customer Management

**FR-CUS-001**
The system shall allow authorized users to create customer records.

**FR-CUS-002**
The system shall store the customer's name.

**FR-CUS-003**
The system shall store the customer's phone number.

**FR-CUS-004**
The system shall store the customer's WhatsApp number where different from the primary phone number.

**FR-CUS-005**
The system shall allow a customer address to be stored.

**FR-CUS-006**
The system shall store the customer's city.

**FR-CUS-007**
The system shall allow preferred brands to be associated with a customer.

**FR-CUS-008**
The system shall allow preferred clothing types to be associated with a customer.

**FR-CUS-009**
The system shall maintain customer purchase history.

**FR-CUS-010**
The system shall calculate and display the customer's current outstanding balance.

**FR-CUS-011**
The system shall maintain historical customer transactions.

**FR-CUS-012**
The system shall not require a customer's birthday.

**FR-CUS-013**
The system shall not require customer email addresses.

**FR-CUS-014**
The system shall not require customer Instagram information.

---

# 6.12 Reservation Management

**FR-RES-001**
The system shall allow available inventory to be reserved for a customer.

**FR-RES-002**
A reservation shall have a default duration of 48 hours.

**FR-RES-003**
The system shall allow an authorized user to manually extend a reservation.

**FR-RES-004**
The system shall record the reservation start time.

**FR-RES-005**
The system shall record the reservation expiry time.

**FR-RES-006**
The system shall notify authorized users when a reservation has reached or passed its expiry time.

**FR-RES-007**
The system shall not automatically release an expired reservation without authorization from a business user.

**FR-RES-008**
An actively reserved inventory unit shall not be sold to another customer unless the reservation is first cancelled, released, or overridden by an authorized user.

**FR-RES-009**
The system shall allow an authorized user to cancel or release a reservation.

---

# 6.13 Sales and Point of Sale

**FR-SALE-001**
The system shall allow authorized users to create a sale.

**FR-SALE-002**
A sale shall be associated with a customer.

**FR-SALE-003**
A sale shall support one or more products.

**FR-SALE-004**
The system shall record the selling price of each item at the time of sale.

**FR-SALE-005**
The system shall preserve the transaction price even if the product's default selling price changes later.

**FR-SALE-006**
The system shall allow a custom discount to be recorded.

**FR-SALE-007**
The system shall calculate the final order amount.

**FR-SALE-008**
The system shall update inventory after a sale is confirmed.

**FR-SALE-009**
The system shall maintain historical sales records.

**FR-SALE-010**
The system shall support cash-on-delivery sales.

---

# 6.14 Customer Order Requests

**FR-ORD-001**
The customer-facing storefront shall allow customers to submit an order request without creating an account.

**FR-ORD-002**
A submitted online order request shall not automatically become a confirmed sale.

**FR-ORD-003**
The system shall place customer-submitted orders into a pending approval state.

**FR-ORD-004**
An authorized business user shall review an online order request before confirming or rejecting it.

**FR-ORD-005**
The system shall allow an authorized user to approve an order request.

**FR-ORD-006**
The system shall allow an authorized user to reject an order request.

*FR-ORD-007
When a customer submits an online order request, the requested inventory shall be placed on a temporary hold until an authorized business user approves or rejects the request.

FR-ORD-008
Temporary holds created by online order requests shall not expire automatically.

FR-ORD-009
An authorized business user shall manually release the temporary hold when an order request is rejected or cancelled.

FR-ORD-010
Inventory placed on a temporary hold for an online order request shall not be available for another confirmed sale unless the hold is manually released or overridden by an authorized user.

---

# 6.15 Payments

**FR-PAY-001**
The system shall support full payments.

**FR-PAY-002**
The system shall support partial payments.

**FR-PAY-003**
The system shall support customer deposits.

**FR-PAY-004**
The system shall support credit sales.

**FR-PAY-005**
The system shall support at least the following payment methods:

* Cash
* Bank transfer
* JazzCash
* Cash on delivery

**FR-PAY-006**
The system shall record each received payment as an individual transaction.

**FR-PAY-007**
The system shall record the payment amount.

**FR-PAY-008**
The system shall record the payment date.

**FR-PAY-009**
The system shall record the applicable payment method.

**FR-PAY-010**
The system shall calculate the remaining unpaid balance for an order.

**FR-PAY-011**
The system shall calculate the total outstanding balance associated with a customer.

**FR-PAY-012**
The system shall support the following payment states:

* Unpaid
* Partially Paid
* Paid

**FR-PAY-013**
The system shall not require every credit sale to have a fixed payment due date.

**FR-PAY-014**
The system shall allow an optional payment due date to be recorded when one is agreed with the customer.

**FR-PAY-015**
The system shall not enforce customer credit limits.

---

# 6.16 Customer Credit Ledger

**FR-CREDIT-001**
The system shall maintain a financial ledger for customer credit activity.

**FR-CREDIT-002**
The ledger shall identify amounts charged to the customer.

**FR-CREDIT-003**
The ledger shall identify payments received from the customer.

**FR-CREDIT-004**
The ledger shall maintain a running outstanding balance.

**FR-CREDIT-005**
Authorized users shall be able to review a customer's outstanding transactions.

**FR-CREDIT-006**
Authorized users shall be able to review a customer's historical payments.

**FR-CREDIT-007**
Where a due date exists, the system shall be capable of identifying unpaid amounts whose due date has passed.

---

# 6.17 Delivery Management

**FR-DEL-001**
The system shall allow delivery information to be associated with an order.

**FR-DEL-002**
The system shall record the customer delivery address.

**FR-DEL-003**
The system shall record the applicable delivery fee.

**FR-DEL-004**
The system shall support rider-based deliveries.

**FR-DEL-005**
The system shall generate or assign an internal unique tracking number for deliveries.

**FR-DEL-006**
The internal tracking number shall not depend on an external courier provider.

**FR-DEL-007**
The system shall support the following delivery states:

* Processing
* Packed
* Shipped
* Out for Delivery
* Delivered
* Failed Delivery

**FR-DEL-008**
The system shall allow authorized users to update delivery status.

**FR-DEL-009**
The system shall allow rider-related delivery costs to be recorded.

---

# 6.18 Returns

**FR-RET-001**
The system shall support customer returns.

**FR-RET-002**
A standard return shall only be accepted within seven days of the relevant sale.

**FR-RET-003**
A returned product shall be required to be in its original condition.

**FR-RET-004**
The system shall record the date of the return.

**FR-RET-005**
The system shall record the reason for the return.

**FR-RET-006**
The system shall allow an authorized user to approve or reject a return.

**FR-RET-007**
Approved returned products shall only be restored to available inventory if their condition permits resale.

**FR-RET-008**
The system shall retain the original sale record when a return occurs.

**FR-RET-009**
The system shall allow an approved refund to be recorded using cash
or online transfer.

**FR-RET-010**
The system shall record the refund amount, date, method, and associated
return transaction.
---

# 6.19 Exchanges

**FR-EXC-001**
The system shall support product exchanges.

**FR-EXC-002**
The system shall record the product being returned as part of the exchange.

**FR-EXC-003**
The system shall record the replacement product.

**FR-EXC-004**
The system shall calculate any monetary difference between the returned product value and replacement product value.

**FR-EXC-005**
If the replacement product costs more, the system shall record the additional amount owed by the customer.

**FR-EXC-006**
If the replacement product costs less, the system shall record the amount owed back to the customer.

**FR-EXC-007**
The system shall update inventory appropriately for both products involved in an exchange.

**FR-EXC-008**
The system shall preserve the exchange history for audit and reporting purposes.

**FR-EXC-009**
When an exchange creates an amount owed to the customer, the system
shall allow the amount to be refunded immediately.

**FR-EXC-010**
The system shall alternatively allow the amount to be retained as
customer credit.

**FR-EXC-011**
The selected settlement method shall be recorded as part of the exchange.
---

# 6.20 Expenses

**FR-EXP-001**
The system shall allow authorized users to record business expenses.

**FR-EXP-002**
The system shall support at least the following expense categories:

* Shipping
* Rider costs
* Petrol

**FR-EXP-003**
The system shall record the expense amount.

**FR-EXP-004**
The system shall record the expense date.

**FR-EXP-005**
The system shall allow a description or note to be associated with an expense.

**FR-EXP-006**
The system shall permit expenses to be associated with a purchase or order where applicable.

**FR-EXP-007**
Recorded business expenses shall be available for use in net-profit reporting.

**FR-EXP-008**
The system shall allow rider and petrol expenses to be recorded as
general business expenses.

**FR-EXP-009**
The system shall allow rider and petrol expenses to be associated with
a specific customer order when applicable.

---

# 6.21 Receipt and Invoice Generation

**FR-REC-001**
The system shall generate a receipt or invoice for completed sales.

**FR-REC-002**
The receipt shall contain the business name.

**FR-REC-003**
The receipt shall support inclusion of the business logo.

**FR-REC-004**
The receipt shall contain a unique transaction or invoice number.

**FR-REC-005**
The receipt shall display purchased products.

**FR-REC-006**
The receipt shall display applicable prices and discounts.

**FR-REC-007**
The receipt shall display the order total.

**FR-REC-008**
The receipt shall display the amount paid.

**FR-REC-009**
The receipt shall display any remaining customer balance.

**FR-REC-010**
The system shall allow a receipt to be printed.

**FR-REC-011**
The system shall allow a receipt to be generated in PDF form.

**FR-REC-012**
The system shall support sharing receipt information through WhatsApp.

---

# 6.22 Storefront Product Publishing

**FR-STORE-001**
The system shall allow authorized users to choose whether a product is visible on the customer-facing storefront.

**FR-STORE-002**
Available products shall be capable of being displayed on the storefront.

**FR-STORE-003**
Sold products may remain visible on the storefront.

**FR-STORE-004**
Sold products displayed on the storefront shall clearly indicate that they are sold or unavailable.

**FR-STORE-005**
The system shall support products marked as Coming Soon.

**FR-STORE-006**
The system shall allow the business to choose whether the original retail price is displayed for an individual product.

**FR-STORE-007**
Where the original retail price is displayed, the storefront shall be capable of displaying the resulting discount percentage.

**FR-STORE-008**
The storefront shall not be required to publicly display exact inventory quantity.

**FR-STORE-009**
The storefront shall not be required to display low-stock messages such as "Only 1 left."

---

# 6.23 Storefront Search and Browsing

**FR-WEB-001**
Customers shall be able to browse products without authentication.

**FR-WEB-002**
Customers shall be able to search products by brand.

**FR-WEB-003**
Customers shall be able to search or filter products by clothing type or category.

**FR-WEB-004**
Customers shall be able to search or filter products by color.

**FR-WEB-005**
Customers shall be able to view product details.

**FR-WEB-006**
Customers shall be able to view the product image.

**FR-WEB-007**
Customers shall be able to view the current selling price.

**FR-WEB-008**
Customers shall be able to submit an order request as guests.

---

# 6.24 WhatsApp Support

**FR-WA-001**
The system shall support sharing product information through WhatsApp.

**FR-WA-002**
A shared product reference should contain sufficient information or a link to identify the relevant product.

**FR-WA-003**
The system should support a customer enquiry action that identifies the product being discussed.

**FR-WA-004**
The system shall support sharing receipt information through WhatsApp.

---

# 6.25 Notifications

**FR-NOT-001**
The system shall support notifications for reservation expiry.

**FR-NOT-002**
The system shall support notifications for outstanding payments where appropriate.

**FR-NOT-003**
The system shall support notifications for inventory that has remained unsold for a configurable period such as 90 days.

**FR-NOT-004**
The system shall support notifications related to received purchasing shipments.

**FR-NOT-005**
The system shall support notifications for new customer order requests.

**FR-NOT-006**
The system shall support notifications for return requests.

**FR-NOT-007**
The system shall support notifications for pending deliveries.

**FR-NOT-008**
The system may support future price-reduction suggestions for aged inventory.

**FR-NOT-009**
The system shall not require low-stock notifications.

**FR-NOT-010**
The system shall not require customer birthday reminders.

---

# 6.26 Reporting and Analytics

**FR-REP-001**
The system shall calculate total sales revenue over a selected period.

**FR-REP-002**
The system shall calculate gross profit over a selected period.

**FR-REP-003**
The system shall calculate net profit using applicable recorded business expenses.

**FR-REP-004**
The system shall calculate current inventory value.

**FR-REP-005**
The system shall report the number of items sold.

**FR-REP-006**
The system shall calculate average selling price.

**FR-REP-007**
The system shall calculate average product margin where sufficient data exists.

**FR-REP-008**
The system shall report sales by brand.

**FR-REP-009**
The system shall report sales by category.

**FR-REP-010**
The system shall report sales by month.

**FR-REP-011**
The system shall identify top customers according to defined sales criteria.

**FR-REP-012**
The system shall support analysis of customer profitability.

**FR-REP-013**
The system shall identify top-selling brands.

**FR-REP-014**
The system shall report products that have remained unsold for more than 30 days.

**FR-REP-015**
The system shall report products that have remained unsold for more than 90 days.

**FR-REP-016**
The system shall report total outstanding customer balances.

**FR-REP-017**
The system shall allow administrators to view historical business performance.

---

# 6.27 Auditability and Historical Records

**FR-AUD-001**
The system shall preserve historical sales transactions.

**FR-AUD-002**
The system shall preserve payment transaction history.

**FR-AUD-003**
The system shall preserve return history.

**FR-AUD-004**
The system shall preserve exchange history.

**FR-AUD-005**
The system shall preserve relevant inventory changes required to explain product availability.

**FR-AUD-006**
Financial transaction records shall not be silently overwritten when subsequent corrections are required.

**FR-AUD-007**
Changes that materially affect financial or inventory history should be traceable to the relevant business action.

---

# 6.28 Administrative Dashboard

**FR-DASH-001**
The system shall provide administrators with a business dashboard.

**FR-DASH-002**
The dashboard shall display current sales revenue for a selected period.

**FR-DASH-003**
The dashboard shall display profit information.

**FR-DASH-004**
The dashboard shall display current inventory value.

**FR-DASH-005**
The dashboard shall display outstanding customer credit.

**FR-DASH-006**
The dashboard shall display relevant notifications or business alerts.

**FR-DASH-007**
The dashboard should provide access to commonly used management functions.


# 7. Non-Functional Requirements

This section defines the quality, security, performance, reliability, usability, maintainability, and operational requirements of the Retail Resale Management System.

---

## 7.1 Security

**NFR-SEC-001**
The system shall require authenticated access for all internal administrative and employee functionality.

**NFR-SEC-002**
Passwords shall not be stored in plain text.

**NFR-SEC-003**
The system shall use secure password hashing appropriate to the implementation environment.

**NFR-SEC-004**
The system shall enforce role-based access control for protected functionality.

**NFR-SEC-005**
Administrative users shall be able to perform functions that may be unavailable to employees.

**NFR-SEC-006**
Customer-facing users shall not be able to access internal financial, purchasing, customer-credit, or administrative information.

**NFR-SEC-007**
Sensitive authentication credentials, database credentials, API keys, and secrets shall not be committed to the public source-code repository.

**NFR-SEC-008**
Production communication between clients and the deployed system shall use encrypted network transport.

**NFR-SEC-009**
The system shall protect administrative functionality against unauthorized requests.

**NFR-SEC-010**
The system shall validate user-provided input before processing or storing it.

**NFR-SEC-011**
The system shall take reasonable measures to prevent common web application vulnerabilities applicable to the selected technology stack.

---

# 7.2 Privacy and Customer Data Protection

**NFR-PRIV-001**
Customer personal information shall only be accessible to authorized internal users.

**NFR-PRIV-002**
The system shall not expose customer addresses, phone numbers, payment history, or outstanding balances through the public storefront.

**NFR-PRIV-003**
Real customer production data shall not be stored in the public GitHub repository.

**NFR-PRIV-004**
Development and testing environments should use anonymized, synthetic, or otherwise non-sensitive customer data wherever practical.

**NFR-PRIV-005**
The system shall collect only customer information required for legitimate business operations.

---

# 7.3 Performance

**NFR-PERF-001**
Common administrative pages should become usable within a reasonable time under normal business operating conditions.

**NFR-PERF-002**
Typical inventory searches should return results within two seconds under expected initial business load.

**NFR-PERF-003**
Normal product, customer, and order creation operations should complete without noticeable unnecessary delay.

**NFR-PERF-004**
The system should support at least several thousand product records without requiring fundamental redesign.

**NFR-PERF-005**
The system should support growth substantially beyond the business's current approximately 40 monthly product sales.

**NFR-PERF-006**
Public product images should be delivered in a size and format appropriate for normal web and mobile usage.

---

# 7.4 Availability

**NFR-AVL-001**
The production system should normally be available whenever business users require access.

**NFR-AVL-002**
The customer-facing storefront should be capable of continuous availability independent of normal business operating hours.

**NFR-AVL-003**
Planned maintenance should minimize disruption to business operations.

**NFR-AVL-004**
Temporary loss of a single user's device shall not result in loss of centrally stored business information.

---

# 7.5 Reliability and Data Integrity

**NFR-REL-001**
The system shall maintain consistent inventory quantities.

**NFR-REL-002**
A completed sale shall not result in negative available inventory.

**NFR-REL-003**
Financial transactions shall not be silently lost or overwritten.

**NFR-REL-004**
Recorded payments shall remain associated with the appropriate customer and order.

**NFR-REL-005**
Inventory, payment, return, exchange, and order operations that require multiple related data changes shall preserve system consistency if an operation fails.

**NFR-REL-006**
The system shall reject invalid operations rather than intentionally creating inconsistent business records.

**NFR-REL-007**
Historical transaction information required for accounting or business analysis shall remain accessible even if related product information changes later.

---

# 7.6 Backup and Recovery

**NFR-BACK-001**
Production business data shall be backed up regularly.

**NFR-BACK-002**
The deployed solution shall provide a documented procedure for recovering business data from backup.

**NFR-BACK-003**
Backups shall include critical transactional data required to reconstruct inventory, orders, payments, and customer balances.

**NFR-BACK-004**
Product images and business documents requiring long-term retention shall have an appropriate recovery strategy.

**NFR-BACK-005**
The project shall document the selected backup frequency before production deployment.

---

# 7.7 Usability

**NFR-USE-001**
The administrative interface shall be understandable to non-technical business users.

**NFR-USE-002**
Common operations shall minimize unnecessary data entry.

**NFR-USE-003**
Frequently performed tasks such as product lookup, sales creation, payment recording, and customer lookup should require minimal navigation.

**NFR-USE-004**
System messages and validation errors shall use understandable language.

**NFR-USE-005**
Destructive or financially significant actions should clearly communicate their effect before completion where appropriate.

**NFR-USE-006**
The system shall visually distinguish important states such as:

* Available
* Reserved
* On Hold
* Sold
* Outstanding Payment
* Failed Delivery
* Returned

**NFR-USE-007**
The public storefront shall allow customers to browse products without requiring technical knowledge or account registration.

---

# 7.8 Mobile and Responsive Use

**NFR-MOB-001**
The customer-facing storefront shall support modern mobile devices.

**NFR-MOB-002**
Core administrative functionality shall be usable through a mobile browser.

**NFR-MOB-003**
The administrative interface shall also remain practical on desktop and laptop displays.

**NFR-MOB-004**
Core operations shall not depend exclusively on hover interactions or other desktop-only input behavior.

---

# 7.9 Accessibility

**NFR-ACC-001**
The user interface should provide sufficient visual contrast for important text and controls.

**NFR-ACC-002**
Interactive controls should contain meaningful text or accessible labels.

**NFR-ACC-003**
Important system state shall not be communicated solely through color.

**NFR-ACC-004**
The system should support keyboard navigation for primary administrative and storefront functions where practical.

**NFR-ACC-005**
Form validation should clearly identify the field and problem requiring correction.

---

# 7.10 Maintainability

**NFR-MAIN-001**
The software shall be organized into clearly separated responsibilities appropriate to the selected architecture.

**NFR-MAIN-002**
The project shall maintain source code through Git version control.

**NFR-MAIN-003**
Production code changes shall be traceable through repository history.

**NFR-MAIN-004**
Important application configuration shall be externalized from source code where appropriate.

**NFR-MAIN-005**
Repeated business logic should be centralized rather than duplicated across unrelated parts of the system.

**NFR-MAIN-006**
The project shall maintain technical documentation required for future maintenance.

**NFR-MAIN-007**
The system design should allow future features to be introduced without requiring complete replacement of the existing application.

---

# 7.11 Scalability

**NFR-SCALE-001**
The system shall be designed to support substantially more customers, products, orders, and employees than the current business volume.

**NFR-SCALE-002**
The initial design should not assume that the business will permanently remain limited to approximately 15 regular customers.

**NFR-SCALE-003**
The system should permit future growth in product image volume.

**NFR-SCALE-004**
The system should permit additional employee accounts and permissions without redesigning the authentication model.

**NFR-SCALE-005**
The architecture should permit future integration with additional sales channels and services where justified.

---

# 7.12 Auditability

**NFR-AUD-001**
Important financial records shall contain sufficient information to determine when the transaction occurred.

**NFR-AUD-002**
The system should record which authenticated internal user performed financially or operationally significant actions where practical.

**NFR-AUD-003**
Changes to payment, return, exchange, and inventory history shall remain explainable after the fact.

**NFR-AUD-004**
Historical reporting shall use preserved transaction information rather than relying exclusively on current product values.

---

# 7.13 Compatibility

**NFR-COMP-001**
The web application shall support current mainstream desktop and mobile web browsers.

**NFR-COMP-002**
The customer-facing interface shall function without requiring installation of a native application.

**NFR-COMP-003**
Generated PDF receipts shall be readable using commonly available PDF software.

**NFR-COMP-004**
Printable receipts shall be formatted so that they can be reasonably printed using standard consumer or business printing equipment.

---

# 7.14 Observability and Error Handling

**NFR-OBS-001**
The production system shall provide sufficient logging to diagnose application failures.

**NFR-OBS-002**
Logs shall not intentionally expose passwords or authentication secrets.

**NFR-OBS-003**
System failures presented to customers shall not unnecessarily disclose sensitive technical implementation information.

**NFR-OBS-004**
Important backend failures should be logged with sufficient context for troubleshooting.

**NFR-OBS-005**
The system should make operational failures distinguishable from user validation errors.

---

# 7.15 Testing Quality

**NFR-TEST-001**
Core business rules shall be covered by automated tests where practical.

**NFR-TEST-002**
Inventory quantity logic shall be tested.

**NFR-TEST-003**
Payment and outstanding-balance calculations shall be tested.

**NFR-TEST-004**
Reservation and temporary-hold behavior shall be tested.

**NFR-TEST-005**
Returns and exchanges shall be tested for correct inventory and financial effects.

**NFR-TEST-006**
Authorization rules shall be tested to verify that restricted users cannot access prohibited functionality.

**NFR-TEST-007**
The project shall include a documented testing process before production releases.

---

# 7.16 Documentation

**NFR-DOC-001**
Project requirements documentation shall be maintained with the source repository.

**NFR-DOC-002**
System design documentation shall be added before implementation of the applicable architectural components.

**NFR-DOC-003**
The project shall document local development setup once implementation begins.

**NFR-DOC-004**
The project shall document deployment configuration and operational procedures before production release.

**NFR-DOC-005**
Public-facing README documentation shall accurately reflect the current project state and shall not claim incomplete features as implemented.


# 8. Scope Boundaries

## 8.1 Overall Product Scope

The Retail Resale Management System is intended to provide a centralized platform for managing the business's product acquisition, inventory, customers, sales, payments, credit balances, reservations, deliveries, receipts, reporting, and customer-facing product discovery.

The complete product vision may be delivered incrementally across multiple releases.

The existence of a requirement in the long-term SRS does not necessarily mean that requirement must be included in the first production release.

Release-specific scope shall therefore be explicitly defined and controlled.

---

## 8.2 Version 1 Objective

Version 1 shall focus on replacing the most important internal manual business processes currently performed using Microsoft Excel, handwritten notebooks, receipts, and memory.

The primary objective of Version 1 is to provide a reliable internal business-management system before advanced customer-facing functionality is introduced.

Version 1 shall prioritize:

* Accurate inventory records.
* Purchasing records.
* Customer management.
* Sales processing.
* Customer credit management.
* Payment tracking.
* Reservations.
* Returns and exchanges.
* Delivery tracking.
* Receipts.
* Basic business analytics.
* Administrative security.

---

# 9. Version 1 Mandatory Scope

The following capabilities are mandatory for the first production-ready release.

## 9.1 Authentication and Users

Version 1 shall include:

* Administrative authentication.
* Multiple administrator accounts.
* Employee accounts.
* Role-based authorization.
* Account activation and deactivation.

---

## 9.2 Product Management

Version 1 shall include:

* Product creation.
* Product editing.
* Product identification.
* SKU support.
* Brand management.
* Category management.
* Subcategory support.
* Color.
* Material.
* Style.
* Season.
* Product condition.
* Product image.
* Pricing information.
* Quantity.
* Notes.
* Product lifecycle status.

---

## 9.3 Purchasing

Version 1 shall include:

* Purchase recording.
* Purchase source/store.
* Online and physical purchase types.
* Purchase date.
* External order number where applicable.
* Receipt attachment or reference.
* Product acquisition cost.
* Shipping expense.
* Business versus personal purchase distinction.
* Product receiving workflow.

---

## 9.4 Inventory

Version 1 shall include:

* Ordered inventory tracking.
* In-transit products.
* Receiving products.
* Available inventory.
* Reserved inventory.
* On-hold inventory.
* Sold inventory.
* Damaged inventory.
* Inventory quantity tracking.
* Prevention of negative inventory.
* Inventory search and filtering.

---

## 9.5 Customer Management

Version 1 shall include:

* Customer name.
* Phone number.
* WhatsApp number.
* Address.
* City.
* Preferred brands.
* Preferred clothing types.
* Purchase history.
* Outstanding balance.
* Customer transaction history.

---

## 9.6 Reservations

Version 1 shall include:

* Customer reservations.
* Default 48-hour reservation period.
* Manual reservation extension.
* Reservation expiry notification.
* Manual reservation release.
* Prevention of conflicting sales while inventory remains reserved.

---

## 9.7 Sales and POS

Version 1 shall include:

* Internal sale creation.
* Customer association.
* Multiple products per sale.
* Custom selling price.
* Discounts.
* Final order calculation.
* Inventory adjustment.
* Historical sales records.
* Cash-on-delivery support.

---

## 9.8 Payments and Credit

Version 1 shall include:

* Full payments.
* Partial payments.
* Deposits.
* Credit sales.
* Cash payments.
* Bank transfer.
* JazzCash.
* Cash on delivery.
* Individual payment transactions.
* Remaining order balance.
* Customer outstanding balance.
* Optional payment due dates.
* Customer credit ledger.

---

## 9.9 Delivery

Version 1 shall include:

* Delivery information.
* Customer delivery address.
* Delivery fee.
* Internal delivery tracking/reference number.
* Rider-based delivery workflow.
* Delivery status.
* Delivery history.

---

## 9.10 Returns and Exchanges

Version 1 shall include:

* Returns within seven days.
* Return-condition validation.
* Return approval.
* Inventory restoration where appropriate.
* Exchange processing.
* Price-difference calculation.
* Additional customer payment where required.
* Amount owed back to the customer where required.
* Exchange history.

---

## 9.11 Expenses

Version 1 shall include basic business expense recording for:

* Shipping.
* Rider expenses.
* Petrol expenses.

Version 1 shall support using recorded expenses in net-profit reporting.

---

## 9.12 Receipts

Version 1 shall include:

* Unique invoice/receipt number.
* Business name.
* Business logo support.
* Customer information.
* Product information.
* Prices.
* Discounts.
* Total amount.
* Amount paid.
* Remaining balance.
* Printable receipt.
* PDF receipt.

WhatsApp-friendly receipt sharing may be implemented using a generated receipt or shareable document rather than requiring direct WhatsApp API integration.

---

## 9.13 Dashboard and Reporting

Version 1 shall include reporting for:

* Revenue.
* Gross profit.
* Net profit.
* Current inventory value.
* Number of items sold.
* Outstanding customer credit.
* Monthly sales.
* Sales by brand.
* Sales by category.
* Top customers.
* Inventory older than 30 days.
* Inventory older than 90 days.

The Version 1 dashboard does not need to contain every possible analytical visualization defined in the long-term product requirements.

---

# 10. Version 1 Exclusions

The following capabilities are explicitly outside the mandatory scope of Version 1.

They may be considered for later releases.

## 10.1 Public Online Storefront

A complete customer-facing e-commerce storefront is not mandatory for Version 1.

This includes:

* Public product browsing.
* Guest online checkout.
* Online order requests.
* Coming Soon collections.
* Public sold-product history.
* Customer product filtering.

The internal system should nevertheless be designed so that a storefront can be introduced later without replacing the core inventory and order-management system.

---

## 10.2 Automated Online Payments

Version 1 shall not require integration with:

* Credit-card processors.
* Debit-card processors.
* Online payment gateways.
* Easypaisa APIs.
* JazzCash merchant APIs.
* Banking APIs.

Payments may be recorded manually by authorized business users.

---

## 10.3 Direct WhatsApp Business API Integration

Version 1 shall not require automatic messaging through the WhatsApp Business API.

Version 1 may support:

* Copyable product information.
* Shareable links.
* PDF receipts.
* WhatsApp-compatible receipt sharing.

Full API automation may be introduced later.

---

## 10.4 Native Mobile Applications

Version 1 shall not require separate:

* Android applications.
* iOS applications.

The system shall instead provide responsive web access.

---

## 10.5 Artificial Intelligence and Machine Learning

Version 1 shall not require:

* AI-generated pricing.
* Demand prediction.
* Customer recommendation algorithms.
* Automated product descriptions.
* AI sales forecasting.
* Customer segmentation models.

These features require reliable historical business data and shall only be considered after sufficient production data has been collected.

---

## 10.6 Advanced Inventory Forecasting

Version 1 shall not require:

* Automatic restocking.
* Low-stock alerts.
* Supplier replenishment.
* Demand-based stock purchasing.

The current business generally purchases discounted opportunities rather than maintaining standard replenishment inventory.

---

## 10.7 Courier Integrations

Version 1 shall not require integration with external courier providers.

The business currently uses riders and shall use internally generated delivery reference numbers.

---

## 10.8 International Operations

Version 1 shall not require:

* International delivery.
* Multi-currency accounting.
* Foreign taxation.
* Customs management.
* International payment processing.

The initial business currency shall be PKR.

---

## 10.9 Advanced Accounting

The system is not intended to replace professional accounting software in Version 1.

Version 1 shall not require:

* Double-entry bookkeeping.
* General ledger accounting.
* Tax filing.
* Payroll.
* Formal financial statements.
* Regulatory accounting reports.

Business reports are intended for operational management purposes.

---

# 11. Future Release Candidates

The following capabilities may be considered after Version 1 has been successfully adopted.

Potential Version 2 capabilities include:

* Public customer storefront.
* Guest order requests.
* Temporary online inventory holds.
* WhatsApp product sharing.
* Product collections.
* Coming Soon products.
* Sold-product visibility.
* Extended dashboards.
* Improved inventory-ageing analysis.
* Customer enquiry functionality.

Potential later releases may include:

* Barcode scanning.
* Advanced employee permissions.
* Supplier analytics.
* Automated reminders.
* Customer targeting.
* Price recommendations.
* Demand forecasting.
* Recommendation systems.
* Additional sales-channel integrations.

These items are roadmap candidates and shall not be treated as committed functionality until formally added to an approved release scope.

---

# 12. Project Constraints

## 12.1 Business Process Constraints

The software must accommodate the existing business rather than requiring immediate replacement of all current practices.

WhatsApp is currently a major communication and marketing channel.

The system must therefore be capable of operating alongside WhatsApp-based sales activity.

---

## 12.2 Inventory Constraints

The business primarily sells unstitched clothing.

Size shall therefore not be mandatory.

Products are not considered sellable until physically received.

Identical products may occasionally exist in quantities greater than one.

---

## 12.3 Financial Constraints

The business:

* Does not use a fixed markup percentage.
* Allows negotiated prices.
* Allows sales at cost.
* Does not normally permit sales below cost.
* Allows credit sales.
* Allows partial payments.
* Does not use fixed customer credit limits.
* Does not always define credit payment deadlines.

The software shall therefore support flexible financial workflows.

---

## 12.4 Operational Constraints

Inventory is currently stored at the business owner's residence.

No mandatory shelf or warehouse-location structure currently exists.

The system shall not require storage-location assignment in Version 1.

---

## 12.5 Technical Constraints

No final implementation technology shall be considered mandatory solely because it was discussed before formal architecture evaluation.

Technology selection must consider:

* Functional requirements.
* Security.
* Maintainability.
* Developer experience.
* Hosting cost.
* Scalability.
* Deployment complexity.
* Portfolio and educational value.

---

# 13. External Dependencies

The system may depend on external infrastructure or services.

Possible dependencies include:

* Application hosting.
* Database hosting.
* Image/document storage.
* Email or notification services.
* PDF generation capability.
* Domain registration.
* HTTPS/TLS certificates.
* Future WhatsApp services.

Specific providers shall be selected during architecture and deployment design.

---

# 14. Assumptions Affecting Delivery

The following assumptions apply to the initial project:

1. At least one business administrator will participate in testing.
2. The business owner will validate workflows during development.
3. Development will initially use test or synthetic customer data.
4. Real business data will only be migrated after the applicable features are validated.
5. Internet connectivity will normally be available during system use.
6. The system will initially serve one business organization.
7. Multi-company or franchise functionality is not required in Version 1.
8. Initial transaction volume will remain relatively small compared with large commercial retail systems.
9. Business processes may evolve as the system is tested with real operations.

---

# 15. Version 1 Acceptance Criteria

Version 1 shall not be considered complete merely because all screens have been implemented.

Completion requires successful end-to-end validation of the primary business workflows.

## AC-V1-001 — Product Acquisition

Given an authorized administrator has purchased a business product,

the administrator must be able to:

1. Record the purchase.
2. Record the source.
3. Record its cost.
4. Record shipping where applicable.
5. Attach or reference the receipt.
6. Mark the product as ordered or in transit.
7. Receive the product.
8. Make the product available as inventory.

The product must not become sellable before receiving.

---

## AC-V1-002 — Product Inventory

Given a physically received product,

an authorized user must be able to:

1. Enter its product information.
2. Assign its brand and classification.
3. Record pricing.
4. Store its image.
5. Record quantity.
6. Find it through inventory search.
7. determine its current availability.

---

## AC-V1-003 — Customer Creation

An authorized user must be able to create a customer containing the business-required contact information and subsequently locate that customer.

---

## AC-V1-004 — Standard Sale

Given an available product and an existing customer,

an authorized user must be able to:

1. Create a sale.
2. Select the customer.
3. Select the product.
4. Set the transaction price.
5. Apply a discount if required.
6. Record payment.
7. Confirm the sale.
8. Update inventory.
9. Generate a receipt.

The same sold inventory unit must not remain available for another standard sale.

---

## AC-V1-005 — Partial Payment

Given an order valued at PKR 10,000 where the customer pays PKR 4,000,

the system must:

1. Record the PKR 4,000 payment.
2. Preserve the original order total.
3. Calculate a PKR 6,000 remaining balance.
4. Add the unpaid amount to the customer's outstanding balance.
5. Allow additional payments to be recorded later.

---

## AC-V1-006 — Multiple Payments

Given a customer has an outstanding order balance,

an authorized user must be able to record multiple later payments until the remaining balance reaches zero.

Every payment must remain visible as a separate historical transaction.

---

## AC-V1-007 — Customer Credit Overview

An administrator must be able to select a customer and determine:

* Total outstanding balance.
* Relevant unpaid orders.
* Payment history.
* Purchase history.

---

## AC-V1-008 — Reservation

Given an available product,

an authorized user must be able to reserve it for a customer.

The system must:

1. Record the reservation.
2. Apply the default 48-hour period.
3. Prevent an ordinary conflicting sale.
4. Notify authorized users when the reservation expires.
5. Keep the reservation active until manually released, extended, cancelled, or overridden.

---

## AC-V1-009 — Return

Given an eligible sale less than or equal to seven days old,

an authorized user must be able to process an approved return provided the product is in original condition.

The original sale must remain historically visible.

The product may only return to available inventory when it remains suitable for resale.

---

## AC-V1-010 — Exchange

Given a customer exchanges one product for another,

the system must:

1. Record the returned product.
2. Record the replacement product.
3. Calculate the financial difference.
4. Record additional customer payment where required.
5. Record money owed to the customer where applicable.
6. Correctly update both inventory records.
7. Preserve the exchange history.

---

## AC-V1-011 — Delivery

Given a confirmed order requiring delivery,

an authorized user must be able to:

1. Create delivery information.
2. Assign an internal tracking/reference number.
3. Record the delivery address.
4. Record the delivery charge.
5. Update delivery status through the defined delivery workflow.

---

## AC-V1-012 — Receipt

A completed sale must allow an authorized user to generate a receipt containing:

* Unique receipt or invoice number.
* Business name.
* Products.
* Selling prices.
* Discounts.
* Total.
* Amount paid.
* Outstanding balance where applicable.

The receipt must be printable and capable of PDF generation.

---

## AC-V1-013 — Reporting

Using recorded business data, an administrator must be able to determine at minimum:

* Sales revenue.
* Gross profit.
* Net profit.
* Inventory value.
* Number of items sold.
* Customer outstanding credit.
* Sales by month.
* Sales by brand.
* Sales by category.
* Inventory older than 30 days.
* Inventory older than 90 days.

---

## AC-V1-014 — Permissions

An employee account must not automatically receive the same privileged access as an administrator.

Restricted functions must reject unauthorized access even if the user attempts to access them directly rather than through the user interface.

---

## AC-V1-015 — Data Persistence

After a user logs out or closes the application, previously committed products, customers, orders, payments, and inventory records must remain available when the system is accessed again.

---

## AC-V1-016 — End-to-End Business Scenario

Before Version 1 is considered production-ready, the business owner shall successfully complete an end-to-end test representing a real transaction:

Purchase a product
→ receive it
→ add it to available inventory
→ create or select a customer
→ sell the product
→ record a partial payment
→ create an outstanding balance
→ record delivery
→ generate a receipt
→ later record the remaining payment
→ verify inventory, customer balance, revenue, and profit information.

Successful completion of this scenario is mandatory for Version 1 acceptance.

---

# 16. Requirements Change Control

After the SRS has been baselined, new requirements shall not be silently inserted into the project.

A proposed requirement change shall identify:

1. The requested change.
2. The business reason.
3. Existing requirements affected.
4. Expected impact on scope.
5. Expected impact on implementation.
6. Expected impact on testing.
7. Release in which the change should be considered.

Minor wording corrections that do not alter system behavior do not require formal change approval.

Significant scope or business-rule changes shall be reviewed before implementation.
