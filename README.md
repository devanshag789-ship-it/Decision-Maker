# Decision Maker 🎯

A simple Python project that helps you make everyday decisions when you are confused about what to choose.

Enter any question, let the program think for a moment, and get a randomly selected response.

## ✨ Features

* Accepts a question from the user
* Displays a short thinking message
* Randomly selects a decision category
* Picks a response from the selected category
* Simple, interactive command-line interface

## 🛠️ Technologies Used

* **Python** — core programming language
* **random** — selects a random category and response
* **time** — adds a short delay before displaying the result

## 📋 Requirements

* Python 3.10 or later
* No external Python packages required

## 🚀 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Decision-Maker.git
cd Decision-Maker
```
*Note: Replace `YOUR_USERNAME` with your GitHub username.*

### 2. Create a Virtual Environment
**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
The project uses Python's built-in modules, so no external packages are required.
```bash
python -m pip install -r requirements.txt
```

### 4. Run the Program
```bash
python Decision_Maker.py
```

## 💻 Example Output
```text
Ask your question: Will I pass my exam?
Thinking...
AI Decision: Absolutely
```
*The response may differ each time because the program selects its answer randomly.*

## 🧠 How It Works

1. The program asks the user to enter a question.
2. It displays `Thinking...` and waits for two seconds.
3. It randomly selects one of three categories:
   * **Yes:** Positive responses
   * **No:** Negative responses
   * **Maybe:** Uncertain responses
4. It randomly selects a final response from that category.

**Note:** The program does not analyze the text of the question or use a neural network. It generates a random response for entertainment purposes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
