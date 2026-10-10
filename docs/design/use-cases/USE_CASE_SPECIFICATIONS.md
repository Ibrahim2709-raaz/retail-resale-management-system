# RRMS Use Case Specifications

**Document ID:** RRMS-UCS-001  
**Version:** 1.0  
**Status:** Baseline  
**Related Requirements:** RRMS-SRS-001 v1.0  
**Related Model:** RRMS-UCM-001  

---

# 1. Purpose

This document specifies the detailed behavior of the primary Version 1 use cases for the Retail Resale Management System (RRMS).

Each use case defines:

- primary actor;
- supporting actors where applicable;
- trigger;
- preconditions;
- main success flow;
- alternate flows;
- exception flows;
- postconditions;
- related business rules and functional requirements.

These specifications provide behavioral input for later domain modeling, database design, interface design, API design, and testing.

---

# 2. Use Case Specification Conventions

## 2.1 Preconditions

Conditions that must already be true before the use case begins.

## 2.2 Main Success Flow

The normal sequence of events that results in successful completion.

## 2.3 Alternate Flow

A valid variation of the main flow.

## 2.4 Exception Flow

A situation that prevents the normal use case from completing.

## 2.5 Postconditions

The system state after successful completion.

---

# 3. UC-003 — Record Purchase

## Use Case ID

UC-003

## Name

Record Purchase

## Primary Actor

Business Administrator

## Goal

Record the acquisition of products purchased for business resale or personal use.

## Trigger

The administrator purchases one or more products from an online retailer, physical store, or supply market.

## Preconditions

1. The administrator is authenticated.
2. The administrator has permission to record purchases.
3. Relevant product or purchase information is available.

## Main Success Flow

1. The administrator selects **Record Purchase**.
2. The system creates a new purchase record.
3. The administrator selects the purchase type:
   - Business
   - Personal
4. The administrator enters the purchase source/store.
5. The administrator enters the purchase date.
6. If applicable, the administrator enters an external order number.
7. The administrator adds one or more purchased products.
8. For each product, the administrator enters:
   - product name;
   - brand;
   - category;
   - quantity;
   - purchase price.
9. The administrator records applicable shipping or acquisition costs.
10. The administrator attaches or references a purchase receipt where available.
11. The administrator confirms the purchase.
12. The system validates the entered information.
13. The system saves the purchase.
14. Business purchases enter the acquisition/inventory workflow.
15. Personal purchases are recorded but excluded from business inventory and profitability calculations.

## Alternate Flows

### AF-003-01 — Physical Purchase

If the purchase was made physically:

1. External order number may be omitted.
2. The administrator records the store or market as the source.
3. The remainder of the main flow continues.

### AF-003-02 — Multiple Identical Products

If multiple identical units were purchased:

1. The administrator records the appropriate quantity.
2. The system associates the quantity with the purchase item.

### AF-003-03 — Receipt Not Available

If no receipt is available:

1. Receipt information may be omitted.
2. The purchase may still be saved.

## Exception Flows

### EF-003-01 — Invalid Purchase Data

If required purchase information is missing or invalid:

1. The system rejects the save operation.
2. The system identifies the fields requiring correction.
3. The administrator corrects the information and retries.

## Postconditions

1. A purchase record exists.
2. Business purchases are available for receiving/inventory processing.
3. Personal purchases do not affect business inventory.
4. Purchase costs are available for later profitability calculations.

## Related Requirements

- FR-PUR-001 through FR-PUR-012
- BR-PUR-001 through BR-PUR-003

---

# 4. UC-004 — Receive Product

## Use Case ID

UC-004

## Name

Receive Product

## Primary Actor

Business Administrator or Employee

## Goal

Record that a previously purchased business product has physically arrived.

## Trigger

A purchased product is physically received by the business.

## Preconditions

1. The user is authenticated.
2. The user has permission to update inventory.
3. A business purchase record exists.
4. The product has not already been fully received.

## Main Success Flow

1. The user opens the relevant purchase.
2. The system displays products awaiting receipt.
3. The user selects the product being received.
4. The user verifies the received quantity.
5. The user records the product condition.
6. The user confirms receipt.
7. The system records the received date.
8. The system changes the product status from:
   - Ordered, or
   - In Transit
   to:
   - Received.
9. If the product is suitable for resale, the system allows it to become Available inventory.
10. The system updates inventory quantity.
11. The system records the receiving activity in history.

## Alternate Flows

### AF-004-01 — Partial Receipt

If only part of a multi-unit purchase arrives:

1. The user records the received quantity.
2. The remaining quantity stays outstanding.
3. Only the received quantity may become inventory.

### AF-004-02 — Damaged or Defective Product

If the product arrives damaged or defective:

1. The user records the appropriate condition.
2. The product is not automatically made Available.
3. An authorized user may later determine how the product should be handled.

## Exception Flows

### EF-004-01 — Receipt Exceeds Purchased Quantity

If the entered received quantity exceeds the purchased outstanding quantity:

1. The system rejects the operation.
2. The user must correct the quantity.

## Postconditions

1. Received quantity is recorded.
2. Appropriate inventory exists.
3. Sellable received products may become Available.
4. Products not physically received remain unsellable.

## Related Requirements

- FR-INV-001 through FR-INV-006
- FR-QTY-001 through FR-QTY-005
- BR-INV-001 through BR-INV-006

---

# 5. UC-010 — Reserve Product

## Use Case ID

UC-010

## Name

Reserve Product

## Primary Actor

Business Administrator or Employee

## Goal

Temporarily reserve available inventory for a customer.

## Trigger

A customer requests that a product be held.

## Preconditions

1. The user is authenticated.
2. The customer exists.
3. The product has been physically received.
4. The requested product quantity is available.
5. The inventory is not already reserved, held, or sold.

## Main Success Flow

1. The user searches for the customer.
2. The user selects the product.
3. The user selects **Reserve Product**.
4. The system verifies product availability.
5. The system assigns the default reservation period of 48 hours.
6. The user confirms the reservation.
7. The system records:
   - customer;
   - product;
   - reservation start time;
   - reservation expiry time;
   - reservation status.
8. The system changes the affected inventory to Reserved.
9. The reserved inventory becomes unavailable for ordinary conflicting sales.

## Alternate Flows

### AF-010-01 — Extend Reservation

1. An authorized user opens an existing reservation.
2. The user selects **Extend Reservation**.
3. A new expiry date/time is entered.
4. The system updates the reservation.

### AF-010-02 — Reservation Expires

1. The reservation reaches its expiry time.
2. The system generates an expiry notification.
3. Inventory remains Reserved.
4. An authorized user decides whether to:
   - extend;
   - release;
   - cancel;
   - override.

### AF-010-03 — Manual Release

1. An authorized user releases the reservation.
2. The reservation status changes accordingly.
3. The inventory becomes Available if no other hold prevents it.

## Exception Flows

### EF-010-01 — Product No Longer Available

If availability changes before confirmation:

1. The system rejects the reservation.
2. The user is informed that the product cannot be reserved.

## Postconditions

1. Reservation history exists.
2. Reserved stock is protected from ordinary conflicting sales.
3. Reservation expiry is tracked.

## Related Requirements

- FR-RES-001 through FR-RES-009
- BR-RES-001 through BR-RES-006

---

# 6. UC-011 — Create Sale

## Use Case ID

UC-011

## Name

Create Sale

## Primary Actor

Business Administrator or Employee

## Goal

Record a confirmed sale of one or more inventory items to a customer.

## Trigger

A customer decides to purchase one or more products.

## Preconditions

1. The user is authenticated.
2. The user has permission to create sales.
3. A customer record exists or can be created.
4. Products have been physically received.
5. Required product quantity is available or validly reserved for the customer.

## Main Success Flow

1. The user starts a new sale.
2. The system generates a new sale record.
3. The user selects or creates the customer.
4. The user searches available inventory.
5. The user adds one or more products.
6. The system displays default selling prices.
7. The user may adjust transaction selling prices.
8. The user may apply authorized discounts.
9. The system calculates the transaction subtotal.
10. The system calculates discounts.
11. The system calculates the final sale total.
12. The system calculates estimated profit information.
13. The user confirms the sale.
14. The system preserves the transaction prices.
15. The system reduces available inventory.
16. Sold inventory is marked appropriately.
17. The system creates the customer's payment obligation.
18. Payment processing begins through UC-012.
19. The system stores the completed sale record.
20. A receipt may be generated.

## Alternate Flows

### AF-011-01 — Reserved Product

If the item is reserved for the selected customer:

1. The reservation is identified.
2. The sale consumes the reserved inventory.
3. The reservation is closed appropriately.

### AF-011-02 — Sell At Cost

If final sale price equals product cost:

1. The transaction is permitted.
2. The system records zero product profit where applicable.

### AF-011-03 — Below-Cost Sale

If proposed sale price is below final product cost:

1. The system displays a warning.
2. The authorized user may:
   - cancel/change the price, or
   - acknowledge the warning and continue.
3. If continued, the decision is preserved with the transaction where appropriate.

### AF-011-04 — Credit Sale

If full payment is not collected:

1. The sale may still be confirmed.
2. The unpaid amount becomes part of the customer outstanding balance.

## Exception Flows

### EF-011-01 — Insufficient Inventory

If requested quantity is unavailable:

1. The system rejects the conflicting sale item.
2. Inventory quantity must be corrected before confirmation.

### EF-011-02 — Negative Inventory Attempt

The system shall prevent confirmation if the sale would result in negative inventory.

## Postconditions

1. A confirmed sale exists.
2. Transaction prices are permanently preserved.
3. Inventory quantities are updated.
4. Customer payment obligation exists.
5. Revenue and profitability reports can include the transaction.

## Related Requirements

- FR-SALE-001 through FR-SALE-010
- FR-PRICE-001 through FR-PRICE-014
- FR-QTY-004 through FR-QTY-005
- BR-PRICE-001 through BR-PRICE-007

---

# 7. UC-012 — Record Payment

## Use Case ID

UC-012

## Name

Record Payment

## Primary Actor

Business Administrator or Employee

## Goal

Record money received from a customer against a sale or outstanding balance.

## Trigger

A customer makes a payment.

## Preconditions

1. The user is authenticated.
2. The customer exists.
3. A sale or customer balance exists.
4. Payment amount is known.

## Main Success Flow

1. The user opens the relevant customer or sale.
2. The system displays the outstanding amount.
3. The user selects **Record Payment**.
4. The user enters the payment amount.
5. The user selects the payment method:
   - Cash;
   - Bank Transfer;
   - JazzCash;
   - Cash on Delivery.
6. The user records the payment date.
7. The user confirms the payment.
8. The system creates a separate payment transaction.
9. The payment is associated with the appropriate sale/customer.
10. The system recalculates the remaining order balance.
11. The system recalculates the customer's total outstanding balance.
12. The system updates payment status to:
   - Unpaid;
   - Partially Paid; or
   - Paid.

## Alternate Flows

### AF-012-01 — Partial Payment

If payment is less than the outstanding amount:

1. The payment is recorded.
2. Remaining balance stays outstanding.
3. Status becomes Partially Paid.

### AF-012-02 — Final Payment

If the payment settles the remaining amount:

1. Remaining balance becomes zero.
2. Payment status becomes Paid.

### AF-012-03 — Deposit

A payment may be recorded as a deposit before the full amount is collected.

## Exception Flows

### EF-012-01 — Invalid Payment Amount

If the payment amount is invalid:

1. The system rejects the payment.
2. The user must correct the amount.

## Postconditions

1. Payment transaction exists.
2. Outstanding balances are recalculated.
3. Historical payment information remains available.

## Related Requirements

- FR-PAY-001 through FR-PAY-015
- FR-CREDIT-001 through FR-CREDIT-007
- BR-PAY-001 through BR-PAY-007

---

# 8. UC-013 — Manage Credit / Outstanding Balance

## Use Case ID

UC-013

## Name

Manage Credit / Outstanding Balance

## Primary Actor

Business Administrator or Employee

## Goal

Review a customer's unpaid obligations and payment history.

## Trigger

A business user needs to determine what a customer owes.

## Preconditions

1. The user is authenticated.
2. The customer exists.

## Main Success Flow

1. The user searches for the customer.
2. The system opens the customer account.
3. The system calculates the total outstanding balance.
4. The system displays relevant unpaid or partially paid sales.
5. The system displays payment history.
6. The system displays optional due dates where recorded.
7. The user may open individual transactions.
8. The user may initiate a payment through UC-012.

## Alternate Flows

### AF-013-01 — No Outstanding Balance

If the customer owes nothing:

1. The system displays a zero balance.
2. Historical credit/payment records remain accessible.

### AF-013-02 — Due Date Exists

If a due date was recorded:

1. The system compares it with the current date.
2. The system may identify the balance as overdue.

## Postconditions

No financial data is modified unless another use case, such as Record Payment, is performed.

## Related Requirements

- FR-CREDIT-001 through FR-CREDIT-007
- FR-CUS-010 through FR-CUS-011

---

# 9. UC-015 — Manage Delivery

## Use Case ID

UC-015

## Name

Manage Delivery

## Primary Actor

Business Administrator or Employee

## Supporting Participant

Delivery Rider — indirect/manual participant

## Goal

Create and manage delivery information for a customer order.

## Trigger

A confirmed order requires delivery.

## Preconditions

1. User is authenticated.
2. Sale/order exists.
3. Customer delivery details are available.

## Main Success Flow

1. The user opens the relevant order.
2. The user selects **Create Delivery**.
3. The system generates a unique internal tracking/reference number.
4. The system loads the customer delivery address.
5. The user verifies or modifies the delivery address.
6. The user records the delivery fee.
7. The user records rider information where applicable.
8. Initial delivery status is set to Processing.
9. The delivery record is saved.
10. The user updates delivery status as the order progresses:
    - Processing;
    - Packed;
    - Shipped;
    - Out for Delivery;
    - Delivered.
11. The final delivery outcome is recorded.

## Alternate Flows

### AF-015-01 — Failed Delivery

If delivery cannot be completed:

1. Status is changed to Failed Delivery.
2. Relevant notes may be recorded.
3. The order and payment records remain intact.

### AF-015-02 — Rider Expense

If rider or petrol expenses relate directly to the order:

1. The expense may be associated with the delivery/order.
2. The expense is included in applicable net-profit calculations.

## Postconditions

1. Delivery history exists.
2. Internal tracking/reference number exists.
3. Current delivery status is available.
4. Delivery remains independent of payment status.

## Related Requirements

- FR-DEL-001 through FR-DEL-009
- BR-DEL-001 through BR-DEL-004

---

# 10. UC-017 — Process Return

## Use Case ID

UC-017

## Name

Process Return

## Primary Actor

Business Administrator or Employee

## Goal

Process an eligible customer return while preserving transaction history.

## Trigger

A customer requests to return a purchased product.

## Preconditions

1. User is authenticated.
2. Original sale exists.
3. Product was sold to the customer.
4. Standard return period has not exceeded seven days unless authorized otherwise.
5. Product condition can be evaluated.

## Main Success Flow

1. The user locates the original sale.
2. The user selects the product being returned.
3. The system displays original transaction information.
4. The user records the return date.
5. The user records the reason for return.
6. The user confirms that the product is in acceptable original condition.
7. The user approves the return.
8. The system creates a return transaction.
9. The original sale record remains preserved.
10. If the product is suitable for resale, inventory is restored appropriately.
11. If money was already paid, the user selects the refund method:
    - Cash; or
    - Online Transfer.
12. The system records refund information.
13. Customer financial balance is updated where necessary.

## Alternate Flows

### AF-017-01 — Product Not Suitable for Resale

1. Return may be recorded.
2. Product does not return to Available inventory.
3. Appropriate damaged/defective status is used.

### AF-017-02 — No Refund Required

If no money needs to be returned:

1. Financial refund steps are skipped.
2. Return transaction is still preserved.

## Exception Flows

### EF-017-01 — Return Outside Standard Window

If the return is outside the seven-day period:

1. The system identifies the return as outside standard policy.
2. Normal processing shall not proceed without appropriate authorization.

### EF-017-02 — Condition Not Acceptable

If the product is not in required condition:

1. The return may be rejected.
2. The reason is recorded.

## Postconditions

1. Return transaction is preserved.
2. Original sale remains historically available.
3. Inventory is updated where appropriate.
4. Refunds are recorded where applicable.

## Related Requirements

- FR-RET-001 through FR-RET-010
- BR-RET-001 through BR-RET-006

---

# 11. UC-018 — Process Exchange

## Use Case ID

UC-018

## Name

Process Exchange

## Primary Actor

Business Administrator or Employee

## Goal

Replace a previously purchased product with another product while correctly adjusting inventory and customer finances.

## Trigger

A customer requests an exchange.

## Preconditions

1. User is authenticated.
2. Original sale exists.
3. Returned product is identifiable.
4. Replacement product exists and is available.
5. Exchange is approved according to business policy.

## Main Success Flow

1. The user locates the original sale.
2. The user selects **Process Exchange**.
3. The user selects the product being returned.
4. The system records return-side information.
5. The user selects the replacement product.
6. The system verifies replacement inventory availability.
7. The system compares:
   - original exchange value;
   - replacement transaction price.
8. The system calculates the financial difference.
9. If replacement is more expensive:
   - the system records the amount owed by the customer.
10. If replacement is cheaper:
    - the system records the amount owed to the customer.
11. The user selects the settlement method where applicable.
12. Inventory for the returned product is updated.
13. Inventory for the replacement product is reduced.
14. The exchange transaction is saved.
15. Historical links to the original sale are preserved.

## Alternate Flows

### AF-018-01 — Replacement More Expensive

1. Customer owes the difference.
2. The amount may be paid immediately or added to the applicable outstanding balance.

### AF-018-02 — Replacement Cheaper — Immediate Refund

1. Business owes the customer the difference.
2. The user records an immediate refund.

### AF-018-03 — Replacement Cheaper — Customer Credit

1. Business owes the customer the difference.
2. Instead of immediate refund, the value is retained as customer credit.
3. The credit is recorded.

### AF-018-04 — Equal Value

If both products have equal applicable values:

1. No additional payment or refund is required.
2. Inventory adjustments still occur.

## Exception Flows

### EF-018-01 — Replacement Product Unavailable

If replacement inventory is unavailable:

1. Exchange cannot be completed using that product.
2. User must select another product or cancel the exchange.

## Postconditions

1. Exchange history exists.
2. Returned inventory is updated.
3. Replacement inventory is updated.
4. Any financial difference is properly recorded.
5. Original sale remains historically traceable.

## Related Requirements

- FR-EXC-001 through FR-EXC-011
- BR-EXC-001 through BR-EXC-006

---

# 12. Cross-Use-Case Integrity Rules

The following behavior applies across the specifications:

1. Inventory shall never become negative.
2. Products cannot be sold before physical receipt.
3. Historical transaction prices shall remain preserved.
4. Financial transactions shall not be silently overwritten.
5. Payment status and delivery status shall remain independent.
6. Returns and exchanges shall preserve original sale history.
7. Personal purchases shall remain excluded from business inventory and profit.
8. Authorization shall be enforced independently of whether a function is visible in the user interface.