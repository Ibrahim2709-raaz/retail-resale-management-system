# RRMS Process / Activity Models

**Document ID:** RRMS-PAM-001  
**Version:** 1.0  
**Status:** Baseline  
**Related Requirements:** RRMS-SRS-001 v1.0  
**Related Use Case Specifications:** RRMS-UCS-001  
**Related Domain Model:** RRMS-DM-001  

## 1. Purpose

This document defines the main business workflows of the Retail Resale Management System (RRMS) before database and implementation design.

The activity models describe business behavior and decision points. They do not define user-interface screens, API endpoints, or database operations.

## 2. Modeled Processes

Stage 2.5 contains three workflow diagrams:

1. Purchase, Receiving & Inventory
2. Reservation, Sale, Payment & Delivery
3. Return & Exchange

## 3. Purchase, Receiving & Inventory

The process begins when an authorized user records a purchase.

Business purchases enter the acquisition workflow. Personal purchases remain recorded but do not create business inventory or affect business profitability.

Business products remain in acquisition states such as Ordered or In Transit until physically received. When received, condition and quantity are verified. Sellable items may become Available inventory, while damaged, defective, or otherwise unsuitable items remain unavailable.

Key rules:

- products cannot be sold before physical receipt;
- received quantity cannot exceed outstanding purchased quantity;
- personal purchases do not create business stock;
- damaged or defective products do not automatically become Available.

Diagram files:

- `PURCHASE_RECEIVING_ACTIVITY.drawio`
- `PURCHASE_RECEIVING_ACTIVITY.png`

## 4. Reservation, Sale, Payment & Delivery

A customer may purchase an available product directly or request a reservation first.

An active reservation protects inventory from ordinary conflicting sales. The standard reservation period is 48 hours. Expiry generates a notification but does not automatically release the stock.

When a sale is confirmed, the system records the selected inventory and preserves the final transaction prices. Payment may be full, partial, deposit-based, or credit-based.

If the sale is not fully paid, the remaining amount contributes to the customer outstanding balance. A sale may have multiple payment transactions.

Delivery is handled independently from payment status. If delivery is required, the system creates an internal delivery record and tracks its progress.

Key rules:

- inventory must never become negative;
- reserved inventory is unavailable to ordinary conflicting sales;
- historical transaction prices remain preserved;
- below-cost sales require warning and authorized acknowledgement;
- payment status and delivery status are independent;
- one sale may have multiple payments.

Diagram files:

- `SALES_FULFILLMENT_ACTIVITY.drawio`
- `SALES_FULFILLMENT_ACTIVITY.png`

## 5. Return & Exchange

Returns and exchanges must preserve the original sale history.

For a return, the system identifies the original sale and validates the request according to business policy. If the returned product remains suitable for resale, inventory may be restored to Available. Otherwise, the item is placed into an appropriate damaged or unavailable state.

For an exchange, the system identifies the original transaction, verifies replacement inventory, and records the replacement. If the replacement costs more, the customer owes the difference. If it costs less, the business may issue an immediate refund or retain the difference as customer credit. Equal-value exchanges require no financial adjustment.

Key rules:

- the original sale must never be deleted or overwritten;
- returned inventory becomes Available only when resellable;
- replacement inventory must be available;
- refunds and customer credits remain recorded historically;
- exchange financial differences must be explicitly settled.

Diagram files:

- `RETURN_EXCHANGE_ACTIVITY.drawio`
- `RETURN_EXCHANGE_ACTIVITY.png`

## 6. Cross-Process Integrity Rules

1. Business inventory originates from physically received business purchases.
2. Inventory shall never become negative.
3. Personal purchases remain separate from business inventory and profit.
4. Reservation expiry does not automatically release inventory.
5. Historical transaction values remain preserved.
6. Payments are independent financial events.
7. Payment and delivery status remain independent.
8. Returns and exchanges preserve the original sale.
9. Expenses may be general or transaction-linked.
10. Important state-changing operations remain attributable to an authenticated user.

## 7. Deliberate Exclusions

These models do not define:

- database tables or SQL;
- API endpoints;
- UI screens;
- framework classes;
- deployment architecture.

Those belong to later stages.

## 8. Stage 2.5 Completion Criteria

Stage 2.5 is complete when the repository contains:

- `PROCESS_ACTIVITY_MODELS.md`
- `PURCHASE_RECEIVING_ACTIVITY.drawio`
- `PURCHASE_RECEIVING_ACTIVITY.png`
- `SALES_FULFILLMENT_ACTIVITY.drawio`
- `SALES_FULFILLMENT_ACTIVITY.png`
- `RETURN_EXCHANGE_ACTIVITY.drawio`
- `RETURN_EXCHANGE_ACTIVITY.png`

and these artifacts remain consistent with the SRS, use-case specifications, and domain model.
