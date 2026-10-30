# Medically Frail: The Exemption States Can't Afford To Get Wrong

**Medicaid 2027 Series - Part 2**

Members who are medically frail are exempt from Medicaid work requirements, but only if the state can find them in its own data. Most eligibility systems were built to check income and household size, not to read a year of medical claims, so a seriously ill member can easily receive a notice they can't answer in time. On October 29, 2026, a federal court also struck down part of the federal definition, which means frailty logic built over the summer may already need rework.

Written for state eligibility and policy teams, and for the vendors who build their systems.

**Live guide:** https://archanacontent.github.io/medically-frail-guide/

## What's Inside

- **Where Frail Members Get Missed** - the problem, the key numbers and the projected coverage losses.
- **Who Counts As Medically Frail** - the five federal groups and each state's condition list.
- **What The October 29 Ruling Changed** - what the court struck down, what it kept and what is still unsettled.
- **Finding Frail Members In Existing Data** - a data-first method using CMS's optional three-tier framework.
- **When The Data Falls Short** - member statements, documentation and the 2028 limit.
- **Rules And Dates** - the rules in one table, the sources and the change log.
- **Caseworker Quick Reference** - a printable one-page decision flow, *Is This Member Exempt?*

## How It's Built

The guide is authored in DITA 1.3 and published to a website and a PDF with [DITA-OT](https://www.dita-ot.org/) 4.4.1.

- **Topic types** - concept, task, reference and glossary topics, assembled by one ditamap.
- **Keys** - dates and source links are defined once in the map and reused across every topic.
- **Content references** - shared sentences live in `dita/reuse/shared.dita` and are pulled into topics with conref, so each one is updated in one place.
- **Website** - the DITA-OT HTML5 output with a custom header, footer, stylesheet and script in `build/html`.
- **PDF** - DITA-OT's PDF2 output with print styling in `build/pdf`.

```
dita/        DITA source: map, topics, reusable content, images, downloads
build/       Build script, theme files and PDF customization
onepager/    Source for the caseworker quick reference
```

To build it yourself, install DITA-OT 4.4.1 and Python 3, then run:

```
DITA=/path/to/dita-ot-4.4.1/bin/dita build/build.sh
```

The website lands in `out/site` and the PDF in `out/pdf`.

## Sources

Every claim links to its source in the guide. The main sources are CMS's guidance [Implementing Medical Frailty Under Community Engagement](https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation/community-engagement/ImplementingMedicalFrailtyDeck.pdf), the [interim final rule CMS-2454-IFC](https://www.federalregister.gov/documents/2026/06/03/2026-11094/medicaid-program-community-engagement-requirement-for-certain-individuals), and coverage of the October 29, 2026 ruling by [HFMA](https://www.hfma.org/payment-reimbursement-and-managed-care/medicaid-work-requirement-medical-frailty-ruling/) and [Becker's](https://www.beckershospitalreview.com/legal-regulatory-issues/judge-rules-cms-overstepped-on-medically-frail-definition-for-medicaid-work-requirements/).

An independent guide for informational purposes. It is not legal advice and is not affiliated with CMS or any state agency.

## Also In The Series

- [Medicaid 2027 Implementation Guide](https://archanacontent.github.io/medicaid-2027-implementation-guide/) - Part 1, on work requirements and six-month renewals.

## License

Content is licensed under [CC BY 4.0](LICENSE). Written by [Archana Panda](https://archanacontent.github.io/).
