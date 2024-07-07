from flask import Flask, request, jsonify, send_file
import openai
import pandas as pd
from docx import Document
import json
import matplotlib.pyplot as plt
import pdfkit
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

# Firebase configuration and initialization
firebaseConfig = {
  "apiKey": "AIzaSyCnCcU0t2naj59OC_cQ-MFgLFuHNMr9uek",
  "authDomain": "reliabilityiq.firebaseapp.com",
  "projectId": "reliabilityiq",
  "storageBucket": "reliabilityiq.appspot.com",
  "messagingSenderId": "104501551043",
  "appId": "1:104501551043:web:7ef9bed841151eafefe776",
  "measurementId": "G-N2M5E7Q133"
}

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    return df.head().to_json()

def analyze_pdf(file_path):
    return "PDF analysis result"

def analyze_docx(file_path):
    doc = Document(file_path)
    full_text = "\n".join([para.text for para in doc.paragraphs])
    return full_text

def create_visualization(data, chart_type):
    plt.figure()
    if chart_type == 'bar':
        data.plot(kind='bar')
    elif chart_type == 'line':
        data.plot(kind='line')
    plot_path = 'visualization.png'
    plt.savefig(plot_path)
    return plot_path

@app.route('/analyze-sensor-data', methods=['POST'])
def analyze_sensor_data():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Analyze the following sensor data and maintenance logs: {data['sensor_data']} {data['maintenance_logs']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/recommend-maintenance-schedule', methods=['POST'])
def recommend_maintenance_schedule():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Recommend an optimal maintenance schedule based on: {data['equipment_usage']} {data['history']} {data['industry_best_practices']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/generate-maintenance-report', methods=['POST'])
def generate_maintenance_report():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Generate a maintenance report based on: {data['equipment_data']} {data['maintenance_history']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/answer-query', methods=['POST'])
def answer_query():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Answer the following query: {data['query']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/interpret-report', methods=['POST'])
def interpret_report():
    file = request.files['file']
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)

    if file.filename.endswith('.csv'):
        result = analyze_csv(file_path)
    elif file.filename.endswith('.pdf'):
        result = analyze_pdf(file_path)
    elif file.filename.endswith('.docx') or file.filename.endswith('.doc'):
        result = analyze_docx(file_path)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Interpret the following maintenance report: {result}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/cost-benefit-analysis', methods=['POST'])
def cost_benefit_analysis():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Provide a cost-benefit analysis for the following maintenance strategies: {data['strategies']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/explain-technical-concept', methods=['POST'])
def explain_technical_concept():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Explain the following technical concept in simple terms: {data['concept']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/troubleshoot', methods=['POST'])
def troubleshoot():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Suggest potential causes for the following equipment issue based on symptoms and data: {data['issue']} {data['data']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/safety-recommendations', methods=['POST'])
def safety_recommendations():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant for predictive maintenance."},
            {"role": "user", "content": f"Provide safety recommendations for the following maintenance procedure: {data['procedure']}"}
        ]
    )
    return jsonify(response['choices'][0]['message']['content'])

@app.route('/create-visualization', methods=['POST'])
def create_visualization_endpoint():
    data = request.json
    chart_type = data.get('chart_type', 'line')
    df = pd.DataFrame(data['data'])
    plot_path = create_visualization(df, chart_type)
    return send_file(plot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

