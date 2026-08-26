# Software Requirements Specification

## Retail Resale Management System

**Document ID:** RRMS-SRS-001
**Version:** 0.4
**Status:** Draft
**Project Phase:** Requirements Engineering
**Author:** Ibrahim Salman
**Primary Stakeholder:** Business Owner
**Last Updated:** August 2026

---

## Document Revision History

| Version | Date        | Author         | Description                                                 | Status |
| ------- | ----------- | -------------- | ----------------------------------------------------------- | ------ |
| 0.4     | August 2026 | Ibrahim Salman | Added non-functional requirements      | Draft  |

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
The system shall warn an authorized user when a proposed selling price is below final product cost.

**FR-PRICE-013**
The system shall not require a fixed percentage markup.

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
