
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:11998e,100:38ef7d&height=180&section=header&text=🌾%20Rice%20Type%20Classifier%20Using%20CNN&fontSize=34&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

A **Deep Learning–based application** that classifies different types of rice grains from uploaded images.  
Built with **Python**, **TensorFlow/Keras**, and **Streamlit** for an interactive web interface.  

---

## 🔗 Live Demo  
<p align="center">👉 Visit <strong>Rice Grain Classifier Web App</strong></p>
<p align="center">
  <a href="https://rice-grain-classifier-project.streamlit.app/">
    <img src="https://img.shields.io/badge/Demo-ClickHere-success?logo=streamlit&logoColor=white&color=ff4b4b" alt="Live Demo Badge">
  </a>
</p>


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


## 📌 Project Workflow  

```mermaid
flowchart LR
    A[Importing Libraries] --> B[Loading Image Dataset]
    B --> C[Data Preprocessing: Normalization, Augmentation]
    C --> D[Model Building: CNN]
    D --> E[Prediction Result]
    E --> F[Project Deployment: Streamlit / FastAPI]

    %% Styles
    style A fill:#FFD54F,stroke:#F57F17,stroke-width:2px,color:#000;
    style B fill:#4FC3F7,stroke:#0277BD,stroke-width:2px,color:#fff;
    style C fill:#AED581,stroke:#33691E,stroke-width:2px,color:#000;
    style D fill:#BA68C8,stroke:#4A148C,stroke-width:2px,color:#fff;
    style E fill:#FF8A65,stroke:#BF360C,stroke-width:2px,color:#fff;
    style F fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000;

```

## 👨‍💻 Author  

**Lomada Siva Gangi Reddy**  
- 🎓 B.Tech CSE (Data Science), RGMCET (2021–2025)  
- 💡 Interests: Python | Machine Learning | Deep Learning | Data Science  
- 📍 Open to **Internships & Job Offers**

 **Contact Me**:  

- 📧 **Email**: lomadasivagangireddy3@gmail.com  
- 📞 **Phone**: 9346493592  
- 💼 [LinkedIn](https://www.linkedin.com/in/lomada-siva-gangi-reddy-a64197280/)  🌐 [GitHub](https://github.com/shivareddy2002)  🚀 [Portfolio](https://lsgr-portfolio-pulse.lovable.app/)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:11998e,100:38ef7d&height=120&section=footer"/>
</p>
