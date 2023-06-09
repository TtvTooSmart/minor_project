from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import numpy as np 


app = Flask(__name__)
model = pickle.load(open('projectname.pickle','rb'))

    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    gender = (request.form.get('gender'))
    age = int(request.form.get('age'))
    smoke = request.form.get('smoking')
    cigspd = int(request.form.get('cigspd'))
    bpmeds = request.form.get('bpmeds')
    diabetes = request.form.get('diabetes')
    totChol = request.form.get('totChol')
    sysBP = int(request.form.get('sysBP'))
    diaBP = int(request.form.get('diaBP'))
    BMI = int(request.form.get('BMI'))
    heart_rate = int(request.form.get('heart_rate'))
    gluclvl = int(request.form.get('gluclvl'))
    tenchd = request.form.get('tenchd')
    
    
    int_features = [int(x)  for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict(final)
    print(prediction)    
    
    
    
    
    
    
    
    
    
    
    
    # heart_attack_weight_value = 8
    # artery_block_weight_value = 4
    
    # # Determine the weight of heart attack and artery blockage
    # heart_attack_weight = 0
    # artery_block_weight = 0

    # # print (heart_attack_weight)
    # # print (artery_block_weight)

    # if smoke == 'yes':
    #     heart_attack_weight += heart_attack_weight_value
    #     artery_block_weight += artery_block_weight_value

    # if fried_food == 'yes':
    #     artery_block_weight += 7
        
    # if alcohol == 'yes':
    #     heart_attack_weight += 5
    #     artery_block_weight += 3
    #     print (heart_attack_weight)
    #     print (artery_block_weight)
        
    # if exercise == 'no':
    #     heart_attack_weight += 7
    #     artery_block_weight += 7
    #     print (heart_attack_weight)
    #     print (artery_block_weight)
        
    # if age >= 40:
    #     heart_attack_weight += 9
    #     artery_block_weight += 8
    #     print (heart_attack_weight)
    #     print (artery_block_weight)    

    # if diabetes == 'yes':
    #     heart_attack_weight += 7
    #     artery_block_weight += 7
    #     print (heart_attack_weight)
    #     print (artery_block_weight)

    # if heart_disease == 'yes':
    #     heart_attack_weight += 12
    #     artery_block_weight += 11
    #     print (heart_attack_weight)
    #     print (artery_block_weight)
        
        
    # global heart_attack_weight_g 
    # heart_attack_weight_g = heart_attack_weight
    # global artery_block_weight_g 
    # artery_block_weight_g= artery_block_weight
        
    # # global heart_attack_weight_g 
    # # heart_attack_weight_g = heart_attack_weight
    # # global artery_block_weight_g 
    # # artery_block_weight_g= artery_block_weight

    # # Generate a response based on the form data and the weight of heart attack and artery blockage
    
    # # 33 31.2

    # if heart_attack_weight >= 33 :
    #     const_heart_attack_chances = "highly likely"
    # elif heart_attack_weight < 15 :
    #     const_heart_attack_chances = "less"
    # else:
    #     const_heart_attack_chances = "medium"
        
    # if artery_block_weight >= 31.2 :
    #     const_artery_block_chances = "highly likely"
    # elif artery_block_weight < 13.6 :
    #     const_artery_block_chances = "less"
    # else:
    #     const_artery_block_chances = "medium"

    # # return const_heart_attack_chances, const_artery_block_chances
    


    # new_block_of_idk_anything_abt()
    
    # response = {
    # 'gender':gender
    # 'age':age
    # 'smoke':smoke
    # 'cigspd':cigspd
    # 'bpmeds':bpmeds
    # 'diabetes':diabetes
    # 'totChol':totChol
    # 'sysBP':sysBP
    # 'diaBP':diaBP
    # 'BMI':BMI
    # 'heart-rate':heart-rate
    # 'gluclvl':gluclvl
    # 'tenchd':tenchd
    # }

    # Redirect to a new webpage to display the result
    # return redirect(url_for('result', **response))


# @app.context_processor
# def context_processor():
    
    


@app.route('/result')
def result():
    smoke = request.args.get('smoke')
    fried_food = request.args.get('fried_food')
    alcohol = request.args.get('alcohol')
    exercise = request.args.get('exercise')
    age = request.args.get('age')
    diabetes = request.args.get('diabetes')
    heart_disease = request.args.get('heart_disease')
    const_heart_attack_chances = request.args.get('const_heart_attack_chances')
    const_artery_block_chances = request.args.get('const_artery_block_chances')
    
    return render_template('result.html', smoke=smoke, fried_food=fried_food, alcohol=alcohol, exercise=exercise,
                           age=age, diabetes=diabetes, heart_disease=heart_disease, 
                        #    heart_attack_weight=heart_attack_weight, artery_block_weight=artery_block_weight, )
                           const_heart_attack_chances=const_heart_attack_chances, const_artery_block_chances=const_artery_block_chances,)

if __name__ == '__main__':
    app.run(debug=True)


