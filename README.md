# Agentic AI using Browser-Use Agent🌀

Agentic AI is a **Streamlit-based web application** that leverages [browser-use](https://github.com/browser-use/browser-use) and OpenAI's **GPT-4o** to automate browser tasks using Python. The application allows users to input tasks, executes them using an autonomous browsing agent, and formats the results into a readable markdown format.

## Features 🚀
- **Automate browser tasks** using `browser-use`
- **Integrate OpenAI GPT-4o** for intelligent decision-making
- **Streamlit UI** for an interactive user experience
- **JSON result formatting** into structured Markdown output
- **Expander to view raw results** before formatted display
- **Error handling** to ensure browser shutdown on failures

---

## Installation 📥

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Google Chrome installed (if using custom Chrome instance)

### Setup
1. **Clone the Repository**
   ```bash
   git clone git@github.com:sajithamma/browseruseapp.git
   cd browseruseapp
   ```

2. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Rename `.env.example` to `.env`
   - Open `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-key-here
     ```

---

## Running the Streamlit App 🎨
The **Streamlit UI** allows users to input tasks and receive structured markdown-formatted results.

### Start the App
```bash
streamlit run streamlitapp.py
```

### Usage
1. Enter a **task** in the text area (e.g., "Find the latest news on AI regulations").
2. Click **Assign Task 🎯**.
3. The app will:
   - Execute the browser task using an autonomous agent.
   - Display the raw JSON result.
   - Format the output into readable Markdown.

---

## Running the Python Script 📜
For those who want to run an **agentic AI task** directly via Python:

```bash
python app.py
```

This script will:
- Search for "Sajith Amma LinkedIn and Google"
- Retrieve links and check his latest activities
- Print the results in the console

---

## Code Overview 📝

### `streamlitapp.py`
The Streamlit application:
- Initializes the **browser-use** agent.
- Takes user input and assigns tasks.
- Retrieves and formats the results into Markdown.
- Displays both raw and formatted results.

### `app.py`
The standalone script:
- Executes a predefined browser task using `browser-use`.
- Uses GPT-4o for intelligent automation.
- Prints results in the terminal.

---

## Technologies Used 🛠️
- **[Streamlit](https://streamlit.io/)** – For interactive UI
- **[LangChain](https://python.langchain.com/)** – For AI task execution
- **[browser-use](https://github.com/browser-use/browser-use)** – Browser automation
- **[OpenAI GPT-4o](https://openai.com/)** – AI-powered decision-making
- **Python (Asyncio, dotenv)** – Task execution and environment management

---

## Contributing 🤝
Contributions are welcome! Feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

## License 📜
This project is licensed under the **MIT License**.

---

## Contact 📧
For any issues or inquiries, reach out via [LinkedIn](https://www.linkedin.com/in/sajithamma/)

---

Enjoy using **Agentic AI 🌀** for your browser automation tasks!
