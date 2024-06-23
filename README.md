# Llama3-Radiology-Report-Augmentation

Llama3 is one of the most recognized and widely used large language models (LLMs) today. Due to its capabilities, it is interesting to leverage it for generating more data through text augmentation. In this repository, Llama3 is used to generate different reports based on an original report.

## Usage Example

```
from ta_api import generate_new_report_Llama3

REPORT = "Lateral view somewhat limited due to overlying motion artifact. The lungs are low in volume. There is no focal airspace consolidation to suggest pneumonia. A 1.2-cm calcified granuloma just below the medial aspect of the right hemidiaphragm is unchanged from prior study. No pleural effusions or pulmonary edema. There is no pneumothorax. The inferior sternotomy wire is fractured but unchanged. Surgical clips and vascular markers in the thorax are related to prior CABG surgery."

new_report = generate_new_report_Llama3(REPORT, reorder=True)
print(new_report)
```
