

# ECG Cardiopathy Classification: Direct vs Cascade Learning

This repository implements a comparative study between a standard Multiclass CNN and a **3-Stage Cascade CNN** for electrocardiogram (ECG) image classification.

## 🔬 Research Context
Traditional CNNs often struggle with fine-grained differences between clinically similar cardiac conditions. Our approach uses a **staged refinement strategy** that mimics clinical diagnostic reasoning.

## 🚀 Key Results
- **Direct Multiclass CNN:** 92.0% Accuracy
- **Cascade CNN (Ours):** **97.1% Accuracy**
- The Cascade method shows superior performance in distinguishing between "History of MI" and "Current MI".

## 🛠️ Methodologies
1. **Direct CNN:** A single 4-class model trained on all pathologies.
2. **Cascade CNN:** 
   - **Stage 1:** Binary classification (Normal vs. Pathological).
   - **Stage 2:** 3-class refinement (Normal, Current MI, Others).
   - **Stage 3:** Final 4-class classification using weights transfer.

## 📂 Project Structure
- `models/`: Architecture definition.
- `data/`: Image preprocessing and loading utilities.
- `notebooks/`: Full experimental notebooks for both methods.
