"""One-time script to author the two synthetic sample PDFs used by the eval dataset.

Content is hardcoded here (not derived from anywhere else) so it stays auditable and the
ground-truth Q&A pairs in eval/dataset/qa_dataset.json can be written against exact facts.
Re-run this script any time the PDFs need to be regenerated:

    uv run python eval/generate_sample_pdfs.py
"""

from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUT_DIR = Path(__file__).parent / "pdfs"

PRODUCT_REQUIREMENTS = """Product Requirements Document - Project Falcon
Company: Acme Robotics, Inc.
Document version: 2.3
Prepared by: Maria Chen, Senior Product Manager
Date: March 12, 2026
Status: Approved

1. Overview
Project Falcon is Acme Robotics' second-generation autonomous home cleaning robot, codenamed \
"Falcon." It succeeds the "Sparrow" model launched in 2024. Falcon is designed for medium to \
large homes up to 2,500 square feet and introduces LiDAR-based mapping, a self-emptying dock, \
and a mobile app with room-specific scheduling.

2. Goals and Success Metrics
- Achieve a battery life of at least 150 minutes per charge on the Standard cleaning mode.
- Reduce customer support tickets related to navigation errors by 40 percent compared to Sparrow.
- Reach 100,000 units sold within the first six months of launch.
- Maintain a customer satisfaction (CSAT) score of 4.5 out of 5 or higher.

3. Target Launch Date
Falcon is scheduled for general availability on September 15, 2026, with a limited early-access \
rollout beginning August 1, 2026 for 5,000 waitlisted customers.

4. Team
- Product Manager: Maria Chen
- Engineering Lead: Devon Okafor
- Hardware Lead: Priya Raman
- QA Lead: Tom Whitfield
The Falcon team consists of 14 engineers across firmware, mobile, and mechanical design.

5. Budget
The total approved budget for Project Falcon is $8.2 million, allocated as follows: $4.5 million \
for hardware R&D, $2.1 million for software development, $1.0 million for marketing, and $0.6 \
million for contingency.

6. Key Features
- LiDAR navigation with room mapping, up to 5 floors saved per household
- Self-emptying dock with a 60-day dust bag capacity
- Battery life: 150 minutes on Standard mode, 90 minutes on Max Power mode
- Suction power: 4,000 Pa
- Weight: 3.8 kg
- Retail price: $649
- Companion mobile app supporting iOS 16+ and Android 12+
- Voice control via Alexa and Google Assistant integration

7. Out of Scope for v1
- Multi-robot coordination, planned for Falcon v2, targeted for 2027
- Outdoor or patio cleaning mode
- Integration with third-party smart-home hubs other than Alexa and Google Assistant

8. Risks
- The LiDAR sensor supplier, OptiSense Corp, has a lead time of 16 weeks, which could delay \
hardware production if orders are not placed by April 30, 2026.
- An industry-wide battery cell shortage could affect the Max Power mode battery target.

9. Approval
This document was approved by the Product Steering Committee on March 20, 2026.
"""

EMPLOYEE_HANDBOOK = """Employee Handbook
Company: Northwind Analytics Inc.
Effective Date: January 1, 2026

1. About Northwind Analytics
Northwind Analytics Inc. was founded in 2016 and is headquartered in Austin, Texas, with a \
satellite office in Toronto, Canada. The company has approximately 340 employees as of 2026.

2. Working Hours
Standard working hours are 9:00 AM to 5:30 PM local time, Monday through Friday, with a \
30-minute unpaid lunch break. Core collaboration hours, during which all employees must be \
reachable, are 10:00 AM to 3:00 PM.

3. Remote Work Policy
Employees may work remotely up to 3 days per week. Fully remote arrangements require written \
approval from a Director-level manager or above. Employees must be available on video for all \
scheduled meetings regardless of location.

4. Paid Time Off
Full-time employees accrue 18 days of paid vacation per year during their first three years of \
employment, increasing to 23 days after three years of tenure. Employees also receive 8 paid \
sick days per year and 11 paid company holidays.

5. Probation Period
All new hires undergo a 90-day probationary period, during which either party may terminate \
employment with 2 weeks' notice.

6. Benefits
Northwind offers a 401(k) retirement plan with a 4 percent company match on employee \
contributions up to 6 percent of salary. Health insurance premiums are covered at 85 percent by \
the company for employees and 60 percent for dependents. Employees become eligible for benefits \
on the first day of the month following their start date.

7. Expense Policy
Employees may expense up to $75 per day for meals while traveling on company business, and must \
submit receipts for any single expense over $25. Expense reports must be submitted within 30 \
days of the expense being incurred.

8. Code of Conduct
Employees are expected to treat colleagues, clients, and partners with respect and \
professionalism. Harassment, discrimination, and retaliation of any kind are strictly \
prohibited and should be reported to Human Resources or via the anonymous ethics hotline.

9. Performance Reviews
Formal performance reviews are conducted twice per year, in June and December. New hires \
receive an additional 90-day review during their probation period.
"""


def write_pdf(text: str, out_path: Path) -> None:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("helvetica", size=11)
    for line in text.split("\n"):
        if not line.strip():
            pdf.ln(4)
            continue
        pdf.multi_cell(0, 6, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.output(str(out_path))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_pdf(PRODUCT_REQUIREMENTS, OUT_DIR / "product_requirements.pdf")
    write_pdf(EMPLOYEE_HANDBOOK, OUT_DIR / "employee_handbook.pdf")
