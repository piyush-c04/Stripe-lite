Phase 1 (MVP) – Basic Billing

User signup/login (multi-tenant support: company A, company B)

Create subscription plans (e.g., ₹499/month, $20/year)

Subscribe a user → start billing cycle

Generate an invoice (store in DB, maybe PDF later)

Integrate with one payment gateway (e.g., Razorpay)

Phase 2 – Smart Billing

Auto-renewal: charge users automatically each cycle

Handle failed payments (retry 3 times, mark as unpaid if fails)

Email notifications for billing events (payment success/failure)

Phase 3 – Compliance & Scaling

GST/VAT tax calculation per region

Multi-currency support

Usage-based billing (e.g., pay per API call, per GB storage)

Dashboard for tenants to view their invoices & subscriptions