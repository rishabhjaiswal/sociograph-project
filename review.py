from flask import Flask, request,render_template,jsonify
import review_db 


app = Flask(__name__)

@app.route('/review',methods=['GET','POST'])
def reviews():
	if request.method=='GET':
		if request.headers.get('api_key')!='SocioGraphSolutions':
			return "wrong api key",401
		all_reviews=review_db.get_all()
		reviews=[]
		for review in all_reviews:
			id=review[0]
			title=review[1]
			rating=review[2]
			comments=review[3]
			reviews.append({'id':id,'title':title,'rating':rating,'comments':comments})
		return jsonify({'reviews':reviews})
	elif request.method=='POST':
		if request.form:
			title=request.form.get('title',None)
			rating=request.form['rating']
			comments=request.form.get('comments',None)
			review_db.insert(title=title,rating=rating,comments=comments)
			return "thanks for your review",200
		
		if request.json:
			if request.headers.get('api_key')!='SocioGraphSolutions':
				return "wrong api key",401
			if  not request.json.get('rating'):
				return "please give some rating",404
			title=request.json.get('title',None)
			rating=request.json.get('rating')
			comments=request.json.get('comments',None)
			review_db.insert(title=title,rating=rating,comments=comments)
		else:
			return "bad request",400

		return "thanks for your review",200


	else:
		return "bad request",400

@app.route('/review/<id>',methods=['GET','PUT','DELETE'])
def get_review(id):
	if request.headers.get('api_key')!='SocioGraphSolutions':
			return "wrong api key",401
	if request.method=='GET':
		review={}
		review_by_id=review_db.select_by_id(id)
		if review_by_id:
			id=review_by_id[0]
			title=review_by_id[1]
			rating=review_by_id[2]
			comments=review_by_id[3]
			review.update({'id':id,'title':title,'rating':rating,'comments':comments})
			return jsonify({'review':review})
		else:
			return "no review at given id",400
	elif request.method=='PUT':
		if request.json:
			review_by_id=review_db.select_by_id(id)
			if review_by_id:
				title=request.json.get('title',None)
				rating=request.json.get('rating',None)
				comments=request.json.get('comments',None)
				print id,title,rating,comments
				review_db.update_by_id(id,title=title,rating=rating,comments=comments)
				return "recored updated",200
			else:
				return "bad request",400
		
	elif request.method=='DELETE':
		review_by_id=review_db.select_by_id(id)
		if review_by_id:
			review_db.delete_by_id(id)
			return "row deleted", 200
		else:
			return "bad request",400


@app.route('/review/new',methods=['GET'])
def new_review():
	return render_template('new_review.html')


if __name__=="__main__":
	app.run(debug =True )
