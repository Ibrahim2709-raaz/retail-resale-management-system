# RRMS System Context Model

**Document ID:** RRMS-SCM-001  
**Version:** 1.0  
**Status:** Baseline  
**Related Requirements:** RRMS-SRS-001 v1.0

## 1. Purpose

The System Context Model defines the boundary of the Retail Resale Management System (RRMS) and identifies the primary external actors and external systems that exchange information with it.

The model intentionally excludes internal implementation details such as application frameworks, databases, servers, deployment topology, and internal APIs.

## 2. System Boundary

RRMS acts as the central system of record for the business's operational information. At the product level, the system manages information relating to:

- purchasing;
- products;
- inventory;
- customers;
- reservations;
- sales;
- payments and customer credit;
- deliveries;
- returns and exchanges;
- expenses;
- receipts;
- reporting and analytics.

The system context represents the long-term RRMS product boundary. Some customer-facing functionality shown in the model is outside the mandatory Version 1 release scope, as defined in the SRS.

## 3. External Actors and Systems

### 3.1 Business Administrator

Business administrators are the owner and co-administrator. They perform management and operational activities including purchasing, product and inventory management, customer management, sales, payments, credit management, returns, exchanges, expenses, delivery administration, reporting, and user administration.

RRMS provides administrators with inventory information, customer balances, sales records, receipts, reports, and alerts or notifications.

### 3.2 Employee

Employees use RRMS for authorized operational activities such as product, inventory, customer, sales, payment, and delivery updates.

Specific permissions are governed by role-based authorization requirements rather than by the context model itself.

### 3.3 Customer

Customers interact with the business through product enquiries, order requests, purchases, payments, returns, exchanges, and delivery activity.

Direct customer-facing interaction with RRMS expands when the public storefront is introduced. The storefront is part of the long-term product boundary but is not mandatory for Version 1.

### 3.4 Product Source / Supplier

Products are obtained from online retailers, physical stores, and supply markets.

Supplier-side information such as product information, purchase information, order numbers, and receipts is initially entered into RRMS manually by an authorized business user. Direct supplier-system integration is not required.

### 3.5 Delivery Rider

Delivery riders perform physical delivery of customer orders.

RRMS maintains internal delivery reference numbers, customer delivery details, delivery fees, and delivery status. In Version 1, rider interactions are represented as manual business processes rather than a direct rider application or external courier API integration.

### 3.6 WhatsApp

WhatsApp remains an important external communication and product-marketing channel.

RRMS may generate product information, links, or receipt information suitable for sharing through WhatsApp. Direct WhatsApp Business API integration is outside Version 1 scope.

## 4. Information Flows

### Business Administrator → RRMS

- product information;
- purchases;
- customer information;
- sales;
- payments;
- reservations;
- returns and exchanges;
- expenses;
- delivery updates;
- user-management actions.

### RRMS → Business Administrator

- inventory status;
- customer balances;
- sales records;
- receipts;
- business reports;
- alerts and notifications.

### Employee → RRMS

- operational data;
- sales;
- payments;
- inventory updates;
- customer information;
- delivery updates.

### RRMS → Employee

- inventory information;
- customer information;
- sales information;
- operational alerts.

### Customer → RRMS

- order requests;
- product enquiries;
- customer details;
- return requests.

### RRMS → Customer

- product information;
- order information;
- receipt information;
- payment or balance information;
- delivery information.

### Product Source / Supplier → RRMS

- product information;
- purchase and order information;
- receipts.

This information is initially recorded manually by an authorized business user.

### RRMS ↔ Delivery Rider

RRMS provides delivery assignments, customer delivery details, and internal tracking references. Delivery status and outcomes are recorded back into RRMS. In Version 1 these interactions are handled manually by business users rather than through a direct rider integration.

### RRMS → WhatsApp

RRMS may provide shareable product and receipt information. No direct WhatsApp Business API integration is required for Version 1.

## 5. Context-Level Assumptions

1. RRMS is the authoritative digital system for business records managed through the application.
2. External supplier information is initially captured manually.
3. Rider information and delivery outcomes are initially entered manually by authorized business users.
4. WhatsApp remains external to the core system in Version 1.
5. Customer-facing storefront functionality is within the long-term RRMS product vision but outside mandatory Version 1 scope.
6. Internal implementation components are intentionally excluded from this model.

## 6. Diagram Files

- `SYSTEM_CONTEXT.drawio` — editable diagrams.net source.
- `SYSTEM_CONTEXT.png` — exported image for quick viewing in GitHub.
