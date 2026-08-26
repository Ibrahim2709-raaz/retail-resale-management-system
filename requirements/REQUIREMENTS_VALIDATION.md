# Retail Resale Management System — Requirements Validation

**Document ID:** RRMS-RV-001
**Version:** 0.1
**Status:** In Review
**Related Document:** RRMS-SRS-001 v0.5
**Validation Stage:** Requirements Baseline Review

---

# 1. Purpose

This document records the formal validation of the Software Requirements Specification for the Retail Resale Management System.

The purpose of requirements validation is to verify that the documented requirements accurately represent the business needs identified during stakeholder discovery and are sufficiently complete, consistent, understandable, feasible, and testable to serve as the baseline for system design.

System design shall not begin until the mandatory requirements-validation process has been completed.

---

# 2. Validation Criteria

Each requirement set shall be reviewed against the following criteria.

## 2.1 Correctness

The documented requirement must reflect an actual business need or agreed system behavior.

## 2.2 Completeness

Required business behavior must not be omitted from the applicable workflow.

## 2.3 Consistency

Requirements must not contradict other requirements or established business rules.

## 2.4 Clarity

Requirements must be sufficiently clear that their meaning does not depend on hidden assumptions.

## 2.5 Testability

Mandatory requirements must be capable of being verified through testing, inspection, or stakeholder acceptance.

## 2.6 Feasibility

Requirements must be technically and operationally achievable within reasonable project constraints.

## 2.7 Traceability

Requirements must possess unique identifiers and remain traceable to business needs, business rules, design decisions, implementation work, or test cases where appropriate.

---

# 3. Validation Review

## 3.1 Business Scope

Review the following with the primary stakeholder.

* [ ] The SRS accurately describes the clothing resale business.
* [ ] Online and physical product sourcing are correctly represented.
* [ ] The business primarily sells unstitched clothing.
* [ ] Size is therefore not required for current products.
* [ ] Products are only treated as sellable inventory after physical receipt.
* [ ] The system's primary currency is PKR.
* [ ] International sales are correctly excluded from the initial scope.
* [ ] WhatsApp remains an important part of the current business process.

### Stakeholder Comments

Record any corrections here:

---

## 3.2 Purchasing

Confirm:

* [ ] Online purchases are supported.
* [ ] Physical/supply-market purchases are supported.
* [ ] External order numbers may be recorded.
* [ ] Purchase receipts are retained.
* [ ] Shipping costs may be recorded.
* [ ] Rider and petrol expenses may be recorded.
* [ ] Personal purchases are distinguishable from business purchases.
* [ ] Personal purchases do not affect business inventory or profit.

### Stakeholder Comments

---

## 3.3 Inventory

Confirm:

* [ ] Products may exist as individual pieces.
* [ ] Multiple identical units may occasionally exist.
* [ ] Ordered products are not automatically available inventory.
* [ ] Products cannot be sold before receipt.
* [ ] Reserved items remain unavailable for conflicting ordinary sales.
* [ ] Damaged and defective items are handled separately.
* [ ] Low-stock notifications are not required.
* [ ] Home storage currently does not require shelf-location tracking.

### Stakeholder Comments

---

## 3.4 Pricing

Confirm:

* [ ] The business does not use a fixed markup.
* [ ] Selling price can be set manually.
* [ ] Negotiated pricing is supported.
* [ ] Discounts may be manually applied.
* [ ] Products may be sold at cost.
* [ ] Below-cost sales should generate a warning.
* [ ] Minimum acceptable selling price may be stored.
* [ ] Profit should be visible to authorized business users.

### Stakeholder Comments

---

## 3.5 Customers

Confirm:

* [ ] Customer name is required.
* [ ] Phone number is stored.
* [ ] WhatsApp information is supported.
* [ ] Address and city are supported.
* [ ] Preferred brands may be stored.
* [ ] Preferred clothing types may be stored.
* [ ] Purchase history is required.
* [ ] Outstanding balances are required.
* [ ] Birthday information is not required.
* [ ] Email is not required.

### Stakeholder Comments

---

## 3.6 Reservations

Confirm:

* [ ] Products may be reserved for customers.
* [ ] Default reservation duration is 48 hours.
* [ ] Reservation duration may be manually extended.
* [ ] The system should notify the business when the reservation expires.
* [ ] Expired reservations should not automatically release inventory.
* [ ] The business user decides when to release an expired reservation.

### Stakeholder Comments

---

## 3.7 Sales and POS

Confirm:

* [ ] A sale is associated with a customer.
* [ ] A sale may contain multiple products.
* [ ] Selling price may differ from the default product price.
* [ ] Discounts are supported.
* [ ] Sales must update inventory.
* [ ] Historical sale values must remain unchanged if product prices change later.
* [ ] Cash-on-delivery sales are supported.

### Stakeholder Comments

---

## 3.8 Payments and Credit

Confirm:

* [ ] Full payments are supported.
* [ ] Partial payments are supported.
* [ ] Deposits are supported.
* [ ] Credit sales are supported.
* [ ] Cash is supported.
* [ ] Bank transfer is supported.
* [ ] JazzCash is supported.
* [ ] Cash on delivery is supported.
* [ ] Each payment should be recorded separately.
* [ ] Customer outstanding balances should be visible.
* [ ] Credit limits are not required.
* [ ] Payment due dates are optional rather than mandatory.

### Stakeholder Comments

---

## 3.9 Returns

Confirm:

* [ ] Customer returns are allowed.
* [ ] Standard return window is seven days.
* [ ] Returned products must be in their original condition.
* [ ] Returns require business approval.
* [ ] Returned products only re-enter available inventory when suitable for resale.
* [ ] Historical sale records remain preserved after a return.

### Stakeholder Comments

---

## 3.10 Exchanges

Confirm:

* [ ] Exchanges are supported.
* [ ] A replacement product can have a different price.
* [ ] Customer pays the difference when the replacement costs more.
* [ ] Business owes the customer the difference when the replacement costs less.
* [ ] Inventory changes for both products must be recorded.
* [ ] Exchange history is retained.

### Stakeholder Comments

---

## 3.11 Delivery

Confirm:

* [ ] Rider-based delivery is the normal workflow.
* [ ] External courier integration is not required.
* [ ] The business system should generate its own delivery tracking/reference number.
* [ ] Delivery fee is stored.
* [ ] Delivery status is tracked.
* [ ] Delivery status is separate from payment status.

### Stakeholder Comments

---

## 3.12 Receipts

Confirm:

* [ ] Printed receipts are required.
* [ ] PDF receipts are required.
* [ ] Receipt information should be shareable through WhatsApp.
* [ ] Business name is shown.
* [ ] Business logo may be shown.
* [ ] Amount paid is shown.
* [ ] Outstanding balance is shown where applicable.

### Stakeholder Comments

---

## 3.13 Reporting

Confirm the business wants reporting for:

* [ ] Revenue.
* [ ] Gross profit.
* [ ] Net profit.
* [ ] Inventory value.
* [ ] Number of products sold.
* [ ] Outstanding customer credit.
* [ ] Sales by month.
* [ ] Sales by brand.
* [ ] Sales by category.
* [ ] Top customers.
* [ ] Inventory older than 30 days.
* [ ] Inventory older than 90 days.

### Stakeholder Comments

---

## 3.14 Version 1 Scope

Confirm that Version 1 should focus primarily on the internal business-management platform.

* [ ] Inventory.
* [ ] Purchasing.
* [ ] Customers.
* [ ] Sales/POS.
* [ ] Credit and payments.
* [ ] Reservations.
* [ ] Deliveries.
* [ ] Returns and exchanges.
* [ ] Receipts.
* [ ] Expenses.
* [ ] Reporting.
* [ ] Authentication and user roles.

Confirm that the following may wait until later releases:

* [ ] Full public storefront.
* [ ] Automated payment gateway.
* [ ] WhatsApp Business API automation.
* [ ] Native mobile application.
* [ ] AI/ML functionality.
* [ ] Courier API integration.
* [ ] International operations.
* [ ] Advanced accounting.

---

# 4. Ambiguity Review

The following questions shall be answered before SRS baselining.

## VAL-001 — Employee Financial Visibility

Should normal employees be allowed to see:

* Product purchase cost?
* Product profit?
* Overall business revenue?
* Customer outstanding balances?

**Stakeholder Decision:** Pending

---

## VAL-002 — Sale Below Cost

The current business rule states that below-cost sales are not normally permitted and the system must display a warning.

Determine whether the warning:

**Option A:** Warns the user but allows an administrator to continue.

**Option B:** Completely blocks the transaction.

**Stakeholder Decision:** Pending

---

## VAL-003 — Return Refund Handling

When a customer returns a product after already paying for it, determine how the value should normally be handled.

Possible outcomes include:

* Cash repayment.
* Bank/JazzCash repayment.
* Customer credit balance.
* Exchange only.

**Stakeholder Decision:** Pending

---

## VAL-004 — Money Owed to Customer After Exchange

When a cheaper replacement creates money owed back to the customer, determine whether the system should:

* Record an immediate refund.
* Maintain an amount owed to the customer.
* Allow either option.

**Stakeholder Decision:** Pending

---

## VAL-005 — Expense Allocation

Determine whether petrol and rider costs should:

* Always be general business expenses,
* Be linked to particular orders when known,
* Or support both approaches.

**Stakeholder Decision:** Pending

---

# 5. Requirements Review Outcome

The requirements baseline shall receive one of the following outcomes:

### APPROVED

The stakeholder accepts the requirements as representing the intended system.

### APPROVED WITH MINOR CHANGES

Small corrections are required but do not materially change system scope.

### REQUIRES REVISION

One or more significant business requirements require further investigation before design can begin.

---

# 6. Stakeholder Sign-Off

Once all mandatory validation items and open decisions have been resolved:

**SRS Version Reviewed:** __________________

**Review Outcome:** __________________

**Primary Stakeholder:** __________________

**Date Reviewed:** __________________

**Developer:** Ibrahim Salman

### Approval Statement

The stakeholder confirms that the reviewed Software Requirements Specification reasonably represents the required business processes, functionality, constraints, and Version 1 scope of the Retail Resale Management System.

The stakeholder understands that future changes may be processed through requirements change control.

**Stakeholder Approval:** Yes / No

---

# 7. Baseline Condition

The SRS may be promoted from Draft status to **Baseline Version 1.0** only after:

* All mandatory validation sections have been reviewed.
* All material contradictions have been resolved.
* All open validation decisions have been answered.
* Version 1 scope has been explicitly accepted.
* Acceptance criteria have been reviewed.
* The primary stakeholder has approved the requirements baseline.
