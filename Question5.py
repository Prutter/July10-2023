from flask import Flask, request, jsonify

app = Flask(__name__)

posts = []

@app.route("/createPost", methods =["POST"])
def createPost():
    id = request.form["id"]
    comment = request.form["comment"]
    newPost = {}
    newPost['id'] = id
    newPost["comment"] = comment
    posts.append(newPost)
    return "Post is added to your account"

@app.route("/getPost")
def getPost():
    id = request.form["id"]
    for p in posts:
        if p["id"] == id:
            return jsonify({'post' : p}) 
    return "Post is not found on your account"

@app.route("/deletePost", methods =["DELETE"])
def deletePost():
    id = request.form["id"]
    for p in posts:
        if p["id"] == id:
            posts.remove(p)
            return "post is deleted"
    return "Post is not found on your account"

@app.route("/updatePost")
def updatePost():
    id = request.form["id"]
    newcomment = request.form["comment"]
    for p in posts:
        if p["id"] == id:
            p["comment"] = newcomment
            return "post is updated"
    return "Post is not found on your account"


if __name__ == '__main__':
    app.run(debug=True)