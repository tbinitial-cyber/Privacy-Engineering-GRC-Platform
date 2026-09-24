# 📐 FOLDER 01: Step 1 - Canonical Evidence Schema

### What is in this folder?
- `evidence.schema.json`: The master technical blueprint (JSON Schema Draft 2020-12).

### Plain English Explanation:
- **What is it?** Think of this as the "blank standardized audit form" or "passport format". Before taking any data from a website, we must strictly define what fields are allowed.
- **Why is it so big?** Because in real audits, you capture cookies, HTTP network requests, headers, SSL certificates, and storage. Every single field must have a strict data type (string, integer, boolean) so bad or fake data cannot enter.
- **Why is it important?** If an auditor or regulator asks: *"How do I know this data is standard and not made up?"*, you show them this schema. It proves that every piece of evidence followed a strict mathematical contract.
