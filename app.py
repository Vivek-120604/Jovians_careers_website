from flask import Flask, jsonify ,render_template,jsonify

app = Flask(__name__)


JOBS = [
  
{
"id":1,
"title": "Software Engineer",
"salary": "₹12,00,000 ",
"location": "Bangalore, India"
},
       {   "id":2,
          "title": "Data Analyst",
          "salary": "₹8,50,000 ",
          "location": "Hyderabad, India"
      },
      {    "id":3,
          "title": "Product Manager",

          "location": "San Francisco, USA"
      },
       {   
          "id" :4,
          "title": "UI/UX Designer",
          "salary": "€60,000 ",
          "location": "Berlin, Germany"
      },
       {  
         "id":5,
          "title": "DevOps Engineer",
          "salary": "$90,000 ",
          "location": "Toronto, Canada"
      },
       {   "id":6,
          "title": "Machine Learning Engineer",
          "salary": "£75,000 ",
          "location": "London, UK"
      },
      {    "id" :7,
          "title": "Cybersecurity Analyst",
          
          "location": "Singapore"
      },
    {   
          "id":8,
          "title": "Frontend Developer",
          "salary": "$80,000 ",
          "location": "Remote"
      }
       
]



@app.route('/')
def hello_world():
  return render_template("home.html",jobs = JOBS,company_name ="Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0',port= True)
