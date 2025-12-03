# 🌐 Internet Speed Test (Tkinter)

A simple and elegant **Internet Speed Test** desktop application built with **Python** and **Tkinter**. It measures your **download** and **upload** internet speeds using the `speedtest` module and displays results in a clean GUI.

---

## 🚀 Features

✔️ Check **Download Speed** (Mbps)
✔️ Check **Upload Speed** (Mbps)
✔️ Simple & modern Tkinter GUI
✔️ Custom fonts and colors
✔️ One-click **CHECK SPEED** button
✔️ **EXIT** button to close app

---

## 📂 Project Structure

```
internet-speed-test/
├── main.py       # Main application file
├── README.md                    # Project documentation
```

---

## 🧰 Technologies Used

* 🐍 Python
* 🪟 Tkinter (GUI)
* 🌐 Speedtest (from `speedtest-cli`)

---

## 📦 Installation

### 1️⃣ Install Python (if not installed)

Download from [https://www.python.org/](https://www.python.org/)

### 2️⃣ Install required package

```bash
pip install speedtest-cli
```

> Note: The module `speedtest` comes from `speedtest-cli`.

---

## ▶️ How to Run

```bash
python internet_speed_test.py
```

After running the script, a window titled **"Internet Speed Test"** will appear.

---

## 🕹️ Usage

1. Click **CHECK SPEED** button
2. Wait a few seconds while the app tests speed
3. Speed will be displayed as:

   * `Download Speed: XX.XX Mbps`
   * `Upload Speed: XX.XX Mbps`
4. Click **EXIT** to close the window

---

## 🧱 Code Overview

* **`speedcheck()` function:**

  * Creates `Speedtest()` object
  * Selects best server
  * Measures download & upload speed
  * Updates GUI labels

* Tkinter interface includes:

  * Title label
  * Download & upload display labels
  * **CHECK SPEED** and **EXIT** buttons
  * Informative footer

---

## 📌 Future Enhancements

* 📍 Show ping/latency
* 📊 Add animated progress bar
* 💾 Save results history
* 🎨 Add theme switcher

---

## 🤝 Contributing

Feel free to fork this project and suggest improvements. Pull requests are welcome.

---

## 📄 License

This project is open-source and free to use for study or development purposes.

---

## 🙌 Author

Developed by Meet Bataviya to practice Python GUI development.

💬 Suggestions and improvements are always welcome.

---

## ⭐ Support

If you like this project, give it a **star ⭐ on GitHub**!

Happy Coding! 😄
