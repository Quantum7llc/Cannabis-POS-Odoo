# MSPMP Reporting Specification

**Mississippi State Prescription Monitoring Program**

## Overview

Daily batch reporting of controlled substance dispensing to the PMP Clearinghouse via SFTP.

## Format

- **Standard**: ASAP 4.2 (American Society for Automation in Pharmacy)
- **Delivery**: SFTP batch upload
- **Frequency**: Daily (end of business day)
- **Destination**: PMP Clearinghouse (state-assigned SFTP credentials)

## Required Data Per Transaction

- Patient: name, DOB, ID number, ID state, address
- Product: name, NDC (if applicable), quantity, days supply
- Prescriber/Recommending physician info
- Dispensary: DEA number, license, facility info
- Transaction: date, time, payment method
- Employee: dispensing budtender ID

## Implementation Notes

Both versions must generate identical ASAP 4.2 formatted files for the same transaction data. Test by comparing output from both systems against the same sample dataset.
