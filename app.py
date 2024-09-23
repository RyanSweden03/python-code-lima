
from flask import Flask, render_template
from database import get_all_employees, create_employee_table, insert_fake_data
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

create_employee_table()
insert_fake_data(record_count=20)

def generate_age_salary_bar_chart(employee_data):
    ages = [employee['age'] for employee in employee_data]
    salaries = [employee['salary'] for employee in employee_data]
    
    plt.figure(figsize=(8, 6))
    plt.bar(ages, salaries)
    plt.xlabel("Edad")
    plt.ylabel("Salario")
    plt.title("Gráfico de barras con la relación entre la edad y el salario de los registros.")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

def generate_city_distribution_pie_chart(employee_data):
    cities = [employee['city'] for employee in employee_data]
    unique_cities = set(cities)
    city_counts = [cities.count(city) for city in unique_cities]
    labels = [f"{city} ({count})" for city, count in zip(unique_cities, city_counts)]

    
    plt.figure(figsize=(8, 6))
    plt.pie(city_counts, labels=labels, autopct='%1.1f%%')
    plt.title("Cantidad de personas por ciudad")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def index():
    employee_data = get_all_employees()
    bar_chart = generate_age_salary_bar_chart(employee_data)
    pie_chart = generate_city_distribution_pie_chart(employee_data)
    return render_template('index.html', data=employee_data, bar_chart=bar_chart, pie_chart=pie_chart)

if __name__ == '__main__':
    app.run(debug=True)
