# 🎥 Motion Detection with Email Alerts

This project uses **OpenCV** and a webcam to detect motion. When a moving object is detected, it captures an image and sends an alert email with the image attached. The system runs in real-time and automatically cleans up saved images.

---

## 🚀 Features

- 📹 Real-time motion detection using webcam and OpenCV
- 📷 Automatically captures frames when motion is detected
- 📧 Sends email alerts with the captured image
- 🧹 Auto-cleans image folder after alerts
- 🧠 Multi-threaded email sending and cleanup
- 🔐 Uses `.env` for email credentials (safe for GitHub)

---

## 🧠 Tech Stack

| Tool         | Purpose                             |
|--------------|-------------------------------------|
| Python       | Core programming language           |
| OpenCV       | Image capture and motion detection  |
| smtplib      | Email functionality                 |
| threading    | To run email and cleanup in parallel|
| `python-dotenv` | Load sensitive data securely     |

---

## 📁 Project Structure

```
Motion-Detector/
├── images/                 # Auto-saved motion frames
├── Emailing.py             # Email sending logic (uses .env)
├── img.py                  # Optional image utilities
├── motion_detector.py      # Main script (your current code)
├── .env                    # Email credentials (NOT in GitHub)
├── .env.example            # Template for environment variables
├── .gitignore              # Ignores .env and cache
└── README.md               # You’re here!
```

---

## 🔐 .env Setup

Create a `.env` file in the root folder:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
EMAIL_RECEIVER=receiver_email@gmail.com
```

> ⚠️ Never push your actual `.env` to GitHub! Use `.gitignore`.

---

## 📦 requirements.txt

```
dotenv==0.9.9
numpy==2.2.0
opencv-python==4.10.0.84
python-dotenv==1.1.0

```

Install everything with:

```bash
pip install -r requirements.txt
```

---

## 💻 How to Run

```bash
python motion_detector.py
```

- Press `q` to quit the video window and clean images.
- Make sure your webcam is enabled and accessible.

---

## 📌 Notes

- You must have `images/` folder created already, or add a line in code to auto-create it.
- Ensure `.env` is properly configured before running.
- Uses threading for faster performance and no UI freeze.

---

## 👤 Author

Built by [Mugdho Jeferson Rozario](https://github.com/mugjeff12)  
> Engineering Physics @ McMaster | AI + Automation Enthusiast | Python Developer  

---

## 📜 License

MIT License – Free to use, modify, and distribute. Just don’t forget to give credit 🙌
