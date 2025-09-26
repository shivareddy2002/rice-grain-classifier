# 🌾 Rice Type Classifier using CNN  

A **Deep Learning–based application** that classifies different types of rice grains from uploaded images.  
Built with **Python**, **TensorFlow/Keras**, and **Streamlit** for an interactive web interface.  

---

## 🚀 Live Demo  

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit&logoColor=white&color=ff4b4b)](https://rice-grain-classifier-project.streamlit.app/)  
👉 Click the badge above to try the **Rice Grain Classifier Web App**  

---

## ✨ Key Features  

- 📤 **Upload & Predict** – Upload a rice grain image and get instant predictions  
- 🔎 **Top-K Results** – Displays most probable varieties with confidence scores  
- 🌾 **Supported Varieties**:  
  - Arborio  
  - Basmati  
  - Ipsala  
  - Jasmine  
  - Karacadag  
- 💻 **Clean Web UI** – Simple and interactive Streamlit interface  
- ⚡ **Real-Time Predictions** – Powered by a custom-trained CNN  

---

## 📊 Dataset  

- Custom-labeled dataset of different rice varieties (Arborio, Basmati, Ipsala, Jasmine, Karacadag)  
- Preprocessing: **resize, normalize, data augmentation**  
- Model trained on **balanced rice image dataset**  

---

## 🛠️ Tech Stack  

| Technology            | Purpose                          |
|-----------------------|----------------------------------|
| **Python 3.8+**       | Core Programming                 |
| **TensorFlow / Keras**| Deep Learning (CNN Model)        |
| **Streamlit**         | Web App Interface                |
| **FastAPI** *(optional)* | REST API Backend             |
| **OpenCV & PIL**      | Image Preprocessing              |
| **NumPy / Pandas**    | Data Handling                    |
| **Matplotlib / Seaborn** | Training Visualizations       |

---

## 🔮 How It Works  

1️⃣ **Upload** a rice grain image (JPG/PNG)  
2️⃣ Image is **preprocessed** (resize → normalize)  
3️⃣ **CNN model** predicts probabilities of each variety  
4️⃣ App shows **Top-K predictions with confidence scores**  

---

## 🖼️ Web Interface Screenshots  

### 🌾 Home Page (Uploading Image) 
![Upload Page](galary_rice/Screenshot%202025-09-21%20234547.png)  

### 🔍  Resizing the uploaded image 
![Prediction Page](galary_rice/Screenshot%202025-09-21%20234630.png)  

### 📊 Prediction with Confidence Score
![Confidence View](galary_rice/Screenshot%202025-09-21%20234755.png)  

---

## 🚀 Future Enhancements  

- ➕ Add more rice varieties and expand dataset  
- 📱 Mobile-friendly responsive UI  
- ☁️ Deploy on **Hugging Face Spaces**, **AWS**, or **GCP**  
- 🧩 Enable **batch prediction** for multiple grains  

---

## 🤝 Contributing  

Contributions are welcome!  

1. 🍴 Fork the repository  
2. 🌱 Create a feature branch  
3. 🚀 Submit a pull request  

---

## 👨‍💻 Author  

**Lomada Siva Gangi Reddy**  
- 🎓 B.Tech CSE (Data Science), RGMCET (2021–2025)  
- 💡 Interests: Python | Machine Learning | Deep Learning | Data Science  
- 📍 Open to **Internships & Job Offers**  

📬 **Contact Me**:  
- 📞 9346493592  
- [💼 LinkedIn](https://www.linkedin.com/in/lomada-siva-gangi-reddy-a64197280/) [🌐 GitHub](https://github.com/shivareddy2002)  

---
## 📌 Project Workflow  

```mermaid
flowchart LR
    A[📥 Import Libraries]:::step --> B[🖼️ Load Image Dataset]:::data
    B --> C[⚙️ Preprocessing<br/>-Augmentation, Normalization]:::process
    C --> D[🧠 Model Building<br/>-CNN]:::model
    D --> E[📊 Prediction Result]:::result
    E --> F[🌐 Project Deployment<br/>-Streamlit/FastAPI]:::deploy

    %% Styles
    classDef step fill=#FFD54F,stroke=#F57F17,stroke-width=2px,color=#000,font-weight=bold;
    classDef data fill=#4FC3F7,stroke=#0277BD,stroke-width=2px,color=#fff,font-weight=bold;
    classDef process fill=#AED581,stroke=#33691E,stroke-width=2px,color=#000,font-weight=bold;
    classDef model fill=#BA68C8,stroke=#4A148C,stroke-width=2px,color=#fff,font-weight=bold;
    classDef result fill=#FF8A65,stroke=#BF360C,stroke-width=2px,color=#fff,font-weight=bold;
    classDef deploy fill=#90CAF9,stroke=#0D47A1,stroke-width=2px,color=#000,font-weight=bold;
