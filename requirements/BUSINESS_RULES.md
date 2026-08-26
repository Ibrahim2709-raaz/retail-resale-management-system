# Retail Resale Management System — Business Rules

**Document ID:** RRMS-BR-001  
**Version:** 0.1  
**Status:** Draft  
**Last Updated:** August 2026


Inventory and product rules

BR-INV-001
A purchased product shall not be treated as sellable inventory until it has been physically received by the business.

BR-INV-002
Products shall not be sold before physical receipt.

BR-INV-003
The business primarily sells unstitched clothing; product size is therefore not mandatory.

BR-INV-004
The system shall support both single-unit products and rare cases where multiple identical units of the same product are held.

BR-INV-005
Available inventory quantity shall never become negative.

BR-INV-006
Damaged or defective products shall not be treated as normally sellable inventory unless an authorized user explicitly approves them for sale.

Purchase rules

BR-PUR-001
Purchases must distinguish between business resale purchases and personal purchases.

BR-PUR-002
Personal purchases shall not contribute to business inventory value, revenue, or profitability calculations.

BR-PUR-003
Shipping, rider, and petrol costs may be recorded as business expenses when applicable.

Pricing rules

BR-PRICE-001
The business does not use a fixed markup percentage.

BR-PRICE-002
The business may manually determine the selling price of a product.

BR-PRICE-003
The business may negotiate selling prices with customers.

BR-PRICE-004
Products may be sold at cost.

BR-PRICE-005
The system shall warn the user when a proposed sale price is below final product cost.

BR-PRICE-006
The business does not normally permit intentional below-cost sales.

Reservation rules

BR-RES-001
A product may be reserved for a customer.

BR-RES-002
The default reservation period is 48 hours.

BR-RES-003
An authorized user may manually extend a reservation.

BR-RES-004
Expired reservations shall generate a notification.

BR-RES-005
Expired reservations shall not be released automatically.

BR-RES-006
A reserved product shall not be sold to another customer unless the reservation is released, cancelled, or explicitly overridden by an authorized user.

Online order-request rules

BR-ORD-001
Online customers may submit order requests without creating an account.

BR-ORD-002
An online order request does not immediately constitute a confirmed sale.

BR-ORD-003
Every online order request must be approved or rejected by an authorized business user.

BR-ORD-004
Inventory associated with a submitted online order request shall be placed on temporary hold.

BR-ORD-005
Temporary holds created by online order requests shall not expire automatically.

BR-ORD-006
A temporary hold shall remain in effect until an authorized user approves, rejects, releases, cancels, or overrides the request.

Payment and credit rules

BR-PAY-001
Customers may pay in full, partially, through deposits, on credit, or through cash on delivery.

BR-PAY-002
Each payment received shall be recorded as a separate transaction.

BR-PAY-003
A customer may have an outstanding balance.

BR-PAY-004
The business does not enforce a fixed customer credit limit.

BR-PAY-005
Credit sales do not require a mandatory payment due date.

BR-PAY-006
A payment due date may be recorded when one is agreed upon.

BR-PAY-007
Order status, payment status, and delivery status are independent business concepts.

That last rule is important. For example, an order may be DELIVERED while payment is still PARTIALLY_PAID.

Return rules

BR-RET-001
Customer returns are permitted within seven days of the original sale.

BR-RET-002
Returned products must be in their original condition.

BR-RET-003
A return must be approved by an authorized business user.

BR-RET-004
A returned item may only return to available inventory if it is suitable for resale.

BR-RET-005
The original sale record shall remain in the system after a return.

Exchange rules

BR-EXC-001
Customer exchanges are permitted.

BR-EXC-002
When the replacement product costs more than the returned product, the customer must pay the difference.

BR-EXC-003
When the replacement product costs less than the returned product, the business owes the customer the difference.

BR-EXC-004
Both the returned and replacement products must have their inventory records updated during an exchange.

BR-EXC-005
Exchange history shall be preserved.

Delivery rules

BR-DEL-001
The business primarily uses riders for delivery rather than courier services.

BR-DEL-002
The system shall assign its own unique tracking/reference number to deliveries.

BR-DEL-003
Delivery charges are normally paid by the customer.

BR-DEL-004
Delivery status shall be tracked separately from payment status.

Customer rules

BR-CUS-001
Customers do not require registered storefront accounts.

BR-CUS-002
Customer phone and WhatsApp information are important customer identifiers.

BR-CUS-003
Customer birthdays are not required.

BR-CUS-004
Customer email addresses are not required.

Storefront rules

BR-STORE-001
All suitable inventory may be published to the customer-facing storefront.

BR-STORE-002
Sold products may remain visible after sale.

BR-STORE-003
Sold products must clearly indicate that they are unavailable.

BR-STORE-004
The business may choose whether to display the original retail price for each product.

BR-STORE-005
Exact inventory quantity shall not be required on the customer-facing storefront.

BR-STORE-006
Low-stock messaging such as “Only 1 left” is not required.

BR-STORE-007
The storefront may display products as Coming Soon, especially for seasonal changes.

Reporting rules

BR-REP-001
Business reporting shall distinguish revenue from profit.

BR-REP-002
Net-profit reporting shall take recorded business expenses into account.

BR-REP-003
Personal purchases shall not be included in business profitability calculations.

BR-REP-004
Outstanding customer credit must remain visible in business reporting.

BR-REP-005
The system shall support identification of ageing inventory, including products unsold for more than 30 and 90 days.

User and access rules

BR-SEC-001
The business owner and co-administrator shall have administrative access.

BR-SEC-002
Employees may have more limited permissions than administrators.

BR-SEC-003
Customer-facing users shall not have access to internal business or financial information.

BR-SEC-004
Sensitive financial functionality shall be restricted to authorized internal users.


## Rule Governance

Business rules in this document are derived from stakeholder interviews and the approved functional requirements.

Changes to a business rule that affect an existing functional requirement shall also trigger a review of the corresponding SRS requirement.

The business rules remain in Draft status until stakeholder validation is completed.