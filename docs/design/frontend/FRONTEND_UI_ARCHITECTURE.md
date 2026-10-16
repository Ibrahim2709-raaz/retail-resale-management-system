# RRMS Frontend / UI Architecture

**Document ID:** RRMS-UI-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.5 — Frontend / UI Architecture Design  
**Related Architecture:** RRMS-ARCH-001  
**Related API Design:** RRMS-API-001  
**Related Requirements:** RRMS-SRS-001 v1.0  

---

## 1. Purpose

This document defines the frontend structure, navigation model, screen hierarchy, interaction patterns, permission behavior, and API boundaries for the Retail Resale Management System.

It does not define final visual branding, CSS styling, component code, or frontend framework implementation.

---

## 2. Frontend Scope

Version 1 prioritizes the internal business application for:

- Administrator
- Employee

The future customer storefront is treated as a separate customer-facing experience.

The internal UI and future storefront may share selected data services but should not share navigation or authorization assumptions.

---

## 3. Application Shell

After login, internal users enter a common application shell.

The shell should provide:

- persistent sidebar navigation;
- page title / breadcrumb area;
- user account menu;
- global search where useful;
- notification/alert entry point;
- responsive navigation behavior;
- consistent success/error feedback.

The shell should remain stable while page content changes.

---

## 4. Primary Navigation

Recommended main navigation:

1. Dashboard
2. Products
3. Purchasing
4. Inventory
5. Customers
6. Reservations
7. Sales
8. Payments & Credit
9. Deliveries
10. Returns & Exchanges
11. Expenses
12. Reports
13. User Management — Administrator only

The navigation should use business language rather than technical database terminology.

---

## 5. Authentication Screens

### Login

Fields:

- login identifier
- password

Behavior:

- show generic authentication failure;
- never reveal whether an account exists;
- redirect authenticated users into the internal dashboard;
- inactive users cannot log in.

---

## 6. Dashboard

The dashboard is a business overview, not a replacement for detailed reports.

Recommended content:

- current available inventory;
- active reservations;
- unpaid / partially paid sales;
- outstanding customer balances;
- recent sales;
- pending deliveries;
- aged stock alerts;
- recent received inventory;
- selected revenue/profit summary;
- operational notifications.

Widgets shown should depend on the authenticated user's permissions.

---

## 7. Product Screens

### Product List

Should support search, brand/category filtering, active/inactive filtering, season filtering, pagination, and quick access to product details.

### Product Details

Should show product master data, brand/category, images, SKU/barcode fields, current inventory summary, and related history references.

### Create / Edit Product

Use sections for identity, classification, descriptive attributes, media, and notes.

Historical transaction fields must never be editable from Product master forms.

---

## 8. Purchasing Screens

### Purchase List

Show source, date, business/personal type, status, external order number, and totals where relevant.

### Create Purchase

Recommended flow:

1. purchase header;
2. business vs personal classification;
3. source;
4. purchased line items;
5. costs;
6. receipt attachment;
7. review and confirm.

### Receive Purchase

Receiving should be a dedicated workflow showing outstanding purchased quantity, quantity received, condition, received date/time, and resulting inventory behavior.

---

## 9. Inventory Screens

### Inventory List

Recommended filters:

- available;
- reserved;
- sold;
- damaged;
- on hold;
- returned;
- product;
- brand;
- category;
- condition.

Important columns include product, status, condition, quantity received, quantity available, acquisition reference, and received date.

Direct editing of available quantity should not be a standard form control.

---

## 10. Customer Screens

### Customer List

Support name search, phone search, city filtering where useful, and current outstanding balance indicators.

### Customer Profile

Recommended sections:

- overview;
- sales;
- payments;
- reservations;
- outstanding balances;
- delivery details;
- notes/preferences.

Outstanding balance is a calculated display value, not an editable field.

---

## 11. Reservation Screens

### Reservation List

Highlight active, expired-but-held, extended, released, completed, and cancelled reservations.

Expired reservations must be visually distinct because expiry does not automatically release inventory.

### Create Reservation

1. select customer;
2. select available inventory;
3. enter quantity;
4. review default expiry;
5. confirm.

### Reservation Detail

Actions may include extend, release, cancel, and opening linked customer/product records.

---

## 12. Sales Screens

### Sale List

Recommended columns include sale reference, customer, date, total, payment status, and delivery status where applicable.

### Create Sale

Recommended flow:

1. select/create customer;
2. add available or customer-reserved inventory;
3. display pricing;
4. adjust price where authorized;
5. apply discount where allowed;
6. display totals;
7. show below-cost warning if triggered;
8. confirm sale;
9. proceed to payment or leave balance outstanding;
10. offer receipt generation.

Inventory and pricing must be revalidated by the backend at confirmation.

### Sale Detail

Show sale items, preserved transaction prices, authorized cost/profit data, payment history, outstanding amount, delivery, return/exchange history, and receipt actions.

---

## 13. Payments & Credit Screens

### Outstanding Balances

Allow users to view customer, total outstanding, unpaid/partially paid sales, optional due dates, and overdue indicators.

### Record Payment

1. select customer/sale;
2. display outstanding amount;
3. enter payment;
4. choose payment method;
5. confirm;
6. display new balance/payment status.

Payment history should be displayed as a sequence of transactions.

---

## 14. Delivery Screens

### Delivery List

Show tracking/reference, customer, related sale, status, delivery address, delivery fee, and rider where applicable.

### Delivery Detail

Allow valid status transitions only.

---

## 15. Returns & Exchanges Screens

### Return Flow

1. locate original sale;
2. select eligible SaleItem;
3. enter quantity;
4. record reason;
5. record returned condition;
6. determine restock result;
7. record refund if required;
8. confirm.

### Exchange Flow

1. locate original transaction;
2. select item being exchanged;
3. select replacement inventory;
4. compare values;
5. calculate difference;
6. select settlement;
7. confirm.

Original sale history remains preserved.

---

## 16. Expense Screens

Expense screens should support general and transaction-linked expenses, with filtering by date, type, sale, and delivery.

---

## 17. Reports Screens

Initial reports include:

- revenue;
- gross profit;
- net profit;
- expenses;
- sales by time period;
- sales by brand/category;
- inventory value;
- aged inventory;
- outstanding balances;
- customer activity.

Reports are read-only.

---

## 18. User Management

Administrator-only area for listing users, creating employees, viewing roles, and activating/deactivating accounts.

---

## 19. Future Storefront

The customer storefront is a separate UI surface with planned screens for:

- product browse;
- product details;
- order request;
- order-request confirmation.

Customers do not require accounts in the initial planned storefront.

Order-request holds do not automatically expire.

---

## 20. List / Table Pattern

Operational list screens should use a consistent structure:

- page title;
- primary action;
- search/filter area;
- table or structured list;
- pagination;
- row actions;
- empty state;
- loading state;
- error state.

---

## 21. Form Pattern

Forms should use clear labels, required-field indication, logical grouping, inline validation, backend validation feedback, explicit submit actions, destructive-action confirmation, and duplicate-submit prevention.

Multi-step transactions should use review/confirmation before final submission.

---

## 22. Status Presentation

Statuses must use clear text labels consistently. Color may assist recognition but must not be the only indicator.

---

## 23. Permission-Aware UI

The frontend may hide or disable controls based on role for usability, but backend authorization remains authoritative.

The UI must correctly handle `403 Forbidden` responses.

---

## 24. Frontend State Ownership

### Local UI State
Dialogs, tabs, temporary form state.

### Server State
Products, Inventory, Customers, Sales, Payments, Reports.

### Authentication State
Current user, role, authenticated state.

The frontend should not duplicate business-source-of-truth values when the API can provide them.

---

## 25. API Integration Boundary

The frontend communicates only with the RRMS Backend API.

It must not directly query PostgreSQL or independently enforce authoritative inventory, pricing, or balance rules.

---

## 26. Error and Feedback Pattern

The UI should support:

- field validation messages;
- business-rule warnings;
- conflict dialogs;
- success confirmations;
- recoverable API errors;
- unexpected-error fallback.

Technical stack traces must never be shown to users.

---

## 27. Responsive Behavior

The internal application should prioritize desktop/laptop use while remaining usable on tablets and mobile.

The future customer storefront should be mobile-first.

---

## 28. Accessibility

The frontend should provide keyboard-accessible controls, visible focus states, proper labels, semantic headings, sufficient contrast, icon text alternatives, and non-color-only status communication.

---

## 29. Deliberate Deferrals

Stage 3.5 does not yet define:

- exact frontend framework;
- design system library;
- colors;
- typography;
- logo usage;
- pixel-level layouts;
- component source code;
- CSS architecture;
- state-management library;
- frontend folder structure;
- animation behavior.

---

## 30. Diagram Files

- `FRONTEND_SCREEN_MAP.drawio`
- `FRONTEND_SCREEN_MAP.png`

---

## 31. Stage 3.5 Completion Gate

Stage 3.5 is complete when:

1. `FRONTEND_UI_ARCHITECTURE.md` is committed;
2. `FRONTEND_SCREEN_MAP.drawio` is committed;
3. `FRONTEND_SCREEN_MAP.png` is committed;
4. all core Version 1 business capabilities have a UI entry point;
5. navigation and permission behavior are clear;
6. frontend and backend responsibilities are separated;
7. the future storefront remains clearly separated from the internal business UI;
8. no unresolved frontend-architecture issue blocks detailed UI or implementation planning.
