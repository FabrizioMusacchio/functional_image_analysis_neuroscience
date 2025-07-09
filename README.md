# Functional Imaging Data Analysis in Neuroscience: From Calcium Signals to Integrated Behavior Mapping

In this course, students will learn essential computational approaches for analyzing functional imaging data in neuroscience. The focus is on the full workflow: quantitative processing of calcium imaging data, inference of neuronal spiking activity, and the integration of behavioral measurements with neuronal activity. All analyses are based on open-source Python tools (CaImAn, CASCADE), and the course emphasizes practical, reproducible methods that do not require advanced programming skills.

## Learning outcomes
Upon successful completion, students will be able to:

* **Understand the principles and workflow of functional calcium imaging data analysis in neuroscience**
  * Explain the rationale for using calcium imaging and its advantages and limitations for studying neuronal population dynamics.
* **Process and analyze calcium imaging data using CaImAn**
  * Perform motion correction, segmentation, and extraction of fluorescence signals from raw calcium imaging data.
  * Apply quantitative quality control and data visualization methods to extracted traces.
* **Infer neuronal spiking activity from calcium imaging signals using CASCADE**
  * Understand the challenges and approaches for inferring action potentials from slow calcium dynamics.
  * Apply the CASCADE pipeline to convert calcium traces into estimated spike trains and evaluate inference accuracy.
* **Integrate behavioral data with neuronal activity**
  * Synchronize, merge, and visualize behavioral measurements (e.g., locomotion, stimulus presentation) with inferred neuronal activity.
  * Implement basic statistical and visualization methods to explore relationships between neuronal population activity and behavior.
* **Critically evaluate the limitations, sources of error, and reproducibility of each analysis step**
  * Identify common pitfalls in calcium imaging analysis and spike inference.
  * Document and reproduce analysis workflows using recommended open-source tools.

## Acknowledgements
Sample data used in this course include:
* **CaImAn sample calcium imaging data:** Example datasets are provided by the CaImAn project (Giovannucci et al., *eLife*, 2019) and are available through the official [CaImAn GitHub repository](https://github.com/flatironinstitute/CaImAn){{site.data.scuts.extlink}}. Please refer to the repository for detailed licensing and citation information.
* **CASCADE sample traces:** Example datasets and ground truth traces are provided by the CASCADE project (Giovannucci et al., *Nature Methods*, 2020) and are available via the official [CASCADE repository](https://github.com/HelmchenLabSoftware/Cascade/tree/master){{site.data.scuts.extlink}}. Refer to the repository and associated publications for further details.

We gratefully acknowledge the original authors and maintainers of CaImAn and CASCADE for making their sample data publicly available for educational and research purposes.